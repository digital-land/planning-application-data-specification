from pathlib import Path

from generate_field_datatypes_doc import (
    FieldUsage,
    UpstreamDatatype,
    build_upstream_rows,
    build_used_datatypes_rows,
    group_field_usages,
    parse_upstream_datatype,
)


def test_group_field_usages_preserves_exact_datatype_values():
    usages = [
        FieldUsage("first", "First", "boolean", Path("specification/field/first.md")),
        FieldUsage("second", "Second", "Boolean", Path("specification/field/second.md")),
        FieldUsage("third", "Third", "boolean", Path("specification/field/third.md")),
    ]

    grouped = group_field_usages(usages)

    assert list(grouped) == ["boolean", "Boolean"]
    assert [usage.ref for usage in grouped["boolean"]] == ["first", "third"]
    assert [usage.ref for usage in grouped["Boolean"]] == ["second"]


def test_parse_upstream_datatype_extracts_heading_metadata_and_description():
    upstream = parse_upstream_datatype(
        """---
datatype: datetime
name: Datetime
---

A combination of a date and a time.

Further notes are not part of the short description.
""",
        "https://raw.githubusercontent.com/digital-land/specification/main/content/datatype/datetime.md",
    )

    assert upstream.datatype == "datetime"
    assert upstream.name == "Datetime"
    assert upstream.description == "A combination of a date and a time."


def test_upstream_rows_use_datatype_identifier_not_display_name():
    rows = build_upstream_rows(
        [
            UpstreamDatatype(
                "datetime",
                "Datetime",
                "A date and time value.",
                "https://example.com/datetime.md",
            )
        ]
    )

    assert rows[0][0] == "datetime"


def test_used_datatype_rows_mark_local_and_unknown_datatypes():
    grouped = {
        "boolean": [
            FieldUsage(
                "confirmed",
                "Confirmed",
                "boolean",
                Path("specification/field/confirmed.md"),
            )
        ],
        "Boolean": [
            FieldUsage(
                "unknown-proposed",
                "Unknown proposed",
                "Boolean",
                Path("specification/field/unknown-proposed.md"),
            )
        ],
        "datetime": [
            FieldUsage(
                "submitted",
                "Submitted",
                "datetime",
                Path("specification/field/submitted.md"),
            )
        ],
    }
    upstream = [
        UpstreamDatatype(
            "datetime",
            "Datetime",
            "A date and time value.",
            "https://example.com/datetime.md",
        )
    ]

    rows = build_used_datatypes_rows(grouped, upstream)
    rows_by_datatype = {row[0]: row for row in rows}

    assert rows_by_datatype["datetime"][1] == "Upstream"
    assert rows_by_datatype["boolean"][1] == "Local to this specification"
    assert rows_by_datatype["Boolean"][1] == "Unknown / check"
    assert rows_by_datatype["Boolean"][2] == 1
    assert rows_by_datatype["Boolean"][3] == (
        "[Unknown proposed](../specification/field/unknown-proposed.md)"
    )
