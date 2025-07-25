from integrity_checks.utils import has_reference_error, print_error

# APPLICATIONS
# ============

# 1. application must be a string, kebab-case and unique
# 2. each application schema must have the application field in the fields list
# 3. each application schema must have a modules attr
# 4. each module in modules list must have a module_name.schema.md file in specification/module/


def check_application_names(applications):
    """
    Check rule 1: application must be a string, kebab-case and unique
    """
    seen_applications = set()
    has_errors = False

    for app_name, application in applications.items():

        has_errors |= has_reference_error(app_name, "application", seen_applications)

        seen_applications.add(app_name)

    return not has_errors


def check_application_field_present(applications, fields):
    """
    Check rule 2: each application schema must have the application field in the fields list
    """
    has_errors = False

    for app_name, application in applications.items():
        app_fields = application.get("fields", [])

        # Check if 'application' field is present in the fields list
        application_field_found = False
        for field_def in app_fields:
            if field_def.get("field") == "application":
                application_field_found = True
                break

        if not application_field_found:
            print_error(
                "application", app_name, "missing 'application' field in fields list"
            )
            has_errors = True

        # Also check that the application field exists in field definitions
        if "application" not in fields:
            print_error(
                "application",
                app_name,
                "referenced 'application' field not found in field definitions",
            )
            has_errors = True

    return not has_errors


def check_modules_attr_present(applications):
    """
    Check rule 3: each application schema must have a modules attr
    """
    has_errors = False

    for app_name, application in applications.items():
        if "modules" not in application:
            print_error("application", app_name, "missing 'modules' attribute")
            has_errors = True

    return not has_errors


def check_module_references_exist(applications, modules_list):
    """
    Check rule 4: each module in modules list must exist in the modules definitions
    """
    has_errors = False

    for app_name, application in applications.items():
        app_modules = application.get("modules", [])

        for module in app_modules:
            if module["module"] not in modules_list:
                print_error(
                    "application",
                    app_name,
                    f"referenced module '{module['module']}' not found in module definitions",
                )
                has_errors = True

    return not has_errors


def check_all(applications, fields, modules):
    """Run all application integrity checks.

    Args:
        applications: Dictionary of application definitions
        fields: Dictionary of field definitions
        modules: Dictionary of module definitions
    """
    # Define checks and their required arguments
    checks_with_args = [
        (check_application_names, [applications]),
        (check_application_field_present, [applications, fields]),
        (check_modules_attr_present, [applications]),
        (check_module_references_exist, [applications, modules]),
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
