import csv

def csv_to_markdown(
    filename="data/output.csv", 
    fields=None, 
    first_field="reference", 
    last_field=None, 
    encoding="utf-8"
):
    """
    Convert CSV to markdown table, optionally limiting to specific fields
    fields: List of field names to include in output. If None, includes all fields.
    """
    with open(filename, newline="", encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        
        # If fields specified, filter headers to only those fields
        if fields:
            headers_to_use = [h for h in headers if h in fields]
            # Get indices of fields we want to keep
            field_indices = [headers.index(h) for h in headers_to_use]
        else:
            headers_to_use = headers
            field_indices = range(len(headers))

        # Initialize markdown table with selected headers
        markdown_table = "| " + " | ".join(headers_to_use) + " |\n"
        markdown_table += "| " + " | ".join(["---"] * len(headers_to_use)) + " |\n"

        # Add rows with only selected fields
        for row in reader:
            selected_values = [row[i] for i in field_indices]
            # Clean values (strip quotes if present)
            cleaned_values = [
                val.strip("'") if val.startswith("'") and val.endswith("'") else val
                for val in selected_values
            ]
            markdown_table += "| " + " | ".join(cleaned_values) + " |\n"

    return markdown_table
