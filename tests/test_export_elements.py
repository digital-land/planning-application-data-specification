import csv

import bin.export_elements as export_elements
from bin.loader import load_specification_model


def test_export_applications_excludes_parent_only_base_types(tmp_path, monkeypatch):
    monkeypatch.setattr(export_elements, "OUTPUT_DIR", tmp_path)

    export_elements.export_applications(load_specification_model())

    with (tmp_path / "applications.csv").open(newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    refs = {row["reference"] for row in rows}

    assert "full" in refs
    assert "outline-all" in refs
    assert "pa-extension" in refs
    assert "outline" not in refs
    assert "prior-approval" not in refs
    assert "ldc" not in refs
