import csv

from completeness import evaluate_scope


def write_rows(path, rows):
    fieldnames = [
        "stats-app-name",
        "2024-total",
        "applications-types",
        "application-name",
        "form-name",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def test_evaluate_scope_applies_rules_and_shared_volume(tmp_path):
    csv_path = tmp_path / "volumes.csv"
    write_rows(
        csv_path,
        [
            {
                "stats-app-name": "Row with form",
                "2024-total": "0",
                "applications-types": "hh",
                "application-name": "Householder planning application",
                "form-name": "Householder form",
                "notes": "",
            },
            {
                "stats-app-name": "Row with volume",
                "2024-total": "20",
                "applications-types": "full",
                "application-name": "Full planning permission",
                "form-name": "",
                "notes": "",
            },
            {
                "stats-app-name": "Inheritance row",
                "2024-total": "0",
                "applications-types": "outline",
                "application-name": "Outline planning",
                "form-name": "",
                "notes": "Used for module inheritance",
            },
            {
                "stats-app-name": "Out-of-scope row",
                "2024-total": "0",
                "applications-types": "waste-dev",
                "application-name": "Waste development",
                "form-name": "",
                "notes": "",
            },
            {
                "stats-app-name": "Combined row",
                "2024-total": "10",
                "applications-types": "hh,demolition-con-area",
                "application-name": "",
                "form-name": "",
                "notes": "",
            },
        ],
    )

    result = evaluate_scope(csv_path)
    summary = result["summary"]

    assert summary["total_rows"] == 5
    assert summary["in_scope_rows"] == 4
    assert summary["out_of_scope_rows"] == 1
    assert summary["total_2024_volume"] == 30
    assert summary["in_scope_2024_volume"] == 30
    assert summary["volume_treatment"] == "shared"

    inheritance = [
        item
        for item in result["in_scope"]
        if item["application-types"] == ["outline"]
    ][0]
    assert "Inheritance-only application type" in inheritance["notes"]

    out_scope = result["out_of_scope"][0]
    assert out_scope["application-types"] == ["waste-dev"]


def test_evaluate_scope_accepts_semicolon_delimited_application_types(tmp_path):
    csv_path = tmp_path / "volumes.csv"
    write_rows(
        csv_path,
        [
            {
                "stats-app-name": "Combined semicolon row",
                "2024-total": "12",
                "applications-types": "hh;demolition-con-area",
                "application-name": "",
                "form-name": "",
                "notes": "",
            }
        ],
    )

    result = evaluate_scope(csv_path)
    item = result["in_scope"][0]

    assert item["type"] == "combined"
    assert item["application-types"] == ["hh", "demolition-con-area"]
    assert item["volume"] == 12
