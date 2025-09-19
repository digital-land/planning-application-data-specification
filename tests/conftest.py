# tests/conftest.py
import json
import pytest
import sys

from pathlib import Path

# Define PROJECT_ROOT using pathlib
PROJECT_ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "bin"))


@pytest.fixture()
def project_root():
    return PROJECT_ROOT
