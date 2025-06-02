#!/usr/bin/env python3

import os
from datetime import datetime

import click
from bin.application_types import (
    add_modules,
    app_type_overview,
    generate_application_markdown,
    generate_specification_index_file,
    get_app_type_from_ref,
    get_app_types_with_module,
    print_all,
    print_app_types_as_markdown_table,
    print_sub_types,
)
from bin.checks import check_requirements
from bin.forms import (
    form_details,
    get_app_types_covered,
    get_form,
    get_forms,
    get_forms_by_app_type,
    print_all_forms,
)
from bin.loader import load_all, load_data, load_requirements
from bin.modules import (
    check_codelists,
    check_modules,
    get_expected_joins,
    get_module_discussion_url,
    get_modules,
    join_data_maker,
)
from bin.requirements import display_requirements, get_requirements

# these are taken from data/planning-application-sub-type.csv
SUB_TYPES = (
    "ldc-existing-use",
    "ldc-prospective-use",
    "ldc-proposed-work-lb",
    "outline-some",
    "outline-all",
    "pa-extension",
    "pa-storey",
)


@click.group()
def cli():
    pass


def prepare_and_generate_application(app, app_mod_joins, modules, sub_types):
    try:
        # Get modules for this application type
        app_module_refs = [
            j["application-module"]
            for j in app_mod_joins
            if j["application-type"] == app["reference"] and not j.get("end-date")
        ]
        app["modules"] = get_modules(app_module_refs, modules)

        # Get any sub-types for this application
        app_sub_types = [
            s for s in sub_types if s["application-type"] == app["reference"]
        ]
        app["sub-types"] = []

        if app_sub_types:
            # If app has sub-types, only generate those
            print(f"\nGenerating markdown for {app['name']} sub-types")
            for st in app_sub_types:
                print(f"  -> {st['name']}")
                # Get modules for this sub-type
                st_module_refs = [
                    j["application-module"]
                    for j in app_mod_joins
                    if j["application-sub-type"] == st["reference"]
                    and not j.get("end-date")
                ]
                st["modules"] = get_modules(st_module_refs, modules)
                app["sub-types"].append(st)
                generate_application_markdown(app, sub_type_ref=st["reference"])
        else:
            # Only generate base application markdown if no sub-types
            print(f"\nGenerating markdown for {app['name']}")
            generate_application_markdown(app)

    except Exception as e:
        return f"Error processing {app['name']}: {str(e)}"
    return None


