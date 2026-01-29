def format_field_display_name(field_entry, field_def):
    name = field_def.get("name", field_entry["field"])
    # Append [] for cardinality n
    if field_def.get("cardinality") == "n":
        name += "[]"
    # Append {} for object type
    if field_def.get("datatype") == "object":
        name += "{}"
    return name


def get_applicable_app_types(field_entry):
    """
    Get the applicable application types for a field entry.
    """
    app_types = None
    applies_if = field_entry.get("applies-if")
    if applies_if:
        # Try to extract application-type(s)
        # applies-if can be a list of dicts or a dict (should fix this)
        if isinstance(applies_if, list):
            for cond in applies_if:
                if not isinstance(cond, dict) or "application-type" not in cond:
                    continue
                app_cond = cond["application-type"]
                if isinstance(app_cond, dict):
                    app_types = app_cond.get("in")
                elif isinstance(app_cond, list):
                    for item in app_cond:
                        if isinstance(item, dict) and "in" in item:
                            app_types = item.get("in")
                            break
                if app_types:
                    break
        elif isinstance(applies_if, dict):
            if "application-type" in applies_if:
                app_cond = applies_if["application-type"]
                if isinstance(app_cond, dict):
                    app_types = app_cond.get("in")
                elif isinstance(app_cond, list):
                    for item in app_cond:
                        if isinstance(item, dict) and "in" in item:
                            app_types = item.get("in")
                            break
        if app_types:
            return app_types
        return []
    return None


def get_notes_for_info_model(field_entry, field_def):
    notes = []
    # Add codelist enum note
    if field_def.get("codelist"):
        notes.append(f"Select from the **{field_def['codelist']}** enum")
    # Add required-if rules
    if "required-if" in field_entry:
        for cond in field_entry["required-if"]:
            if "field" in cond and "value" in cond:
                notes.append(
                    f"Rule: is a MUST if `{cond['field']}` is `{cond['value']}`"
                )
    # Add extra notes from description if present
    desc = field_def.get("notes") or ""
    if desc:
        notes.append(desc)
    return notes


def get_requirement_str(field_entry):
    if field_entry.get("required") is True:
        return "MUST"
    return "MAY"


def is_field_applicable_to_app_type(field_entry, app_type):
    """
    Check if a field entry is applicable to a specific application type.
    """
    applicable_app_types = get_applicable_app_types(field_entry)
    if applicable_app_types:
        return app_type in applicable_app_types
    return True  # If no applies-if, assume applicable to all types


def get_codelist(field_def):
    return field_def.get("codelist", None)


def find_field_usage(field_ref, specification):
    """
    Return sequences of modules and components that reference the given field.

    The specification argument should match the structure from loader.load_content().
    Results are sorted by reference for deterministic output.
    """
    modules = (specification or {}).get("module") or {}
    components = (specification or {}).get("component") or {}

    def collect(records):
        matches = []
        for ref, post in records.items():
            fields = post.get("fields") if hasattr(post, "get") else None
            if not isinstance(fields, list):
                continue
            for entry in fields:
                entry_ref = entry if isinstance(entry, str) else entry.get("field")
                if entry_ref == field_ref:
                    name = post.get("name", ref) if hasattr(post, "get") else ref
                    matches.append((ref, name))
                    break
        matches.sort(key=lambda item: item[0])
        return matches

    return {
        "modules": collect(modules),
        "components": collect(components),
    }
