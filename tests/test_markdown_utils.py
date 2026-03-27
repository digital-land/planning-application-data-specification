from pathlib import Path

from bin.markdown_utils import (
    csv_to_markdown,
    markdown_bullet_list,
    markdown_link,
    markdown_table,
)


def test_markdown_link_returns_markdown_link():
    assert markdown_link("Example", "https://example.com") == "[Example](https://example.com)"


def test_markdown_table_returns_markdown_table():
    result = markdown_table(
        ["Name", "Reference"],
        [["Householder", "hh"], ["Full", "full"]],
    )

    assert result == (
        "| Name | Reference |\n"
        "| --- | --- |\n"
        "| Householder | hh |\n"
        "| Full | full |\n"
    )


def test_markdown_bullet_list_returns_markdown_list():
    result = markdown_bullet_list(["one", "two"])

    assert result == "* one\n* two\n"


def test_markdown_bullet_list_returns_empty_string_for_empty_input():
    assert markdown_bullet_list([]) == ""


def test_csv_to_markdown_renders_selected_fields(tmp_path):
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text(
        "reference,name,notes\nitem-1,Item 1,'quoted'\n",
        encoding="utf-8",
    )

    result = csv_to_markdown(str(csv_path), fields=["reference", "notes"])

    assert result == "| reference | notes |\n| --- | --- |\n| item-1 | quoted |\n"
