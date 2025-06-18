from utils import check_kebab_case


def print_error(element: str, field_name: str, message: str):
    """Utility function to print errors in a consistent format."""
    print(f"Error in {element} '{field_name}': {message}")


def has_reference_error(ref: str, element: str, seen_fields: list) -> bool:
    """Check if a reference is valid."""
    if not isinstance(ref, str):
        print_error(element, str(ref), f"{element} name must be a string")
        return True

    if not check_kebab_case(ref):
        print_error(element, ref, f"{element} name must be in kebab-case")
        return True

    if ref in seen_fields:
        print_error(element, ref, f"duplicate {element} name")
        return True

    return False
