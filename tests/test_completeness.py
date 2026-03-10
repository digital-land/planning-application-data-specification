import csv

from completeness import calculate_total_volume, evaluate_scope


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

    spec_refs = {"hh", "full", "outline"}
    result = evaluate_scope(csv_path, spec_application_refs=spec_refs)
    in_scope = result["in_scope"]
    out_of_scope = result["out_of_scope"]

    total_rows = len(in_scope) + len(out_of_scope)
    in_scope_rows = len(in_scope)
    out_of_scope_rows = len(out_of_scope)
    total_volume = calculate_total_volume(in_scope + out_of_scope)
    in_scope_volume = calculate_total_volume(in_scope)
    covered_volume = calculate_total_volume(
        [item for item in in_scope if item["covered-by-spec"]]
    )
    completeness_pct = (covered_volume / total_volume * 100) if total_volume else 0.0

    assert total_rows == 5
    assert in_scope_rows == 3
    assert out_of_scope_rows == 2
    assert total_volume == 30
    assert in_scope_volume == 30
    assert covered_volume == 20
    assert round(completeness_pct, 2) == 66.67

    inheritance = [
        item for item in in_scope if item["application-types"] == ["outline"]
    ][0]
    assert "Inheritance-only application type" in inheritance["notes"]

    out_scope_types = [item["application-types"] for item in out_of_scope]
    assert ["waste-dev"] in out_scope_types
    assert ["hh"] in out_scope_types


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

    result = evaluate_scope(csv_path, spec_application_refs={"hh", "demolition-con-area"})
    item = result["in_scope"][0]

    assert item["type"] == "combined"
    assert item["application-types"] == ["hh", "demolition-con-area"]
    assert item["volume"] == 12
    assert item["covered-by-spec"] is False

    result_with_combined = evaluate_scope(
        csv_path,
        spec_application_refs={"hh", "demolition-con-area"},
        combined_apps_covered=True,
    )
    item_with_combined = result_with_combined["in_scope"][0]
    assert item_with_combined["covered-by-spec"] is True
    covered_volume = calculate_total_volume(
        [item for item in result_with_combined["in_scope"] if item["covered-by-spec"]]
    )
    assert covered_volume == 12


def test_tree_work_split_combination_is_covered_without_combined_flag(tmp_path):
    csv_path = tmp_path / "volumes.csv"
    write_rows(
        csv_path,
        [
            {
                "stats-app-name": "Tree works split row",
                "2024-total": "7",
                "applications-types": "consent-under-tpo,notice-trees-in-con-area",
                "application-name": "",
                "form-name": "",
                "notes": "",
            }
        ],
    )

    result = evaluate_scope(
        csv_path,
        spec_application_refs={"consent-under-tpo", "notice-trees-in-con-area"},
        combined_apps_covered=False,
    )
    item = result["in_scope"][0]
    assert item["covered-by-spec"] is True


def test_form_with_explicit_zero_volume_is_out_of_scope(tmp_path):
    csv_path = tmp_path / "volumes.csv"
    write_rows(
        csv_path,
        [
            {
                "stats-app-name": "Zero volume with form",
                "2024-total": "0",
                "applications-types": "pa-fish-struct",
                "application-name": "Tank cage or structure for fish farming",
                "form-name": "Prior Approval: Tank/Cage/Structure for use in fish farming",
                "notes": "",
            }
        ],
    )

    result = evaluate_scope(csv_path, spec_application_refs={"pa-fish-struct"})
    assert len(result["in_scope"]) == 0
    assert len(result["out_of_scope"]) == 1
