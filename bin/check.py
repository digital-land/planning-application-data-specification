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


# FIELDS
# ======

# 1. field attr must be string, kebab-case and unique across all fields

# 2. cardinality is one of: 1 or n

## 3. check the data types
# TODO

# 4. if datatype is object then must have component attr

# 5. component attr must a component reference in /components

# 6. datatype is enum then must have codelist attr

# 7. codelist must be in codelist definitions
# TODO

# 8. every field must have entry-date and end-date attrs


# COMPONENTS
# ===========
# 1. component attr must be string, kebab-case and unique across all components

# 2. each field in fields attr must be a field reference in /fields

# 3. if required-if attr with `application-type` then must be a valid application type

# 4. if required-if attr with `field` then must be a valid field reference in /fields

# 5. every component must have entry-date and end-date attrs


# MODULES (.schema.md files)
# ==========
