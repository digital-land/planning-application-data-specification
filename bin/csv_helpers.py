import csv


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
