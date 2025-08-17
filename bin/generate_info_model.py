from fields import (
    format_field_display_name,
    get_applicable_app_types,
    get_notes_for_info_model,
    get_requirement_str,
    is_field_applicable_to_app_type,
)
from modules import get_codelists_for_module, get_module_parts
from utils import save_string_to_file


def format_main_module_table(module, fields_spec, app_type=None):
    # Determine columns based on app_type
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
    for field_entry in module.get("fields", []):
        if app_type:
            # Skip fields not applicable to the given app_type
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
        notes_md_str = ". ".join(notes)
        if app_type:
            lines.append(
                f"| {ref} | {name} | {description} | {requirement} | {notes_md_str} |"
            )
        else:
            lines.append(
                f"| {ref} | {name} | {description} | {only_for_md_str} | {requirement} | {notes_md_str} |"
            )
    return "\n".join(lines)


def format_component_table(component, fields_spec, app_type=None):
    lines = ["field | name | description | required | notes", "-- | -- | -- | -- | --"]
    # field_entry = the field attr in the module
    for field_entry in component.get("fields", []):
        if app_type:
            # Skip fields not applicable to the given app_type
            if not is_field_applicable_to_app_type(field_entry, app_type):
                continue
        ref = field_entry["field"]
        field_def = fields_spec.get(ref, {})
        name = format_field_display_name(field_entry, field_def)
        description = field_def.get("description", "")
        requirement = get_requirement_str(field_entry)
        notes = get_notes_for_info_model(field_entry, field_def)
        notes_md_str = ". ".join(notes)
        lines.append(f"{ref} | {name} | {description} | {requirement} | {notes_md_str}")
    return "\n".join(lines)


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
    out.append(format_main_module_table(module, fields_spec, app_type) + "\n")
    # Component tables
    for cname, component in related_components.items():
        out.append(f"\n**{component.get('name', cname)} model**\n")
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


def generate_codelist_md_str(codelists):
    # list out the codelist names
    if not codelists:
        return ""
    lines = ["This are the codelist required to support this specification:\n"]
    for codelist in codelists:
        lines.append(f"- {codelist}")
    return "\n".join(lines)


def generate_application(app_ref, specification):
    """
    Generate the information model for a specific application type.
    """
    applications = specification.get("application", {})
    fields = specification.get("field", {})
    app = applications.get(app_ref)
    if not app:
        print(f"Application '{app_ref}' not found in specification.")
        return None

    # get the modules that are part of the application
    modules = app.get("modules", [])
    module_refs = [m["module"] if isinstance(m, dict) else m for m in modules]
    inc_codelists = get_codelists_for_app(module_refs, fields, specification)

    # generate output
    # 1. Heading and Description
    out = [f"# {app.get('name', app_ref)}\n"]
    if app.get("description"):
        out.append(app["description"] + "\n")

    # 2. Contents
    out.append("## Contents\n")
    out.append("* [Application data specification](#application-data-specification)")
    module_refs = [
        m["module"] if isinstance(m, dict) else m for m in app.get("modules", [])
    ]
    out.append("")

    # 3. Modules List (contents)
    out.append("### Modules\n")
    for mod in module_refs:
        mod_schema = specification.get("module", {}).get(mod, {})
        mod_name = mod_schema.get("name", mod.replace("-", " ").capitalize())
        anchor = mod_name.lower().replace(" ", "-")
        out.append(f"* [{mod_name}](#{anchor})")
    out.append("")

    # 4. Application Data Specification
    out.append("## Application data specification\n")
    out.append("| field | description | data-type | required | notes |")
    out.append("| --- | --- | --- | --- | --- |")
    for field_entry in app.get("fields", []):
        ref = field_entry["field"]
        field_def = specification.get("field", {}).get(ref, {})
        description = field_def.get("description", "")
        datatype = field_def.get("datatype", "")
        required = "MUST" if field_entry.get("required") else "MAY"
        notes = field_def.get("notes", "")
        out.append(f"| {ref} | {description} | {datatype} | {required} | {notes} |")
    out.append("")

    # 5. Module Sections
    for mod in module_refs:
        module_md = generate_module(mod, specification, app_type=app_ref)
        if module_md:
            # update first header of md file to be ## instead of #
            module_md = module_md.replace("# ", "## ", 1)
            out.append(module_md)
            out.append("")
        else:
            print(f"Module '{mod}' could not be generated.")

    # 6. Required Codelists
    if inc_codelists:
        out.append("## Required codelists\n")
        out.append(generate_codelist_md_str(inc_codelists))

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
        # result = generate_module("demolition-reason", specification)
        # result = generate_module(
        #     "tree-work-details", specification, app_type="notice-trees-in-con-area"
        # )

        result = save_string_to_file(
            generate_application("full", specification), "tmp/test-gen-app.md"
        )
        print("Function called successfully")
        print(result)

    except Exception as e:
        print(f"✗ Error: {e}")
