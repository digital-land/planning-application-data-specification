from bin.markdown_utils import markdown_link, markdown_table
from planning_application_specification import Specification
from planning_application_specification.specification import (
    ResolvedComponentReference,
    SelectionContext,
)
from bin.utils import save_string_to_file


def format_resolved_field_display_name(resolved_field):
    name = resolved_field.name or resolved_field.ref
    if resolved_field.cardinality == "n":
        name += "[]"
    if resolved_field.datatype == "object":
        name += "{}"
    return name


def get_notes_for_resolved_field(resolved_field):
    notes = []
    codelist = None
    if hasattr(resolved_field.base, "codelist"):
        codelist = resolved_field.base.codelist
    if codelist:
        notes.append(f"Select from the **{codelist}** enum")
    required_if = resolved_field.required_if
    if isinstance(required_if, list):
        for cond in required_if:
            if isinstance(cond, dict) and "field" in cond and "value" in cond:
                notes.append(
                    f"Rule: is a MUST if `{cond['field']}` is `{cond['value']}`"
                )
    desc = resolved_field.notes or ""
    if desc:
        notes.append(desc)
    return notes


def get_only_for_application_str(resolved_item):
    applies_if = resolved_item.usage.applies_if
    if not isinstance(applies_if, dict):
        return ""

    app_type_condition = applies_if.get("application-type")
    if isinstance(app_type_condition, dict):
        allowed = app_type_condition.get("in")
        if isinstance(allowed, list):
            return ", ".join(allowed)

    return ""


def iter_display_rows(resolved_items, app_type=None):
    for resolved in resolved_items:
        if app_type and not resolved.applies:
            continue

        ref = resolved.ref
        name = format_resolved_field_display_name(resolved)
        description = resolved.description or ""
        requirement = "MUST" if resolved.required else "MAY"
        notes = get_notes_for_resolved_field(resolved)
        yield {
            "ref": ref,
            "name": name,
            "description": description,
            "requirement": requirement,
            "notes_md_str": ". ".join(str(n) for n in notes) if notes else "",
            "only_for_md_str": get_only_for_application_str(resolved),
        }


def get_container_ref(container):
    if hasattr(container, "ref"):
        return container.ref
    if isinstance(container, dict):
        return container.get("module") or container.get("component") or ""
    return ""


def get_container_name(container, default_ref=""):
    if hasattr(container, "name"):
        return container.name or default_ref
    if isinstance(container, dict):
        return container.get("name", default_ref)
    return default_ref


def get_container_description(container):
    if hasattr(container, "description"):
        return container.description or ""
    if isinstance(container, dict):
        return container.get("description", "")
    return ""


def _iter_nested_component_refs_from_items(resolved_items, package_spec, app_type=None):
    selection = SelectionContext(application_type=app_type) if app_type else None
    seen = set()
    queue = []

    def enqueue_from_items(resolved_items):
        for item in resolved_items:
            if not isinstance(item, ResolvedComponentReference):
                continue
            if app_type and not item.applies:
                continue
            if item.component_ref in seen:
                continue
            seen.add(item.component_ref)
            queue.append(item.component_ref)

    enqueue_from_items(resolved_items)

    idx = 0
    while idx < len(queue):
        component_ref = queue[idx]
        idx += 1
        yield component_ref
        enqueue_from_items(
            package_spec.resolve_container_items(
                component=component_ref,
                selection=selection,
            )
        )


def iter_module_component_refs(module_ref, package_spec, app_type=None):
    selection = SelectionContext(application_type=app_type) if app_type else None
    resolved_items = package_spec.resolve_container_items(
        module=module_ref,
        selection=selection,
    )
    yield from _iter_nested_component_refs_from_items(
        resolved_items,
        package_spec,
        app_type=app_type,
    )


def iter_component_component_refs(component_ref, package_spec, app_type=None):
    selection = SelectionContext(application_type=app_type) if app_type else None
    resolved_items = package_spec.resolve_container_items(
        component=component_ref,
        selection=selection,
    )
    yield from _iter_nested_component_refs_from_items(
        resolved_items,
        package_spec,
        app_type=app_type,
    )


def get_component_codelists(component):
    codelists = set()
    for field_usage in getattr(component, "field_usages", []):
        codelist = getattr(field_usage.original, "codelist", None)
        if codelist:
            codelists.add(codelist)
    return codelists


