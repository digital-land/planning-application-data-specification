from bin.csv_helpers import read_csv
from bin.loader import load_content
from planning_application_specification.applications import (
    get_application_module_refs as package_get_application_module_refs,
)


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
    """Delegate application module resolution to the shared package logic."""
    return package_get_application_module_refs(application, specification)


def get_applications_with_module(module_ref: str, specification: dict) -> list:
    """
    Given a module reference string and the full specification,
    return a list of application reference strings that include this module.

    - Iterates over all applications in the specification.
    - Uses get_application_module_refs to get modules for each application.
    - Collects applications that include the specified module_ref.
    - Returns a sorted list of application references.
    """
    applications = specification.get("application", {}) or {}
    matching_apps = []

    for app_ref, app_obj in applications.items():
        modules = get_application_module_refs(app_obj, specification)
        if module_ref in modules:
            matching_apps.append(app_ref)

    return sorted(matching_apps)


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
