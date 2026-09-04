import json
import re
from pathlib import Path
from typing import Any

import frontmatter
from bs4 import BeautifulSoup
from markupsafe import Markup

from bin.markdown_utils import render_govuk_markdown


EXAMPLE_REFERENCE_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
EXAMPLE_TABLE_LAYOUTS = {"vertical", "wide"}


def resolve_example_path(
    examples_root: Path, dataset_ref: str, example_ref: str
) -> Path:
    """Resolve a dataset example reference to its JSON source file."""
    if not EXAMPLE_REFERENCE_PATTERN.fullmatch(example_ref):
        raise ValueError(f"Invalid example reference '{example_ref}'")

    path = examples_root / dataset_ref / f"{example_ref}.json"
    if not path.is_file():
        raise FileNotFoundError(
            f"Example '{example_ref}' does not exist for dataset '{dataset_ref}'"
        )
    return path


def load_dataset_example(path: Path) -> dict[str, Any] | list[dict[str, Any]]:
    """Load a dataset example containing one or more JSON records."""
    with path.open(encoding="utf-8") as example_file:
        data = json.load(example_file)

    if isinstance(data, dict):
        return data
    if isinstance(data, list) and data and all(isinstance(item, dict) for item in data):
        return data
    raise ValueError(
        f"Dataset example '{path}' must contain a JSON object or a non-empty "
        "array of JSON objects"
    )


def validate_example_fields(
    record: dict[str, Any], allowed_fields: set[str], example_ref: str
) -> None:
    """Reject fields that are not part of the dataset being demonstrated."""
    unknown_fields = sorted(set(record) - allowed_fields)
    if unknown_fields:
        joined_fields = ", ".join(unknown_fields)
        raise ValueError(
            f"Example '{example_ref}' contains unknown fields: {joined_fields}"
        )


def format_example_table_value(value: Any) -> str:
    """Format a JSON value consistently for display in an HTML table."""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False)


def example_record_to_table_rows(record: dict[str, Any]) -> list[dict[str, str]]:
    """Convert a JSON record into the field/value rows used by the viewer."""
    return [
        {"field": field, "value": format_example_table_value(value)}
        for field, value in record.items()
    ]


def example_records_to_wide_table(
    records: list[dict[str, Any]],
) -> dict[str, list[Any]]:
    """Convert multiple JSON records into columns and one row per record."""
    fields = list(dict.fromkeys(field for record in records for field in record))
    return {
        "fields": fields,
        "rows": [
            [
                format_example_table_value(record[field]) if field in record else ""
                for field in fields
            ]
            for record in records
        ],
    }


def build_dataset_example_view(
    examples_root: Path,
    dataset_ref: str,
    example_ref: str,
    allowed_fields: set[str],
    table_layout: str = "vertical",
) -> dict[str, Any]:
    """Build the view model used to render one dataset example."""
    if table_layout not in EXAMPLE_TABLE_LAYOUTS:
        raise ValueError(
            f"Invalid table layout '{table_layout}' for example '{example_ref}'. "
            "Use 'vertical' or 'wide'."
        )

    path = resolve_example_path(examples_root, dataset_ref, example_ref)
    data = load_dataset_example(path)
    records = data if isinstance(data, list) else [data]
    for record in records:
        validate_example_fields(record, allowed_fields, example_ref)
    return {
        "reference": example_ref,
        "records": [
            {
                "reference": record.get("reference"),
                "table_rows": example_record_to_table_rows(record),
            }
            for record in records
        ],
        "multiple_records": len(records) > 1,
        "table_layout": table_layout,
        "wide_table": example_records_to_wide_table(records),
        "json": json.dumps(data, indent=2, ensure_ascii=False),
    }


def render_dataset_example_component(
    *,
    example_ref: str,
    table_layout: str,
    dataset_ref: str,
    allowed_fields: set[str],
    examples_root: Path,
    template_environment: Any,
) -> str:
    """Render one resolved example using the reusable viewer component."""
    example = build_dataset_example_view(
        examples_root,
        dataset_ref,
        example_ref,
        allowed_fields,
        table_layout,
    )
    return template_environment.get_template(
        "components/dataset-example.html"
    ).render(example=example)


def replace_example_placeholders(
    *,
    rendered_markdown: str,
    dataset_ref: str,
    allowed_fields: set[str],
    examples_root: Path,
    template_environment: Any,
) -> Markup:
    """Replace example placeholders without restyling the component HTML."""
    content = BeautifulSoup(rendered_markdown, "html.parser")
    for placeholder in content.select("dataset-example[data-reference]"):
        replacement_target = placeholder
        if (
            placeholder.parent
            and placeholder.parent.name == "p"
            and not placeholder.parent.get_text(strip=True)
        ):
            replacement_target = placeholder.parent

        heading = replacement_target.find_previous_sibling("h3")
        if heading:
            introduction_nodes = []
            node = heading
            while node and node is not replacement_target:
                next_node = node.next_sibling
                introduction_nodes.append(node)
                node = next_node

            row = content.new_tag("div", attrs={"class": "govuk-grid-row"})
            column = content.new_tag(
                "div", attrs={"class": "govuk-grid-column-two-thirds"}
            )
            replacement_target.insert_before(row)
            row.append(column)
            for introduction_node in introduction_nodes:
                column.append(introduction_node)

        html = render_dataset_example_component(
            example_ref=placeholder["data-reference"],
            table_layout=placeholder.get("data-table", "vertical"),
            dataset_ref=dataset_ref,
            allowed_fields=allowed_fields,
            examples_root=examples_root,
            template_environment=template_environment,
        )
        replacement_target.replace_with(BeautifulSoup(html, "html.parser"))
    return Markup(str(content))


def render_dataset_examples_content(
    *,
    dataset_ref: str,
    allowed_fields: set[str],
    examples_root: Path,
    content_root: Path,
    template_environment: Any,
) -> Markup | str:
    """Render a dataset's examples.md and resolve its example() calls."""
    content_path = content_root / "dataset" / dataset_ref / "examples.md"
    if not content_path.is_file():
        return ""

    content = frontmatter.load(content_path)
    declared_dataset = content.get("dataset")
    if declared_dataset != dataset_ref:
        raise ValueError(
            f"Examples content for '{dataset_ref}' declares dataset "
            f"'{declared_dataset}'"
        )

    referenced_examples: set[str] = set()

    def example_placeholder(
        example_ref: str, table: str = "vertical"
    ) -> Markup:
        if example_ref in referenced_examples:
            raise ValueError(
                f"Example '{example_ref}' is included more than once for "
                f"dataset '{dataset_ref}'"
            )
        referenced_examples.add(example_ref)
        if table not in EXAMPLE_TABLE_LAYOUTS:
            raise ValueError(
                f"Invalid table layout '{table}' for example '{example_ref}'. "
                "Use 'vertical' or 'wide'."
            )
        return Markup(
            f'<dataset-example data-reference="{example_ref}" '
            f'data-table="{table}"></dataset-example>'
        )

    rendered_markdown = template_environment.from_string(content.content).render(
        example=example_placeholder
    )
    return replace_example_placeholders(
        rendered_markdown=str(render_govuk_markdown(rendered_markdown)),
        dataset_ref=dataset_ref,
        allowed_fields=allowed_fields,
        examples_root=examples_root,
        template_environment=template_environment,
    )
