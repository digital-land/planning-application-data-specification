#!/usr/bin/env python3

import click

from bin.application_types import all, overview
from bin.forms import print_all_forms, form_details, get_forms_by_app_type
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
def app_type(ref):
    application_types, forms = load_all()

    if ref:
        overview(application_types[0])
    else:
        all(application_types)
        print(f"\nForms: {len(forms)}")


@cli.command(name="form")
@click.option(
    "--app-type",
    type=str,
    help="Reference of application type",
)
def form(app_type):
    application_types, forms = load_all()

    if app_type:
        print("===")
        print(f"Forms for {app_type}")
        print("===")
        # TO DO: check it is legit app type
        print_all_forms(get_forms_by_app_type(app_type, forms))
    else:
        print_all_forms(forms)



if __name__ == "__main__":
    cli()