@cli.command(name="app-type")
@click.option(
    "--ref",
    type=str,
    help="Reference of application type",
)
@click.option(
    "--refs",
    type=str,
    help="References of application types",
)
@click.option(
    "--all",
    is_flag=True,
    help="Print all references in alphabetical order",
)
@click.option(
    "--combine",
    type=str,
    help="References of application types",
)
@click.option(
    "--sort-by",
    type=str,
    default="reference",
    help="Field name to sort by",
)
@click.option(
    "--show-sub-types",
    is_flag=True,
    help="Print all application sub types",
)
@click.option(
    "--sub-type-ref",
    type=click.Choice(SUB_TYPES, case_sensitive=False),
    help="Show either forms or application types covered by the module",
)
@click.option(
    "--markdown",
    is_flag=True,
    help="Print as Markdown text to the terminal",
)
@click.option(
    "--generate-application",
    is_flag=True,
    help="Build application type markdown",
)
@click.option(
    "--generate-specification-index",
    is_flag=True,
    help="Generate a markdown file containing application model and all active modules",
)
def app_type(
    ref,
    refs,
    all,
    combine,
    sort_by,
    show_sub_types,
    sub_type_ref,
    markdown,
    generate_application,
    generate_specification_index,
):
    application_types, forms, modules, app_mod_joins, sub_types = load_all()

    if generate_specification_index:
        generate_specification_index_file(modules)
        return

    if all:
        if markdown:
            print_app_types_as_markdown_table(application_types)
            return

        if generate_application:
            print("\nGenerating markdown files for all application types...")
            errors = []

            for app in sorted(application_types, key=lambda x: x["name"]):
                error = prepare_and_generate_application(
                    app, app_mod_joins, modules, sub_types
                )
                if error:
                    errors.append(error)

            if errors:
                print("\nErrors encountered:")
                for error in errors:
                    print(f"  {error}")
            else:
                print("\nAll markdown files generated successfully!")
            return

        refs = sorted(app[sort_by] for app in application_types)
        print("\nAll References:\n---")
        for r in refs:
            print(r)
        print("----------------")
        print(f"All application type references: {';'.join(refs)}")
        return

    if show_sub_types:
        print_sub_types(sub_types)
        return

    if refs:
        refs = refs.split(";")
        matching_app_types = sorted(
            [app for r in refs for app in application_types if app["reference"] == r],
            key=lambda x: x["name"],
        )
        print_all(matching_app_types)
        return

    if combine:
        app_types = [
            app_type
            for app_type_ref in combine.split(";")
            if (app_type := get_app_type_from_ref(app_type_ref, application_types))
            is not None
        ]
        app_types = [
            add_modules(app_type, application_types, app_mod_joins, modules)
            for app_type in app_types
        ]
        combined_modules = {
            module["reference"]: module
            for app_type in app_types
            for module in app_type["modules"]
        }
        print(
            f"Combined application: {' + '.join([at['reference'] for at in app_types])}\n----\n"
        )
        print("Modules:\n")
        for module in sorted(combined_modules.values(), key=lambda x: x["name"]):
            print(f"{module['name']} (ref: {module['reference']})")
        return

    if ref:
        app_type = next(
            (app for app in application_types if app["reference"] == ref), None
        )
        if not app_type:
            print(f"Application type {ref} not found")
            return

        if generate_application:
            error = prepare_and_generate_application(
                app_type, app_mod_joins, modules, sub_types
            )
            if error:
                print(error)
            return

        # For display only - prepare the data
        app_module_refs = [
            j["application-module"]
            for j in app_mod_joins
            if j["application-type"] == ref and not j.get("end-date")
        ]
        app_type["modules"] = get_modules(app_module_refs, modules)
        app_type["sub-types"] = []
        for sub_type in [j for j in sub_types if j["application-type"] == ref]:
            matched_modules = [
                j["application-module"]
                for j in app_mod_joins
                if j["application-sub-type"] == sub_type["reference"]
            ]
            sub_type["modules"] = get_modules(matched_modules, modules)
            app_type["sub-types"].append(sub_type)

        app_type_overview(app_type, sub_type_ref=sub_type_ref, markdown=markdown)
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
@click.option(
    "--markdown",
    is_flag=True,
    help="Print as Markdown text to the terminal",
)
def form(app_type, form_ref, module_name, not_in, markdown):
    application_types, forms, modules, app_mod_joins, sub_types = load_all()

    if app_type:
        print("===")
        print(f"Forms for {app_type}")
        print("===")
        # TO DO: check it is legit app type
        print_all_forms(get_forms_by_app_type(app_type, forms))
        return

    if form_ref:
        app_form = get_form(form_ref, forms)
        if not app_form:
            print(f"Form {form_ref} not found")
            return
        applicable_modules = [
            module
            for module in modules
            if form_ref in module["application-forms"].split(";")
        ]
        form_details(get_form(form_ref, forms), modules=applicable_modules)

        if markdown:
            app_types_covered = app_form["application-types"].split(";")
            if len(app_types_covered) > 1:
                print("Form covers multiple application types")
                return
            expected_joins = get_expected_joins(
                app_types_covered[0], applicable_modules, modules
            )
            join_data_maker(expected_joins, app_mod_joins)
        return

    if module_name:
        print(f"\nModule: {module_name}\n\n")
        module = next(
            (module for module in modules if module["name"] == module_name), None
        )
        if not module:
            print(f"Module {module_name} not found")
            return
        form_refs = module["application-forms"].split(";")
        if not_in:
            form_refs = list(set([_f["reference"] for _f in forms]) - set(form_refs))
            print(f"not in {len(form_refs)} forms\n---")
        else:
            print(f"in {len(form_refs)} forms\n---")

        filtered_forms = [get_form(ref, forms) for ref in form_refs]
        print_all_forms(filtered_forms, markdown=markdown)
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
    type=click.Choice(
        ["form", "app-types", "summary", "all", "summary-extra"], case_sensitive=False
    ),
    help="Show either forms or application types covered by the module",
)
@click.option(
    "--make",
    is_flag=True,
    help="Helps make records for module - application type dataset",
)
@click.option(
    "--app-types",
    type=str,
    help="List of application types separated by ';' to use instead of app_types_covered",
)
def module(ref, show, make, app_types):
    application_types, forms, modules, app_mod_joins, sub_types = load_all()

    if not show and not make:
        print("Please provide either --show or --make option")
        return

    if ref:
        module = next(
            (module for module in modules if module["reference"] == ref), None
        )
        if not module:
            print(f"Module {ref} not found")
            return
        print(f"\nModule: {module['name']} (ref: {module['reference']})")

        app_types_covered = get_app_types_with_module(
            ref, app_mod_joins, application_types, sub_types
        )

        if show == "form":
            print(f"Forms: {module['application-forms']}")
        elif show == "app-types":
            print(f"Application types with module:")
            # print the application types with the module
            for at in app_types_covered["application-types"]:
                print(f"  {at['name']}")
            print("\nAll module references:")
            print(
                ";".join(
                    [at["reference"] for at in app_types_covered["application-types"]]
                )
            )
            # print the sub types with the module
            for at in app_types_covered["sub-types"]:
                print(f"  {at['application-type']} -> {at['name']}")
    else:
        print(f"---\n{len(modules)} Modules\n---\n")
        if show == "all":
            print("All:\n")
            for module in modules:
                print(f"{module['name']} (ref: {module['reference']})")
        if show == "summary":
            modules_without_end_date = [
                module for module in modules if not module.get("end-date")
            ]
            print(
                f"Modules with end-date: {len(modules) - len(modules_without_end_date)}"
            )
            modules_with_refs = [
                module
                for module in modules_without_end_date
                if module["reference"] and module["reference"] != ""
            ]
            print(f"Modules with references: {len(modules_with_refs)}")
            modules_without_refs = [
                module
                for module in modules_without_end_date
                if not module.get("reference")
            ]
            print("----")
            print(f"Modules to do: {len(modules_without_refs)}")
            print("----")
            for module in modules_without_refs:
                print(f"{module['name']} (ref: {module['reference']})")


