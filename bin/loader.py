from glob import glob
from applications import get_application_module_refs

import frontmatter

# import here to avoid import-time cycles
from models import ApplicationDef, ComponentDef, ComponentInstance, FieldDef, ModuleDef

tables = {
    "application": {},
    "codelist": {},
    "component": {},
    "field": {},
    "module": {},
    # "planning-requirement": {},
}


def load_table_content(table):
    file_path = "*.md"
    if table in ["application", "module", "codelist"]:
        file_path = "*.schema.md"

    for path in glob(f"specification/{table}/{file_path}"):
        post = frontmatter.load(path)
        tables[table][post[table]] = post


def load_content():
    for table in tables.keys():
        load_table_content(table)
    return tables


def load_specification_model():
    """
    Load raw frontmatter tables and compile them into dataclass model objects
    (ModuleDef, ComponentDef, FieldDef, ApplicationDef) defined in
    `bin.models`. Returns a dict containing the built indices.
    """
    tables = load_content()
    component_index = tables["component"]
    module_index = tables["module"]

    # load field models
    field_defs = {}
    for field_ref, content in tables.get("field", {}).items():
        field_def = dict(content)
        f = FieldDef.from_spec(field_def)
        if f.ref:
            field_defs[f.ref] = f

    # After we've loaded components (below) we'll attach resolved_component
    # wrappers to any FieldDef that references a component. To do that we need
    # component_index populated; we therefore defer creating ComponentInstance
    # wrappers until after component_defs are built.

    # load component models
    component_defs = {}
    for component_ref, content in tables.get("component", {}).items():
        component_def = dict(content)
        c = ComponentDef.from_spec(component_def, field_defs, component_index)
        if c.ref:
            component_defs[c.ref] = c

    # Now attach resolved_component ComponentInstance wrappers to field_defs
    # where applicable. This lets consumers know which component a field
    # references while preserving the shared ComponentDef.
    for f in field_defs.values():
        if f.component:
            comp = component_defs.get(f.component)
            if comp:
                f.resolved_component = ComponentInstance(component=comp, referenced_by_field=f)

    # load module models
    module_defs = {}
    for module_ref, content in tables.get("module", {}).items():
        module_def = dict(content)
        c = ModuleDef.from_spec(module_def, field_defs, component_defs)
        if c.ref:
            module_defs[c.ref] = c

    # load application models
    application_defs = {}
    for application_ref, content in tables.get("application", {}).items():
        application_def = dict(content)
        a = ApplicationDef.from_spec(
            application_def, field_defs, component_defs, module_defs
        )
        if a.application:
            application_defs[a.ref] = a

    # Resolve inheritance for all applications
    for app_ref, app_def in application_defs.items():
        if app_def.extends:
            resolved_module_refs = get_application_module_refs(app_ref, tables)
            resolved_modules = [module_defs.get(ref) for ref in resolved_module_refs if module_defs.get(ref)]
            app_def.modules = resolved_modules

    specification_model = {
        "tables": tables,
        "modules": module_defs,
        "components": component_defs,
        "applications": application_defs,
        "fields": field_defs,
    }

    return specification_model


if __name__ == "__main__":
    specification_model = load_specification_model()

    print(specification_model)
