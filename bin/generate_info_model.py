from fields import get_applicable_app_types, is_field_applicable_to_app_type
from modules import get_module_parts


def format_field_name(field, field_def):
    name = field_def.get("name", field["field"])
    # Append [] for cardinality n
    if field_def.get("cardinality") == "n":
        name += "[]"
    # Append {} for object type
    if field_def.get("datatype") == "object":
        name += "{}"
    return name


def get_requirement(field):
    if field.get("required") is True:
        return "MUST"
    return "MAY"


def get_only_for_application(field):
    applies = field.get("applies-if")
    if applies:
        # Try to extract application-type(s)
        for cond in applies:
            if "application-type" in cond:
                app_types = cond["application-type"].get("in")
                if app_types:
                    return app_types
        return "Yes"
    return ""


def get_notes(field, field_def):
    notes = []
    # Add codelist enum note
    if field_def.get("codelist"):
        notes.append(f"Select from the {field_def['codelist']} enum")
    # Add required-if rules
    if "required-if" in field:
        for cond in field["required-if"]:
            if "field" in cond and "value" in cond:
                notes.append(
                    f"Rule: is a MUST if `{cond['field']}` is `{cond['value']}`"
                )
    # Add extra notes from description if present
    desc = field_def.get("notes") or ""
    if desc:
        notes.append(desc)
    return notes


def format_main_module_table(module, fields_spec, app_type=None):
    # field_entry = the field attr in the module
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
        name = format_field_name(field_entry, field_def)
        description = field_entry.get("description") or field_def.get("description", "")
        only_for = get_only_for_application(field_entry)
        only_for_md_str = (
            ", ".join(only_for) if isinstance(only_for, list) else only_for
        )
        requirement = get_requirement(field_entry)
        notes = get_notes(field_entry, field_def)
        notes_md_str = ". ".join(notes)
        lines.append(
            f"| {ref} | {name} | {description} | {only_for_md_str} | {requirement} | {notes_md_str} |"
        )
    return "\n".join(lines)


def format_component_table(component, fields_spec, app_type=None):
    lines = ["field | description | required | notes", "-- | -- | -- | --"]
    # field_entry = the field attr in the module
    for field_entry in component.get("fields", []):
        if app_type:
            # Skip fields not applicable to the given app_type
            if not is_field_applicable_to_app_type(field_entry, app_type):
                continue
        ref = field_entry["field"]
        field_def = fields_spec.get(ref, {})
        description = field_def.get("description", "")
        requirement = get_requirement(field_entry)
        notes = get_notes(field_entry, field_def)
        notes_md_str = ". ".join(notes)
        lines.append(f"{ref} | {description} | {requirement} | {notes_md_str}")
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


if __name__ == "__main__":
    print("Testing information model generation script.")

    try:
        from loader import load_content

        specification = load_content()
        print("Specification loaded successfully")

        # Test the function
        # result = generate_module("interest-details", specification)
        # result = generate_module("res-units", specification, app_type="full")
        # result = generate_module("demolition-reason", specification)
        result = generate_module(
            "tree-work-details", specification, app_type="notice-trees-in-con-area"
        )
        print("Function called successfully")
        print(result)

    except Exception as e:
        print(f"✗ Error: {e}")
