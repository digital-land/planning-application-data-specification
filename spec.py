# spec.py
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
# Ensure both the project root and bin/ are on sys.path so modules that expect
# to be run from bin/ (e.g. `import csv_helpers`) continue to work.
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "bin"))

import click
from bin.applications import get_application_module_refs, get_applications_with_module
from bin.completeness import (
    build_progress_view_model,
    calculate_scope_summary,
    evaluate_scope,
)
from bin.csv_helpers import read_csv
from bin.fields import find_field_usage
from bin.forms import FORMS_2025_FILEPATH
from bin.loader import load_content, load_needs


@click.group()
@click.option(
    "--spec-dir", default="specification", help="Path to specification directory"
)
@click.pass_context
def cli(ctx, spec_dir):
    """Planning application data specification CLI."""
    ctx.ensure_object(dict)
    ctx.obj["spec_dir"] = Path(spec_dir)


@cli.group()
def find():
    """Find and query specification elements."""
    pass


# Find subcommands
@find.command()
@click.argument("module_ref")
def applications_with_module(module_ref):
    """Find applications that use a specific module."""
    spec = load_content()
    apps = get_applications_with_module(module_ref, spec)

    if apps:
        click.echo(f"Applications using module '{module_ref}':")
        for app_ref in apps:
            app = spec["application"].get(app_ref, {})
            name = app.get("name", app_ref)
            click.echo(f"  • {app_ref}: {name}")
    else:
        click.echo(f"No applications found using module '{module_ref}'")


@find.command()
@click.argument("application_ref")
def modules_in_application(application_ref):
    """Find all modules used by a specific application."""
    spec = load_content()
    modules = get_application_module_refs(application_ref, spec)

    if modules:
        click.echo(f"Modules in application '{application_ref}':")
        for mod_ref in modules:
            mod = spec.get("module", {}).get(mod_ref, {})
            name = mod.get("name", mod_ref)
            click.echo(f"  • {mod_ref}: {name}")
    else:
        click.echo(f"No modules found for application '{application_ref}'")


@find.command()
@click.argument("field_ref")
def field_usage(field_ref):
    """Find modules and components that include a given field."""
    spec = load_content()
    usage = find_field_usage(field_ref, spec)
    module_hits = usage["modules"]
    component_hits = usage["components"]

    if not module_hits and not component_hits:
        click.echo(f"No modules or components found using field '{field_ref}'")
        return

    if module_hits:
        click.echo(f"Modules using field '{field_ref}':")
        for ref, name in module_hits:
            click.echo(f"  • {ref}: {name}")

    if component_hits:
        if module_hits:
            click.echo()
        click.echo(f"Components using field '{field_ref}':")
        for ref, name in component_hits:
            click.echo(f"  • {ref}: {name}")


@find.command()
@click.argument("component_ref")
def component_usage(component_ref):
    """Find fields and modules that use a given component."""
    spec = load_content()
    fields = spec.get("field", {}) or {}
    modules = spec.get("module", {}) or {}

    field_hits = []
    for ref, field in fields.items():
        if field.get("component") == component_ref:
            name = field.get("name", ref)
            field_hits.append((ref, name))
    field_hits.sort(key=lambda item: item[0])

    module_hits = []
    field_refs = {ref for ref, _ in field_hits}
    if field_refs:
        for ref, mod in modules.items():
            entries = mod.get("fields") if hasattr(mod, "get") else None
            if not isinstance(entries, list):
                continue
            for entry in entries:
                entry_ref = entry if isinstance(entry, str) else entry.get("field")
                if entry_ref in field_refs:
                    name = mod.get("name", ref) if hasattr(mod, "get") else ref
                    module_hits.append((ref, name))
                    break
    module_hits.sort(key=lambda item: item[0])

    if not field_hits and not module_hits:
        click.echo(f"No fields or modules found using component '{component_ref}'")
        return

    if field_hits:
        click.echo(f"Fields using component '{component_ref}':")
        for ref, name in field_hits:
            click.echo(f"  • {ref}: {name}")

    if module_hits:
        if field_hits:
            click.echo()
        click.echo(f"Modules using component '{component_ref}':")
        for ref, name in module_hits:
            click.echo(f"  • {ref}: {name}")


# TODO: find all fields that reference a given codelist
# TODO: find all fields that reference a given component
# TODO: find all fields that are not used anywhere


@cli.group()
def decision():
    """Decision-stage reporting."""
    pass


@decision.command()
@click.option("--list", "do_list", is_flag=True, help="List covered need ids")
def summary(do_list):
    """Summarise decision-stage needs coverage by justifications."""
    needs_data = load_needs()
    needs = needs_data.get("need", {})
    justs = needs_data.get("justification", {})

    covered = {}
    for jid, j in justs.items():
        for n in j.get("needs", []):
            covered.setdefault(n, set()).add(jid)

    total_needs = len(needs)
    total_covered = len(covered.keys())
    click.echo(
        f"Decision-stage needs covered by justifications: {total_covered}/{total_needs}"
    )
    if do_list and covered:
        click.echo("Covered needs:")
        for nid in sorted(covered.keys()):
            jids = sorted(covered[nid])
            jlabel = f" ({', '.join(jids)})" if jids else ""
            click.echo(f"  • {nid}{jlabel}")


