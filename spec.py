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
from bin.forms import (
    get_2025_form,
    get_2025_forms_by_app_type,
    get_2025_forms_for_module,
    get_2025_modules_for_form,
)
from bin.loader import load_content, load_needs
from planning_application_specification import Specification
from planning_application_specification.models import ComponentUsage, FieldUsage


def get_spec_summary_counts():
    spec = load_content()
    keys = [
        ("applications", "application"),
        ("modules", "module"),
        ("fields", "field"),
        ("components", "component"),
        ("codelists", "codelist"),
        ("datasets", "dataset"),
        ("specifications", "specification"),
    ]
    return [(label, len(spec.get(table_name, {}) or {})) for label, table_name in keys]


def format_spec_summary(markdown=False):
    counts = get_spec_summary_counts()

    if markdown:
        lines = ["# Specification summary", ""]
        lines.extend(f"- **{label.capitalize()}**: {count}" for label, count in counts)
        return "\n".join(lines)

    return "\n".join(f"{label}: {count}" for label, count in counts)


def print_2025_form_urls(application_type):
    matches = get_2025_forms_by_app_type(application_type)

    if not matches:
        click.echo(f"No form found for application type '{application_type}'")
        return

    def format_types(values) -> str:
        if isinstance(values, list):
            items = values
        else:
            items = [t.strip() for t in str(values).split(";") if t.strip()]
        return " + ".join(items) if items else str(values).strip()

    formatted = []
    for form in matches:
        url = form.get("document-url", "")
        app_types = format_types(form.get("application-types", ""))
        formatted.append(f"- application-type: {app_types}\n  form: {url}")

    click.echo("\n\n".join(formatted))


def print_2025_forms_for_application_type(application_type):
    forms = get_2025_forms_by_app_type(application_type.strip().lower())

    if not forms:
        click.echo(f"No 2025 forms found for application type '{application_type}'")
        return

    click.echo(
        f"Found {len(forms)} matching 2025 forms for application type '{application_type}':"
    )
    for form in forms:
        click.echo(f"- {form['name']} ({form['reference']})")
        click.echo(f"  form: {form['document-url']}")


def _format_application_item(item) -> str:
    if isinstance(item, FieldUsage):
        field_ref = item.original.ref
        required = item.overrides.get("required")
        suffix = " (required)" if required is True else ""
        return f"- field: {field_ref}{suffix}"

    if isinstance(item, ComponentUsage):
        component_ref = item.component.ref
        referenced_by = item.referenced_by_field
        if isinstance(referenced_by, FieldUsage):
            return f"- component: {component_ref} (via field: {referenced_by.original.ref})"
        return f"- component: {component_ref}"

    return f"- item: {item}"


def _format_container_item(item) -> str:
    if isinstance(item, FieldUsage):
        field_ref = item.original.ref
        field_name = item.overrides.get("name") or item.original.name
        return f"- field: {field_ref} ({field_name})"

    if isinstance(item, ComponentUsage):
        component_ref = item.component.ref
        component_name = item.component.name
        referenced_by = item.referenced_by_field
        if isinstance(referenced_by, FieldUsage):
            return (
                f"- component: {component_ref} ({component_name}) "
                f"(via field: {referenced_by.original.ref})"
            )
        return f"- component: {component_ref} ({component_name})"

    return f"- item: {item}"


def print_application_details(application_ref):
    spec = Specification.load(PROJECT_ROOT)
    application = spec.application(application_ref)

    click.echo(f"Application: {application.ref}")
    click.echo(f"Name: {application.name}")
    if application.description:
        click.echo(f"Description: {application.description}")
    click.echo(f"Application types: {', '.join(application.application_types)}")
    click.echo(f"Combined: {'yes' if application.is_combined else 'no'}")
    if application.notes:
        click.echo(f"Notes: {application.notes}")

    click.echo("Application items:")
    if application.items:
        for item in application.items:
            click.echo(_format_application_item(item))
    else:
        click.echo("- none")

    module_count = len(application.modules)
    click.echo(f"Modules: {module_count}")
    if application.modules:
        for module in application.modules:
            click.echo(f"- {module.ref}: {module.name}")
    else:
        click.echo("- none")


def print_field_details(field_ref):
    spec = Specification.load(PROJECT_ROOT)
    field = spec.field(field_ref)

    click.echo(f"Field: {field.ref}")
    click.echo(f"Name: {field.name}")
    click.echo(f"Datatype: {field.datatype}")
    click.echo(f"Required: {'yes' if field.required else 'no'}")
    click.echo(f"Cardinality: {field.cardinality}")
    if field.component:
        click.echo(f"Component: {field.component}")
    if field.description:
        click.echo(f"Description: {field.description}")
    if field.notes:
        click.echo(f"Notes: {field.notes}")
    if field.entry_date:
        click.echo(f"Entry date: {field.entry_date}")
    if field.end_date:
        click.echo(f"End date: {field.end_date}")


