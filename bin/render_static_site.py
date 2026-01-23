#!/usr/bin/env python3
"""
Render a static site for the planning application data specification using
digital_land_frontend Jinja setup and local templates.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import frontmatter
import jinja2
import jinja2.filters as jinja_filters

# digital_land_frontend expects evalcontextfilter (removed in Jinja 3.1); alias it early.
if not hasattr(jinja_filters, "evalcontextfilter"):
    jinja_filters.evalcontextfilter = jinja_filters.pass_eval_context

from bin.renderer import RenderContext
from digital_land_frontend import filters as dlf_filters  # noqa: E402
from digital_land_frontend import globals as dlf_globals  # noqa: E402
from loader import load_needs, load_specification_model
from utils import ensure_dir

try:
    import markdown as markdown_lib
except ImportError:  # pragma: no cover
    markdown_lib = None

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "bin" / "templates"


def render_markdown(md_text: str) -> str:
    if markdown_lib:
        return markdown_lib.markdown(md_text)
    return md_text


def extract_intro(md_text: str, stop_at_heading: str = "## ") -> str:
    lines: List[str] = []
    for line in md_text.splitlines():
        if line.startswith(stop_at_heading) and lines:
            break
        lines.append(line)
    return "\n".join(lines).strip()


def load_decision_stage(decision_stage_path: Path) -> Dict[str, Any]:
    return dict(frontmatter.load(decision_stage_path))


def load_submission_applications(spec_root: Path) -> List[Dict[str, Any]]:
    apps: List[Dict[str, Any]] = []
    for path in sorted(spec_root.glob("application/*.schema.md")):
        post = frontmatter.load(path)
        app = dict(post)
        app["__path"] = path
        apps.append(app)
    return apps


def load_readme(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def need_status(justifications: List[Dict[str, Any]]) -> Tuple[str, str]:
    satisfaction = {j.get("satisfaction", "").lower() for j in justifications}
    if "full" in satisfaction:
        return "Satisfied", "govuk-tag--green"
    if "partial" in satisfaction:
        return "Partially satisfied", "govuk-tag--blue"
    if satisfaction:
        return "Proposed", "govuk-tag--yellow"
    return "Not satisfied", "govuk-tag--grey"


def extract_dataset_refs(blob: Any) -> List[str]:
    refs: List[str] = []
    if isinstance(blob, dict):
        if "dataset" in blob and isinstance(blob["dataset"], str):
            refs.append(blob["dataset"])
        for value in blob.values():
            refs.extend(extract_dataset_refs(value))
    elif isinstance(blob, list):
        for item in blob:
            refs.extend(extract_dataset_refs(item))
    return refs


def extract_dataset_only_refs(blob: Any) -> List[str]:
    """
    Return dataset refs only from entries that specify a dataset alone (no field).
    For satisfied_by lists, this means items that are dicts with a dataset key and
    no other populated keys (or only dataset populated).
    """
    refs: List[str] = []
    if isinstance(blob, dict):
        keys_with_values = [k for k, v in blob.items() if v]
        if "dataset" in blob and isinstance(blob["dataset"], str):
            if len(keys_with_values) == 1 and keys_with_values[0] == "dataset":
                refs.append(blob["dataset"])
    elif isinstance(blob, list):
        for item in blob:
            refs.extend(extract_dataset_only_refs(item))
    return refs


def build_need_maps(
    needs_data: Dict[str, Dict[str, Any]],
) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, List[Dict[str, Any]]]]:
    needs = needs_data.get("need", {})
    justifications = needs_data.get("justification", {})

    need_to_justifications: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    dataset_to_need_justifications: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    for justification in justifications.values():
        need_ids = justification.get("needs", [])
        satisfied_by = justification.get("satisfied_by", {})
        datasets = extract_dataset_only_refs(satisfied_by)
        for n_id in need_ids:
            need_to_justifications[n_id].append(justification)
            # Attach to datasets that are satisfied purely by dataset references
            for dataset in datasets:
                dataset_to_need_justifications[dataset].append(
                    {"need": n_id, "justification": justification}
                )
    return need_to_justifications, dataset_to_need_justifications


def join_list_phrases(items: List[str], conj: str = "and") -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + f" {conj} " + items[-1]


def satisfaction_messages_for_field(
    all_need_justs: List[Tuple[str, Dict[str, Any]]],
    current_dataset: str,
    current_field: str,
    renderer: RenderContext,
) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = []

    def label_item(item: Dict[str, Any]) -> Optional[str]:
        ds = item.get("dataset")
        field = item.get("field")
        if not field:
            return None
        ds_link = (
            f'<a class="govuk-link" href="{renderer.url_for(f"/decision-stage/dataset/{ds}")}">{ds}</a>'
            if ds
            else ""
        )
        field_code = f"<code class='app-code'>{field}</code>"
        if ds and ds != current_dataset:
            return f"field {field_code} (dataset {ds_link})"
        return f"field {field_code}"

    def process_group(
        items: List[Dict[str, Any]], connector: str, need_id: str, need_href: str
    ) -> Optional[str]:
        current_in_group = False
        other_labels: List[str] = []
        for it in items:
            ds = it.get("dataset")
            field = it.get("field")
            if ds == current_dataset and field == current_field:
                current_in_group = True
            else:
                lbl = label_item(it)
                if lbl:
                    other_labels.append(lbl)
        if not current_in_group:
            return None
        if connector == "and":
            if other_labels:
                return f"This field and {join_list_phrases(other_labels, 'and')} satisfy need <a class=\"govuk-link\" href=\"{need_href}\">{need_id}</a>."
            return f'This field satisfies need <a class="govuk-link" href="{need_href}">{need_id}</a>.'
        else:
            if other_labels:
                return f"This field or {join_list_phrases(other_labels, 'or')} satisfy need <a class=\"govuk-link\" href=\"{need_href}\">{need_id}</a>."
            return f'This field satisfies need <a class="govuk-link" href="{need_href}">{need_id}</a>.'

    for need_id, justification in all_need_justs:
        sb = justification.get("satisfied_by")
        need_href = renderer.url_for(f"/decision-stage/need/{need_id}")

        # List of simple dicts (dataset/field)
        if isinstance(sb, list):
            msg = process_group(sb, "and", need_id, need_href)
            if msg:
                messages.append({"text": msg})
            continue

        if isinstance(sb, dict):
            if "allOf" in sb and isinstance(sb["allOf"], list):
                # handle nested anyOf within allOf
                current_matched = False
                other_labels: List[str] = []
                nested_msgs: List[str] = []
                for clause in sb["allOf"]:
                    if isinstance(clause, dict) and "anyOf" in clause:
                        any_msg = process_group(
                            clause["anyOf"], "or", need_id, need_href
                        )
                        if any_msg:
                            nested_msgs.append(
                                any_msg.replace("This field", "One of these fields")
                            )
                            current_matched = True
                        else:
                            # collect other labels for summary text
                            for it in clause["anyOf"]:
                                lbl = label_item(it)
                                if lbl:
                                    other_labels.append(lbl)
                    elif isinstance(clause, dict):
                        ds = clause.get("dataset")
                        field = clause.get("field")
                        if ds == current_dataset and field == current_field:
                            current_matched = True
                        else:
                            lbl = label_item(clause)
                            if lbl:
                                other_labels.append(lbl)
                if current_matched:
                    if other_labels:
                        messages.append(
                            {
                                "text": f"This field and {join_list_phrases(other_labels, 'and')} satisfy need <a class=\"govuk-link\" href=\"{need_href}\">{need_id}</a>."
                            }
                        )
                    messages.extend([{"text": m} for m in nested_msgs])
                continue

            if "anyOf" in sb and isinstance(sb["anyOf"], list):
                msg = process_group(sb["anyOf"], "or", need_id, need_href)
                if msg:
                    messages.append({"text": msg})
                continue

            # rule-based not tied to a specific field
            continue

    return messages


def build_env(base_url: str) -> jinja2.Environment:
    loaders: List[jinja2.BaseLoader] = [
        # Local templates (and subfolders like components/ and assets)
        jinja2.FileSystemLoader(
            [
                str(TEMPLATE_DIR),
                str(TEMPLATE_DIR / "components"),
                str(REPO_ROOT / "bin" / "assets"),
            ]
        ),
        jinja2.PrefixLoader(
            {
                "digital-land-frontend": jinja2.PackageLoader(
                    "digital_land_frontend", "templates"
                ),
                "govuk_frontend_jinja": jinja2.PackageLoader(
                    "govuk_frontend_jinja", "templates"
                ),
            }
        ),
    ]
    env = jinja2.Environment(loader=jinja2.ChoiceLoader(loaders), autoescape=True)

    # Register filters from digital-land-frontend
    env.filters.update(
        {
            "is_list": dlf_filters.is_list_filter,
            "is_valid_uri": dlf_filters.is_valid_uri_filter,
            "make_link": dlf_filters.make_link_filter,
            "float_to_int": dlf_filters.float_to_int_filter,
            "commanum": dlf_filters.commanum_filter,
            "split_to_list": dlf_filters.split_to_list_filter,
            "readable_date": dlf_filters.readable_date_filter,
            "hex_to_rgb_string": dlf_filters.hex_to_rgb_string_filter,
        }
    )

    # Expose globals commonly used by DL templates
    env.globals["random_int"] = dlf_globals.random_int
    env.globals["assetPath"] = base_url.rstrip("/") + "/static"
    env.globals["staticPath"] = base_url.rstrip("/") + "/static"

    return env


def copy_static(output_dir: Path) -> None:
    """
    Copy local static assets (CSS) into the output directory.
    """
    # is it worth replacing this with a make target?
    static_src = REPO_ROOT / "bin" / "assets"
    static_dst = output_dir / "static"
    if static_src.exists():
        for path in static_src.rglob("*"):
            if path.is_file():
                rel = path.relative_to(static_src)
                target = static_dst / rel
                ensure_dir(target.parent)
                target.write_bytes(path.read_bytes())


def render_decision_index(
    renderer: RenderContext,
    datasets: List[Dict[str, Any]],
) -> None:
    # Decision stage index
    decision_ctx = {
        "page_title": "Decision stage specification",
        "datasets": [
            {
                "name": ds.get("name", ds["dataset"]),
                "description": ds.get("description", ""),
                "href": renderer.url_for(f"/decision-stage/dataset/{ds['dataset']}"),
            }
            for ds in datasets
        ],
        "links": {"needs": renderer.url_for("/decision-stage/need")},
    }
    decision_html = renderer.render("decision_index.html", decision_ctx)
    renderer.write_page("decision-stage/index.html", decision_html)


def render_dataset_index(
    renderer: RenderContext, page_title, datasets, specification_slug
) -> None:
    # Decision stage datasets list
    dataset_ctx = {
        "page_title": page_title,
        "datasets": [
            {
                "name": ds.get("name", ds["dataset"]),
                "description": ds.get("description", ""),
                "href": renderer.url_for(
                    f"/{specification_slug}/dataset/{ds['dataset']}"
                ),
            }
            for ds in datasets
        ],
        "links": {
            "justifications": renderer.url_for("/justification"),
            "needs": renderer.url_for(f"/{specification_slug}/need"),
        },
    }
    dataset_html = renderer.render("dataset_index.html", dataset_ctx)
    renderer.write_page(f"{specification_slug}/dataset/index.html", dataset_html)


def render_index(renderer: RenderContext) -> None:
    # render the main Index page
    index_ctx = {
        "page_title": "Planning application data specification",
        "links": {
            "submission": renderer.url_for("/submission"),
            "decision_stage": renderer.url_for("/decision-stage"),
        },
    }
    index_html = renderer.render("index.html", index_ctx)
    renderer.write_page("index.html", index_html)


def render_decision_site(
    renderer: RenderContext,
    datasets: List[Dict[str, Any]],
) -> None:
    render_decision_index(renderer, datasets)
    render_dataset_index(
        renderer, "Decision stage datasets", datasets, "decision-stage"
    )


def render_justifications_index(
    renderer: RenderContext,
    justifications: List[Dict[str, Any]],
) -> None:
    # Justification index page
    justification_index_ctx = {
        "page_title": "Justifications",
        "justifications": [
            {
                "id": j.get("id"),
                "needs": [
                    f'<a class="govuk-link" href="{renderer.url_for(f"/decision-stage/need/{n}")}">{n}</a>'
                    for n in j.get("needs", [])
                ],
                "satisfaction": j.get("satisfaction", ""),
                "confidence": j.get("confidence", ""),
                "status": j.get("status", ""),
                "href": renderer.url_for(f"/justification/{j.get('id')}"),
            }
            for j in justifications
        ],
    }
    justification_index_template = renderer.render(
        "justification_index.html", justification_index_ctx
    )
    renderer.write_page("justification/index.html", justification_index_template)


def build_site(args: argparse.Namespace) -> None:
    output_dir = Path(args.output).resolve()
    ensure_dir(output_dir)
    base_url = args.base_url.rstrip("/")

    spec_root = Path(args.spec_root).resolve()
    needs_root = Path(args.needs_root).resolve()

    root_dir = (
        spec_root.parent
        if (spec_root.parent / "user-needs").exists()
        else needs_root.parent
    )
    original_cwd = Path.cwd()
    os.chdir(root_dir)

    env = build_env(base_url or "")
    env.globals["base_url"] = base_url

    renderer = RenderContext(env, base_url, output_dir)

    try:
        spec_model = load_specification_model()
        spec_tables = spec_model.get("tables", {})
        field_index = spec_model.get("fields", {})
        dataset_index = spec_model.get("tables", {}).get("dataset", {})
        module_index = spec_model.get("modules", {})

        decision_stage = load_decision_stage(spec_root / "decision-stage.schema.md")
        decision_datasets: List[Dict[str, Any]] = []
        for ds in decision_stage.get("datasets", []):
            dataset_id = ds.get("dataset")
            dataset_meta = dataset_index.get(dataset_id, {})
            merged = dict(dataset_meta)
            merged.update(ds)
            decision_datasets.append(merged)

        applications = load_submission_applications(spec_root)

        needs_data = load_needs()
        need_records = list(needs_data.get("need", {}).values())
        need_records.sort(key=lambda n: n.get("need", ""))
        need_to_justifications, dataset_to_need_justifications = build_need_maps(
            needs_data
        )

        # Index
        render_index(renderer)

        # Decision stage
        render_decision_site(renderer, decision_datasets)

        # Decision stage needs list
        needs_ctx = {
            "page_title": "Decision stage needs",
            "needs": [
                {
                    "id": need.get("need"),
                    "statement": need.get("statement") or need.get("name") or "",
                    "href": renderer.url_for(
                        f"/decision-stage/need/{need.get('need')}"
                    ),
                    "tag_label": need_status(
                        need_to_justifications.get(need.get("need"), [])
                    )[0],
                    "tag_class": need_status(
                        need_to_justifications.get(need.get("need"), [])
                    )[1],
                }
                for need in need_records
            ],
        }
        needs_html = env.get_template("needs_index.html").render(**needs_ctx)
        renderer.write_page("decision-stage/need/index.html", needs_html)

        # Decision stage need detail pages
        need_template = env.get_template("need_detail.html")
        for need in need_records:
            n_id = need.get("need")
            justs = need_to_justifications.get(n_id, [])
            label, cls = need_status(justs)
            need_meta = []
            if need.get("priority"):
                need_meta.append({"label": "Priority", "value": need.get("priority")})
            if need.get("status"):
                need_meta.append({"label": "Status", "value": need.get("status")})
            if need.get("themes"):
                need_meta.append(
                    {"label": "Themes", "value": ", ".join(need.get("themes"))}
                )
            if need.get("actors"):
                need_meta.append(
                    {"label": "Actors", "value": ", ".join(need.get("actors"))}
                )
            if need.get("source"):
                sources = need.get("source")
                formatted_sources = (
                    ", ".join([s.get("type", "") for s in sources])
                    if isinstance(sources, list)
                    else str(sources)
                )
                need_meta.append({"label": "Source", "value": formatted_sources})
            if need.get("variations"):
                need_meta.append(
                    {
                        "label": "Variations",
                        "value": ", ".join(
                            [str(v) for v in need.get("variations") if v]
                        ),
                    }
                )
            if need.get("next_step"):
                need_meta.append({"label": "Next step", "value": need.get("next_step")})
            need_ctx = {
                "need_ref": n_id,
                "page_title": f"Need {n_id}",
                "links": {"back": renderer.url_for("/decision-stage/need")},
                "tag_label": label,
                "tag_class": cls,
                "title": need.get("name") or n_id,
                "statement": need.get("statement") or "",
                "meta": need_meta,
                "justifications": [
                    {
                        "id": j.get("id", ""),
                        "satisfaction": j.get("satisfaction", ""),
                        "confidence": j.get("confidence", ""),
                        "notes": j.get("notes", ""),
                        "body": j.get("__body__", ""),
                        "href": renderer.url_for(
                            f"/justification/{j.get('id', '')}"
                        ),
                    }
                    for j in justs
                ],
            }
            need_html = need_template.render(**need_ctx)
            renderer.write_page(
                f"decision-stage/need/{n_id}/index.html", need_html
            )

        # Decision stage dataset detail pages
        dataset_template = env.get_template("dataset_detail.html")
        for ds in decision_datasets:
            ds_id = ds.get("dataset")
            ds_needs = dataset_to_need_justifications.get(ds_id, [])
            all_need_justs = [
                (need_id, j)
                for need_id, just_list in need_to_justifications.items()
                for j in just_list
            ]
            fields = []
            for f in ds.get("fields", []):
                field_ref = f.get("field")
                field_meta = field_index.get(field_ref)
                field_name = getattr(field_meta, "name", None) if field_meta else None
                field_desc = (
                    getattr(field_meta, "description", None) if field_meta else None
                )
                field_cardinality = (
                    getattr(field_meta, "cardinality", None) if field_meta else None
                )
                target_dataset = f.get("dataset")
                fields.append(
                    {
                        "name": field_name or field_ref,
                        "ref": field_ref,
                        "description": render_markdown(
                            f.get("description") or field_desc or ""
                        ),
                        "cardinality": f.get("cardinality") or field_cardinality or "",
                        "target_dataset": target_dataset,
                        "target_dataset_href": (
                            renderer.url_for(f"/decision-stage/dataset/{target_dataset}")
                            if target_dataset
                            else ""
                        ),
                        "satisfactions": satisfaction_messages_for_field(
                            all_need_justs, ds_id, field_ref, renderer
                        ),
                    }
                )
            dataset_ctx = {
                "page_title": f"Dataset {ds_id}",
                "links": {"back": renderer.url_for("/decision-stage/dataset")},
                "title": ds.get("name", ds_id),
                "description": ds.get("description", ""),
                "fields": fields,
                "needs": [
                    {
                        "need_id": item["need"],
                        "need_href": renderer.url_for(
                            f"/decision-stage/need/{item['need']}"
                        ),
                        "just_id": item["justification"].get("id", ""),
                        "satisfaction": item["justification"].get(
                            "satisfaction", "justification"
                        ),
                        "confidence": item["justification"].get("confidence", ""),
                        "notes": render_markdown(
                            item["justification"].get("notes", "") or ""
                        ),
                        "justification_body": render_markdown(
                            getattr(item["justification"], "content", "")
                            or item["justification"].get("body", "")
                            or item["justification"].get("notes", "")
                            or ""
                        ),
                        "requires_dataset": True,
                    }
                    for item in ds_needs
                ],
            }
            dataset_page = dataset_template.render(**dataset_ctx)
            renderer.write_page(
                f"decision-stage/dataset/{ds_id}/index.html", dataset_page
            )

        # Submission index
        submission_ctx = {
            "page_title": "Submission specifications",
            "applications": [
                {
                    "name": app.get("name", app.get("application")),
                    "description": app.get("description", ""),
                    "href": renderer.url_for(
                        f"/submission/application/{app.get('application')}"
                    ),
                }
                for app in applications
            ],
        }
        submission_html = env.get_template("submission_index.html").render(
            **submission_ctx
        )
        renderer.write_page("submission/index.html", submission_html)

        # Submission module index and detail pages
        submission_modules = list(spec_tables.get("module", {}).values())
        submission_modules.sort(key=lambda m: m.get("module", ""))
        module_index_ctx = {
            "page_title": "Submission modules",
            "modules": [
                {
                    "ref": m.get("module"),
                    "name": m.get("name", m.get("module")),
                    "description": m.get("description", ""),
                    "href": renderer.url_for(f"/submission/module/{m.get('module')}"),
                }
                for m in submission_modules
            ],
        }
        module_index_html = env.get_template("module_index.html").render(
            **module_index_ctx
        )
        renderer.write_page("submission/module/index.html", module_index_html)

        module_template = env.get_template("module_detail.html")
        for m in submission_modules:
            mod_fields = []
            for f in m.get("fields", []):
                field_ref = f.get("field")
                field_meta = field_index.get(field_ref)
                mod_fields.append(
                    {
                        "ref": field_ref,
                        "name": getattr(field_meta, "name", None) or field_ref,
                        "description": getattr(field_meta, "description", None) or "",
                        "required": f.get("required"),
                    }
                )
            module_ctx = {
                "page_title": f"Module {m.get('module')}",
                "ref": m.get("module"),
                "name": m.get("name", m.get("module")),
                "description": m.get("description", ""),
                "fields": mod_fields,
                "rules": m.get("rules", []),
                "links": {"back": renderer.url_for("/submission/module")},
            }
            module_html = module_template.render(**module_ctx)
            renderer.write_page(
                f"submission/module/{m.get('module')}/index.html", module_html
            )

        # Submission application detail pages
        app_template = env.get_template("submission_application_detail.html")
        for app in applications:
            app_id = app.get("application")
            fields = []
            for f in app.get("fields", []):
                field_ref = f.get("field")
                field_meta = field_index.get(field_ref)
                fields.append(
                    {
                        "ref": field_ref,
                        "name": getattr(field_meta, "name", None) or field_ref,
                        "description": getattr(field_meta, "description", None) or "",
                        "required": f.get("required"),
                    }
                )
            modules = []
            for m in app.get("modules", []):
                mref = m.get("module")
                mobj = module_index.get(mref)
                mdesc = ""
                if mobj:
                    mdesc = getattr(mobj, "description", None) or mobj.content.get(
                        "description", ""
                    )
                modules.append(
                    {
                        "ref": mref,
                        "required": m.get("required"),
                        "description": mdesc,
                    }
                )
            app_ctx = {
                "page_title": f"Application {app_id}",
                "title": app.get("name", app_id),
                "description": app.get("description", ""),
                "application": app_id,
                "synonyms": app.get("synonyms", []),
                "notes": app.get("notes", ""),
                "entry_date": app.get("entry-date", ""),
                "legislation": app.get("legislation", []),
                "fields": fields,
                "modules": modules,
                "links": {"back": renderer.url_for("/submission")},
            }
            app_html = app_template.render(**app_ctx)
            renderer.write_page(
                f"submission/application/{app_id}/index.html", app_html
            )

        # Justification index and detail pages
        justification_template = env.get_template("justification_detail.html")
        justifications = list(needs_data.get("justification", {}).values())
        justifications.sort(key=lambda j: j.get("id", ""))

        render_justifications_index(renderer, justifications)

        for j in justifications:
            j_ctx = {
                "page_title": f"Justification {j.get('id')}",
                "id": j.get("id", ""),
                "needs": j.get("needs", []),
                "needs_links": [
                    f'<a class="govuk-link" href="{renderer.url_for(f"/decision-stage/need/{n}")}">{n}</a>'
                    for n in j.get("needs", [])
                ],
                "satisfaction": j.get("satisfaction", ""),
                "confidence": j.get("confidence", ""),
                "status": j.get("status", ""),
                "body": render_markdown(
                    getattr(j, "content", "")
                    or j.get("body", "")
                    or j.get("notes", "")
                    or ""
                ),
                "raw": j,
                "links": {"back": renderer.url_for("/justification")},
                "github_issue_url": f"https://github.com/digital-land/planning-application-data-specification/issues/new?title=Feedback%20on%20justification%20{j.get('id')}",
                "github_edit_url": f"https://github.com/digital-land/planning-application-data-specification/edit/main/user-needs/justification/{j.get('id')}.md",
            }
            j_html = justification_template.render(**j_ctx)
            renderer.write_page(f"justification/{j.get('id')}/index.html", j_html)

        # Emit a sitemap for inspection
        site_map = {
            "index": "index.html",
            "decision_stage": "decision-stage/index.html",
            "needs": [
                f"decision-stage/need/{n.get('need')}.html" for n in need_records
            ],
            "datasets": [
                f"decision-stage/dataset/{ds.get('dataset')}/index.html"
                for ds in decision_datasets
            ],
            "submission": "submission/index.html",
        }
        renderer.write_page("sitemap.json", json.dumps(site_map, indent=2))

        # Copy static assets (CSS)
        copy_static(output_dir)
    finally:
        os.chdir(original_cwd)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render static specification site.")
    parser.add_argument(
        "--output",
        default=REPO_ROOT / "docs",
        help="Output directory for rendered site.",
    )
    parser.add_argument(
        "--base-url",
        default="/planning-application-data-specification",
        help='Base URL for links (e.g. /planning-spec when hosting under a subpath). Use "" for local root preview.',
    )
    parser.add_argument(
        "--spec-root",
        default=REPO_ROOT / "specification",
        help="Path to specification directory.",
    )
    parser.add_argument(
        "--needs-root",
        default=REPO_ROOT / "user-needs",
        help="Path to user-needs directory.",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    build_site(parse_args())
