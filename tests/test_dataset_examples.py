import json

import jinja2
import pytest

from bin.dataset_examples import (
    build_dataset_example_view,
    example_record_to_table_rows,
    example_records_to_wide_table,
    render_dataset_examples_content,
    resolve_example_path,
)


def test_resolve_example_path_uses_the_current_dataset_directory(tmp_path):
    path = tmp_path / "planning-application" / "basic.json"
    path.parent.mkdir(parents=True)
    path.write_text("{}", encoding="utf-8")

    assert (
        resolve_example_path(tmp_path, "planning-application", "basic")
        == path
    )


def test_resolve_example_path_rejects_a_path_in_place_of_a_reference(tmp_path):
    with pytest.raises(ValueError, match="Invalid example reference"):
        resolve_example_path(tmp_path, "planning-application", "../site/basic")


def test_example_record_to_table_rows_preserves_field_order():
    assert example_record_to_table_rows(
        {"reference": "PA-1", "application-types": ["full"], "active": False}
    ) == [
        {"field": "reference", "value": "PA-1"},
        {"field": "application-types", "value": '["full"]'},
        {"field": "active", "value": "false"},
    ]


def test_example_records_to_wide_table_uses_one_row_per_record():
    assert example_records_to_wide_table(
        [
            {"reference": "document-001", "name": "Plan V1"},
            {
                "reference": "document-002",
                "name": "Plan V2",
                "replaces": "document-001",
            },
        ]
    ) == {
        "fields": ["reference", "name", "replaces"],
        "rows": [
            ["document-001", "Plan V1", ""],
            ["document-002", "Plan V2", "document-001"],
        ],
    }


def test_build_dataset_example_view_rejects_unknown_fields(tmp_path):
    path = tmp_path / "planning-application" / "basic.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"reference": "PA-1", "unknown": "value"}))

    with pytest.raises(ValueError, match="unknown fields: unknown"):
        build_dataset_example_view(
            tmp_path,
            "planning-application",
            "basic",
            {"reference"},
        )


def test_build_dataset_example_view_supports_multiple_records(tmp_path):
    path = tmp_path / "planning-application-document" / "replacement.json"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            [
                {"reference": "document-001"},
                {"reference": "document-002", "replaces": "document-001"},
            ]
        )
    )

    view = build_dataset_example_view(
        tmp_path,
        "planning-application-document",
        "replacement",
        {"reference", "replaces"},
    )

    assert view["multiple_records"] is True
    assert [record["reference"] for record in view["records"]] == [
        "document-001",
        "document-002",
    ]


def test_render_dataset_examples_content_resolves_example_call(tmp_path):
    examples_root = tmp_path / "examples"
    example_path = examples_root / "planning-application" / "basic.json"
    example_path.parent.mkdir(parents=True)
    example_path.write_text(json.dumps({"reference": "PA-1"}))

    content_root = tmp_path / "content"
    content_path = content_root / "dataset" / "planning-application" / "examples.md"
    content_path.parent.mkdir(parents=True)
    content_path.write_text(
        "---\ndataset: planning-application\n---\n\n"
        "## Examples\n\n{{ example(\"basic\") }}\n",
        encoding="utf-8",
    )

    template_dir = tmp_path / "templates" / "components"
    template_dir.mkdir(parents=True)
    (template_dir / "dataset-example.html").write_text(
        "<div>{{ example.reference }} {{ example.json }}</div>",
        encoding="utf-8",
    )
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(tmp_path / "templates"),
        autoescape=True,
    )

    rendered = render_dataset_examples_content(
        dataset_ref="planning-application",
        allowed_fields={"reference"},
        examples_root=examples_root,
        content_root=content_root,
        template_environment=environment,
    )

    assert "Examples" in rendered
    assert "basic" in rendered
    assert "PA-1" in rendered
