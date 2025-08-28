from integrity_checks.utils import has_reference_error, print_error
from utils import check_kebab_case


def print_error(field_name: str, message: str):
    """Utility function to print errors in a consistent format."""
    print(f"Error in field '{field_name}': {message}")


# FIELDS
# ======

# 1. field attr must be string, kebab-case and unique across all fields
# 2. cardinality is one of: 1 or n
# 3. check the data types TODO
# 4. if datatype is object then must have component attr
# 5. component attr must a component reference in /components
# 6. if datatype is enum then must have codelist attr, and if has codelist then datatype must be enum
# 7. codelist must be in codelist definitions TODO
# 8. every field must have entry-date and end-date attrs


def check_field_names(fields):
    """
    Check rule 1: field attr must be string, kebab-case and unique across all fields
    """
    seen_fields = set()
    has_errors = False

    for field_name, field in fields.items():

        has_errors |= has_reference_error(field_name, "field", seen_fields)

        seen_fields.add(field_name)

    return not has_errors


def check_cardinality(fields):
    """
    Check rule 2: cardinality is one of: 1 or n
    """
    valid_values = {"1", "n"}
    has_errors = False

    for field_name, field in fields.items():
        cardinality = field.get("cardinality")
        if str(cardinality) not in valid_values:
            print_error(
                field.get("field", "unknown"),
                f"cardinality must be one of {valid_values}, got {cardinality}",
            )
            has_errors = True

    return not has_errors


def check_object_components(fields, components):
    """
    Check rules 4 & 5: if datatype is object then must have component attr,
    and component must exist
    """
    has_errors = False

    for field_name, field in fields.items():
        if field.get("datatype") == "object":
            component = field.get("component")
            field_name = field.get("field", "unknown")

            if not component:
                print_error(field_name, "object type must have component attribute")
                has_errors = True
            elif component not in components:
                print_error(
                    field_name,
                    f"component '{component}' not found in component definitions",
                )
                has_errors = True

    return not has_errors


def check_enum_codelist(fields):
    """
    Check rule 6: if datatype is enum then must have codelist attr,
    and if has codelist attr then datatype must be enum
    """
    has_errors = False

    for field_name, field in fields.items():
        datatype = field.get("datatype")
        codelist = field.get("codelist")
        field_name = field.get("field", "unknown")

        # If datatype is enum, must have codelist
        if datatype == "enum" and not codelist:
            print_error(field_name, "enum datatype must have codelist attribute")
            has_errors = True

        # If has codelist, datatype must be enum
        if codelist and datatype != "enum":
            print_error(
                field_name, f"codelist attribute requires enum datatype, got {datatype}"
            )
            has_errors = True

    return not has_errors


def check_codelist_exists(fields, codelists):
    """
    Check rule 7: any field that has a codelist attribute must reference an
    existing codelist definition.
    Args:
        fields: dict of field definitions
        codelists: iterable or dict of available codelist names
    """
    has_errors = False

    # Normalize codelists to a set of names for lookup
    if isinstance(codelists, dict):
        available = set(codelists.keys())
    else:
        try:
            available = set(codelists)
        except Exception:
            available = set()

    for field_name, field in fields.items():
        codelist = field.get("codelist")
        field_name = field.get("field", "unknown")
        if codelist:
            # codelists in other checks are kebab-case ids; allow either the
            # codelist key or the codelist value to be used as lookup.
            if codelist not in available:
                print_error(
                    field_name,
                    f"codelist '{codelist}' not found in codelist definitions",
                )
                has_errors = True

    return not has_errors


def check_dates(fields):
    """
    Check rule 8: every field must have entry-date and end-date attrs
    """
    has_errors = False

    for field_name, field in fields.items():
        if "entry-date" not in field:
            print_error(field_name, "missing entry-date")
            has_errors = True
        if "end-date" not in field:
            print_error(field_name, "missing end-date")
            has_errors = True

    return not has_errors


def check_all(fields, components):
    """Run all field integrity checks.

    Args:
        fields: Dictionary of field definitions
        components: List of component names
    """
    # Define checks and their required arguments
    checks_with_args = [
        (check_field_names, [fields]),
        (check_cardinality, [fields]),
        (check_object_components, [fields, components]),
        (check_enum_codelist, [fields]),
        (
            check_codelist_exists,
            [
                fields,
                components.get("codelists", []) if isinstance(components, dict) else [],
            ],
        ),
        (check_dates, [fields]),
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