def print_module_details(module_ref):
    spec = Specification.load(PROJECT_ROOT)
    module = spec.module(module_ref)

    click.echo(f"Module: {module.ref}")
    click.echo(f"Name: {module.name}")
    if module.description:
        click.echo(f"Description: {module.description}")
    click.echo(f"Field usages: {len(module.field_usages)}")
    click.echo(f"Component usages: {len(module.component_usages)}")
    if module.entry_date:
        click.echo(f"Entry date: {module.entry_date}")
    if module.end_date:
        click.echo(f"End date: {module.end_date}")

    click.echo("Top-level items:")
    if module.items:
        for item in module.items:
            click.echo(_format_container_item(item))
    else:
        click.echo("- none")


def print_component_details(component_ref):
    spec = Specification.load(PROJECT_ROOT)
    component = spec.component(component_ref)

    click.echo(f"Component: {component.ref}")
    click.echo(f"Name: {component.name}")
    if component.description:
        click.echo(f"Description: {component.description}")
    click.echo(f"Field usages: {len(component.field_usages)}")
    click.echo(f"Component usages: {len(component.component_usages)}")
    if component.entry_date:
        click.echo(f"Entry date: {component.entry_date}")
    if component.end_date:
        click.echo(f"End date: {component.end_date}")

    click.echo("Top-level items:")
    if component.items:
        for item in component.items:
            click.echo(_format_container_item(item))
    else:
        click.echo("- none")


def print_codelist_details(codelist_ref):
    spec = Specification.load(PROJECT_ROOT)
    codelist = spec.codelist(codelist_ref)

    click.echo(f"Codelist: {codelist.ref}")
    click.echo(f"Name: {codelist.name}")
    if codelist.description:
        click.echo(f"Description: {codelist.description}")
    click.echo(f"Items: {len(codelist.items)}")

    click.echo("Items preview:")
    if codelist.items:
        for item in codelist.items[:10]:
            line = f"- {item.reference}: {item.name}"
            if item.parent:
                line += f" (parent: {item.parent})"
            click.echo(line)
        if len(codelist.items) > 10:
            click.echo(f"- ... {len(codelist.items) - 10} more")
    else:
        click.echo("- none")


def print_2025_form_details(form_ref):
    form = get_2025_form(form_ref.strip())

    if not form:
        click.echo(f"No 2025 form found with reference '{form_ref}'")
        return

    app_types = ", ".join(form.get("application-types", []))

    click.echo(f"Form: {form['name']}")
    click.echo(f"Reference: {form['reference']}")
    click.echo(f"Application types: {app_types}")
    click.echo(f"Document URL: {form['document-url']}")


def print_2025_forms_for_module(module_ref):
    forms = get_2025_forms_for_module(module_ref.strip())

    if not forms:
        click.echo(f"No analysed 2025 forms found for module '{module_ref}'")
        return

    click.echo(f"Found {len(forms)} analysed 2025 forms for module '{module_ref}':")
    click.echo(
        "These results come from the 2025 forms analysis data, not the specification model."
    )
    for form in forms:
        click.echo(f"- {form['name']} ({form['reference']})")
        click.echo(f"  form: {form['document-url']}")


def print_2025_modules_for_form(form_ref):
    modules = get_2025_modules_for_form(form_ref.strip())

    if not modules:
        click.echo(f"No analysed 2025 modules found for form '{form_ref}'")
        return

    click.echo(f"Found {len(modules)} analysed 2025 modules for form '{form_ref}':")
    click.echo(
        "These results come from the 2025 forms analysis data, not the specification model."
    )
    for module in modules:
        click.echo(f"- {module['name']} ({module['reference']})")


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
def inspect():
    """Inspect canonical specification elements."""
    pass


# Inspect subcommands
@inspect.command()
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


@inspect.command()
@click.argument("application_ref")
def modules_in_application(application_ref):
    """Find all modules used by a specific application."""
    spec = load_content()
    modules = get_application_module_refs(application_ref, spec)

    if modules:
        click.echo(f"Modules in application '{application_ref}' ({len(modules)}):")
        for mod_ref in modules:
            mod = spec.get("module", {}).get(mod_ref, {})
            name = mod.get("name", mod_ref)
            click.echo(f"  • {mod_ref}: {name}")
    else:
        click.echo(f"No modules found for application '{application_ref}'")


@inspect.command(name="application")
@click.argument("application_ref")
def find_application(application_ref):
    """Show a resolved application definition."""
    print_application_details(application_ref)


@inspect.command(name="module")
@click.argument("module_ref")
def inspect_module(module_ref):
    """Show a canonical module definition."""
    print_module_details(module_ref)


@inspect.command(name="component")
@click.argument("component_ref")
def inspect_component(component_ref):
    """Show a canonical component definition."""
    print_component_details(component_ref)


