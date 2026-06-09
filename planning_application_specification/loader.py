from __future__ import annotations

from glob import glob
from pathlib import Path

import frontmatter

from .applications import get_application_module_refs
from .models import ApplicationDef, ComponentDef, ComponentUsage, FieldDef, ModuleDef


def make_tables():
    return {
        "application": {},
        "codelist": {},
        "component": {},
        "dataset": {},
        "field": {},
        "module": {},
        "specification": {},
        "usage": {},
    }


def make_needs_tables():
    return {"need": {}, "justification": {}}


def _resolve_repo_root(path: str | Path | None = None) -> Path:
    if path is not None:
        root = Path(path).resolve()
        if not (root / "specification").exists():
            raise FileNotFoundError(
                f"Could not find a specification directory under {root}"
            )
        return root

    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "specification").exists():
            return candidate

    raise FileNotFoundError(
        "Could not detect the repository root. Pass the repo path to Specification.load(...)."
    )


def load_table_content(table, target_tables, root_path: str | Path | None = None):
    root = _resolve_repo_root(root_path)
    file_path = "*.md"
    if table in ["application", "module", "codelist", "dataset", "usage"]:
        file_path = "*.schema.md"

    if table == "specification":
        pattern = str(root / "specification" / "*.schema.md")
    else:
        pattern = str(root / "specification" / table / file_path)

    for path in glob(pattern):
        post = frontmatter.load(path)
        target_tables[table][post[table]] = post


def load_content(root_path: str | Path | None = None):
    tables = make_tables()
    for table in tables.keys():
        load_table_content(table, tables, root_path=root_path)
    tables["__root_path__"] = _resolve_repo_root(root_path)
    return tables


def load_needs(root_path: str | Path | None = None):
    root = _resolve_repo_root(root_path)
    needs_tables = make_needs_tables()

    def load_dir(target, pattern, key_fields, target_tables):
        for path in glob(str(root / pattern)):
            post = frontmatter.load(path)
            post["__body__"] = post.content
            key = next((post.get(k) for k in key_fields if post.get(k)), None)
            if key:
                target_tables[target][key] = post

    load_dir("need", "user-needs/need/*.md", ["need"], needs_tables)
    load_dir("justification", "user-needs/justification/*.md", ["id"], needs_tables)

    return needs_tables


def load_specification_model(root_path: str | Path | None = None):
    tables = load_content(root_path=root_path)

    field_defs = {}
    for field_ref, content in tables.get("field", {}).items():
        field_def = dict(content)
        field = FieldDef.from_spec(field_def)
        field.body = content.content
        if field.ref:
            field_defs[field.ref] = field

    component_index = tables["component"]
    component_defs = {}
    for component_ref, content in tables.get("component", {}).items():
        component_def = dict(content)
        component = ComponentDef.from_spec(component_def, field_defs, component_index)
        if component.ref:
            component_defs[component.ref] = component

    for field in field_defs.values():
        if field.component:
            component = component_defs.get(field.component)
            if component:
                field.resolved_component = ComponentUsage(
                    component=component, referenced_by_field=field
                )

    module_defs = {}
    for module_ref, content in tables.get("module", {}).items():
        module_def = dict(content)
        module = ModuleDef.from_spec(module_def, field_defs, component_defs)
        if module.ref:
            module_defs[module.ref] = module

    application_defs = {}
    for application_ref, content in tables.get("application", {}).items():
        application_def = dict(content)
        application = ApplicationDef.from_spec(
            application_def, field_defs, component_defs, module_defs
        )
        if application.application:
            application_defs[application.ref] = application

    for app_ref, app_def in application_defs.items():
        if app_def.extends:
            resolved_module_refs = get_application_module_refs(app_ref, tables)
            resolved_modules = [
                module_defs.get(ref)
                for ref in resolved_module_refs
                if module_defs.get(ref)
            ]
            app_def.modules = resolved_modules

    return {
        "tables": tables,
        "modules": module_defs,
        "components": component_defs,
        "applications": application_defs,
        "fields": field_defs,
    }