def format_main_module_table(module, app_type=None, package_spec=None):
    if package_spec is None:
        package_spec = Specification.load()

    selection = SelectionContext(application_type=app_type) if app_type else None
    rows = list(
        iter_display_rows(
            package_spec.resolve_container_items(
                module=get_container_ref(module),
                selection=selection,
            ),
            app_type=app_type,
        )
    )

    if app_type:
        lines = [
            "| reference | name | description | requirement | notes |",
            "| --- | --- | --- | --- | --- |",
        ]
        for row in rows:
            lines.append(
                f"| {row['ref']} | {row['name']} | {row['description']} | {row['requirement']} | {row['notes_md_str']} |"
            )
    else:
        lines = [
            "| reference | name | description | only for application | requirement | notes |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for row in rows:
            lines.append(
                f"| {row['ref']} | {row['name']} | {row['description']} | {row['only_for_md_str']} | {row['requirement']} | {row['notes_md_str']} |"
            )

    return "\n".join(lines)


def format_component_table(component, app_type=None, package_spec=None):
    if package_spec is None:
        package_spec = Specification.load()

    selection = SelectionContext(application_type=app_type) if app_type else None
    rows = list(
        iter_display_rows(
            package_spec.resolve_container_items(
                component=get_container_ref(component),
                selection=selection,
            ),
            app_type=app_type,
        )
    )
    has_applies_if = any(row["only_for_md_str"] for row in rows)
    if has_applies_if:
        lines = [
            "field | name | description | required | notes | only for application",
            "-- | -- | -- | -- | -- | --",
        ]
        for row in rows:
            lines.append(
                f"{row['ref']} | {row['name']} | {row['description']} | {row['requirement']} | {row['notes_md_str']} | {row['only_for_md_str']}"
            )
    else:
        lines = [
            "field | name | description | required | notes",
            "-- | -- | -- | -- | --",
        ]
        for row in rows:
            lines.append(
                f"{row['ref']} | {row['name']} | {row['description']} | {row['requirement']} | {row['notes_md_str']}"
            )

    return "\n".join(lines)


def format_rules_md_str(rules):
    if not rules:
        return ""
    lines = ["**Validation rules**\n"]
    for rule in rules:
        if isinstance(rule, dict):
            if "rule" in rule:
                lines.append(f"- {rule['rule']}")
            elif "description" in rule:
                lines.append(f"- {rule['description']}")
            else:
                lines.append(f"- {str(rule)}")
        else:
            lines.append(f"- {str(rule)}")
    return "\n".join(lines)


def append_titled_table_section(out, title, table_markdown, leading_newline=False):
    heading = f"**{title}**\n"
    if leading_newline:
        heading = "\n" + heading
    out.append(heading)
    out.append(table_markdown + "\n")


def append_component_sections(out, components, app_type=None, package_spec=None):
    component_iter = components.values() if hasattr(components, "values") else components
    for component in component_iter:
        cref = get_container_ref(component)
        append_titled_table_section(
            out,
            f"{get_container_name(component, cref)} component",
            format_component_table(
                component,
                app_type=app_type,
                package_spec=package_spec,
            ),
            leading_newline=True,
        )


def generate_module(module_ref, _specification=None, app_type=None, package_spec=None):
    if package_spec is None:
        package_spec = Specification.load()
    try:
        module = package_spec.module(module_ref)
    except KeyError:
        print(f"Module '{module_ref}' not found in specification.")
        return None

    related_components = [
        package_spec.component(component_ref)
        for component_ref in iter_module_component_refs(
            module_ref,
            package_spec,
            app_type=app_type,
        )
    ]
    rules = module.rules
    # Header
    out = [
        f"# {get_container_name(module, module_ref)}\n",
        get_container_description(module) + "\n",
    ]
    append_titled_table_section(
        out,
        f"{get_container_name(module, module_ref)} module",
        format_main_module_table(
            module,
            app_type=app_type,
            package_spec=package_spec,
        ),
    )
    append_component_sections(
        out,
        related_components,
        app_type=app_type,
        package_spec=package_spec,
    )
    out.append(format_rules_md_str(rules))
    return "\n".join(out)


def get_codelists_for_app(module_refs, package_spec):
    codelists = set()
    for module_ref in module_refs:
        for component_ref in iter_module_component_refs(module_ref, package_spec):
            component = package_spec.component(component_ref)
            codelists.update(get_component_codelists(component))
    return codelists


def codelist_item_rows(codelist_obj):
    rows = [item.row for item in codelist_obj.items if item.row]
    if not rows:
        return [], []

    headers = list(rows[0].keys())
    return headers, [[row.get(header, "") for header in headers] for row in rows]


def create_codelist_table(codelist_obj):
    lines = []
    name = getattr(codelist_obj, "name", None) or "Unknown"
    source = getattr(codelist_obj, "source", "") or ""

    # Heading
    heading = f"### {name}"
    lines.append(heading)

    # Source information
    if not source:
        lines.append("\n_codelist source not provided_\n")
    else:
        if isinstance(source, str) and (
            source.startswith("http://") or source.startswith("https://")
        ):
            lines.append(
                f"\nThis codelist is sourced from {markdown_link(source, source)}\n"
            )
        else:
            headers, rows = codelist_item_rows(codelist_obj)
            if not headers:
                lines.append(f"\nNo codelist rows available from: {source}\n")
            else:
                lines.append("")
                lines.append(markdown_table(headers, rows).rstrip())
                lines.append("")

    return "\n".join(lines) if lines else ""


def generate_codelist_md_str(codelists):
    """
    Generates a Markdown-formatted string with the codelists required for the
    specification.

    Args:
        codelists (list): A list of objects representing codelists. Each
            object should be convertible to a string or be a dict-like object.

    Returns:
        str: A Markdown-formatted string enumerating the codelist names, or an
        empty string if no codelists are provided.
    """
    # list out the codelist names
    if not codelists:
        return ""

    lines = []
    lines.append("Below are the codelists required to support this specification:\n")
    for codelist in codelists:
        lines.append(create_codelist_table(codelist))
    return "\n".join(lines)


def generate_application_fields_section(app_type=None, package_spec=None):
    if package_spec is None:
        package_spec = Specification.load()

    try:
        submission_details_field = package_spec.field("submission-details")
    except KeyError:
        print("Field definition for 'submission-details' not found in specification.")
        return None

    component_ref = submission_details_field.component or "submission-details"
    try:
        submission_details_component = package_spec.component(component_ref)
    except KeyError:
        print("Component definition for submission-details fields not found in specification.")
        return None

    heading_name = (submission_details_field.name or "Submission details").strip()
    if not heading_name:
        heading_name = "Submission details"
    heading_title = (
        heading_name
        if heading_name.lower().endswith("fields")
        else f"{heading_name} fields"
    )

    out = [f"## {heading_title}\n"]

    description = (
        get_container_description(submission_details_component)
        or submission_details_field.description
    )
    if description:
        out.append(description.strip() + "\n")

    module_label = (
        heading_title
        if heading_title.lower().endswith("fields")
        else f"{heading_title} fields"
    )
    append_titled_table_section(
        out,
        f"{module_label} module",
        format_component_table(
            submission_details_component,
            app_type=app_type,
            package_spec=package_spec,
        ),
    )

    related_components = [
        package_spec.component(component_ref)
        for component_ref in iter_component_component_refs(
            component_ref,
            package_spec,
            app_type=app_type,
        )
    ]
    append_component_sections(
        out,
        related_components,
        app_type=app_type,
        package_spec=package_spec,
    )

    validation_rules = submission_details_component.rules
    rules_str = format_rules_md_str(validation_rules)
    if rules_str:
        out.append(rules_str)

    return "\n".join(out)


def generate_application(app_ref, _specification=None):
    """
    Generate the information model for a specific application type.
    """
    package_spec = Specification.load()
    try:
        app = package_spec.application(app_ref)
    except KeyError:
        print(f"Application '{app_ref}' not found in specification.")
        return None

    # get the modules that are part of the application
    module_refs = [module.ref for module in app.modules]
    inc_codelists = get_codelists_for_app(module_refs, package_spec)
    inc_codelist_objs = sorted(
        [package_spec.codelist(ref) for ref in inc_codelists],
        key=lambda c: c.name,
    )

    # generate output
    # 1. Heading and Description
    out = [f"# {app.name or app_ref}\n"]
    if app.description:
        out.append(app.description + "\n")

    # 2. Contents
    out.append("## Contents\n")
    out.append("* [Application data specification](#application-data-specification)")
    # get full list of applicable modules
    out.append("")

    # 3. Modules List (contents)
    out.append("### Modules\n")
    for mod in module_refs:
        mod_name = package_spec.module(mod).name or mod.replace("-", " ").capitalize()
        anchor = mod_name.lower().replace(" ", "-")
        out.append(f"* [{mod_name}](#{anchor})")
    out.append("")

    # 4. Codelists (contents)
    out.append("### Codelists\n")
    for codelist in inc_codelist_objs:
        codelist_name = codelist.name or "Name unknown"
        anchor = codelist_name.lower().replace(" ", "-")
        out.append(f"* [{codelist_name}](#{anchor})")
    out.append("")

    # 5. Application Data Specification
    application_fields_section = generate_application_fields_section(
        app_type=app_ref, package_spec=package_spec
    )
    if application_fields_section:
        out.append(application_fields_section)
        out.append("")

    # 6. Module Sections
    for mod in module_refs:
        module_md = generate_module(
            mod,
            app_type=app_ref,
            package_spec=package_spec,
        )
        if module_md:
            # update first header of md file to be ## instead of #
            module_md = module_md.replace("# ", "## ", 1)
            out.append(module_md)
            out.append("")
        else:
            print(f"Module '{mod}' could not be generated.")

    # 7. Required Codelists
    if inc_codelists:
        out.append("## Required codelists\n")
        out.append(generate_codelist_md_str(inc_codelist_objs))

    return "\n".join(out)


if __name__ == "__main__":
    print("Testing information model generation script.")

    try:
        from bin.loader import load_content

        specification = load_content()
        print("Specification loaded successfully")

        # Test the function
        # result = save_string_to_file(
        #     "\n".join(generate_module("interest-details", specification)), "tmp/test-gen.md"
        # )
        # result = generate_module("res-units", specification, app_type="full")
        result = generate_module("demolition-reason", specification)
        # result = generate_module(
        #     "tree-work-details", specification, app_type="notice-trees-in-con-area"
        # )

        result = save_string_to_file(
            generate_application("advertising", specification),
            "generated/info_model/application/advertising.md",
        )
        print("Function called successfully")
        print(result)

    except Exception as e:
        print(f"✗ Error: {e}")
