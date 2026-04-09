def get_application_module_refs(application: object | str, specification: dict) -> list:
    """
    Given an application object (or application ref string) and the full specification,
    return a deduplicated, alphabetical list of module reference strings.
    """
    applications = specification.get("application", {}) or {}
    collected = set()
    visited_apps = set()

    if isinstance(application, str):
        app_obj = applications.get(application)
        if not app_obj:
            return []
    elif hasattr(application, "get") and callable(getattr(application, "get")):
        app_obj = application
    else:
        return []

    def extract_module_ref(entry):
        if isinstance(entry, str):
            return entry
        if isinstance(entry, dict):
            if "module" in entry:
                return extract_module_ref(entry["module"])
            for value in entry.values():
                ref = extract_module_ref(value)
                if ref:
                    return ref
        return None

    def collect_from_app(current_app):
        mods = current_app.get("modules", None)
        if mods is None:
            mods = current_app.get("module", [])
        mods_iter = list(mods.values()) if isinstance(mods, dict) else (mods or [])

        for module_entry in mods_iter:
            module_ref = extract_module_ref(module_entry)
            if isinstance(module_ref, str) and module_ref:
                collected.add(module_ref)

        extends = current_app.get("extends")
        if not extends:
            return

        parent_refs = extends if isinstance(extends, list) else [extends]
        for parent_ref in parent_refs:
            if not isinstance(parent_ref, str) or not parent_ref:
                continue
            if parent_ref in visited_apps:
                continue
            visited_apps.add(parent_ref)
            parent_app = applications.get(parent_ref)
            if parent_app:
                collect_from_app(parent_app)

    collect_from_app(app_obj)
    return sorted(collected)
