#!/usr/bin/env python3

import click
from bin.csv_helpers import read_csv, write_csv
from bin.markdown_helpers import csv_to_markdown


@click.group()
def cli():
    pass


@cli.command(name="csv")
@click.option(
    "--filename",
    type=str,
    help="CSV file to read",
)
@click.option(
    "--fieldname",
    type=str,
    help="Fieldname for performing action",
)
@click.option(
    "--fields",
    type=str,
    help="Comma-separated list of fields to include in output",
)
@click.option(
    "--action",
    type=click.Choice(["sort"], case_sensitive=False),
    help="Action to perform on the CSV file",
)
@click.option(
    "--col-order",
    type=str,
    help="Order of columns in output",
)
@click.option(
    "--markdown",
    is_flag=True,
    help="Print the CSV as Markdown to the terminal",
)
def csv(filename, fieldname, fields, action, col_order, markdown):
    if not filename:
        print("Please provide a filename")
        return
    print(filename)

    data = read_csv(filename, as_dict=True)

    if markdown:
        fields_list = fields.split(",") if fields else None
        print(csv_to_markdown(filename, fields=fields_list))
        return

    if not fieldname:
        print("Please provide a fieldname")
        return
    if fieldname not in data[0].keys():
        print(f"fieldname {fieldname} is not a field in this file")
        return

    if action == "sort":
        # sort by the field given
        sorted_data = sorted(data, key=lambda x: x[fieldname])
        if col_order:
            write_csv(
                sorted_data,
                output_file=filename,
                first_headers=col_order.split(","),
                final_headers=[],
            )
            return
        write_csv(sorted_data, output_file=filename, final_headers=[])
    else:
        print(f"Action {action} is not supported")


if __name__ == "__main__":
    cli()
