import csv
from pathlib import Path


def read_csv(filename, encoding="utf-8", as_dict=False, include_row_num=False):
    # Read the CSV file
    with open(filename, newline="", encoding=encoding) as csvfile:
        data = []
        if as_dict:
            reader = csv.DictReader(csvfile)
            # Start row numbering at 1
            for i, row in enumerate(reader, start=1):

                if include_row_num:
                    row["_row_num"] = i
                data.append(row)
        else:
            reader = csv.reader(csvfile)
            # Start row numbering at 1
            for i, row in enumerate(reader, start=1):
                if include_row_num:
                    # Insert the row number at the start of the row
                    row.insert(0, i)
                data.append(row)

    return data


def read_csv_with_headers(filename, encoding="utf-8"):
    """
    Read a CSV file and return its headers plus row dicts.
    """
    with open(filename, newline="", encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames or [], list(reader)


# expects data to be list of dicts
def write_csv(
    data,
    output_file="data/output.csv",
    first_headers=["reference"],
    final_headers=["entry-date", "start-date", "end-date"],
):
    # Determine the headers
    # Start with 'reference', then sort the rest alphabetically, excluding the last 3 specified columns
    first_headers = first_headers
    final_headers = final_headers
    other_columns = sorted(
        k for k in data[0].keys() if k not in first_headers + final_headers
    )

    # Combine the columns in the desired order
    headers = first_headers + other_columns + final_headers

    # Write to a CSV file
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the headers
        writer.writeheader()

        # Write the data rows
        for row in data:
            writer.writerow(row)


def csv_to_markdown(
    filename="data/output.csv",
    fields=None,
    exclude_fields=None,
    first_field="reference",
    last_field=None,
    encoding="utf-8",
):
    """
    Convert CSV to markdown table, optionally limiting to specific fields
    fields: List of field names to include in output. If None, includes all fields.
    """
    with open(filename, newline="", encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        # Start with headers as read from file
        headers_to_use = list(headers)

        # If fields specified, restrict to those fields (in CSV order)
        if fields:
            headers_to_use = [h for h in headers_to_use if h in fields]

        # If exclude_fields specified, remove them if present
        if exclude_fields:
            headers_to_use = [h for h in headers_to_use if h not in exclude_fields]

        # Determine the indices of columns to output (preserve CSV ordering)
        field_indices = [headers.index(h) for h in headers_to_use]

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


def csvs_to_excel(csv_paths, output_path):
    """
    Combine multiple CSV files into a single Excel workbook, one sheet per CSV.
    Sheet names are derived from the CSV stem and truncated to 31 chars.
    """
    try:
        from openpyxl import Workbook
    except ImportError as e:  # pragma: no cover
        raise RuntimeError("openpyxl is required to combine CSVs to Excel") from e

    wb = Workbook()
    # remove default sheet
    if wb.active:
        wb.remove(wb.active)

    for csv_file in csv_paths:
        sheet_name = Path(csv_file).stem[:31]
        ws = wb.create_sheet(title=sheet_name)
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                ws.append(row)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output_path)
    return output_path
