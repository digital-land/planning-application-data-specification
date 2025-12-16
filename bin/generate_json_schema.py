import csv
import json
from functools import lru_cache
from glob import glob
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

from json_schema_helpers import parse_and_generate_required_if_rules
from loader import load_content
from models import ComponentInstance, FieldDef, FieldInstance
from utils import save_string_to_file

OUTPUT_DIR = "generated/json-schema"
APPLICATIONS_OUTPUT_DIR = f"{OUTPUT_DIR}/applications"
CODELIST_DATA_DIR = "data/codelist"


@lru_cache(maxsize=1)
def get_codelists() -> Dict[str, List[str]]:
    """Get all field -> codelist values mappings from raw specification data (cached)"""
    try:
        script_dir = Path(__file__).parent.resolve()
        project_root = script_dir.parent
        data_dir = project_root / "data"
        all_csv_files = glob(str(data_dir / "**/*.csv"), recursive=True)
        codelist_path_map = {Path(f).stem: f for f in all_csv_files}
        raw_spec = load_content()
        codelists = {}

        for field_ref, raw_field in raw_spec.get("field", {}).items():
            if raw_field and hasattr(raw_field, "get"):
                codelist_name = raw_field.get("codelist")
                if codelist_name:
                    codelist_path = codelist_path_map.get(codelist_name)
                    if not codelist_path:
                        # Handle cases where filename doesn't match codelist name
                        if codelist_name == "application-type":
                            codelist_path = codelist_path_map.get(
                                "planning-application-type"
                            )
                        elif codelist_name == "application-sub-type":
                            codelist_path = codelist_path_map.get(
                                "planning-application-sub-type"
                            )

                    if not codelist_path:
                        print(f"Warning: Codelist file not found for {codelist_name}")
                        codelists[field_ref] = []
                    else:
                        try:
                            with open(codelist_path, "r", encoding="utf-8") as file:
                                reader = csv.DictReader(file)
                                values = [
                                    row["reference"]
                                    for row in reader
                                    if row.get("reference")
                                ]
                                codelists[field_ref] = values
                        except Exception as e:
                            print(f"Error loading codelist {codelist_name}: {e}")
                            codelists[field_ref] = []
        return codelists

    except Exception as e:
        print(f"Warning: Could not load field codelists: {e}")
        return {}


def get_field_codelist(field_ref: str) -> List[str]:
    """Get codelist values for a field from cached field codelist mapping"""
    codelists = get_codelists()
    return codelists.get(field_ref, [])


def resolve_field_schema(field_item, specification) -> Dict[str, Any]:
    """Convert FieldDef or FieldInstance to JSON Schema property"""

    if isinstance(field_item, FieldInstance):
        field_def = field_item.original
        overrides = field_item.overrides
        datatype = overrides.get("datatype", field_def.datatype)
        cardinality = overrides.get("cardinality", field_def.cardinality)
        component = overrides.get("component", field_def.component)
    else:
        field_def = field_item
        datatype = field_def.datatype
        cardinality = field_def.cardinality
        component = field_def.component

    schema = {}

    # Basic datatype mapping
    if datatype == "string":
        schema = {"type": "string"}
    elif datatype == "number":
        schema = {"type": "number"}
    elif datatype == "boolean":
        schema = {"type": "boolean"}
    elif datatype == "enum":
        codelist = get_field_codelist(field_def.ref)
        if codelist:
            schema = {"type": "string", "enum": codelist}
        else:
            # Fallback to empty enum if no codelist specified
            schema = {"type": "string", "enum": []}
    elif datatype == "object":
        if component:
            schema = {"$ref": f"#/definitions/{component}"}
        else:
            schema = {"type": "object"}
    else:
        # Default to string for unknown types
        schema = {"type": "string"}

    # Handle cardinality - wrap in array if cardinality is "n"
    if str(cardinality) == "n":
        items_schema = schema
        schema = {"type": "array", "items": items_schema, "minItems": 1}

    return schema


def process_items(
    items: List[Any],
    specification,
    collected_components: Set[str],
    app_ref: str,
) -> Tuple[Dict[str, Any], List[str], List[Dict[str, Any]]]:
    """Process a list of items and collect schema properties, required fields, and conditional logic for a specific application type."""
    properties = {}
    required = []
    conditional_rules = []

    for item in items:
        field_instance = None
        if isinstance(item, FieldInstance):
            field_instance = item
        elif isinstance(item, ComponentInstance):
            if isinstance(item.referenced_by_field, FieldInstance):
                field_instance = item.referenced_by_field

        if field_instance:
            field = field_instance.original
            overrides = getattr(field_instance, "overrides", {})

            # Check if the field applies to the current application type
            applies_if = overrides.get("applies-if")
            if applies_if:
                app_type_condition = applies_if.get("application-type")
                if app_type_condition and "in" in app_type_condition:
                    if app_ref not in app_type_condition["in"]:
                        continue  # Skip this field if it doesn't apply

            # If we are here, the field should be included
            field_schema = resolve_field_schema(field_instance, specification)
            properties[field.ref] = field_schema

            if field.component:
                collected_components.add(field.component)

            # Handle required logic
            is_required = overrides.get("required", field.required)
            required_if = overrides.get("required-if")

            if required_if:
                conditional_rules.extend(
                    parse_and_generate_required_if_rules(field.ref, required_if)
                )
            elif is_required:
                required.append(field.ref)

        elif isinstance(item, FieldDef):
            # This handles direct fields in an application's `fields` array
            field_schema = resolve_field_schema(item, specification)
            properties[item.ref] = field_schema
            if item.component:
                collected_components.add(item.component)
            if item.required:
                required.append(item.ref)

    return properties, required, conditional_rules


