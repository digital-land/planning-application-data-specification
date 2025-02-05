#!/usr/bin/env python3

import click

from bin.application_types import all, overview
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


if __name__ == "__main__":
    cli()
