import csv
import re

from bs4 import BeautifulSoup
from markdown import markdown
from markupsafe import Markup
from slugify import slugify


def markdown_link(text, url):
    """Return a markdown link string."""
    return f"[{text}]({url})"


def markdown_table(headers, rows):
    """Return a markdown table string from headers and row values."""
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in rows:
        values = [str(value) for value in row]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines) + "\n"


def markdown_bullet_list(items):
    """Return a markdown bullet list string."""
    if not items:
        return ""

    return "\n".join(f"* {item}" for item in items) + "\n"


def csv_to_markdown(
    filename="data/output.csv",
    fields=None,
    exclude_fields=None,
    encoding="utf-8",
):
    """
    Convert CSV to a markdown table, optionally limiting to specific fields.
    """
    with open(filename, newline="", encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        headers_to_use = list(headers)

        if fields:
            headers_to_use = [header for header in headers_to_use if header in fields]

        if exclude_fields:
            headers_to_use = [
                header for header in headers_to_use if header not in exclude_fields
            ]

        field_indices = [headers.index(header) for header in headers_to_use]

        markdown_table = "| " + " | ".join(headers_to_use) + " |\n"
        markdown_table += "| " + " | ".join(["---"] * len(headers_to_use)) + " |\n"

        for row in reader:
            selected_values = [row[index] for index in field_indices]
            cleaned_values = [
                (
                    value.strip("'")
                    if value.startswith("'") and value.endswith("'")
                    else value
                )
                for value in selected_values
            ]
            markdown_table += "| " + " | ".join(cleaned_values) + " |\n"

    return markdown_table


def render_govuk_markdown(text, make_safe=True, capitalise=False):
    """Render markdown as HTML with GOV.UK Design System classes."""
    if text is None:
        return ""

    soup = BeautifulSoup(markdown(text, extensions=["tables"]), "html.parser")
    add_govuk_markdown_attrs(soup)

    if capitalise:
        capitalise_first_visible_character(soup)

    if make_safe:
        return Markup(str(soup))
    return soup


def capitalise_first_visible_character(soup):
    """Capitalise the first letter in rendered content, ignoring HTML markup."""
    for node in soup.find_all(string=True):
        match = re.search(r"[A-Za-z]", str(node))
        if not match:
            continue
        position = match.start()
        text = str(node)
        node.replace_with(text[:position] + text[position].upper() + text[position + 1 :])
        return


def add_govuk_markdown_attrs(soup):
    """Add GOV.UK Design System classes to rendered markdown HTML."""
    for tag in soup.select("p"):
        tag["class"] = "govuk-body"

    for tag in soup.select("h1, h2, h3, h4, h5"):
        tag["id"] = slugify(tag.get_text())

    for tag in soup.select("h1"):
        tag["class"] = "govuk-heading-xl"

    for tag in soup.select("h2"):
        tag["class"] = "govuk-heading-l"

    for tag in soup.select("h3"):
        tag["class"] = "govuk-heading-m"

    for tag in soup.select("h4, h5"):
        tag["class"] = "govuk-heading-s"

    for tag in soup.select("ul"):
        tag["class"] = "govuk-list govuk-list--bullet"

    for tag in soup.select("ol"):
        tag["class"] = "govuk-list govuk-list--number"

    for tag in soup.select("table"):
        tag["class"] = "govuk-table"

    for tag in soup.select("thead"):
        tag["class"] = "govuk-table__head"

    for tag in soup.select("tbody"):
        tag["class"] = "govuk-table__body"

    for tag in soup.select("tr"):
        tag["class"] = "govuk-table__row"

    for tag in soup.select("th"):
        tag["class"] = "govuk-table__header"
        tag["scope"] = "col"

    for tag in soup.select("td"):
        tag["class"] = "govuk-table__cell"

    for tag in soup.select("a"):
        tag["class"] = "govuk-link"

    for tag in soup.select("hr"):
        tag["class"] = "govuk-section-break govuk-section-break--l"

    for tag in soup.select("code"):
        tag["class"] = "app-code"