def walk_components(
    component_item, specification, collected_components: Set[str], app_ref: str
) -> Tuple[Dict[str, Any], List[str], List[Dict[str, Any]]]:
    """Walk component recursively and collect schema properties, required fields, and conditional logic"""

    if isinstance(component_item, ComponentInstance):
        component_def = component_item.component
    else:
        component_def = component_item

    return process_items(
        component_def.items, specification, collected_components, app_ref
    )


def generate_definitions(
    refs, specification, spec_key: str, walker_func, app_ref: str
) -> Dict[str, Any]:
    """Function to generate definitions for components or modules"""
    definitions = {}
    all_refs = set(refs)
    processed: Set[str] = set()

    # Process items recursively to handle nested references (for components)
    while all_refs - processed:
        ref = next(iter(all_refs - processed))
        item_def = specification[spec_key].get(ref)

        if item_def is None:
            processed.add(ref)
            continue

        nested_components: Set[str] = set()
        properties, required, conditional_rules = walker_func(
            item_def, specification, nested_components, app_ref
        )

        schema = {"type": "object", "properties": properties, "required": required}

        # Add conditional logic if present
        if conditional_rules:
            if len(conditional_rules) == 1:
                # Single rule - add directly to schema
                schema.update(conditional_rules[0])
            else:
                # Multiple rules - use allOf
                schema["allOf"] = conditional_rules

        definitions[ref] = schema
        processed.add(ref)

        # Add any newly discovered nested components (for components only)
        if spec_key == "components":
            all_refs.update(nested_components)

    return definitions


def generate_component_definitions(
    components, specification, app_ref: str
) -> Dict[str, Any]:
    """Generate definitions for components used by fields"""
    return generate_definitions(
        components, specification, "components", walk_components, app_ref
    )


def walk_modules(
    module_def, specification, collected_components: Set[str], app_ref: str
) -> Tuple[Dict[str, Any], List[str], List[Dict[str, Any]]]:
    """Walk module items and collect schema properties, required fields, and conditional logic"""
    return process_items(module_def.items, specification, collected_components, app_ref)


def generate_module_definitions(modules, specification, app_ref: str) -> Dict[str, Any]:
    """Generate definitions for modules used by application"""
    return generate_definitions(
        modules, specification, "modules", walk_modules, app_ref
    )


def generate_application_schema(app_ref, specification) -> Dict[str, Any]:
    """Generate complete JSON Schema for application type"""
    app_def = specification["applications"].get(app_ref)
    if not app_def:
        raise ValueError(f"Application {app_ref} not found")

    # TODO: work out what url will need to be for $id, for now just use file name but when publishing worked out change to URL.
    schema = {
        "$schema": "https://json-schema.org/draft-07/schema#",
        "$id": f"{app_ref}.json",
        "title": app_def.name,
        "additionalProperties": getattr(app_def, "allow_additional_properties", False),
        "description": getattr(app_def, "description", ""),
        "type": "object",
        "properties": {},
        "required": [],
        "definitions": {},
    }

    # Collect component references from all modules to ensure they are all defined
    component_refs = set()
    for mod in app_def.modules:
        if mod:
            # This is a bit inefficient, but it ensures all components are found
            walk_modules(mod, specification, component_refs, app_ref)

    # Generate component definitions
    component_definitions = generate_component_definitions(
        component_refs, specification, app_ref
    )
    schema["definitions"].update(component_definitions)

    # Generate module definitions
    module_refs = [mod.ref for mod in app_def.modules if mod]
    module_definitions = generate_module_definitions(
        module_refs, specification, app_ref
    )
    schema["definitions"].update(module_definitions)

    # Add module properties to main schema and mark them as required
    for module_ref in module_refs:
        if module_ref in module_definitions:
            schema["properties"][module_ref] = {"$ref": f"#/definitions/{module_ref}"}
            schema["required"].append(module_ref)

    # Handle application-level fields
    app_level_properties, app_level_required, app_level_conditionals = process_items(
        app_def.items, specification, component_refs, app_ref
    )
    schema["properties"].update(app_level_properties)
    schema["required"].extend(app_level_required)
    if app_level_conditionals:
        if "allOf" not in schema:
            # No existing allOf, so apply the same logic as before
            if len(app_level_conditionals) == 1:
                schema.update(app_level_conditionals[0])
            else:
                schema["allOf"] = app_level_conditionals
        else:
            # Already has allOf from module conditionals, extend it
            schema["allOf"].extend(app_level_conditionals)

    # Re-process any components found at the application level
    if component_refs - set(component_definitions.keys()):
        new_comp_defs = generate_component_definitions(
            component_refs, specification, app_ref
        )
        schema["definitions"].update(new_comp_defs)

    return schema


def generate_json_schemas():
    """Main function to generate all JSON schemas"""
    from loader import load_specification_model

    print("Loading specification model...")
    specification = load_specification_model()
    applications = specification["applications"]

    # Ensure output directories exist
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    Path(APPLICATIONS_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating JSON schemas for {len(applications)} applications...\n")

    for app_ref, app_def in applications.items():
        print(f"Generating schema for: {app_def.name} ({app_ref})")

        try:
            schema = generate_application_schema(app_ref, specification)
            schema_json = json.dumps(schema, indent=2, ensure_ascii=False)
            out_path = f"{APPLICATIONS_OUTPUT_DIR}/{app_ref}.json"
            save_string_to_file(schema_json, out_path)

            print(f"  -> Saved: {out_path}")

        except Exception as e:
            print(f"  -> Error: {e}")


if __name__ == "__main__":
    print("Running JSON Schema generation...")
    generate_json_schemas()
    print("\nJSON Schema generation completed.")
