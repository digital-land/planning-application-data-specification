"""Component integrity checks."""

from typing import Any, Dict, List

from utils import check_kebab_case


def print_error(component_name: str, message: str) -> None:
    """Print error message in a consistent format."""
    print(f"Error in component '{component_name}': {message}")


# COMPONENTS
# ===========
# 1. component attr must be string, kebab-case and unique across all components
# 2. each field in fields attr must be a field reference in /fields
# 3. if required-if attr with `application-type` then must be a valid application type TODO
# 4. if required-if attr with `field` then must be a valid field reference in /fields
# 5. every component must have entry-date and end-date attrs


def check_component_names(components: List[Dict[str, Any]]) -> bool:
    """Check rule 1: component attr must be string, kebab-case and unique."""
    seen_components = set()
    has_errors = False

    for component_name, component in components.items():
        # components use 'module' as name
        if not isinstance(component_name, str):
            print_error(str(component_name), "component name must be a string")
            has_errors = True
            continue
        if not check_kebab_case(component_name):
            print_error(component_name, "component name must be in kebab-case")
            has_errors = True
        if component_name in seen_components:
            print_error(component_name, "duplicate component name")
            has_errors = True
        seen_components.add(component_name)
    return not has_errors


def check_field_references(
    components: List[Dict[str, Any]], fields: Dict[str, Any]
) -> bool:
    """Check rule 2: each field must reference an existing field."""
    has_errors = False
    for component_name, component in components.items():

        component_fields = component.get("fields", [])
        for field_def in component_fields:
            field_name = field_def.get("field")
            if not field_name:
                print_error(component_name, "missing field name in fields list")
                has_errors = True
                continue
            if field_name not in fields:
                print_error(
                    component_name,
                    f"field '{field_name}' not found in field definitions",
                )
                has_errors = True
    return not has_errors


def check_application_type_references(
    components: List[Dict[str, Any]], valid_types: List[str]
) -> bool:
    """Check rule 3: application-type in required-if must be valid."""
    has_errors = False
    for component in components:
        component_name = component.get("module", "unknown")
        fields = component.get("fields", [])
        for field_def in fields:
            required_if = field_def.get("required-if", [])
            for condition in required_if:
                app_type = condition.get("application-type", {}).get("in", [])
                if app_type:
                    for type_name in app_type:
                        if type_name not in valid_types:
                            print_error(
                                component_name,
                                f"invalid application type '{type_name}'",
                            )
                            has_errors = True
    return not has_errors


def check_field_condition_references(
    components: List[Dict[str, Any]], fields: Dict[str, Any]
) -> bool:
    """Check rule 4: field in required-if must reference valid field."""
    has_errors = False
    for component_name, component in components.items():
        component_fields = component.get("fields", [])
        for field_def in component_fields:
            required_if = field_def.get("required-if", [])

            # Check if required_if is a list
            if not isinstance(required_if, list):
                print_error(
                    component_name,
                    f"required-if must be a list of conditions, got {type(required_if).__name__}",
                )
                has_errors = True
                continue

            for condition in required_if:
                # Check if condition is a dictionary
                if not isinstance(condition, dict):
                    print_error(
                        component_name,
                        f"required-if condition must be a dictionary, got {type(condition).__name__}",
                    )
                    has_errors = True
                    continue

                # First check if condition has any valid condition keys
                valid_condition_keys = ["field", "application-type"]
                has_valid_condition = any(
                    key in condition for key in valid_condition_keys
                )

                if not has_valid_condition:
                    print_error(
                        component_name,
                        f"required-if condition must contain at least one of: {', '.join(valid_condition_keys)}",
                    )
                    has_errors = True
                    continue

                # Check field references if present
                field_name = condition.get("field", None)
                if field_name and field_name not in fields:
                    print_error(
                        component_name, f"field '{field_name}' in required-if not found"
                    )
                    has_errors = True
    return not has_errors


def check_dates(components: List[Dict[str, Any]]) -> bool:
    """Check rule 5: must have entry-date and end-date."""
    has_errors = False
    for component_name, component in components.items():

        if "entry-date" not in component:
            print_error(component_name, "missing entry-date")
            has_errors = True
        if "end-date" not in component:
            print_error(component_name, "missing end-date")
            has_errors = True
    return not has_errors


def check_all(
    components: List[Dict[str, Any]], fields: Dict[str, Any], valid_types: List[str]
) -> bool:
    """Run all component integrity checks.

    Args:
        components: List of component definitions
        fields: Dictionary of field definitions
        valid_types: List of valid application types

    Returns:
        bool: True if all checks pass, False otherwise
    """
    checks_with_args = [
        (check_component_names, [components]),
        (check_field_references, [components, fields]),
        # (check_application_type_references, [components, valid_types]),
        (check_field_condition_references, [components, fields]),
        (check_dates, [components]),
    ]

    all_passed = True
    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False
    return all_passed


if __name__ == "__main__":
    # Load data for standalone testing
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from loader import load_content

    specification = load_content()
    components = specification["component"]
    fields = specification["field"]
    valid_types = []  # TODO: load valid application types

    success = check_all(components, fields, valid_types)
    exit(0 if success else 1)
