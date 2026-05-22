from datetime import date
from pathlib import Path

from csv_helpers import read_csv, read_csv_with_headers
from integrity_checks.utils import (
    has_reference_error,
    print_error,
    print_warning,
    run_checks,
)

# APPLICATIONS
# ============

# 1. application must be a string, kebab-case and unique
# 2. each application schema must have the submission-details field in the fields list
# 3. each application schema must have a modules attr
# 4. each module in modules list must have a module_name.schema.md file in specification/module/


# TODO
# 5. base-type is allowable field
# 6. if extends then must be a valid application reference in application schemas
# 7. define which fields are overridden and which are added to
# 8. listing app types should list base types and their 'children' applications
# 9. check the application is part of the official application or sub application dataset

COMBINED_APPLICATION_TYPES_PATH = (
    Path(__file__).resolve().parents[2] / "specification" / "combined-application-types.csv"
)
PLANNING_APPLICATION_TYPE_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "planning-application-type.csv"
)
COMBINED_APPLICATION_REQUIRED_HEADERS = [
    "application-types",
    "name",
    "description",
    "notes",
    "entry-date",
    "start-date",
    "end-date",
]


def parse_iso_date(value, element_name, field_name):
    if value == "":
        return None

    try:
        return date.fromisoformat(value)
    except ValueError:
        print_error(
            "combined application type",
            element_name,
            f"invalid {field_name} '{value}', expected YYYY-MM-DD",
        )
        return False


def split_application_types(raw_value):
    return [item.strip() for item in raw_value.split(";") if item.strip()]


def get_row_value(row, key):
    value = row.get(key, "")
    return value.strip() if isinstance(value, str) else ""


def get_known_application_types(applications):
    known = set(applications.keys())

    if PLANNING_APPLICATION_TYPE_PATH.exists():
        for row in read_csv(PLANNING_APPLICATION_TYPE_PATH, as_dict=True):
            reference = row.get("reference", "")
            if isinstance(reference, str) and reference.strip():
                known.add(reference.strip())

    return known


def check_combined_application_types_headers():
    if not COMBINED_APPLICATION_TYPES_PATH.exists():
        print_error(
            "combined application type",
            str(COMBINED_APPLICATION_TYPES_PATH),
            "missing combined application types csv",
        )
        return False

    headers, _ = read_csv_with_headers(COMBINED_APPLICATION_TYPES_PATH)
    has_errors = False

    for header in COMBINED_APPLICATION_REQUIRED_HEADERS:
        if header not in headers:
            print_error(
                "combined application type",
                str(COMBINED_APPLICATION_TYPES_PATH),
                f"missing required column '{header}'",
            )
            has_errors = True

    return not has_errors


def check_combined_application_type_rows(applications):
    if not COMBINED_APPLICATION_TYPES_PATH.exists():
        return False

    _, rows = read_csv_with_headers(COMBINED_APPLICATION_TYPES_PATH)
    has_errors = False
    seen_combinations = set()
    known_application_types = get_known_application_types(applications)

    for row_num, row in enumerate(rows, start=2):
        combo_ref = get_row_value(row, "application-types")
        element_name = combo_ref or f"row {row_num}"

        if combo_ref == "":
            print_error(
                "combined application type",
                element_name,
                "missing 'application-types' value",
            )
            has_errors = True
            continue

        app_types = split_application_types(combo_ref)
        canonical_app_types = sorted(app_types)
        canonical_ref = ";".join(canonical_app_types)

        if get_row_value(row, "name") == "":
            print_error("combined application type", element_name, "missing 'name' value")
            has_errors = True

        if get_row_value(row, "description") == "":
            print_error(
                "combined application type",
                element_name,
                "missing 'description' value",
            )
            has_errors = True

        if get_row_value(row, "entry-date") == "":
            print_error(
                "combined application type",
                element_name,
                "missing 'entry-date' value",
            )
            has_errors = True

        if app_types != canonical_app_types:
            print_error(
                "combined application type",
                element_name,
                f"'application-types' must be in canonical alphabetical order '{canonical_ref}'",
            )
            has_errors = True

        if len(app_types) != len(set(app_types)):
            print_error(
                "combined application type",
                element_name,
                "contains duplicate application types",
            )
            has_errors = True

        if canonical_ref in seen_combinations:
            print_error(
                "combined application type",
                element_name,
                f"duplicate combined application type '{canonical_ref}'",
            )
            has_errors = True
        seen_combinations.add(canonical_ref)

        if len(app_types) >= 3:
            print_warning(
                "combined application type",
                element_name,
                "contains three or more application types; current implementation expects pairs",
            )

        if get_row_value(row, "start-date") == "":
            print_warning(
                "combined application type",
                element_name,
                "blank 'start-date' means this combination is recognised but inactive",
            )

        for app_type in app_types:
            if app_type not in known_application_types:
                print_error(
                    "combined application type",
                    element_name,
                    f"references unknown application type '{app_type}'",
                )
                has_errors = True

        entry_date = parse_iso_date(
            get_row_value(row, "entry-date"), element_name, "entry-date"
        )
        start_date = parse_iso_date(
            get_row_value(row, "start-date"), element_name, "start-date"
        )
        end_date = parse_iso_date(
            get_row_value(row, "end-date"), element_name, "end-date"
        )

        if False in (entry_date, start_date, end_date):
            has_errors = True
            continue

        if entry_date and start_date and start_date < entry_date:
            print_error(
                "combined application type",
                element_name,
                "'start-date' must not be earlier than 'entry-date'",
            )
            has_errors = True

        if start_date and end_date and end_date < start_date:
            print_error(
                "combined application type",
                element_name,
                "'end-date' must not be earlier than 'start-date'",
            )
            has_errors = True

        if entry_date and end_date and end_date < entry_date:
            print_error(
                "combined application type",
                element_name,
                "'end-date' must not be earlier than 'entry-date'",
            )
            has_errors = True

    return not has_errors


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
    Check rule 2: each application schema must have the submission-details field in the fields list
    """
    has_errors = False

    for app_name, application in applications.items():
        app_fields = application.get("fields", [])
        has_extends = "extends" in application

        # If 'extends' is not present, 'submission-details' field must be present in fields list
        if not has_extends:
            # Check if 'submission-details' field is present in the fields list
            submission_details_field_found = False
            for field_def in app_fields:
                if field_def.get("field") == "submission-details":
                    submission_details_field_found = True
                    break

            if not submission_details_field_found:
                print_error(
                    "application",
                    app_name,
                    "missing 'submission-details' field in fields list",
                )
                has_errors = True

        # If fields are present, check that all referenced fields exist in field definitions
        if app_fields:
            for field_def in app_fields:
                field_name = field_def.get("field")
                if field_name and field_name not in fields:
                    print_error(
                        "application",
                        app_name,
                        f"referenced field '{field_name}' not found in field definitions",
                    )
                    has_errors = True

    return not has_errors


def check_modules_attr_present(applications):
    """
    Check rule 3: each application schema must have a modules attr
    """

    has_errors = False

    for app_name, application in applications.items():
        # If 'extends' is present, modules attr is not required
        if "extends" in application:
            continue
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
        (check_combined_application_types_headers, []),
        (check_combined_application_type_rows, [applications]),
    ]

    return run_checks(checks_with_args)


if __name__ == "__main__":
    success = check_all()
    exit(0 if success else 1)
