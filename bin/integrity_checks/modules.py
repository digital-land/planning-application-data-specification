from integrity_checks.utils import (
    get_object_field_names,
    has_reference_error,
    iter_required_if_field_refs,
    print_error,
    run_checks,
)

# MODULES (.schema.md files)
# ==========

# 1. module attr must be string, kebab-case and unique across all modules
# 2. each field in fields attr must be a field reference in /fields
# 3. every module must have entry-date and end-date attrs

# . if applies-if attr with `application-type` then must be a valid application type TODO
# applies-if condition should be a dict not a list TODO
# . if required-if attr with `application-type` then must be a valid application type TODO
# . if required-if attr with `field` then must be a valid field TODO
# . warning if module is defined but not used in any application TODO


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
    and must not be end-dated/deprecated
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
                continue

            field_def = fields[field_name]
            # Treat fields with an end-date as deprecated/inactive
            if field_def.get("end-date"):
                print_error(
                    "module",
                    module_name,
                    f"referenced field '{field_name}' is deprecated (has end-date {field_def.get('end-date')})",
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


def check_attrs(modules):
    """
    Check rule 4: each module only has the permitted attributes
    """
    has_errors = False

    attrs = [
        "module",
        "name",
        "description",
        "fields",
        "entry-date",
        "end-date",
        "rules",
        "notes",
        "implementation",
    ]

    for module_name, module in modules.items():
        # Robustly get keys from dict or frontmatter.Post
        if hasattr(module, "keys"):
            keys = module.keys()
        elif hasattr(module, "metadata"):
            keys = module.metadata.keys()
        else:
            keys = []
        for attr in keys:
            if attr not in attrs:
                print_error("module", module_name, f"unexpected attribute '{attr}'")
                has_errors = True

    return not has_errors


def check_applies_if_structure(modules):
    """
    Ensure that any `applies-if` condition in module field entries is a dict
    (not a list). The model expects a mapping of conditions, for example:

      applies-if:
        application-type:
          in: [outline, reserved-matters]

    Some authors use a list of condition objects; flag those as errors.
    """
    has_errors = False

    for module_name, module in modules.items():
        module_fields = module.get("fields", [])
        for idx, field_def in enumerate(module_fields):
            applies_if = field_def.get("applies-if")
            if applies_if is None:
                continue
            # if it's a list (common mistake) that's an error
            if isinstance(applies_if, list):
                print_error(
                    "module",
                    module_name,
                    f"field #{field_def.get('field')} has 'applies-if' as a list; expected mapping/dict",
                )
                has_errors = True
            # also reject other non-dict types
            elif not isinstance(applies_if, dict):
                print_error(
                    "module",
                    module_name,
                    f"field #{field_def.get('field')} has 'applies-if' with unexpected type {type(applies_if).__name__}",
                )
                has_errors = True

    return not has_errors


def check_required_if_fields(modules):
    """
    Check rule: if required-if attribute is present, and references other fields that those fields must exist
    """
    has_errors = False

    for module_name, module in modules.items():
        module_fields = module.get("fields", [])
        module_field_names = get_object_field_names(module_fields)
        for field_def in module_fields:
            required_if = field_def.get("required-if")
            if required_if is None:
                continue

            if not isinstance(required_if, (list, dict)):
                print_error(
                    "module",
                    module_name,
                    f"field #{field_def.get('field')} has 'required-if' with unexpected type {type(required_if).__name__}",
                )
                has_errors = True
                continue

            for ref_field in iter_required_if_field_refs(required_if):
                if ref_field not in module_field_names:
                    print_error(
                        "module",
                        module_name,
                        f"field #{field_def.get('field')} references missing required-if field '{ref_field}' in this module",
                    )
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
        (check_attrs, [modules]),
        (check_applies_if_structure, [modules]),
        (check_required_if_fields, [modules]),
    ]

    return run_checks(checks_with_args)


if __name__ == "__main__":
    success = check_all()
    exit(0 if success else 1)
