import pytest
import jsonschema


def test_valid_householder_application(hh_application_payload, hh_json_schema):
    try:
        validator = jsonschema.Draft7Validator(hh_json_schema)
        validator.validate(hh_application_payload)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Validation failed: {e}")
