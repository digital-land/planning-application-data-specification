#!/usr/bin/env python3

from loader import load_content


def perform_checks():
    from integrity_checks.components import check_all as check_components
    from integrity_checks.fields import check_all as check_fields
    from integrity_checks.modules import check_all as check_modules

    # Load from specification files
    specification = load_content()
    fields = specification["field"]
    components = specification["component"]
    modules = specification["module"]

    # Perform checks
    print("\nChecking fields\n===========")
    fields_valid = check_fields(fields, components)
    print("\nChecking components\n===========")
    components_valid = check_components(components, fields, None)
    print("\nChecking modules\n===========")
    modules_valid = check_modules(modules, fields)

    print("------------------------------------")
    if fields_valid and components_valid and modules_valid:
        print("All integrity checks passed.")
    else:
        print("Integrity checks failed.")


if __name__ == "__main__":
    perform_checks()
