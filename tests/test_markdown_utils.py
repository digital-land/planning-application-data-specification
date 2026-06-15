from pathlib import Path

from markupsafe import Markup

from bin.markdown_utils import (
    csv_to_markdown,
    markdown_bullet_list,
    markdown_link,
    markdown_table,
    render_govuk_markdown,
)


def test_markdown_link_returns_markdown_link():
    assert (
        markdown_link("Example", "https://example.com")
        == "[Example](https://example.com)"
    )


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


def test_render_govuk_markdown_adds_govuk_classes_and_heading_ids():
    result = render_govuk_markdown(
        "## Decision: Example\n\n"
        "Some text with [a link](https://example.com).\n\n"
        "* one\n"
        "* two\n\n"
        "`code`\n\n"
        "---"
    )

    assert isinstance(result, Markup)
    assert '<h2 class="govuk-heading-l" id="decision-example">' in result
    assert '<p class="govuk-body">Some text with ' in result
    assert '<a class="govuk-link" href="https://example.com">a link</a>' in result
    assert '<ul class="govuk-list govuk-list--bullet">' in result
    assert '<code class="app-code">code</code>' in result
    assert '<hr class="govuk-section-break govuk-section-break--l"/>' in result


def test_render_govuk_markdown_adds_numbered_list_class():
    result = render_govuk_markdown("1. first\n2. second")

    assert '<ol class="govuk-list govuk-list--number">' in result


def test_render_govuk_markdown_can_return_soup():
    result = render_govuk_markdown("# Heading", make_safe=False)

    assert result.select_one("h1")["class"] == "govuk-heading-xl"
    assert result.select_one("h1")["id"] == "heading"


def test_render_govuk_markdown_returns_empty_string_for_none():
    assert render_govuk_markdown(None) == ""
