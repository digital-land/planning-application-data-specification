#!/usr/bin/env python3

from loader import load_content, load_needs


def perform_checks():
    from integrity_checks.applications import check_all as check_applications
    from integrity_checks.codelists import check_all as check_codelists
    from integrity_checks.components import check_all as check_components
    from integrity_checks.datasets import check_all as check_datasets
    from integrity_checks.fields import check_all as check_fields
    from integrity_checks.modules import check_all as check_modules
    from integrity_checks.needs import check_all as check_needs

    # Load from specification files
    specification = load_content()
    fields = specification["field"]
    codelists = specification["codelist"]
    components = specification["component"]
    datasets = specification["dataset"]
    modules = specification["module"]
    applications = specification["application"]

    # load needs (for some checks)
    needs_content = load_needs()
    needs = needs_content.get("need", {})
    justifications = needs_content.get("justification", {})

    # Perform checks
    print("\nChecking fields\n===========")
    fields_valid = check_fields(fields, components, codelists)
    print("\nChecking components\n===========")
    components_valid = check_components(components, fields, applications)
    print("\nChecking datasets\n===========")
    datasets_valid = check_datasets(datasets, fields)
    print("\nChecking modules\n===========")
    modules_valid = check_modules(modules, fields)

    print("\nChecking applications\n===========")
    applications_valid = check_applications(applications, fields, modules)

    print("\nChecking codelists\n===========")
    codelists_valid = check_codelists(codelists)

    print("\nChecking needs\n===========")
    needs_valid = check_needs(needs)

    print("------------------------------------")
    if (
        fields_valid
        and components_valid
        and datasets_valid
        and modules_valid
        and applications_valid
        and codelists_valid
        and needs_valid
    ):
        print("All integrity checks passed.")
    else:
        print("Integrity checks failed.")


if __name__ == "__main__":
    perform_checks()