@inspect.command(name="field")
@click.argument("field_ref")
def inspect_field(field_ref):
    """Show a canonical field definition."""
    print_field_details(field_ref)


@inspect.command(name="codelist")
@click.argument("codelist_ref")
def inspect_codelist(codelist_ref):
    """Show a canonical codelist definition."""
    print_codelist_details(codelist_ref)


@inspect.command()
@click.argument("field_ref")
def field_usage(field_ref):
    """Find modules and components that include a given field."""
    spec = Specification.load(PROJECT_ROOT)
    usage = spec.field_usages(field_ref)
    module_hits = usage.modules
    component_hits = usage.components

    if not module_hits and not component_hits:
        click.echo(f"No modules or components found using field '{field_ref}'")
        return

    if module_hits:
        click.echo(f"Modules using field '{field_ref}':")
        for match in module_hits:
            click.echo(f"  • {match.container.ref}: {match.container.name}")

    if component_hits:
        if module_hits:
            click.echo()
        click.echo(f"Components using field '{field_ref}':")
        for match in component_hits:
            click.echo(f"  • {match.container.ref}: {match.container.name}")


@inspect.command()
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
def report():
    """Repository reporting commands."""
    pass


@report.group()
def decision():
    """Decision-stage reporting."""
    pass


@report.command(name="summary")
@click.option("--markdown", is_flag=True, help="Print the summary in markdown format")
def spec_summary(markdown):
    """Print a summary of loaded specification record counts."""
    click.echo(format_spec_summary(markdown=markdown))


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
            need = needs.get(nid, {})
            name = need.get("name", "")
            if name:
                click.echo(f"  • {nid}: {name}{jlabel}")
            else:
                click.echo(f"  • {nid}{jlabel}")


@cli.group(name="form-analysis")
def form_analysis():
    """2025 forms analysis commands."""
    pass


@form_analysis.command(name="urls")
@click.argument("application_type")
def form_analysis_urls(application_type):
    """Return matching 2025 form URLs for an application type or subtype."""
    print_2025_form_urls(application_type)


@form_analysis.command(name="list")
@click.argument("application_type")
def form_analysis_list(application_type):
    """List 2025 forms that cover an application type or subtype."""
    print_2025_forms_for_application_type(application_type)


@form_analysis.command(name="show")
@click.argument("form_ref")
def form_analysis_show(form_ref):
    """Show core details for a 2025 form by reference."""
    print_2025_form_details(form_ref)


@form_analysis.command(name="for-module")
@click.argument("module_ref")
def form_analysis_for_module(module_ref):
    """List analysed 2025 forms that include a module."""
    print_2025_forms_for_module(module_ref)


@form_analysis.command(name="modules")
@click.argument("form_ref")
def form_analysis_modules(form_ref):
    """List analysed 2025 modules found in a form."""
    print_2025_modules_for_form(form_ref)


@cli.command()
@click.argument("application_type")
def form_url(application_type):
    """Return the PDF form URL for an application type or subtype."""
    print_2025_form_urls(application_type)


@cli.command(name="forms")
@click.argument("application_type")
def forms_for_application_type(application_type):
    """List 2025 forms that cover an application type or subtype."""
    print_2025_forms_for_application_type(application_type)


@cli.command(name="form")
@click.argument("form_ref")
def form_details(form_ref):
    """Show core details for a 2025 form by reference."""
    print_2025_form_details(form_ref)


@cli.command(name="module-forms")
@click.argument("module_ref")
def forms_for_module(module_ref):
    """List analysed 2025 forms that include a module."""
    print_2025_forms_for_module(module_ref)


@cli.command(name="form-modules")
@click.argument("form_ref")
def modules_for_form(form_ref):
    """List analysed 2025 modules found in a form."""
    print_2025_modules_for_form(form_ref)


@report.group(invoke_without_command=True)
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
    help="Print in-scope rows split by covered-by-spec status, ordered by volume",
)
@click.pass_context
def completeness(ctx, input_path, verbose):
    """Completeness reporting."""
    if ctx.invoked_subcommand is None:
        ctx.invoke(
            completeness_summary,
            input_path=input_path,
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
    "-v",
    "--verbose",
    is_flag=True,
    help="Print in-scope rows split by covered-by-spec status, ordered by volume",
)
def completeness_summary(input_path, verbose):
    """Print completeness summary including covered volume and percentage."""
    result = calculate_scope_summary(Path(input_path))

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

    progress = build_progress_view_model(Path(input_path))
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
def scope(input_path, verbose):
    """Summarise in-scope and out-of-scope application types for completeness."""
    result = evaluate_scope(Path(input_path))
    in_scope = result["in_scope"]
    out_of_scope = result["out_of_scope"]

    total_rows = len(in_scope) + len(out_of_scope)
    in_scope_rows = len(in_scope)
    out_of_scope_rows = len(out_of_scope)
    summary_data = calculate_scope_summary(Path(input_path))
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
