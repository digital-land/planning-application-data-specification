from utils import check_kebab_case

ANSI_RED = "\033[31m"
ANSI_YELLOW = "\033[33m"
ANSI_RESET = "\033[0m"


def print_error(element: str, field_name: str, message: str):
    """Utility function to print errors in a consistent format."""
    print(f"{ANSI_RED}Error in {element} '{field_name}': {message}{ANSI_RESET}")


def print_warning(element: str, element_name: str, message: str):
    """Utility function to print warnings in a consistent format."""
    print(f"{ANSI_YELLOW}Warning in {element} '{element_name}': {message}{ANSI_RESET}")


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


def get_object_field_names(field_definitions):
    """Return set of field names defined on a module/component fields list."""
    field_names = set()
    for field_def in field_definitions or []:
        if isinstance(field_def, dict):
            field_name = field_def.get("field")
            if isinstance(field_name, str):
                field_names.add(field_name)
    return field_names


def iter_redundant_field_component_overrides(field_instances, fields):
    """Yield field instances that repeat their field definition's component."""
    for field_instance in field_instances or []:
        if not isinstance(field_instance, dict):
            continue
        if "component" not in field_instance:
            continue

        field_name = field_instance.get("field")
        if field_name not in fields:
            continue

        default_component = fields[field_name].get("component")
        override_component = field_instance.get("component")
        if default_component and override_component == default_component:
            yield field_name, override_component


def iter_required_if_field_refs(required_if, *, inside_contains=False):
    """Yield top-level `field` references found within a required-if structure."""
    if isinstance(required_if, list):
        for item in required_if:
            yield from iter_required_if_field_refs(item, inside_contains=inside_contains)
        return

    if isinstance(required_if, dict):
        for key, value in required_if.items():
            if key == "field" and not inside_contains:
                if isinstance(value, str):
                    yield value
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, str):
                            yield item
            elif key == "contains":
                # TODO: resolve nested selectors such as `contains.field` against the
                # component referenced by the parent field when component paths are
                # modelled explicitly enough for integrity checks.
                yield from iter_required_if_field_refs(value, inside_contains=True)
            else:
                yield from iter_required_if_field_refs(value, inside_contains=inside_contains)


def run_checks(checks_with_args):
    """Run a sequence of checks and return True only if all pass."""
    all_passed = True

    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False

    return all_passed