@cli.command()
@click.argument("application_type")
def form_url(application_type):
    """Return the PDF form URL for an application type or subtype."""
    forms_path = PROJECT_ROOT / FORMS_2025_FILEPATH
    rows = read_csv(str(forms_path), as_dict=True)
    query = application_type.strip().lower()
    matches = []

    for row in rows:
        raw_types = row.get("application-types", "")
        types = [t.strip().lower() for t in raw_types.split(";") if t.strip()]
        if query in types:
            matches.append(row)

    if not matches:
        click.echo(f"No form found for application type '{application_type}'")
        return

    def format_types(raw: str) -> str:
        items = [t.strip() for t in raw.split(";") if t.strip()]
        return " + ".join(items) if items else raw.strip()

    formatted = []
    for row in matches:
        url = row.get("document-url", "")
        app_types = format_types(row.get("application-types", ""))
        formatted.append(f"- application-type: {app_types}\n  form: {url}")

    click.echo("\n\n".join(formatted))


@cli.group(invoke_without_command=True)
@click.option(
    "--input",
    "input_path",
    default="bin/admin_data/2024-application-volumes.csv",
    show_default=True,
    help="Path to completeness source CSV",
)
@click.option(
    "--combined-apps-covered",
    is_flag=True,
    help="Treat combined application rows as covered when all component refs exist in the specification",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print in-scope rows split by covered-by-spec status, ordered by volume",
)
@click.pass_context
def completeness(ctx, input_path, combined_apps_covered, verbose):
    """Completeness reporting."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(
            completeness_summary,
            input_path=input_path,
            combined_apps_covered=combined_apps_covered,
            verbose=verbose,
        )


@completeness.command(name="summary")
@click.option(
    "--input",
    "input_path",
    default="bin/admin_data/2024-application-volumes.csv",
    show_default=True,
    help="Path to completeness source CSV",
)
@click.option(
    "--combined-apps-covered",
    is_flag=True,
    help="Treat combined application rows as covered when all component refs exist in the specification",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print in-scope rows split by covered-by-spec status, ordered by volume",
)
def completeness_summary(input_path, combined_apps_covered, verbose):
    """Print completeness summary including covered volume and percentage."""
    result = calculate_scope_summary(
        Path(input_path), combined_apps_covered=combined_apps_covered
    )

    click.echo("Completeness summary")
    click.echo("====================")
    click.echo(f"Input CSV: {result['input']}")
    click.echo(f"Total rows: {result['total_rows']}")
    click.echo(f"In-scope rows: {result['in_scope_rows']}")
    click.echo(f"Out-of-scope rows: {result['out_of_scope_rows']}")
    click.echo(f"Total 2024 volume: {result['total_2024_volume']}")
    click.echo(f"In-scope 2024 volume: {result['in_scope_2024_volume']}")
    click.echo(f"Volume covered by spec: {result['covered_2024_volume']}")
    click.echo(f"Completeness: {result['completeness_pct']}%")

    if not verbose:
        return

    progress = build_progress_view_model(
        Path(input_path), combined_apps_covered=combined_apps_covered
    )
    covered = progress["covered_by_spec"]
    not_covered = progress["not_covered_by_spec"]

    click.echo()
    click.echo("Covered by spec")
    click.echo("===============")
    for row in covered:
        click.echo(f"{row['label']} | volume: {row['volume']}")

    click.echo()
    click.echo("Not covered by spec")
    click.echo("===================")
    for row in not_covered:
        click.echo(f"{row['label']} | volume: {row['volume']}")


@completeness.command()
@click.option(
    "--input",
    "input_path",
    default="bin/admin_data/2024-application-volumes.csv",
    show_default=True,
    help="Path to completeness source CSV",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Print in-scope and out-of-scope lists",
)
@click.option(
    "--combined-apps-covered",
    is_flag=True,
    help="Treat combined application rows as covered when all component refs exist in the specification",
)
def scope(input_path, verbose, combined_apps_covered):
    """Summarise in-scope and out-of-scope application types for completeness."""
    result = evaluate_scope(
        Path(input_path), combined_apps_covered=combined_apps_covered
    )
    in_scope = result["in_scope"]
    out_of_scope = result["out_of_scope"]

    total_rows = len(in_scope) + len(out_of_scope)
    in_scope_rows = len(in_scope)
    out_of_scope_rows = len(out_of_scope)
    summary_data = calculate_scope_summary(
        Path(input_path), combined_apps_covered=combined_apps_covered
    )
    total_volume = summary_data["total_2024_volume"]
    in_scope_volume = summary_data["in_scope_2024_volume"]

    click.echo("Completeness scope summary")
    click.echo("==========================")
    click.echo(f"Input CSV: {input_path}")
    click.echo(f"Total rows: {total_rows}")
    click.echo(f"In-scope rows: {in_scope_rows}")
    click.echo(f"Out-of-scope rows: {out_of_scope_rows}")
    click.echo(f"Total 2024 volume: {total_volume}")
    click.echo(f"In-scope 2024 volume: {in_scope_volume}")

    if not verbose:
        return

    click.echo()
    click.echo("In-scope application types")
    click.echo("==========================")
    for item in in_scope:
        app_types = ",".join(item["application-types"])
        notes = f" | notes: {item['notes']}" if item.get("notes") else ""
        covered = "yes" if item.get("covered-by-spec") else "no"
        if item["name"].startswith("Form: ") or item["name"].endswith(f"({app_types})"):
            click.echo(
                f"- {item['name']} | volume: {item['volume']} | covered-by-spec: {covered}{notes}"
            )
        else:
            click.echo(
                f"- {item['name']} ({app_types}) | volume: {item['volume']} | covered-by-spec: {covered}{notes}"
            )

    click.echo()
    click.echo("Out-of-scope application types")
    click.echo("==============================")
    for item in out_of_scope:
        app_types = ",".join(item["application-types"])
        notes = f" | notes: {item['notes']}" if item.get("notes") else ""
        click.echo(f"- {item['name']} ({app_types}){notes}")


if __name__ == "__main__":
    cli()
