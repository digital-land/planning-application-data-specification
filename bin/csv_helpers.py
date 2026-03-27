import csv
from pathlib import Path

from markdown_utils import csv_to_markdown


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
