#!/usr/bin/env python3
"""
Render a static site for the planning application data specification using
digital_land_frontend Jinja setup and local templates.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote

import frontmatter
import jinja2
import jinja2.filters as jinja_filters

# digital_land_frontend expects evalcontextfilter (removed in Jinja 3.1); alias it early.
if not hasattr(jinja_filters, "evalcontextfilter"):
    jinja_filters.evalcontextfilter = jinja_filters.pass_eval_context

from digital_land_frontend import filters as dlf_filters  # noqa: E402
from digital_land_frontend import globals as dlf_globals  # noqa: E402
from bin.completeness import build_progress_view_model
from bin.jinja_filters import commanum_filter
from bin.loader import load_needs, load_specification_model
from bin.markdown_utils import render_govuk_markdown
from bin.models import FieldDef, ComponentInstance, FieldInstance
from bin.renderer import RenderContext
from bin.utils import ensure_dir
from planning_application_specification import Specification
from planning_application_specification.models import (
    ComponentUsage as SpecificationComponentUsage,
)
from planning_application_specification.models import FieldUsage as SpecificationFieldUsage

try:
    import markdown as markdown_lib
except ImportError:  # pragma: no cover
    markdown_lib = None

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "bin" / "templates"
DEFAULT_PROGRESS_INPUT = REPO_ROOT / "bin" / "admin_data" / "2024-application-volumes.csv"


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


def load_active_combined_applications(spec_root: Path) -> List[Dict[str, str]]:
    combined_path = spec_root / "combined-application-types.csv"
    if not combined_path.exists():
        return []

    with combined_path.open(newline="", encoding="utf-8") as csvfile:
        return [
            row
            for row in csv.DictReader(csvfile)
            if (row.get("start-date") or "").strip()
            and not (row.get("end-date") or "").strip()
        ]


def load_design_decisions(documentation_root: Path) -> List[Dict[str, Any]]:
    decisions_path = documentation_root / "design-decisions"
    if not decisions_path.exists():
        return []

    decisions = [
        parse_design_decision(path) for path in sorted(decisions_path.glob("*.md"))
    ]
    return sorted(decisions, key=lambda decision: decision["decision_id"])


def parse_design_decision(path: Path) -> Dict[str, Any]:
    content = path.read_text(encoding="utf-8")
    slug = path.stem
    decision_id = slug.split("-", 1)[0]
    title = extract_design_decision_title(content, slug)
    body_markdown = strip_design_decision_page_metadata(content)

    return {
        "decision_id": decision_id,
        "slug": slug,
        "title": title,
        "date": extract_design_decision_metadata(content, "Date"),
        "status": extract_design_decision_metadata(content, "Status"),
        "body": render_govuk_markdown(body_markdown),
    }


def extract_design_decision_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        match = re.match(r"^#{1,2}\s+(.*)$", line.strip())
        if match:
            title = match.group(1).strip()
            return re.sub(r"^Decision:\s*", "", title, flags=re.IGNORECASE)
    return fallback.replace("-", " ").capitalize()


def extract_design_decision_metadata(content: str, label: str) -> str:
    pattern = rf"^\*\*{re.escape(label)}:\*\*\s*(.*?)\s*$"
    for line in content.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            return match.group(1).strip()
    return ""


def strip_design_decision_page_metadata(content: str) -> str:
    lines = []
    skipped_heading = False
    for line in content.splitlines():
        stripped = line.strip()
        if not skipped_heading and re.match(r"^#{1,2}\s+", stripped):
            skipped_heading = True
            continue
        if re.match(r"^\*\*(Date|Status):\*\*", stripped):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def design_decision_feedback_url(decision: Dict[str, Any]) -> str:
    title = f"[{decision['decision_id']}] Feedback on design decision: {decision['title']}"
    encoded_title = quote(title)
    return (
        "https://github.com/digital-land/planning-application-data-specification/"
        f"issues/new?title={encoded_title}"
    )


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


def need_status_dict(justifications: List[Dict[str, Any]]) -> Dict[str, str]:
    label, cls = need_status(justifications)
    return {"tag_label": label, "tag_class": cls}


def build_module_summary(
    module_ref: str, module_index: Dict[str, Any]
) -> Dict[str, str]:
    mobj = module_index.get(module_ref)
    if mobj:
        name = getattr(mobj, "name", None) or getattr(mobj, "content", {}).get(
            "name", module_ref
        )
        desc = getattr(mobj, "description", None) or getattr(mobj, "content", {}).get(
            "description", ""
        )
    else:
        name, desc = module_ref, ""
    return {"ref": module_ref, "name": name, "description": desc}


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
            f'<a class="govuk-link" href="{renderer.url_for(f"/dataset/{ds}")}">{ds}</a>'
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
        need_href = renderer.url_for(f"/user-need/{need_id}")

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


def build_need_meta(need: Dict[str, Any]) -> List[Dict[str, str]]:
    meta: List[Dict[str, str]] = []
    if need.get("priority"):
        meta.append({"label": "Priority", "value": need.get("priority")})
    if need.get("status"):
        meta.append({"label": "Status", "value": need.get("status")})
    if need.get("themes"):
        meta.append({"label": "Themes", "value": ", ".join(need.get("themes"))})
    if need.get("actors"):
        meta.append({"label": "Actors", "value": ", ".join(need.get("actors"))})
    if need.get("source"):
        sources = need.get("source")
        formatted_sources = (
            ", ".join([s.get("type", "") for s in sources])
            if isinstance(sources, list)
            else str(sources)
        )
        meta.append({"label": "Source", "value": formatted_sources})
    if need.get("variations"):
        meta.append(
            {
                "label": "Variations",
                "value": ", ".join([str(v) for v in need.get("variations") if v]),
            }
        )
    if need.get("next_step"):
        meta.append({"label": "Next step", "value": need.get("next_step")})
    return meta


class FieldView:
    def __init__(
        self,
        ref,
        name,
        description,
        cardinality,
        datatype,
        codelist,
        required,
        children=None,
        target_dataset=None,
        target_dataset_href="",
        satisfactions=None,
        component_name=None,
        inherited_from=None,
    ):
        self.ref = ref
        self.name = name
        self.description = description
        self.cardinality = cardinality
        self.datatype = datatype
        self.codelist = codelist
        self.required = required
        self.children = children or []
        self.target_dataset = target_dataset
        self.target_dataset_href = target_dataset_href
        self.satisfactions = satisfactions or []
        self.component_name = component_name
        self.inherited_from = inherited_from


def build_field_display(field_entry: Any, field_index: Dict[str, Any] = None) -> FieldView:
    # If already a FieldView
    if isinstance(field_entry, FieldView):
        return field_entry

    # Handle FieldInstance (from models)
    from bin.models import FieldInstance, FieldDef as FD  # type: ignore

    if isinstance(field_entry, FieldInstance):
        orig = field_entry.original
        overrides = field_entry.overrides or {}
        name = overrides.get("name") or orig.name
        description = overrides.get("description") or orig.description
        cardinality = overrides.get("cardinality") or orig.cardinality
        datatype = overrides.get("datatype") or orig.datatype
        codelist = overrides.get("codelist") or orig.codelist
        required = overrides.get("required")
        if required is None:
            required = orig.required
        children = overrides.get("children", [])
        comp_name = None
        if orig.resolved_component:
            comp = orig.resolved_component.component
            comp_name = comp.name or comp.ref
        return FieldView(
            ref=orig.ref,
            name=name,
            description=description,
            cardinality=cardinality,
            datatype=datatype,
            codelist=codelist,
            required=required,
            children=children,
            component_name=comp_name,
        )

    if isinstance(field_entry, SpecificationFieldUsage):
        orig = field_entry.original
        overrides = field_entry.overrides or {}
        name = overrides.get("name") or orig.name
        description = overrides.get("description") or orig.description
        cardinality = overrides.get("cardinality") or orig.cardinality
        datatype = overrides.get("datatype") or orig.datatype
        codelist = overrides.get("codelist") or orig.codelist
        required = overrides.get("required")
        if required is None:
            required = orig.required
        comp_name = None
        if orig.resolved_component:
            comp_name = orig.resolved_component.component.name or orig.resolved_component.component.ref
        return FieldView(
            ref=orig.ref,
            name=name,
            description=description,
            cardinality=cardinality,
            datatype=datatype,
            codelist=codelist,
            required=required,
            component_name=comp_name,
        )

    # Fallback for dict-based field entries (datasets, etc.)
    field_ref = field_entry.get("field")
    fd = None
    if field_index:
        fd = field_index.get(field_ref)
    fd = FD.from_spec(fd) if fd else FD.from_spec(field_ref)
    name = field_entry.get("name") or fd.name or field_ref
    description = field_entry.get("description") or fd.description or ""
    cardinality = field_entry.get("cardinality") or fd.cardinality
    datatype = field_entry.get("datatype") or fd.datatype
    codelist = field_entry.get("codelist") or fd.codelist
    comp_name = None
    if fd.resolved_component:
        comp = fd.resolved_component.component
        comp_name = comp.name or comp.ref
    return FieldView(
        ref=field_ref,
        name=name,
        description=description,
        cardinality=cardinality,
        datatype=datatype,
        codelist=codelist,
        required=field_entry.get("required"),
        children=field_entry.get("children", []),
        component_name=comp_name,
    )


def build_field_views_from_items(items: List[Any], field_index: Dict[str, Any]) -> List[FieldView]:
    views: List[FieldView] = []
    for item in items:
        if isinstance(item, FieldInstance):
            fv = build_field_display(item)
            # attach children if the underlying field references a component
            if item.original.resolved_component:
                fv.children = build_field_views_from_items(
                    item.original.resolved_component.component.items, field_index
                )
            views.append(fv)
        elif isinstance(item, ComponentInstance):
            fi = item.referenced_by_field
            fv = build_field_display(fi)
            fv.children = build_field_views_from_items(item.component.items, field_index)
            views.append(fv)
        elif isinstance(item, SpecificationFieldUsage):
            fv = build_field_display(item)
            if item.original.resolved_component:
                fv.children = build_field_views_from_items(
                    item.original.resolved_component.component.items, field_index
                )
            views.append(fv)
        elif isinstance(item, SpecificationComponentUsage):
            referenced_by = item.referenced_by_field
            if referenced_by:
                fv = build_field_display(referenced_by)
                fv.children = build_field_views_from_items(item.component.items, field_index)
                views.append(fv)
    return views


def application_parent_refs(application: Dict[str, Any]) -> List[str]:
    extends = application.get("extends")
    if not extends:
        return []
    if isinstance(extends, list):
        return [ref for ref in extends if ref]
    return [extends]


def application_module_refs(application: Dict[str, Any]) -> List[str]:
    refs: List[str] = []
    for module in application.get("modules", []) or []:
        if isinstance(module, dict) and module.get("module"):
            refs.append(module["module"])
        elif isinstance(module, str):
            refs.append(module)
    return refs


def application_field_entries(
    application: Dict[str, Any],
    application_index: Dict[str, Dict[str, Any]],
    visited: Optional[set[str]] = None,
) -> List[Tuple[Dict[str, Any], Optional[str]]]:
    visited = visited or set()
    application_ref = application.get("application")
    if application_ref in visited:
        return []
    if application_ref:
        visited.add(application_ref)

    fields: List[Tuple[Dict[str, Any], Optional[str]]] = []
    for parent_ref in application_parent_refs(application):
        parent = application_index.get(parent_ref)
        if parent:
            fields.extend(
                (field, inherited_from or parent_ref)
                for field, inherited_from in application_field_entries(
                    parent, application_index, visited
                )
            )

    fields.extend((field, None) for field in application.get("fields", []) or [])

    deduped_fields: List[Tuple[Dict[str, Any], Optional[str]]] = []
    index_by_ref: Dict[str, int] = {}
    for field, inherited_from in fields:
        field_ref = field.get("field")
        if field_ref in index_by_ref:
            deduped_fields[index_by_ref[field_ref]] = (field, inherited_from)
        else:
            index_by_ref[field_ref] = len(deduped_fields)
            deduped_fields.append((field, inherited_from))
    return deduped_fields


def inherited_from_label(parent_refs: List[str]) -> Optional[str]:
    if not parent_refs:
        return None
    return ", ".join(parent_refs)


def build_application_fields(
    application: Dict[str, Any],
    application_index: Dict[str, Dict[str, Any]],
    field_index: Dict[str, Any],
) -> List[FieldView]:
    fields = []
    for field_entry, field_inherited_from in application_field_entries(
        application, application_index
    ):
        fv = build_field_display(field_entry, field_index)
        meta = field_index.get(fv.ref)
        if getattr(meta, "resolved_component", None):
            fv.children = build_field_views_from_items(
                meta.resolved_component.component.items, field_index
            )
        fv.required = field_entry.get("required")
        fv.inherited_from = field_inherited_from
        fields.append(fv)
    return fields


def build_combined_application_fields(
    application: Any,
    field_index: Dict[str, Any],
) -> List[FieldView]:
    return build_field_views_from_items(application.items, field_index)


def build_application_modules(
    application: Dict[str, Any],
    specification: Specification,
    module_index: Dict[str, Any],
    renderer: RenderContext,
) -> List[Dict[str, Any]]:
    app_id = application.get("application")
    parent_refs = application_parent_refs(application)
    own_module_refs = set(application_module_refs(application))
    inherited_from = inherited_from_label(parent_refs)

    if parent_refs:
        module_entries = [
            {
                "module": module.ref,
                "inherited_from": inherited_from
                if module.ref not in own_module_refs
                else None,
            }
            for module in specification.application(app_id).modules
        ]
    else:
        module_entries = application.get("modules", [])

    return build_module_display(module_entries, module_index, renderer)


def build_combined_application_modules(
    application: Any,
    module_index: Dict[str, Any],
    renderer: RenderContext,
) -> List[Dict[str, Any]]:
    module_entries = [{"module": module.ref} for module in application.modules]
    return build_module_display(module_entries, module_index, renderer)


def build_module_display(
    module_entries: List[Any],
    module_index: Dict[str, Any],
    renderer: RenderContext,
) -> List[Dict[str, Any]]:
    modules = []
    for module_entry in module_entries:
        if isinstance(module_entry, str):
            module_entry = {"module": module_entry}
        elif not isinstance(module_entry, dict):
            continue
        module_ref = module_entry.get("module")
        module_obj = module_index.get(module_ref)
        if not module_obj:
            continue
        modules.append(
            {
                "ref": module_obj.ref,
                "name": module_obj.name or module_obj.ref,
                "description": module_obj.description or "",
                "href": renderer.url_for(f"/module/{module_obj.ref}"),
                "required": module_entry.get("required"),
                "inherited_from": module_entry.get("inherited_from"),
            }
        )
    return modules


def build_module_usage_view(
    specification: Any,
    module_ref: str,
    renderer: RenderContext,
) -> Dict[str, List[Dict[str, Any]]]:
    return {
        "applications": [
            {
                "ref": application.ref,
                "name": application.name or application.ref,
                "href": renderer.url_for(f"/application-type/{application.ref}"),
                "is_combined": bool(application.is_combined),
            }
            for application in specification.applications_with_module(module_ref)
        ]
    }


def build_field_usage_view(
    specification: Any,
    field_ref: str,
    renderer: RenderContext,
) -> Dict[str, List[Dict[str, Any]]]:
    usages = specification.field_usages(field_ref)
    return {
        "modules": [
            {
                "ref": match.container.ref,
                "name": match.container.name or match.container.ref,
                "href": renderer.url_for(f"/module/{match.container.ref}"),
            }
            for match in usages.modules
        ],
        "components": [
            {
                "ref": match.container.ref,
                "name": match.container.name or match.container.ref,
                "href": renderer.url_for(f"/component/{match.container.ref}"),
            }
            for match in usages.components
        ],
    }


def build_component_usage_view(
    specification: Any,
    component_ref: str,
    renderer: RenderContext,
) -> Dict[str, List[Dict[str, Any]]]:
    usages = specification.component_usages(component_ref)
    return {
        "fields": [
            {
                "ref": field.ref,
                "name": field.name or field.ref,
                "href": renderer.url_for(f"/field/{field.ref}"),
            }
            for field in usages.fields
        ],
        "modules": [
            {
                "ref": match.container.ref,
                "name": match.container.name or match.container.ref,
                "href": renderer.url_for(f"/module/{match.container.ref}"),
            }
            for match in usages.modules
        ],
    }


def find_modules_using_component(component_ref: str, modules: Dict[str, Any]) -> List[str]:
    refs: List[str] = []
    for mref, m in modules.items():
        items = getattr(m, "items", []) or []
        for item in items:
            if isinstance(item, FieldInstance):
                if getattr(item.original, "component", None) == component_ref:
                    refs.append(mref)
                    break
            elif isinstance(item, ComponentInstance):
                if getattr(item.referenced_by_field.original, "component", None) == component_ref:
                    refs.append(mref)
                    break
    return sorted(set(refs))


def build_codelist_source_link(codelist_ref: str, raw_codelist: Dict[str, Any]) -> str:
    src_obj = raw_codelist.get("source") if hasattr(raw_codelist, "get") else None
    src = None
    if src_obj:
        if isinstance(src_obj, dict):
            src = src_obj.get("src")
        else:
            # if source is a simple string
            src = str(src_obj)
    if src:
        if src.startswith("data/"):
            return f"https://github.com/digital-land/planning-application-data-specification/blob/main/{src}"
        return src
    # default to GitHub CSV
    return f"https://github.com/digital-land/planning-application-data-specification/blob/main/data/codelist/{codelist_ref}.csv"


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
            "commanum": commanum_filter,
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


def create_renderer(
    base_url: str, output_dir: Path
) -> Tuple[jinja2.Environment, RenderContext]:
    env = build_env(base_url or "")
    env.globals["base_url"] = base_url
    renderer = RenderContext(env, base_url, output_dir)
    env.globals["url_for"] = renderer.url_for
    return env, renderer


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


def render_dataset_index(
    renderer: RenderContext,
    page_title: str,
    datasets: List[Dict[str, Any]],
    index_path: str,
    detail_route: str,
    needs_route: str,
) -> None:
    # Decision stage datasets list
    dataset_ctx = {
        "page_title": page_title,
        "datasets": [
            {
                "name": ds.get("name", ds["dataset"]),
                "description": ds.get("description", ""),
                "href": renderer.url_for(f"/{detail_route}/{ds['dataset']}"),
            }
            for ds in datasets
        ],
        "links": {
            "justifications": renderer.url_for("/justification"),
            "needs": renderer.url_for(f"/{needs_route}"),
        },
    }
    dataset_html = renderer.render("dataset_index.html", dataset_ctx)
    renderer.write_page(f"{index_path}/index.html", dataset_html)


def render_index(renderer: RenderContext) -> None:
    # render the main Index page
    index_ctx = {
        "page_title": "Planning application data standard",
        "isHomepage": True,
        "links": {
            "application_types": renderer.url_for("/application-type/"),
            "datasets": renderer.url_for("/dataset/"),
            "data_model": renderer.url_for("/data-model/"),
            "national_public_view": renderer.url_for("/national-public-view/"),
            "github_feedback": "https://github.com/digital-land/planning-application-data-specification/issues/new",
        },
    }
    index_html = renderer.render("index.html", index_ctx)
    renderer.write_page("index.html", index_html)


def render_data_model(renderer: RenderContext) -> None:
    data_model_ctx = {
        "page_title": "Data model",
        "links": {
            "application_types": renderer.url_for("/application-type/"),
            "modules": renderer.url_for("/module/"),
            "components": renderer.url_for("/component/"),
            "fields": renderer.url_for("/field/"),
            "codelists": renderer.url_for("/codelist/"),
            "datasets": renderer.url_for("/dataset/"),
            "design_decisions": renderer.url_for("/design-decision/"),
        },
    }
    data_model_html = renderer.render("data_model.html", data_model_ctx)
    renderer.write_page("data-model/index.html", data_model_html)


def render_national_public_view(renderer: RenderContext) -> None:
    public_view_html = renderer.render(
        "national_public_view.html",
        {"page_title": "National public view"},
    )
    renderer.write_page("national-public-view/index.html", public_view_html)


def render_design_decisions(
    renderer: RenderContext,
    design_decisions: List[Dict[str, Any]],
) -> None:
    decisions = [
        {
            **decision,
            "href": renderer.url_for(f"/design-decision/{decision['slug']}"),
            "feedback_href": design_decision_feedback_url(decision),
        }
        for decision in design_decisions
    ]
    index_html = renderer.render(
        "design_decision_index.html",
        {
            "page_title": "Design decisions",
            "decisions": decisions,
        },
    )
    renderer.write_page("design-decision/index.html", index_html)

    for decision in decisions:
        detail_html = renderer.render(
            "design_decision_detail.html",
            {
                "page_title": f"Design decision {decision['decision_id']}",
                "decision": decision,
            },
        )
        renderer.write_page(
            f"design-decision/{decision['slug']}/index.html", detail_html
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
                    f'<a class="govuk-link" href="{renderer.url_for(f"/user-need/{n}")}">{n}</a>'
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


def build_submission_progress_data(
    input_path: Path = DEFAULT_PROGRESS_INPUT,
) -> Dict[str, Any]:
    return build_progress_view_model(input_path=input_path)


def render_submission_progress_data(
    renderer: RenderContext,
    input_path: Path = DEFAULT_PROGRESS_INPUT,
) -> None:
    progress_data = build_submission_progress_data(input_path=input_path)
    renderer.write_page(
        "submissions/progress/data.json", json.dumps(progress_data, indent=2)
    )


def render_submission_progress_page(
    renderer: RenderContext,
    input_path: Path = DEFAULT_PROGRESS_INPUT,
) -> None:
    progress_data = build_submission_progress_data(input_path=input_path)

    def prepare_rows(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        prepared: List[Dict[str, Any]] = []
        for row in rows:
            refs = row.get("refs", []) or []
            trailing = f"({','.join(refs)})" if refs else ""
            display_name = row.get("label", "")
            if trailing and display_name.endswith(trailing):
                display_name = display_name[: -len(trailing)].rstrip()
            prepared.append(
                {
                    **row,
                    "display_name": display_name,
                    "refs_with_href": [
                        {
                            "ref": ref,
                            "href": renderer.url_for(f"/application-type/{ref}"),
                        }
                        for ref in refs
                    ],
                    "used_for_inheritance": "Inheritance-only application type"
                    in (row.get("notes") or ""),
                }
            )
        return prepared

    progress_ctx = {
        "page_title": "Submission progress",
        "summary": progress_data["summary"],
        "covered_rows": prepare_rows(progress_data["covered_by_spec"]),
        "not_covered_rows": prepare_rows(progress_data["not_covered_by_spec"]),
        "links": {
            "home": renderer.url_for("/"),
            "back": renderer.url_for("/application-type"),
            "application_types": renderer.url_for("/application-type"),
            "github_issue_url": "https://github.com/digital-land/planning-application-data-specification/issues/new?title=Feedback%20on%20submission%20progress%20page",
            "github_edit_url": "https://github.com/digital-land/planning-application-data-specification/edit/main/bin/templates/submission_progress.html",
        },
    }
    progress_html = renderer.render("submission_progress.html", progress_ctx)
    renderer.write_page("submissions/progress/index.html", progress_html)


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

    env, renderer = create_renderer(base_url, output_dir)

    try:
        spec_model = load_specification_model()
        spec_tables = spec_model.get("tables", {})
        field_index = spec_model.get("fields", {})
        dataset_index = spec_model.get("tables", {}).get("dataset", {})
        module_index = spec_model.get("modules", {})
        codelist_index = spec_model.get("tables", {}).get("codelist", {})
        component_index = spec_model.get("components", {})
        specification = Specification.load(root_dir)

        decision_stage = load_decision_stage(spec_root / "decision-stage.schema.md")
        decision_datasets: List[Dict[str, Any]] = []
        for ds in decision_stage.get("datasets", []):
            dataset_id = ds.get("dataset")
            dataset_meta = dataset_index.get(dataset_id, {})
            merged = dict(dataset_meta)
            merged.update(ds)
            decision_datasets.append(merged)

        applications = load_submission_applications(spec_root)
        application_index = {
            application.get("application"): application
            for application in applications
            if application.get("application")
        }
        combined_applications = load_active_combined_applications(spec_root)
        design_decisions = load_design_decisions(root_dir / "documentation")

        needs_data = load_needs()
        need_records = list(needs_data.get("need", {}).values())
        need_records.sort(key=lambda n: n.get("need", ""))
        need_to_justifications, dataset_to_need_justifications = build_need_maps(
            needs_data
        )

        # Index
        render_index(renderer)
        render_data_model(renderer)
        render_national_public_view(renderer)
        render_design_decisions(renderer, design_decisions)

        # Datasets
        render_dataset_index(
            renderer,
            "Datasets",
            decision_datasets,
            "dataset",
            "dataset",
            "user-need",
        )

        # Decision stage needs list
        needs_ctx = {
            "page_title": "Decision stage needs",
            "needs": [
                {
                    "id": need.get("need"),
                    "name": need.get("name", ""),
                    "statement": need.get("statement") or need.get("name") or "",
                    "href": renderer.url_for(f"/user-need/{need.get('need')}"),
                    **need_status_dict(
                        need_to_justifications.get(need.get("need"), [])
                    ),
                }
                for need in need_records
            ],
        }
        needs_html = env.get_template("needs_index.html").render(**needs_ctx)
        renderer.write_page("user-need/index.html", needs_html)

        # Decision stage need detail pages
        need_template = env.get_template("need_detail.html")
        for need in need_records:
            n_id = need.get("need")
            justs = need_to_justifications.get(n_id, [])
            label, cls = need_status(justs)
            need_meta = build_need_meta(need)
            need_ctx = {
                "need_ref": n_id,
                "page_title": f"Need {n_id}",
                "links": {"back": renderer.url_for("/user-need")},
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
                        "satisfied_by": j.get("satisfied_by"),
                        "href": renderer.url_for(f"/justification/{j.get('id', '')}"),
                    }
                    for j in justs
                ],
            }
            need_html = need_template.render(**need_ctx)
            renderer.write_page(f"user-need/{n_id}/index.html", need_html)

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
            raw_fields = ds.get("fields", [])
            # build FieldViews and attach children for component refs
            for f in raw_fields:
                fv = build_field_display(f, field_index)
                # attach children if this field references a component
                meta = field_index.get(fv.ref)
                if getattr(meta, "resolved_component", None):
                    fv.children = build_field_views_from_items(
                        meta.resolved_component.component.items, field_index
                    )
                target_dataset = getattr(f, "get", lambda k, default=None: f.get(k, default))(
                    "dataset", None
                )
                fv.description = render_markdown(fv.description or "")
                fv.target_dataset = target_dataset
                fv.target_dataset_href = (
                    renderer.url_for(f"/dataset/{target_dataset}")
                    if target_dataset
                    else ""
                )
                fv.satisfactions = satisfaction_messages_for_field(
                    all_need_justs, ds_id, fv.ref, renderer
                )
                fields.append(fv)
            dataset_ctx = {
                "page_title": f"Dataset {ds_id}",
                "links": {"back": renderer.url_for("/dataset")},
                "title": ds.get("name", ds_id),
                "description": ds.get("description", ""),
                "fields": fields,
                "needs": [
                    {
                        "need_id": item["need"],
                        "need_href": renderer.url_for(f"/user-need/{item['need']}"),
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
            renderer.write_page(f"dataset/{ds_id}/index.html", dataset_page)

        # Submission index
        submission_ctx = {
            "page_title": "Application types",
            "links": {
                "progress": renderer.url_for("/submissions/progress"),
                "combined_application_decision": renderer.url_for(
                    "/design-decision/0012-use-a-controlled-list-for-combined-application-types/"
                ),
            },
            "applications": [
                {
                    "name": app.get("name", app.get("application")),
                    "description": app.get("description", ""),
                    "href": renderer.url_for(
                        f"/application-type/{app.get('application')}"
                    ),
                }
                for app in applications
                if not app.get("base-type")
            ],
            "combined_applications": [
                {
                    "name": app.get("name", app.get("application-types")),
                    "description": app.get("description", ""),
                    "href": renderer.url_for(
                        f"/application-type/{app.get('application-types')}"
                    ),
                }
                for app in combined_applications
            ],
        }
        submission_html = env.get_template("submission_index.html").render(
            **submission_ctx
        )
        renderer.write_page("application-type/index.html", submission_html)

        # Submission progress data seed for /submission/progress page build-out.
        render_submission_progress_data(renderer)
        render_submission_progress_page(renderer)

        # Submission module index and detail pages
        submission_modules = list(spec_model.get("modules", {}).values())
        submission_modules.sort(key=lambda m: m.name or m.ref)
        module_index_ctx = {
            "page_title": "Modules",
            "links": {"back": renderer.url_for("/data-model")},
            "modules": [
                {
                    "ref": m.ref,
                    "name": m.name or m.ref,
                    "description": m.description or "",
                    "href": renderer.url_for(f"/module/{m.ref}"),
                }
                for m in submission_modules
            ],
        }
        module_index_html = env.get_template("module_index.html").render(
            **module_index_ctx
        )
        renderer.write_page("module/index.html", module_index_html)

        module_template = env.get_template("module_detail.html")
        for m in submission_modules:
            mod_fields = build_field_views_from_items(m.items, field_index)
            rules = spec_tables.get("module", {}).get(m.ref, {}).get("rules", [])
            module_ctx = {
                "page_title": f"Module {m.ref}",
                "ref": m.ref,
                "name": m.name or m.ref,
                "description": m.description or "",
                "fields": mod_fields,
                "rules": rules,
                "usage": build_module_usage_view(specification, m.ref, renderer),
                "links": {"back": renderer.url_for("/module")},
            }
            module_html = module_template.render(**module_ctx)
            renderer.write_page(f"module/{m.ref}/index.html", module_html)

        # Component index and detail pages
        component_index_ctx = {
            "page_title": "Components",
            "components": [
                {
                    "ref": c.ref,
                    "name": c.name or c.ref,
                    "description": c.description or "",
                    "href": renderer.url_for(f"/component/{c.ref}"),
                }
                for c in sorted(component_index.values(), key=lambda c: c.ref)
            ],
            "breadcrumbs": [],
        }
        comp_index_html = env.get_template("component_index.html").render(
            **component_index_ctx
        )
        renderer.write_page("component/index.html", comp_index_html)

        comp_template = env.get_template("component_detail.html")
        raw_components = spec_tables.get("component", {})
        for cref, comp in component_index.items():
            comp_fields = build_field_views_from_items(comp.items, field_index)
            comp_rules = raw_components.get(cref, {}).get("rules", [])
            module_refs = find_modules_using_component(cref, module_index)
            modules_list = [
                {
                    "ref": mr,
                    "name": getattr(module_index.get(mr), "name", mr),
                    "href": renderer.url_for(f"/module/{mr}"),
                }
                for mr in module_refs
                if mr in module_index
            ]
            comp_ctx = {
                "page_title": f"Component {cref}",
                "ref": cref,
                "name": comp.name or comp.ref,
                "description": comp.description or "",
                "fields": comp_fields,
                "rules": comp_rules,
                "modules": modules_list,
                "breadcrumbs": [],
            }
            comp_html = comp_template.render(**comp_ctx)
            renderer.write_page(f"component/{cref}/index.html", comp_html)

        # Codelist index and detail pages
        codelists_raw = spec_tables.get("codelist", {})
        codelists_list = sorted(codelists_raw.values(), key=lambda c: c.get("codelist"))
        codelist_index_ctx = {
            "page_title": "Codelists",
            "codelists": [
                {
                    "ref": c.get("codelist"),
                    "codelist": c.get("codelist"),
                    "name": c.get("name", c.get("codelist")),
                    "description": c.get("description", ""),
                    "href": renderer.url_for(f"/codelist/{c.get('codelist')}"),
                }
                for c in codelists_list
            ],
        }
        codelist_index_html = env.get_template("codelist_index.html").render(
            **codelist_index_ctx
        )
        renderer.write_page("codelist/index.html", codelist_index_html)

        cl_detail_template = env.get_template("codelist_detail.html")
        for c in codelists_list:
            cref = c.get("codelist")
            source_link = build_codelist_source_link(cref, c)
            cl_ctx = {
                "page_title": f"Codelist {cref}",
                "codelist": c,
                "source_link": source_link,
            }
            cl_html = cl_detail_template.render(**cl_ctx)
            renderer.write_page(f"codelist/{cref}/index.html", cl_html)

        # Fields index and detail pages
        fields_index_ctx = {
            "page_title": "Fields",
            "fields": [
                {
                    "ref": f.ref,
                    "name": f.name,
                    "description": f.description,
                    "href": renderer.url_for(f"/field/{f.ref}"),
                }
                for f in sorted(field_index.values(), key=lambda f: f.ref)
            ],
        }
        fields_index_html = env.get_template("fields_index.html").render(
            **fields_index_ctx
        )
        renderer.write_page("field/index.html", fields_index_html)

        field_detail_template = env.get_template("field_detail.html")
        for f in field_index.values():
            ctx = {
                "page_title": f"Field {f.ref}",
                "field": f,
                "usage": build_field_usage_view(specification, f.ref, renderer),
            }
            field_html = field_detail_template.render(**ctx)
            renderer.write_page(f"field/{f.ref}/index.html", field_html)

        # Submission application detail pages
        app_template = env.get_template("submission_application_detail.html")
        for app in applications:
            app_id = app.get("application")
            app_ctx = {
                "page_title": f"Application {app_id}",
                "title": app.get("name", app_id),
                "description": app.get("description", ""),
                "application": app_id,
                "application_types": [],
                "base_type": app.get("base-type", False),
                "extends": {
                    "ref": app.get("extends"),
                    "href": renderer.url_for(f"/application-type/{app.get('extends')}"),
                }
                if app.get("extends")
                else None,
                "synonyms": app.get("synonyms", []),
                "notes": app.get("notes", ""),
                "entry_date": app.get("entry-date", ""),
                "legislation": app.get("legislation", []),
                "fields": build_application_fields(
                    app, application_index, field_index
                ),
                "modules": build_application_modules(
                    app, specification, module_index, renderer
                ),
                "links": {"back": renderer.url_for("/application-type")},
            }
            app_html = app_template.render(**app_ctx)
            renderer.write_page(f"application-type/{app_id}/index.html", app_html)

        for combined in combined_applications:
            application_types = combined.get("application-types")
            if not application_types:
                continue

            application = specification.application(application_types)
            app_ctx = {
                "page_title": f"Application {application.ref}",
                "title": application.name,
                "description": application.description,
                "application": application.ref,
                "application_types": application.application_types,
                "base_type": False,
                "extends": None,
                "synonyms": [],
                "notes": application.notes,
                "entry_date": application.entry_date,
                "legislation": [],
                "fields": build_combined_application_fields(
                    application, field_index
                ),
                "modules": build_combined_application_modules(
                    application, module_index, renderer
                ),
                "links": {"back": renderer.url_for("/application-type")},
            }
            app_html = app_template.render(**app_ctx)
            renderer.write_page(
                f"application-type/{application.ref}/index.html", app_html
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
                    f'<a class="govuk-link" href="{renderer.url_for(f"/user-need/{n}")}">{n}</a>'
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
            "needs": [
                f"user-need/{n.get('need')}/index.html" for n in need_records
            ],
            "datasets": [
                f"dataset/{ds.get('dataset')}/index.html"
                for ds in decision_datasets
            ],
            "application_types": "application-type/index.html",
            "submission_progress": "submissions/progress/index.html",
            "data_model": "data-model/index.html",
            "national_public_view": "national-public-view/index.html",
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