@cli.command(name="requirements")
@click.option(
    "--app-type",
    type=str,
    help="Reference of application type",
)
@click.option(
    "--sub-type",
    type=str,
    help="Reference of application sub-type",
)
def requirements(app_type, sub_type):
    """List national planning requirements for an application type or sub-type."""
    data = load_data()
    matched_reqs = []

    def match_on(term, fieldname, row):
        return term.lower() in row[fieldname].lower() if row.get(fieldname) else False

    if app_type:
        app_type = app_type.lower()
        matched_reqs = [
            req
            for req in data["national-requirements"]
            if match_on(app_type, "application-type", req)
        ]

    # To do: should check app type and sub type are a valid pair
    if sub_type:
        sub_type = sub_type.lower()
        matched_reqs += [
            req
            for req in data["national-requirements"]
            if match_on(sub_type, "application-sub-type", req)
        ]

    # Get full requirement details
    planning_req_refs = [req["planning-requirement"] for req in matched_reqs]
    reqs_with_details = get_requirements(planning_req_refs, data["requirements"])

    # Print results
    display_requirements(reqs_with_details, app_type, sub_type)


@cli.command(name="check")
@click.option(
    "--module",
    is_flag=True,
    help="Check module references and markdown files",
)
@click.option(
    "--codelist",
    is_flag=True,
    help="Check codelists for module references",
)
@click.option(
    "--requirements",
    is_flag=True,
    help="Check planning requirements",
)
def check(module, codelist, requirements):
    if module or codelist:
        _, _, modules, app_mod_joins, _ = load_all()
        if module:
            check_modules(modules, "../specification/module", app_mod_joins)
        if codelist:
            check_codelists(modules)

    if requirements:
        check_requirements()


if __name__ == "__main__":
    cli()
