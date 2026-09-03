from planning_application_specification.guidance import load_guidance

from integrity_checks.utils import print_error, run_checks


def _uses_field(container, field_ref, fields, components, seen_components=None):
    """Return whether a container uses a field, including through components."""
    seen_components = seen_components or set()

    for field_usage in container.get("fields", []):
        usage_ref = field_usage.get("field")
        if usage_ref == field_ref:
            return True

        field_definition = fields.get(usage_ref, {})
        component_ref = field_usage.get("component") or field_definition.get(
            "component"
        )
        if not component_ref or component_ref in seen_components:
            continue

        component = components.get(component_ref)
        if component and _uses_field(
            component,
            field_ref,
            fields,
            components,
            seen_components | {component_ref},
        ):
            return True

    return False


def check_references(root, datasets, modules, components, fields):
    """Check every guidance entry refers to an existing container and field usage."""
    try:
        guidance_index = load_guidance(root)
    except ValueError as error:
        print_error("guidance", "metadata", str(error))
        return False

    containers = {
        "dataset": datasets,
        "module": modules,
        "component": components,
    }
    has_errors = False

    for (container_type, container_ref, field_ref), _guidance in guidance_index.items():
        container = containers[container_type].get(container_ref)
        guidance_ref = (
            f"{container_type}/{container_ref}/field/{field_ref}"
            if field_ref
            else f"{container_type}/{container_ref}"
        )

        if container is None:
            print_error(
                "guidance",
                guidance_ref,
                f"referenced {container_type} '{container_ref}' does not exist",
            )
            has_errors = True
            continue

        if field_ref is None:
            continue

        if field_ref not in fields:
            print_error(
                "guidance",
                guidance_ref,
                f"referenced field '{field_ref}' does not exist",
            )
            has_errors = True
            continue

        if not _uses_field(container, field_ref, fields, components):
            print_error(
                "guidance",
                guidance_ref,
                f"field '{field_ref}' is not used by {container_type} '{container_ref}'",
            )
            has_errors = True

    return not has_errors


def check_all(root, datasets, modules, components, fields):
    """Run all guidance integrity checks."""
    return run_checks(
        [(check_references, [root, datasets, modules, components, fields])]
    )
