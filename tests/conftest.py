# tests/conftest.py
import json
import pytest
import sys

from pathlib import Path

# Define PROJECT_ROOT using pathlib
PROJECT_ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "bin"))


@pytest.fixture
def hh_application_payload():
    path = PROJECT_ROOT / "specification" / "example" / "example-hh-payload-minimal.json"
    with open(path) as f:
        return json.load(f)


@pytest.fixture
def hh_json_schema():
    path = PROJECT_ROOT / "generated" / "json-schema" / "applications" / "hh.json"
    with open(path) as f:
        return json.load(f)
