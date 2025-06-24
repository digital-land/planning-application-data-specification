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
