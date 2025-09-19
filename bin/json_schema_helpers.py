from typing import Any, Dict, List


def create_simple_required_if_rule(
    field_ref: str, condition_field: str, condition_value: Any
) -> Dict[str, Any]:
    """Creates a simple 'required-if' JSON Schema rule."""
    return {
        "if": {"properties": {condition_field: {"const": condition_value}}},
        "then": {"required": [field_ref]},
    }


def create_anyof_conditions_rule(
    field_ref: str, any_conditions: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Creates an 'anyOf' JSON Schema rule from a list of dictionaries field-value conditions."""

    def create_condition_property(condition: Dict[str, Any]) -> Dict[str, Any]:
        field = condition.get("field")
        if "value" in condition:
            return {"properties": {field: {"const": condition.get("value")}}}
        if "contains" in condition:
            return {"properties": {field: {"pattern": condition.get("contains")}}}
        # Return an empty condition if the format is not recognized, which will be ignored.
        return {}

    conditions = [create_condition_property(c) for c in any_conditions]
    # Filter out any empty dicts from unrecognized conditions
    valid_conditions = [cond for cond in conditions if cond]

    return {
        "if": {"anyOf": valid_conditions},
        "then": {"required": [field_ref]},
    }


def create_anyof_fields_rule(field_ref: str, any_fields: List[str]) -> Dict[str, Any]:
    """Creates an 'anyOf' JSON Schema rule from a list of field names (checking for 'true')."""
    return {
        "if": {"anyOf": [{"properties": {f: {"const": "true"}}} for f in any_fields]},
        "then": {"required": [field_ref]},
    }


def parse_and_generate_required_if_rules(
    field_ref: str, required_if_config: Any
) -> List[Dict[str, Any]]:
    """
    Parses the required_if configuration and generates a list of JSON Schema conditional rules.
    Handles single dict conditions, lists of conditions (as AND), and 'any' conditions (as OR).
    """
    rules = []

    if isinstance(required_if_config, list):
        # A list of conditions implies an AND condition.
        if not required_if_config:
            return []

        conditions = []
        for condition_item in required_if_config:
            # Recursively parse the sub-condition, which will return a full if/then rule.
            # We need to extract just the 'if' part for our allOf list.
            sub_rules = parse_and_generate_required_if_rules(field_ref, condition_item)
            if sub_rules:
                if_clause = sub_rules[0].get("if")
                if if_clause:
                    conditions.append(if_clause)

        if conditions:
            # If there's only one condition after parsing, don't wrap in allOf.
            if len(conditions) == 1:
                rules.append({"if": conditions[0], "then": {"required": [field_ref]}})
            else:
                rules.append(
                    {"if": {"allOf": conditions}, "then": {"required": [field_ref]}}
                )
        return rules

    if isinstance(required_if_config, dict):
        # Handle dictionary conditions with a flatter if/elif/else structure
        any_conditions_list = required_if_config.get("any")
        any_fields_list = required_if_config.get("field")

        if isinstance(any_conditions_list, list):
            # Case: {"any": [{"field": "f1", "value": "v1"}, ...]}
            rules.append(create_anyof_conditions_rule(field_ref, any_conditions_list))
        elif any_conditions_list is True and isinstance(any_fields_list, list):
            # Case: {"any": True, "field": ["f1", "f2"]}
            rules.append(create_anyof_fields_rule(field_ref, any_fields_list))
        else:
            # Case: Simple {"field": "some_field", "value": "some_value"}
            condition_field = required_if_config.get("field")
            condition_value = required_if_config.get("value")
            if condition_field and condition_value is not None:
                rules.append(
                    create_simple_required_if_rule(
                        field_ref, condition_field, condition_value
                    )
                )

    # Non-dict/list types for required_if_config are ignored,

    return rules
