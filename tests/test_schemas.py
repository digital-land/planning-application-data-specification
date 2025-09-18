import pytest
import jsonschema

from bin.generate_json_schema import (
    create_simple_required_if_rule,
    create_anyof_conditions_rule,
    create_anyof_fields_rule,
    parse_and_generate_required_if_rules,
)


def test_valid_householder_application(hh_application_payload, hh_json_schema):
    try:
        validator = jsonschema.Draft7Validator(hh_json_schema)
        validator.validate(hh_application_payload)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


def test_create_simple_required_if_rule():
    field_ref = "test-field"
    rule = create_simple_required_if_rule(field_ref, "another-field", "some-value")
    expected_rule = {
        "if": {"properties": {"another-field": {"const": "some-value"}}},
        "then": {"required": [field_ref]},
    }
    assert rule == expected_rule


def test_create_anyof_conditions_rule():
    field_ref = "test-field"
    any_conditions = [
        {"field": "field-a", "value": "value-a"},
        {"field": "field-b", "value": "value-b"},
    ]
    rule = create_anyof_conditions_rule(field_ref, any_conditions)
    expected_rule = {
        "if": {
            "anyOf": [
                {"properties": {"field-a": {"const": "value-a"}}},
                {"properties": {"field-b": {"const": "value-b"}}},
            ]
        },
        "then": {"required": [field_ref]},
    }
    assert rule == expected_rule


def test_create_anyof_fields_rule():
    field_ref = "test-field"
    any_fields = ["field-x", "field-y"]
    rule = create_anyof_fields_rule(field_ref, any_fields)
    expected_rule = {
        "if": {
            "anyOf": [
                {"properties": {"field-x": {"const": "true"}}},
                {"properties": {"field-y": {"const": "true"}}},
            ]
        },
        "then": {"required": [field_ref]},
    }
    assert rule == expected_rule


def test_parse_required_if_single_dict():
    field_ref = "test-field"
    required_if_config = {"field": "status", "value": "active"}
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    expected_rules = [
        {
            "if": {"properties": {"status": {"const": "active"}}},
            "then": {"required": [field_ref]},
        }
    ]
    assert rules == expected_rules


def test_parse_required_if_list_of_dicts():
    field_ref = "test-field"
    required_if_config = [
        {"field": "status", "value": "active"},
        {"field": "type", "value": "premium"},
    ]
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    expected_rules = [
        {
            "if": {"properties": {"status": {"const": "active"}}},
            "then": {"required": [field_ref]},
        },
        {
            "if": {"properties": {"type": {"const": "premium"}}},
            "then": {"required": [field_ref]},
        },
    ]
    assert rules == expected_rules


def test_parse_required_if_any_conditions_list():
    field_ref = "test-field"
    required_if_config = {
        "any": [
            {"field": "option-a", "value": "selected"},
            {"field": "option-b", "value": "chosen"},
        ]
    }
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    expected_rules = [
        {
            "if": {
                "anyOf": [
                    {"properties": {"option-a": {"const": "selected"}}},
                    {"properties": {"option-b": {"const": "chosen"}}},
                ]
            },
            "then": {"required": [field_ref]},
        }
    ]
    assert rules == expected_rules


def test_parse_required_if_any_fields_true():
    field_ref = "test-field"
    required_if_config = {"any": True, "field": ["field-x", "field-y"]}
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    expected_rules = [
        {
            "if": {
                "anyOf": [
                    {"properties": {"field-x": {"const": "true"}}},
                    {"properties": {"field-y": {"const": "true"}}},
                ]
            },
            "then": {"required": [field_ref]},
        }
    ]
    assert rules == expected_rules


def test_parse_required_if_mixed_list():
    field_ref = "test-field"
    required_if_config = [
        {"field": "simple-flag", "value": "yes"},
        {"any": [{"field": "any-a", "value": "1"}, {"field": "any-b", "value": "2"}]},
    ]
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    expected_rules = [
        {
            "if": {"properties": {"simple-flag": {"const": "yes"}}},
            "then": {"required": [field_ref]},
        },
        {
            "if": {
                "anyOf": [
                    {"properties": {"any-a": {"const": "1"}}},
                    {"properties": {"any-b": {"const": "2"}}},
                ]
            },
            "then": {"required": [field_ref]},
        },
    ]
    assert rules == expected_rules


def test_parse_required_if_unrecognized_dict_ignored():
    field_ref = "test-field"
    # This config should be ignored as it's not a recognized pattern for rule generation
    required_if_config = {"field": "some-field", "operator": "not_empty"}
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    assert rules == []


def test_parse_required_if_unrecognized_type_ignored():
    field_ref = "test-field"
    # This config should be ignored as it's not a dict or list
    required_if_config = "just-a-string"
    rules = parse_and_generate_required_if_rules(field_ref, required_if_config)
    assert rules == []
