#!/usr/bin/env python3

import click

from bin.application_types import print_all, app_type_overview
from bin.csv_helpers import read_csv, write_csv
from bin.forms import print_all_forms, form_details, get_forms_by_app_type, get_form
from bin.loader import load_all


@click.group()
def cli():
    pass


@cli.command(name="app-type")
@click.option(
    "--ref",
    type=str,
    help="Reference of application type",
)
@click.option(
    "--all",
    is_flag=True,
    help="Print all references in alphabetical order",
)
def app_type(ref, all):
    application_types, forms, modules, app_mod_joins = load_all()

    if all:
        refs = sorted(app["reference"] for app in application_types)
        print("\nAll References:\n---")
        for r in refs:
            print(r)
        return

    if ref:
        app_type = next((app for app in application_types if app["reference"] == ref), None)
        if not app_type:
            print(f"Application type {ref} not found")
            return
        app_modules = [j['application-module'] for j in app_mod_joins if j["application-type"] == ref]
        app_type["modules"] = app_modules
        app_type_overview(app_type)
    else:
        print_all(application_types)
        print(f"\nForms: {len(forms)}")


@cli.command(name="form")
@click.option(
    "--app-type",
    type=str,
    help="Reference of application type",
)
@click.option(
    "--form-ref",
    type=str,
    help="Reference of application form",
)
def form(app_type, form_ref):
    application_types, forms, modules, app_mod_joins = load_all()

    if app_type:
        print("===")
        print(f"Forms for {app_type}")
        print("===")
        # TO DO: check it is legit app type
        print_all_forms(get_forms_by_app_type(app_type, forms))
    elif form_ref:
        applicable_modules = [module for module in modules if form_ref in module['application-forms'].split(';')]
        form_details(get_form(form_ref, forms), modules=applicable_modules)
    else:
        print_all_forms(forms)


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
    "--action",
    type=click.Choice(['sort'], case_sensitive=False),
    help="Action to perform on the CSV file",
)
@click.option(
    "--col-order",
    type=str,
    help="Order of columns in output",
)
def csv(filename, fieldname, action, col_order):
    if not filename:
        print("Please provide a filename")
        return
    
    data = read_csv(filename, as_dict=True)

    if not fieldname:
        print("Please provide a fieldname")
        return
    if fieldname not in data[0].keys():
        print(f"fieldname {fieldname} is not a field in this file")
        return

    if action == 'sort':
        # sort by the field given
        sorted_data = sorted(data, key=lambda x: x[fieldname])
        if col_order:
            write_csv(sorted_data, output_file=filename, first_headers=col_order.split(','), final_headers=[])
            return
        write_csv(sorted_data, output_file=filename, final_headers=[])
    else:
        print(f"Action {action} is not supported")


if __name__ == "__main__":
    cli()
