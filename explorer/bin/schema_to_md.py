#!/usr/bin/env python3

import sys
from pathlib import Path

import click
import frontmatter
import yaml

FIELD_DIR = Path("specification/field")
COMPONENT_DIR = Path("specification/component")

# Helper to load a field or component definition


def load_frontmatter_md(path):
    post = frontmatter.load(path)
    return post.metadata, post.content


def get_field_md(field_name):
    path = FIELD_DIR / f"{field_name}.md"
    if path.exists():
        return load_frontmatter_md(path)
    return None, None


def get_component_md(component_name):
    path = COMPONENT_DIR / f"{component_name}.md"
    if path.exists():
        return load_frontmatter_md(path)
    return None, None


def get_component_name(component_name):
    meta, _ = get_component_md(component_name)
    if meta:
        return meta.get("name") or component_name.replace("-", " ").capitalize()
    return component_name.replace("-", " ").capitalize()


def get_field_description(field_name):
    meta, _ = get_field_md(field_name)
    if meta:
        return meta.get("description", "")
    return ""


def get_field_component(field_name):
    meta, _ = get_field_md(field_name)
    if meta:
        return meta.get("component")
    return None


def get_field_codelist(field_name):
    meta, _ = get_field_md(field_name)
    if meta:
        return meta.get("codelist")
    return None


def get_field_cardinality(field, field_name=None):
    # Returns 'n' if cardinality is n, else None
    # Check inline first, then field definition
    if isinstance(field, dict) and field.get("cardinality") == "n":
        return "n"
    if field_name:
        meta, _ = get_field_md(field_name)
        if meta and meta.get("cardinality") == "n":
            return "n"
    return None


def parse_required(field):
    # Returns (required_str, notes_str)
    if isinstance(field, dict):
        if field.get("required-if"):
            # Only handle the first required-if for now
            cond = field["required-if"][0]
            for k, v in cond.items():
                if isinstance(v, dict) and "in" in v:
                    vals = v["in"]
                    vals_str = ", ".join(str(val) for val in vals)
                    return "MAY", f"MUST if {k} in [{vals_str}]"
                else:
                    return "MAY", f"MUST if {k} == {v}"
        if field.get("required") is True:
            return "MUST", ""
    return "MAY", ""


def get_field_display_name(field_name, is_component, cardinality):
    name = field_name
    # Always [] before {}
    if cardinality == "n":
        name += "[]"
    if is_component:
        name += "{}"
    return name


def any_field_required(fields):
    for field in fields:
        if isinstance(field, dict):
            if field.get("required") or field.get("required-if"):
                return True
        else:
            meta, _ = get_field_md(field)
            if meta and (meta.get("required") or meta.get("required-if")):
                return True
    return False


def render_fields_table(
    fields,
    parent_is_component=False,
    parent_descriptions=None,
    parent_component_name=None,
):
    lines = []
    show_required = parent_is_component and any_field_required(fields)
    if parent_is_component:
        if show_required:
            lines.append("| field | description | required | notes |")
            lines.append("| --- | --- | --- | --- |")
        else:
            lines.append("| field | description | notes |")
            lines.append("| --- | --- | --- |")
    else:
        lines.append("| field | description | application-types | required | notes |")
        lines.append("| --- | --- | --- | --- | --- |")

    parent_descriptions = parent_descriptions or {}

    for field in fields:
        # Determine field name and description
        if isinstance(field, str):
            meta, _ = get_field_md(field)
            name = meta.get("field", field) if meta else field
            desc = meta.get("description", "") if meta else ""
            is_component = bool(meta.get("component")) if meta else False
            component_name = meta.get("component") if meta else None
            codelist = meta.get("codelist") if meta else None
            cardinality = get_field_cardinality(meta or {}, name)
            required, notes = parse_required(meta or {})
            app_types = ""
        elif isinstance(field, dict):
            name = field.get("field", "")
            desc = field.get("description")
            if desc is None:
                desc = get_field_description(name)
            is_component = bool(get_field_component(name))
            component_name = get_field_component(name)
            codelist = get_field_codelist(name)
            cardinality = get_field_cardinality(field, name)
            required, notes = parse_required(field)
            app_types = field.get("application-types", "")
        else:
            continue
        # If component, mark with {}
        display_name = get_field_display_name(name, is_component, cardinality)
        # If parent provided a description for this field, override only if not overridden here
        if parent_descriptions.get(name) and not desc:
            desc = parent_descriptions[name]
        # Compose notes
        notes_list = []
        if notes:
            notes_list.append(notes)
        if is_component and component_name:
            comp_disp_name = get_component_name(component_name)
            notes_list.append(f"See {comp_disp_name}")
        if codelist:
            notes_list.append(f"See {codelist} enum")
        notes_str = ". ".join([n for n in notes_list if n])
        # Compose line
        if parent_is_component:
            if show_required:
                lines.append(f"| {display_name} | {desc} | {required} | {notes_str} |")
            else:
                lines.append(f"| {display_name} | {desc} | {notes_str} |")
        else:
            lines.append(
                f"| {display_name} | {desc} | {app_types} | {required} | {notes_str} |"
            )
    return lines, show_required


