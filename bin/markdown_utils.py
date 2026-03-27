import csv


def markdown_link(text, url):
    """Return a markdown link string."""
    return f"[{text}]({url})"


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
                value.strip("'")
                if value.startswith("'") and value.endswith("'")
                else value
                for value in selected_values
            ]
            markdown_table += "| " + " | ".join(cleaned_values) + " |\n"

    return markdown_table
