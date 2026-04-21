import csv

from bin.csv_helpers import write_csv


def test_write_csv_includes_extra_fields_found_in_later_rows(tmp_path):
    output_file = tmp_path / "output.csv"

    write_csv(
        [
            {"field": "description", "name": "Description"},
            {
                "field": "decision-date",
                "name": "Decision date",
                "date_precision": "day",
            },
        ],
        output_file=output_file,
        first_headers=["field", "name"],
        final_headers=["entry-date", "end-date"],
    )

    with output_file.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        assert reader.fieldnames == ["field", "name", "date_precision"]
        rows = list(reader)

    assert rows[0]["field"] == "description"
    assert rows[0]["date_precision"] == ""
    assert rows[1]["field"] == "decision-date"
    assert rows[1]["date_precision"] == "day"
