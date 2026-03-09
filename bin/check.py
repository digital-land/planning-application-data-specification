#!/usr/bin/env python3

from loader import load_content, load_needs


def run_check_section(title, check_func, *args):
    print(f"\nChecking {title}\n===========")
    return check_func(*args)


def perform_checks():
    from integrity_checks.applications import check_all as check_applications
    from integrity_checks.codelists import check_all as check_codelists
    from integrity_checks.components import check_all as check_components
    from integrity_checks.datasets import check_all as check_datasets
    from integrity_checks.fields import check_all as check_fields
    from integrity_checks.justifications import check_all as check_justifications
    from integrity_checks.modules import check_all as check_modules
    from integrity_checks.needs import check_all as check_needs
    from integrity_checks.specifications import check_all as check_specifications

    # Load from specification files
    specification = load_content()
    fields = specification["field"]
    codelists = specification["codelist"]
    components = specification["component"]
    datasets = specification["dataset"]
    modules = specification["module"]
    applications = specification["application"]
    specifications = specification["specification"]

    # load needs (for some checks)
    needs_content = load_needs()
    needs = needs_content.get("need", {})
    justifications = needs_content.get("justification", {})

    sections = [
        ("fields", check_fields, fields, components, codelists),
        ("components", check_components, components, fields, applications),
        ("datasets", check_datasets, datasets, fields),
        ("modules", check_modules, modules, fields),
        ("applications", check_applications, applications, fields, modules),
        ("codelists", check_codelists, codelists),
        ("needs", check_needs, needs),
        (
            "justification records",
            check_justifications,
            justifications,
            needs,
            datasets,
            fields,
        ),
        ("specifications", check_specifications, specifications, datasets),
    ]

    results = [
        run_check_section(title, check_func, *args)
        for title, check_func, *args in sections
    ]

    print("------------------------------------")
    if all(results):
        print("All integrity checks passed.")
    else:
        print("Integrity checks failed.")


if __name__ == "__main__":
    perform_checks()
