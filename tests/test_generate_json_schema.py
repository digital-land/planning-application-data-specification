from bin.generate_json_schema import (
    generate_application_schema,
    process_items,
    resolve_field_schema,
)
from planning_application_specification import Specification
from planning_application_specification.models import FieldDef, FieldInstance


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
