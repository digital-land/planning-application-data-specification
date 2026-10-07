"""Distribution archives include the canonical resources and no workspace data."""

import subprocess
import sys
import tarfile
import zipfile


def test_wheel_and_sdist_have_same_canonical_resources(project_root, tmp_path):
    output = tmp_path / "dist"
    subprocess.run(
        [sys.executable, "-m", "build", "--no-isolation", "--sdist", "--wheel", "--outdir", str(output)],
        cwd=project_root,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    wheel = next(output.glob("*.whl"))
    source = next(output.glob("*.tar.gz"))
    prefix = "planning_application_specification/resources/"
    with zipfile.ZipFile(wheel) as archive:
        wheel_resources = {name.split(prefix, 1)[1]: archive.read(name) for name in archive.namelist() if prefix in name}
        assert "planning_application_specification/specification.py" in archive.namelist()
        wheel_names = archive.namelist()
    with tarfile.open(source) as archive:
        source_resources = {member.name.split(prefix, 1)[1]: archive.extractfile(member).read() for member in archive.getmembers() if prefix in member.name and member.isfile()}
        assert any(name.endswith("/planning_application_specification/specification.py") for name in archive.getnames())
        source_names = archive.getnames()

    assert wheel_resources == source_resources
    for name, content in wheel_resources.items():
        assert content == (project_root / name).read_bytes()
    for expected in (
        "specification/planning-application-data.schema.md",
        "specification/combined-application-types.csv",
        "specification/application/pa-build-agri-forest.schema.md",
        "specification/component/site-address.md",
        "specification/module/proposal-details.schema.md",
        "specification/field/description.md",
        "specification/guidance/dataset/site/field/name.md",
        "specification/example/site-details-complete.json",
        "data/planning-application-type.csv",
        "data/planning-requirement.csv",
        "data/usage/tenure-type-usage.csv",
        "user-needs/need/dd-need-103.md",
        "user-needs/justification/just-0001.md",
    ):
        assert expected in wheel_resources
    excluded = ("data/analysis/", "data/reporting/", "planning-application-notes/", "documentation/design-decisions/", "docs/", "generated/", "bin/")
    assert not any(any(f"/{part}" in f"/{name}" for part in excluded) for name in wheel_names + source_names)

    unpack = tmp_path / "unpacked"
    unpack.mkdir()
    with tarfile.open(source) as archive:
        archive.extractall(unpack, filter="data")
    source_root = next(unpack.iterdir())
    rebuilt = tmp_path / "rebuilt"
    subprocess.run(
        [sys.executable, "-m", "build", "--no-isolation", "--wheel", "--outdir", str(rebuilt)],
        cwd=source_root,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    with zipfile.ZipFile(next(rebuilt.glob("*.whl"))) as archive:
        rebuilt_resources = {name.split(prefix, 1)[1]: archive.read(name) for name in archive.namelist() if prefix in name}
    assert rebuilt_resources == wheel_resources
