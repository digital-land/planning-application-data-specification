from csv_helpers import read_csv
from loader import load_content


def get_undefined_application_types(
    all_types_csv: str = "data/planning-application-type.csv",
) -> list:
    # read in csv with read_csv
    all_types = read_csv(all_types_csv, as_dict=True)
    # load specification
    specification = load_content()
    undefined_types = []

    for app_type in all_types:
        if app_type["reference"] not in specification.get("application", {}):
            undefined_types.append(app_type)

    # sort undefined_types by 'name'
    return sorted(undefined_types, key=lambda x: x.get("name", ""))


def get_application_module_refs(application: object | str, specification: dict) -> list:
    """
    Given an application object (or application ref string) and the full specification,
    return a deduplicated, alphabetical list of module reference strings.

    - Accepts either the application dict or the application reference (string).
    - Handles modules listed as either strings or dicts with a "module" key.
    - If the application has an 'extends' attribute (string or list), modules from
      parent application(s) are included.
    - Prevents infinite loops in extends chains by tracking visited application refs.
    """
    applications = specification.get("application", {}) or {}
    collected = set()
    visited_apps = set()

    # normalize input: application may be a ref (str) or the application dict itself
    if isinstance(application, str):
        app_obj = applications.get(application)
        if not app_obj:
            return []
    elif hasattr(application, "get") and callable(getattr(application, "get")):
        # Accept frontmatter.Post which expose a `.get()` method. and dicts
        app_obj = application
    else:
        return []

    def extract_module_ref(entry):
        """Return a module ref string from an entry, or None.

        Entry may be:
        - a string 'module-ref'
        - a dict {'module': 'module-ref'}
        - nested dicts where the value of 'module' is a dict (rare)
        """
        if isinstance(entry, str):
            return entry
        if isinstance(entry, dict):
            # prefer explicit 'module' key
            if "module" in entry:
                val = entry["module"]
                # recurse if nested
                return extract_module_ref(val)
            # fallback: if dict has a single string value
            for v in entry.values():
                ref = extract_module_ref(v)
                if ref:
                    return ref
        return None

    def collect_from_app(app_obj):
        # collect modules from this app object; support 'modules' or singular 'module'
        mods = app_obj.get("modules", None)
        if mods is None:
            mods = app_obj.get("module", [])
        # if mods is a dict, iterate its values
        if isinstance(mods, dict):
            mods_iter = list(mods.values())
        else:
            mods_iter = mods or []

        for m in mods_iter:
            mod_ref = extract_module_ref(m)
            if isinstance(mod_ref, str) and mod_ref:
                collected.add(mod_ref)

        # follow extends if present
        extends = app_obj.get("extends")
        if not extends:
            return

        parent_refs = extends if isinstance(extends, list) else [extends]
        for pref in parent_refs:
            if not isinstance(pref, str) or not pref:
                continue
            if pref in visited_apps:
                continue
            visited_apps.add(pref)
            parent_app = applications.get(pref)
            if parent_app:
                collect_from_app(parent_app)

    # start collection from the resolved app_obj
    collect_from_app(app_obj)
    return sorted(collected)


if __name__ == "__main__":

    undefined_types = get_undefined_application_types()
    for app in undefined_types:
        print(f"* {app['name']} (ref: {app['reference']})")

    try:
        specification = load_content()
        print("Specification loaded successfully")

        result = get_application_module_refs(
            specification["application"]["ldc-prospective-use"], specification
        )
        print(result)

    except Exception as e:
        print(f"✗ Error: {e}")
