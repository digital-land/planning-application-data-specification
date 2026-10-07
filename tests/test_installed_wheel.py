"""Exercise package loading from a wheel installed outside this checkout."""

import os
from pathlib import Path
import subprocess
import sys

import pytest

from planning_application_specification import Specification
from planning_application_specification import loader


def test_missing_bundle_requires_explicit_root(tmp_path, monkeypatch):
    monkeypatch.setattr(loader, "__file__", str(tmp_path / "package" / "loader.py"))
    (tmp_path / "specification").mkdir()
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError, match="Bundled specification resources are unavailable"):
        Specification.load()
    with pytest.raises(FileNotFoundError, match="Bundled specification resources are unavailable"):
        loader.load_needs()
    with pytest.raises(FileNotFoundError, match="Could not find a specification directory"):
        Specification.load(tmp_path / "missing")


def test_installed_wheel_uses_bundled_resources_and_explicit_override(project_root, tmp_path):
    dist = tmp_path / "dist"
    subprocess.run(
        [sys.executable, "-m", "build", "--no-isolation", "--sdist", "--wheel", "--outdir", str(dist)],
        cwd=project_root,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    wheel = next(dist.glob("*.whl"))
    target = tmp_path / "installed"
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--no-index", "--no-deps", "--target", str(target), str(wheel)],
        check=True,
        stdout=subprocess.DEVNULL,
    )

    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "specification").mkdir()
    script = """
import json
from pathlib import Path
import shutil
import sys

sys.path.insert(0, sys.argv[1])
import planning_application_specification as package
from planning_application_specification import Specification
from planning_application_specification.loader import load_needs
from planning_application_specification.specification import SelectionContext

site = Path(sys.argv[1]).resolve()
assert site in Path(package.__file__).resolve().parents, package.__file__
spec = Specification.load()
assert spec.source_path == Path(package.__file__).resolve().parent / "resources"
assert spec.application("hh").ref == "hh"
assert spec.application("hh;lbc").is_combined
assert spec.dataset("planning-application").ref == "planning-application"
assert spec.view("national-public").ref == "national-public-view"
assert spec.specification("planning-application-data").ref == "planning-application-data"
assert "market-housing" in [item.reference for item in spec.codelist("tenure-type").items]
assert spec.codelist("tenure-type").applicable(SelectionContext(specification_profile="gla", application_type="full")).usage_rules_applied
assert "Former Riverside Mill" in spec.guidance(dataset="site", field="name").content
assert load_needs()["need"] and load_needs()["justification"]
example = spec.source_path / "specification/example/site-details-complete.json"
assert isinstance(json.loads(example.read_text()), dict)

local = Path(sys.argv[2])
shutil.copytree(spec.source_path, local)
csv = local / "data/codelist/tenure-type.csv"
source = csv.read_text()
assert "market-housing" in source
csv.write_text(source.replace("market-housing", "local-housing", 1))
override = Specification.load(local)
assert override.source_path == local
assert "local-housing" in [item.reference for item in override.codelist("tenure-type").items]
assert "market-housing" in [item.reference for item in spec.codelist("tenure-type").items]
assert load_needs(local)["need"]
"""
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    subprocess.run(
        [sys.executable, "-I", "-c", script, str(target), str(tmp_path / "local-checkout")],
        cwd=outside,
        env=env,
        check=True,
    )
