#!/usr/bin/env python3

import click

from bin.application_types import print_all, overview
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
    application_types, forms, modules = load_all()

    if all:
        refs = sorted(app["reference"] for app in application_types)
        print("\nAll References:\n---")
        for r in refs:
            print(r)
        return

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
@click.option(
    "--form-ref",
    type=str,
    help="Reference of application form",
)
def form(app_type, form_ref):
    application_types, forms, modules = load_all()

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



if __name__ == "__main__":
    cli()
