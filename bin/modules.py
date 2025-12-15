from collections import OrderedDict, deque

from fields import get_applicable_app_types


def get_module(modules, ref):
    """
    Get a module by its reference.
    """
    if isinstance(modules, dict):
        return modules.get(ref)
    else:
        for module in modules:
            if module.get("reference") == ref or module.get("module") == ref:
                return module
        return None


def get_field(fields, ref):
    """
    Get a field by its reference.
    """
    if isinstance(fields, dict):
        return fields.get(ref)
    else:
        for field in fields:
            if field.get("reference") == ref or field.get("field") == ref:
                return field
        return None


def get_field_metadata(field_def):
    """
    Extract metadata from a field definition, handling both frontmatter objects and dicts.
    """
    if hasattr(field_def, "metadata"):
        return field_def.metadata
    elif isinstance(field_def, dict):
        return field_def
    else:
        return {}


def get_codelists_for_module(module, fields):
    """
    Get a list of codelists used in the module's fields.
    Returns a set of unique codelist names.
    """
    codelists = set()
    for field_entry in module.get("fields", []):
        field_ref = field_entry.get("field")
        if not field_ref:
            continue
        field_def = get_field(fields, field_ref)
        if not field_def:
            continue
        codelist = field_def.get("codelist")
        if codelist:
            codelists.add(codelist)
    return codelists


def enqueue_object_type_fields(
    field_entries, components, fields, already_enqueued, app_type=None
):
    """
    Helper to enqueue component references for object-type fields.
    If app_type is set, only enqueue fields whose applies-if matches the app_type (if present).
    """
    refs = []
    for field_entry in field_entries:
        field_name = field_entry.get("field")
        if not field_name:
            continue
        field_def = get_field(fields, field_name)
        if not field_def:
            continue
        field_metadata = get_field_metadata(field_def)
        # Check applies-if logic if app_type is set
        applies_if = field_entry.get("applies-if")
        if app_type and applies_if:
            app_types = get_applicable_app_types(field_entry)
            if app_types and app_type not in app_types:
                continue  # skip this field for this app_type
        # If no applies-if or app_type not set, proceed as before
        if field_metadata.get("datatype") == "object":
            component_ref = field_metadata.get("component")
            if (
                component_ref
                and component_ref in components
                and component_ref not in already_enqueued
            ):
                refs.append(component_ref)
                already_enqueued.add(component_ref)
    return refs


def collect_related_components_bfs(module_fields, components, fields, app_type=None):
    """
    Collect related components in breadth-first order (by nesting level).
    Returns an OrderedDict of component_ref: component_data.
    """
    related_components = OrderedDict()
    queue = deque()
    already_enqueued = set()

    # Enqueue all directly referenced components from module fields
    for ref in enqueue_object_type_fields(
        module_fields, components, fields, already_enqueued, app_type=app_type
    ):
        queue.append(ref)

    # Breadth-first traversal
    while queue:
        component_ref = queue.popleft()
        if component_ref in related_components:
            continue
        component = components.get(component_ref)
        if not component:
            continue
        related_components[component_ref] = component
        # Enqueue nested components from this component's fields
        for ref in enqueue_object_type_fields(
            component.get("fields", []),
            components,
            fields,
            already_enqueued,
            app_type=app_type,
        ):
            queue.append(ref)
    return related_components


# take a module and return a dictionary of module, list of related-components and validation rules
def get_module_parts(specification, ref, app_type=None):
    modules = specification["module"]
    fields = specification["field"]
    components = specification["component"]

    module = get_module(modules, ref)
    if not module:
        return None

    # Get the module fields list
    module_fields = module.get("fields", [])

    # Use breadth-first collection for related components
    related_components = collect_related_components_bfs(
        module_fields, components, fields, app_type=app_type
    )

    # Get validation rules
    rules = module.get("rules", [])

    return {"module": module, "related-components": related_components, "rules": rules}


def count_module_fields(
    specification, module_ref, include_related_components=False, app_type=None
):
    """
    Count the number of fields defined directly on a module. If
    include_related_components is True, include fields from related components
    discovered via collect_related_components_bfs.
    """
    module_parts = get_module_parts(specification, module_ref, app_type=app_type)
    if not module_parts:
        return 0

    count = len(module_parts["module"].get("fields", []))
    if include_related_components:
        for component in module_parts.get("related-components", {}).values():
            count += len(component.get("fields", []))
    return count


def print_module_field_counts(
    specification, include_related_components=False, app_type=None
):
    """
    Iterate over all modules in the specification and print their field counts.
    """
    modules = specification.get("module", {})
    for module_ref, module in modules.items():
        count = count_module_fields(
            specification,
            module_ref,
            include_related_components=include_related_components,
            app_type=app_type,
        )
        module_name = module.get("name", module_ref)
        print(f"{module_name} ({module_ref}): {count}")


if __name__ == "__main__":
    print("Testing modules.py")

    # Simple test to verify the function works
    try:
        from loader import load_content

        print("Loader imported successfully")

        specification = load_content()
        print("Specification loaded successfully")

        print_module_field_counts(specification=specification)

        # Test the function
        # result = get_module_parts(specification, "res-units")
        # result = get_module_parts(specification, "interest-details")
        result = get_module_parts(specification, "proposal-details")
        # result = get_module_parts(specification, "access-rights-of-way")
        print("Function called successfully")

        if result:
            print("✓ Module found and processed")
            print(f"✓ Related components: {len(result['related-components'])}")
            print(f"✓ Validation rules: {len(result['rules'])}")
        else:
            print("✗ Module not found")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback

        traceback.print_exc()
