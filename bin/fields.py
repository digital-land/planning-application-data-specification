def get_applicable_app_types(field_entry):
    """
    Get the applicable application types for a field entry.
    """
    applies_if = field_entry.get("applies-if")
    if applies_if:
        # Try to extract application-type(s)
        # applies-if can be a list of dicts or a dict (should fix this)
        if isinstance(applies_if, list):
            for cond in applies_if:
                if "application-type" in cond:
                    app_types = cond["application-type"].get("in")
                    break
        elif isinstance(applies_if, dict):
            if "application-type" in applies_if:
                app_types = applies_if["application-type"].get("in")
        if app_types:
            return app_types
        return None
    return None


def is_field_applicable_to_app_type(field_entry, app_type):
    """
    Check if a field entry is applicable to a specific application type.
    """
    applicable_app_types = get_applicable_app_types(field_entry)
    if applicable_app_types:
        return app_type in applicable_app_types
    return True  # If no applies-if, assume applicable to all types
