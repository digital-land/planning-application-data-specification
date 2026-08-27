import json
from pathlib import Path

from jsonschema import Draft7Validator

from bin.generate_json_schema import (
    generate_application_schema,
    process_items,
    resolve_field_schema,
)
from planning_application_specification import Specification
from planning_application_specification.models import (
    ComponentInstance,
    FieldDef,
    FieldInstance,
)


def test_resolve_field_schema_maps_decimal_to_json_schema_number():
    field = FieldDef(ref="depth", name="Depth", datatype="decimal")

    schema = resolve_field_schema(field, specification=None)

    assert schema == {"type": "number"}


def test_resolve_field_schema_maps_integer_to_json_schema_integer():
    field = FieldDef(
        ref="advertisement-count", name="Advertisement count", datatype="integer"
    )

    schema = resolve_field_schema(field, specification=None)

    assert schema == {"type": "integer"}


def test_process_items_keeps_unhandled_required_if_over_protective():
    field = FieldDef(ref="agent-reference", name="Agent reference", datatype="string")
    field_instance = FieldInstance(
        original=field,
        overrides={
            "field": "agent-reference",
            "required-if": [
                {
                    "field": "agent-details.agent.reference",
                    "operator": "not_empty",
                }
            ],
        },
    )

    properties, required, conditional_rules = process_items(
        [field_instance],
        specification=Specification.load(),
        collected_components=set(),
        app_ref="hh",
    )

    assert properties == {"agent-reference": {"type": "string"}}
    assert required == ["agent-reference"]
    assert conditional_rules == []


def test_generate_application_schema_applies_parent_application_type_rules():
    schema = generate_application_schema("outline-some", Specification.load())
    proposal_details = schema["definitions"]["proposal-details"]

    assert "description" in proposal_details["properties"]
    assert "description" in proposal_details["required"]
    assert "is-psi" not in proposal_details["properties"]


def test_supporting_info_source_model_defines_both_complete_routes():
    specification = Specification.load()
    supporting_info = specification.modules["supporting-info"]
    fields = {}
    for item in supporting_info.items:
        if isinstance(item, FieldInstance):
            field_instance = item
        elif isinstance(item, ComponentInstance):
            field_instance = item.referenced_by_field
        else:
            continue
        fields[field_instance.original.ref] = field_instance.overrides

    assert fields["approved-drawings"]["required-if"] == [
        {"field": "submitted-drawings-document", "operator": "empty"}
    ]
    assert fields["submitted-drawing-references"]["required-if"] == [
        {"field": "submitted-drawings-document", "operator": "empty"}
    ]
    assert fields["approved-drawings-document"]["required-if"] == [
        {"field": "submitted-drawing-references", "operator": "empty"}
    ]
    assert fields["submitted-drawings-document"]["required-if"] == [
        {"field": "submitted-drawing-references", "operator": "empty"}
    ]


def test_supporting_info_examples_cover_structured_and_document_routes():
    examples_dir = Path("specification/example")
    structured = json.loads((examples_dir / "supporting-info.json").read_text())
    documents = json.loads(
        (examples_dir / "supporting-info-documents.json").read_text()
    )

    assert set(structured["supporting-info"]) >= {
        "approved-drawings",
        "submitted-drawing-references",
    }
    assert set(documents["supporting-info"]) >= {
        "approved-drawings-document",
        "submitted-drawings-document",
    }


def test_supporting_info_schema_requires_a_complete_route_for_empty_values():
    schema = generate_application_schema("reserved-matters", Specification.load())
    supporting_info_schema = {
        "$schema": schema["$schema"],
        "$ref": "#/definitions/supporting-info",
        "definitions": schema["definitions"],
    }
    validator = Draft7Validator(supporting_info_schema)

    document_route = {
        "approved-drawings-document": {"reference": "doc-approved"},
        "submitted-drawings-document": {"reference": "doc-submitted"},
    }
    structured_route = {
        "approved-drawings": [{"reference": "A-100", "name": "Site plan"}],
        "submitted-drawing-references": ["A-101"],
    }

    assert validator.is_valid(document_route)
    assert validator.is_valid(structured_route)
    assert not validator.is_valid({})
    assert not validator.is_valid({"submitted-drawings-document": {}})
    assert not validator.is_valid({"submitted-drawing-references": []})
