from integrity_checks.utils import has_reference_error, print_error

# MODULES (.schema.md files)
# ==========

# 1. module attr must be string, kebab-case and unique across all modules
# 2. each field in fields attr must be a field reference in /fields
# 3. every module must have entry-date and end-date attrs

# . if applies-if attr with `application-type` then must be a valid application type TODO
# . if required-if attr with `application-type` then must be a valid application type TODO
# . if required-if attr with `field` then must be a valid field TODO


def check_module_names(modules):
    """
    Check rule 1: module attr must be string, kebab-case and unique across all modules
    """
    seen_modules = set()
    has_errors = False

    for module_name, module in modules.items():

        has_errors |= has_reference_error(module_name, "module", seen_modules)

        seen_modules.add(module_name)

    return not has_errors


def check_field_references(modules, fields):
    """
    Check rule 2: each field in fields attr must be a field reference in /fields
    """
    has_errors = False

    for module_name, module in modules.items():
        module_fields = module.get("fields", [])

        for field_def in module_fields:
            field_name = field_def.get("field")
            if not field_name:
                print_error("module", module_name, "missing field name in fields list")
                has_errors = True
                continue

            if field_name not in fields:
                print_error(
                    "module",
                    module_name,
                    f"referenced field '{field_name}' not found in field definitions",
                )
                has_errors = True

    return not has_errors


def check_dates(modules):
    """
    Check rule 3: every module must have entry-date and end-date attrs
    """
    has_errors = False

    for module_name, module in modules.items():
        if "entry-date" not in module:
            print_error("module", module_name, "missing entry-date")
            has_errors = True
        if "end-date" not in module:
            print_error("module", module_name, "missing end-date")
            has_errors = True

    return not has_errors


def check_all(modules, fields):
    """Run all module integrity checks.

    Args:
        modules: Dictionary of module definitions
        fields: Dictionary of field definitions
    """
    # Define checks and their required arguments
    checks_with_args = [
        (check_module_names, [modules]),
        (check_field_references, [modules, fields]),
        (check_dates, [modules]),
    ]

    all_passed = True
    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = check_all()
    exit(0 if success else 1)
