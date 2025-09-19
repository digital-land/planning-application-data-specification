import pytest
import json
import jsonschema


@pytest.fixture
def json_dir(project_root):
    path = project_root / "specification" / "example"
    return path

@pytest.fixture
def schema_dir(project_root):
    path = project_root / "generated" / "json-schema" / "applications"
    return path

'''
Add test files to the test_data list. First item of tuple is a filename
of a json payload that should be in the specification/examples directory.
The second item should be the corresponding json schema for the application
type in generated/json-schema/application

for example:

test_data = [
    ("example-hh-payload-minimal.json", "hh.json"),
    ("example-full.json", "full.json"),
    ("example-outline.json", "outline.json")
]
'''


test_data = [
    ("example-hh-payload-minimal.json", "hh.json")
]

@pytest.mark.parametrize("payload, schema", test_data)
def test_valid_application(payload, schema, json_dir, schema_dir):
    application_json = _load_json(json_dir, payload)
    application_json_schema = _load_json(schema_dir, schema)
    try:
        validator = jsonschema.Draft7Validator(application_json_schema)
        validator.validate(application_json)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


def _load_json(dir, filename):
    path = dir / filename
    with open(path, "r") as f:
        return json.load(f)
