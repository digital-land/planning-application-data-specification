import os

from applications import get_application_module_refs
from csv_helpers import csv_to_markdown
from fields import (
    format_field_display_name,
    get_applicable_app_types,
    get_notes_for_info_model,
    get_requirement_str,
    is_field_applicable_to_app_type,
)
from modules import collect_related_components_bfs, get_codelists_for_module, get_module_parts
from utils import save_string_to_file


def format_fields_table(field_entries, fields_spec, table_type="main", app_type=None):
    """
    Generic formatter for field tables.
    table_type: "main" or "component"
    field_entries: list of field entry dicts (module or component fields)
    """
    lines = []
    if table_type == "main":
        if app_type:
            lines = [
                "| reference | name | description | requirement | notes |",
                "| --- | --- | --- | --- | --- |",
            ]
        else:
            lines = [
                "| reference | name | description | only for application | requirement | notes |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
    else:  # component table
        lines = [
            "field | name | description | required | notes",
            "-- | -- | -- | -- | --",
        ]

    for field_entry in field_entries:
        if app_type:
            if not is_field_applicable_to_app_type(field_entry, app_type):
                continue
        ref = field_entry["field"]
        field_def = fields_spec.get(ref, {})
        name = format_field_display_name(field_entry, field_def)
        description = field_entry.get("description") or field_def.get("description", "")
        only_for = get_applicable_app_types(field_entry)
        only_for_md_str = ", ".join(only_for) if isinstance(only_for, list) else ""
        requirement = get_requirement_str(field_entry)
        notes = get_notes_for_info_model(field_entry, field_def)
        # ensure notes is a string for joining
        if isinstance(notes, (list, tuple)):
            notes_md_str = ". ".join(str(n) for n in notes)
        else:
            notes_md_str = str(notes or "")

        if table_type == "main":
            if app_type:
                lines.append(
                    f"| {ref} | {name} | {description} | {requirement} | {notes_md_str} |"
                )
            else:
                lines.append(
                    f"| {ref} | {name} | {description} | {only_for_md_str} | {requirement} | {notes_md_str} |"
                )
        else:
            lines.append(
                f"{ref} | {name} | {description} | {requirement} | {notes_md_str}"
            )

    return "\n".join(lines)


def format_main_module_table(module, fields_spec, app_type=None):
    return format_fields_table(
        module.get("fields", []), fields_spec, table_type="main", app_type=app_type
    )


def format_component_table(component, fields_spec, app_type=None):
    return format_fields_table(
        component.get("fields", []),
        fields_spec,
        table_type="component",
        app_type=app_type,
    )


def format_rules_md_str(rules):
    if not rules:
        return ""
    lines = ["**Validation rules**\n"]
    for rule in rules:
        if isinstance(rule, dict):
            if "rule" in rule:
                lines.append(f"- {rule['rule']}")
            elif "description" in rule:
                lines.append(f"- {rule['description']}")
            else:
                lines.append(f"- {str(rule)}")
        else:
            lines.append(f"- {str(rule)}")
    return "\n".join(lines)


def generate_module(module_ref, specification, app_type=None):
    module_parts = get_module_parts(specification, module_ref, app_type)
    if not module_parts:
        print(f"Module '{module_ref}' not found in specification.")
        return None
    module = module_parts.get("module", {})
    related_components = module_parts.get("related-components", {})
    rules = module_parts.get("rules", [])
    fields_spec = specification.get("field", {})
    # Header
    out = [
        f"# {module.get('name', module_ref)}\n",
        module.get("description", "") + "\n",
    ]
    # Top-level fields table
    out.append(f"**{module.get('name', module_ref)} module**\n")
    out.append(format_main_module_table(module, fields_spec, app_type) + "\n")
    # Component tables
    for cname, component in related_components.items():
        out.append(f"\n**{component.get('name', cname)} component**\n")
        out.append(
            format_component_table(component, fields_spec, app_type=app_type) + "\n"
        )
    # Validation rules
    out.append(format_rules_md_str(rules))
    return "\n".join(out)


def get_codelists_for_app(module_refs, fields, specification):
    codelists = set()
    for module_ref in module_refs:
        module_parts = get_module_parts(specification, module_ref)
        if not module_parts:
            print(f"Module '{module_ref}' not found in specification.")
            continue
        related_components = module_parts.get("related-components", {})
        for component in related_components.values():
            codelists.update(get_codelists_for_module(component, fields))
    return codelists


def create_codelist_table(codelist_obj):
    lines = []
    name = codelist_obj.get("name", "Unknown")

    source = codelist_obj.get("source", "")

    # Heading
    heading = f"### {name}"
    lines.append(heading)

    # Source information
    if not source:
        lines.append("\n_codelist source not provided_\n")
    else:
        if isinstance(source, str) and (
            source.startswith("http://") or source.startswith("https://")
        ):
            lines.append(f"\nThis codelist is sourced from [{source}]({source})\n")
        else:
            path = source
            if not os.path.isabs(path):
                repo_root = os.getcwd()
                path = os.path.join(repo_root, path)

            if not os.path.exists(path):
                lines.append(f"\nSource file not found: {source}\n")
                return "\n".join(lines)

            try:
                md_table = csv_to_markdown(path)
                lines.append("")
                lines.append(md_table)
            except Exception as e:
                lines.append(f"\nError reading source file {source}: {e}\n")

    return "\n".join(lines) if lines else ""


def generate_codelist_md_str(codelists):
    """
    Generates a Markdown-formatted string with the codelists required for the
    specification.

    Args:
        codelists (list): A list of objects representing codelists. Each
            object should be convertible to a string or be a dict-like object.

    Returns:
        str: A Markdown-formatted string enumerating the codelist names, or an
        empty string if no codelists are provided.
    """
    # list out the codelist names
    if not codelists:
        return ""

    lines = []
    lines.append("Below are the codelists required to support this specification:\n")
    for codelist in codelists:
        lines.append(create_codelist_table(codelist))
    return "\n".join(lines)


def generate_application_fields_section(specification, app_type=None):
    fields_spec = specification.get("field", {})
    components = specification.get("component", {})

    application_field = fields_spec.get("application")
    if not application_field:
        print("Field definition for 'application' not found in specification.")
        return None

    component_ref = application_field.get("component") or "application"
    application_component = components.get(component_ref) or components.get("application")
    if not application_component:
        print("Component definition for application fields not found in specification.")
        return None

    heading_name = application_field.get("name", "Application").strip()
    if not heading_name:
        heading_name = "Application"
    heading_title = (
        heading_name
        if heading_name.lower().endswith("fields")
        else f"{heading_name} fields"
    )

    out = [f"## {heading_title}\n"]

    description = application_component.get("description") or application_field.get(
        "description", ""
    )
    if description:
        out.append(description.strip() + "\n")

    module_label = (
        heading_title
        if heading_title.lower().endswith("fields")
        else f"{heading_title} fields"
    )
    out.append(f"**{module_label} module**\n")
    out.append(
        format_component_table(
            application_component, fields_spec, app_type=app_type
        )
        + "\n"
    )

    related_components = collect_related_components_bfs(
        application_component.get("fields", []),
        components,
        fields_spec,
        app_type=app_type,
    )
    for cname, component in related_components.items():
        out.append(f"\n**{component.get('name', cname)} component**\n")
        out.append(
            format_component_table(component, fields_spec, app_type=app_type) + "\n"
        )

    validation_rules = application_component.get("validation")
    rules_str = format_rules_md_str(validation_rules)
    if rules_str:
        out.append(rules_str)

    return "\n".join(out)


def generate_application(app_ref, specification):
    """
    Generate the information model for a specific application type.
    """
    applications = specification.get("application", {})
    fields = specification.get("field", {})
    codelists = specification.get("codelist", {})

    app = applications.get(app_ref)
    if not app:
        print(f"Application '{app_ref}' not found in specification.")
        return None

    # get the modules that are part of the application
    modules = app.get("modules", [])
    module_refs = [m["module"] if isinstance(m, dict) else m for m in modules]
    inc_codelists = get_codelists_for_app(module_refs, fields, specification)
    # Sort codelists by their 'name' attribute
    inc_codelist_objs = sorted(
        [codelists.get(ref) for ref in inc_codelists if codelists.get(ref)],
        key=lambda c: c.get("name", ""),
    )

    # generate output
    # 1. Heading and Description
    out = [f"# {app.get('name', app_ref)}\n"]
    if app.get("description"):
        out.append(app["description"] + "\n")

    # 2. Contents
    out.append("## Contents\n")
    out.append("* [Application data specification](#application-data-specification)")
    # get full list of applicable modules
    module_refs = get_application_module_refs(app, specification)
    out.append("")

    # 3. Modules List (contents)
    out.append("### Modules\n")
    for mod in module_refs:
        mod_schema = specification.get("module", {}).get(mod, {})
        mod_name = mod_schema.get("name", mod.replace("-", " ").capitalize())
        anchor = mod_name.lower().replace(" ", "-")
        out.append(f"* [{mod_name}](#{anchor})")
    out.append("")

    # 4. Codelists (contents)
    out.append("### Codelists\n")
    for codelist in inc_codelist_objs:
        codelist_name = codelist.get("name", "Name unknown")
        anchor = codelist_name.lower().replace(" ", "-")
        out.append(f"* [{codelist_name}](#{anchor})")
    out.append("")

    # 5. Application Data Specification
    application_fields_section = generate_application_fields_section(
        specification, app_type=app_ref
    )
    if application_fields_section:
        out.append(application_fields_section)
        out.append("")

    # 6. Module Sections
    for mod in module_refs:
        module_md = generate_module(mod, specification, app_type=app_ref)
        if module_md:
            # update first header of md file to be ## instead of #
            module_md = module_md.replace("# ", "## ", 1)
            out.append(module_md)
            out.append("")
        else:
            print(f"Module '{mod}' could not be generated.")

    # 7. Required Codelists
    if inc_codelists:
        out.append("## Required codelists\n")
        out.append(generate_codelist_md_str(inc_codelist_objs))

    return "\n".join(out)


if __name__ == "__main__":
    print("Testing information model generation script.")

    try:
        from loader import load_content

        specification = load_content()
        print("Specification loaded successfully")

        # Test the function
        # result = save_string_to_file(
        #     "\n".join(generate_module("interest-details", specification)), "tmp/test-gen.md"
        # )
        # result = generate_module("res-units", specification, app_type="full")
        result = generate_module("demolition-reason", specification)
        # result = generate_module(
        #     "tree-work-details", specification, app_type="notice-trees-in-con-area"
        # )

        result = save_string_to_file(
            generate_application("advertising", specification),
            "generated/info_model/application/advertising.md",
        )
        print("Function called successfully")
        print(result)

    except Exception as e:
        print(f"✗ Error: {e}")
