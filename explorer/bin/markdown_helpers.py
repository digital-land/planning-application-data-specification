import csv

def csv_to_markdown(
    filename="data/output.csv", first_field="reference", last_field=None, encoding="utf-8"
):
    with open(filename, newline="", encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)

        # Read the headers
        headers = next(reader)
        headers_sorted = headers

        if last_field:
            # Sort the headers and keep 'option' as the last one if it exists
            headers_sorted = sorted(
                [
                    header
                    for header in headers
                    if header != first_field and header != last_field
                ]
            )
            if last_field in headers:
                headers_sorted.append(last_field)
            if first_field and first_field in headers:
                headers_sorted.insert(0, first_field)

        # Initialize the markdown table with headers
        markdown_table = "| " + " | ".join(headers_sorted) + " |\n"
        markdown_table += "| " + " | ".join(["---"] * len(headers_sorted)) + " |\n"

        # Add the rows
        for row in reader:
            # Create a dictionary for the row to ensure correct order
            row_dict = {headers[i]: row[i] for i in range(len(headers))}
            row_sorted = [
                row_dict[header].strip("'") if row_dict[header].startswith("'") and row_dict[header].endswith("'") else row_dict[header]
                for header in headers_sorted
            ]
            markdown_table += "| " + " | ".join(row_sorted) + " |\n"

    return markdown_table