def render_component_structure(component_name, rendered=None, parent_descriptions=None):
    if rendered is None:
        rendered = set()
    if component_name in rendered:
        return []  # Prevent infinite recursion
    rendered.add(component_name)
    meta, _ = get_component_md(component_name)
    if not meta:
        return []
    fields = meta.get("fields", [])
    comp_disp_name = meta.get("name") or component_name.replace("-", " ").capitalize()
    lines = [f"\n**{comp_disp_name}**"]
    table_lines, show_required = render_fields_table(
        fields,
        parent_is_component=True,
        parent_descriptions=parent_descriptions,
        parent_component_name=comp_disp_name,
    )
    lines += table_lines
    # For each field, if it is a component, render its structure
    for field in fields:
        field_name = None
        if isinstance(field, str):
            meta_f, _ = get_field_md(field)
            if meta_f and meta_f.get("component"):
                field_name = meta_f["component"]
        elif isinstance(field, dict):
            meta_f, _ = get_field_md(field.get("field", ""))
            if meta_f and meta_f.get("component"):
                field_name = meta_f["component"]
        if field_name:
            lines += render_component_structure(
                field_name, rendered, parent_descriptions
            )
    # Add rules if present
    rules = meta.get("rules")
    if rules:
        lines.append("\nRules:")
        for rule in rules:
            if isinstance(rule, dict) and rule.get("rule"):
                lines.append(f"* {rule['rule']}")
            elif isinstance(rule, str):
                lines.append(f"* {rule}")
    return lines


@click.command()
@click.argument("schema_path", type=click.Path(exists=True))
def main(schema_path):
    schema_path = Path(schema_path)
    post = frontmatter.load(schema_path)
    meta = post.metadata
    # Top-level fields
    fields = meta.get("fields", [])
    # Render main table
    md_lines, _ = render_fields_table(fields)
    # For each field, if it is a component, render its structure
    rendered_components = set()
    for field in fields:
        component_name = None
        if isinstance(field, str):
            meta_f, _ = get_field_md(field)
            if meta_f and meta_f.get("component"):
                component_name = meta_f["component"]
        elif isinstance(field, dict):
            meta_f, _ = get_field_md(field.get("field", ""))
            if meta_f and meta_f.get("component"):
                component_name = meta_f["component"]
        if component_name and component_name not in rendered_components:
            md_lines += render_component_structure(component_name, rendered_components)
    # Write output
    output_dir = Path("explorer/spec/module")
    output_dir.mkdir(parents=True, exist_ok=True)
    module_name = meta.get("module")
    if not module_name:
        # fallback to schema filename if module attribute missing
        module_name = schema_path.stem.replace(".schema", "")
    output_path = output_dir / f"{module_name}.md"
    with open(output_path, "w") as f:
        f.write("\n".join(md_lines))
    print(f"Generated markdown file: {output_path}")


if __name__ == "__main__":
    main()
