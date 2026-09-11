from integrity_checks.utils import (
    field_usage_requirement_errors,
    get_object_field_names,
    has_reference_error,
    iter_all_structure_errors,
    iter_redundant_field_component_overrides,
    iter_required_if_field_refs,
    iter_required_if_operator_errors,
    print_error,
    run_checks,
)

# MODULES (.schema.md files)
# ==========

# 1. module attr must be string, kebab-case and unique across all modules
# 2. each field in fields attr must be a field reference in /fields
# 3. every module must have entry-date and end-date attrs

# . if applies-if attr with `application-type` then must be a valid application type
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


def check_redundant_component_overrides(modules, fields):
    """
    Check field instances do not repeat their field definition's component.
    """
    has_errors = False

    for module_name, module in modules.items():
        for field_name, component_ref in iter_redundant_field_component_overrides(
            module.get("fields", []), fields
        ):
            print_error(
                "module",
                module_name,
                f"field '{field_name}' repeats default component '{component_ref}'",
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


def iter_applies_if_conditions(condition):
    """Walk scope conditions, including those grouped under all."""
    if not isinstance(condition, dict):
        return
    yield condition
    children = condition.get("all", [])
    if isinstance(children, list):
        for child in children:
            yield from iter_applies_if_conditions(child)


def check_applies_if_structure(modules, application_types=None):
    """
    Ensure that any `applies-if` condition in module field entries is a dict
    (not a list). The model expects a mapping of conditions, for example:

      applies-if:
        application-type:
          in: [outline, reserved-matters]

    Some authors use a list of condition objects; flag those as errors.
    Check application-type references inside explicit all groups too.
    """
    has_errors = False
    valid_application_types = (
        set(application_types) if application_types is not None else None
    )

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
                continue
            # also reject other non-dict types
            elif not isinstance(applies_if, dict):
                print_error(
                    "module",
                    module_name,
                    f"field #{field_def.get('field')} has 'applies-if' with unexpected type {type(applies_if).__name__}",
                )
                has_errors = True
                continue

            structure_errors = list(iter_all_structure_errors(applies_if, "applies-if"))
            for error in structure_errors:
                print_error("module", module_name, f"field #{field_def.get('field')} {error}")
                has_errors = True
            if structure_errors:
                continue

            module_field_names = get_object_field_names(module_fields)
            for condition in iter_applies_if_conditions(applies_if):
                # Allow an incomplete equality condition through to the specific
                # missing-value error below, but reject other vocabularies first.
                if set(condition) not in (
                    {"all"}, {"application-type"}, {"field", "value"}, {"field"},
                ):
                    print_error(
                        "module", module_name,
                        f"field #{field_def.get('field')} has an unsupported applies-if condition; "
                        "use application-type with in, field with value, or an all group",
                    )
                    has_errors = True
                    continue
                if "field" in condition:
                    if "value" not in condition:
                        print_error(
                            "module", module_name,
                            f"field #{field_def.get('field')} applies-if answer condition must include 'value'",
                        )
                        has_errors = True
                    reference = condition["field"]
                    error = None
                    if not isinstance(reference, str) or not reference.strip():
                        error = "applies-if field reference must be a non-empty string"
                    elif reference == field_def.get("field"):
                        error = "applies-if field must not reference itself"
                    elif "." in reference or reference not in module_field_names:
                        error = f"applies-if field '{reference}' must name another field in the same module"
                    if error:
                        print_error("module", module_name, f"field #{field_def.get('field')} {error}")
                        has_errors = True

                if "application-type" not in condition:
                    continue
                application_type = condition["application-type"]
                if not isinstance(application_type, dict):
                    print_error(
                        "module", module_name,
                        f"field #{field_def.get('field')} applies-if application-type must be a mapping containing 'in'",
                    )
                    has_errors = True
                    continue
                if set(application_type) - {"in"}:
                    print_error(
                        "module", module_name,
                        f"field #{field_def.get('field')} has an unsupported applies-if application-type selector; use only 'in'",
                    )
                    has_errors = True
                    continue
                application_type_refs = application_type.get("in")
                if (
                    not isinstance(application_type_refs, list)
                    or not application_type_refs
                    or any(not isinstance(ref, str) or not ref.strip() for ref in application_type_refs)
                ):
                    print_error(
                        "module", module_name,
                        f"field #{field_def.get('field')} applies-if application-type.in must be a non-empty list of non-empty strings",
                    )
                    has_errors = True
                    continue
                if valid_application_types is None:
                    continue
                for application_type_ref in application_type_refs:
                    if application_type_ref not in valid_application_types:
                        print_error(
                            "module",
                            module_name,
                            f"field #{field_def.get('field')} references unknown applies-if application-type '{application_type_ref}'",
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
                # TODO: resolve dotted field paths against the full application
                # structure once cross-module path semantics are formalised.
                if "." in ref_field:
                    continue
                if ref_field not in module_field_names:
                    print_error(
                        "module",
                        module_name,
                        f"field #{field_def.get('field')} references missing required-if field '{ref_field}' in this module",
                    )
                    has_errors = True

            for error in iter_required_if_operator_errors(required_if):
                print_error(
                    "module",
                    module_name,
                    f"field #{field_def.get('field')} {error}",
                )
                has_errors = True

    return not has_errors


def check_field_requirement_attributes(modules):
    """Check submission module fields do not use requirement-level."""
    has_errors = False

    for module_name, module in modules.items():
        for field_name, message in field_usage_requirement_errors(
            module.get("fields", []), allow_requirement_level=False
        ):
            print_error("module", module_name, f"field '{field_name}' {message}")
            has_errors = True

    return not has_errors


def check_all(modules, fields, applications=None):
    """Run all module integrity checks.

    Args:
        modules: Dictionary of module definitions
        fields: Dictionary of field definitions
        applications: Dictionary of application definitions
    """
    # Define checks and their required arguments
    checks_with_args = [
        (check_module_names, [modules]),
        (check_field_references, [modules, fields]),
        (check_redundant_component_overrides, [modules, fields]),
        (check_dates, [modules]),
        (check_attrs, [modules]),
        (check_applies_if_structure, [modules, applications]),
        (check_required_if_fields, [modules]),
        (check_field_requirement_attributes, [modules]),
    ]

    return run_checks(checks_with_args)


if __name__ == "__main__":
    success = check_all()
    exit(0 if success else 1)
