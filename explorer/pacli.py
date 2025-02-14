#!/usr/bin/env python3

import click
from datetime import datetime

from bin.application_types import print_all, app_type_overview
from bin.csv_helpers import read_csv, write_csv
from bin.forms import print_all_forms, form_details, get_forms_by_app_type, get_form, get_forms, get_app_types_covered
from bin.loader import load_all
from bin.modules import get_modules


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
        app_module_refs = [j['application-module'] for j in app_mod_joins if j["application-type"] == ref]
        app_type["modules"] = get_modules(app_module_refs, modules)
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
@click.option(
    "--module-name",
    type=str,
    help="Name of a module or section present in forms",
)
@click.option(
    "--not-in",
    is_flag=True,
    help="Only show forms --module-name is not in",
)
def form(app_type, form_ref, module_name, not_in):
    application_types, forms, modules, app_mod_joins = load_all()

    if app_type:
        print("===")
        print(f"Forms for {app_type}")
        print("===")
        # TO DO: check it is legit app type
        print_all_forms(get_forms_by_app_type(app_type, forms))
        return

    if form_ref:
        applicable_modules = [module for module in modules if form_ref in module['application-forms'].split(';')]
        form_details(get_form(form_ref, forms), modules=applicable_modules)
        return

    if module_name:
        print(f"\nModule: {module_name}\n\n")
        module = next((module for module in modules if module["name"] == module_name), None)
        if not module:
            print(f"Module {module_name} not found")
            return
        form_refs = module['application-forms'].split(';')
        if not_in:
            form_refs = list(set([_f['reference'] for _f in forms]) - set(form_refs))
            print(f"not in {len(form_refs)} forms\n---")
        else:
            print(f"in {len(form_refs)} forms\n---")

        filtered_forms = [get_form(ref, forms) for ref in form_refs]
        print_all_forms(filtered_forms)
        return

    print_all_forms(forms)


@cli.command(name="module")
@click.option(
    "--ref",
    type=str,
    help="Reference of module",
)
@click.option(
    "--show",
    type=click.Choice(['form', 'app-types', 'summary', 'all'], case_sensitive=False),
    help="Show either forms or application types covered by the module",
)
@click.option(
    "--make",
    is_flag=True,
    help="Helps make records for module - application type dataset",
)
def module(ref, show, make):
    application_types, forms, modules, app_mod_joins = load_all()

    if not show and not make:
        print("Please provide either --show or --make option")
        return

    if ref:
        module = next((module for module in modules if module["reference"] == ref), None)
        if not module:
            print(f"Module {ref} not found")
            return
        print(f"\nModule: {module['name']} (ref: {module['reference']})")
        
        app_types_covered = get_app_types_covered(get_forms(module['application-forms'].split(';'), forms))

        if show == 'form':
            print(f"Forms: {module['application-forms']}")
        elif show == 'app-types':
            print(f"Application types (as per the forms) with module: {';'.join(app_types_covered)}")
        
        # temp option whilst making this dataset
        if make:
            print("\nPotential entries to application-type-module dataset:\n")
            today = datetime.today().strftime('%Y-%m-%d')
            for app_type in app_types_covered:
                print(f"{app_type}-{module['reference']},{app_type},{module['reference']},{today},")
    else:
        print(f"---\n{len(modules)} Modules\n---\n")
        if show == 'all':
            print("All:\n")
            for module in modules:
                print(f"{module['name']} (ref: {module['reference']})")
        if show == 'summary':
            modules_without_end_date = [module for module in modules if not module.get("end-date")]
            print(f"Modules with end-date: {len(modules) - len(modules_without_end_date)}")
            modules_with_refs = [module for module in modules_without_end_date if module["reference"] and module["reference"] != ""]
            print(f"Modules with references: {len(modules_with_refs)}")


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
