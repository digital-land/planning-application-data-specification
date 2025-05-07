from bin.loader import load_data

def check_requirements_for_duplicates(planning_requirements):
    """
    Check for duplicate references in the planning-requirement.csv file.
    """
    # Check for duplicates in reference column
    references = [row['reference'] for row in planning_requirements]
    seen = set()
    duplicates = set()

    for ref in references:
        if ref in seen:
            duplicates.add(ref)
        seen.add(ref)

    if duplicates:
        print("\nFound duplicate references in planning-requirement.csv:")
        for dup in sorted(duplicates):
            print(f"  - {dup}")
        return True
    else:
        print("\nNo duplicate references found in planning-requirement.csv")
        return False


def check_valid_requirement_references(planning_requirements, application_types, sub_types, requirements):
    """
    Check that all references used in national-planning-requirement.csv exist in their respective datasets
    """
    print("\nChecking national planning requirement data...")

    # Get sets of valid references
    valid_app_types = {at['reference'] for at in application_types}
    valid_sub_types = {st['reference'] for st in sub_types}
    valid_requirements = {r['reference'] for r in requirements}

    # Track invalid references
    invalid_refs = {
        'application-type': set(),
        'application-sub-type': set(),
        'planning-requirement': set()
    }

    # Check each row in planning requirements
    for row in planning_requirements:
        app_type = row['application-type']
        sub_type = row['application-sub-type']
        req = row['planning-requirement']

        if app_type and app_type not in valid_app_types:
            invalid_refs['application-type'].add(app_type)

        if sub_type and sub_type not in valid_sub_types:
            invalid_refs['application-sub-type'].add(sub_type)

        if req and req not in valid_requirements:
            invalid_refs['planning-requirement'].add(req)

    # Print results
    issues_found = False

    if invalid_refs['application-type']:
        issues_found = True
        print("\nInvalid application type references:")
        for ref in sorted(invalid_refs['application-type']):
            print(f"  - {ref}")

    if invalid_refs['application-sub-type']:
        issues_found = True
        print("\nInvalid application sub-type references:")
        for ref in sorted(invalid_refs['application-sub-type']):
            print(f"  - {ref}")

    if invalid_refs['planning-requirement']:
        issues_found = True
        print("\nInvalid planning requirement references:")
        for ref in sorted(invalid_refs['planning-requirement']):
            print(f"  - {ref}")

    if not issues_found:
        print("All references are valid!")

    return bool(issues_found)


def check_requirements():
    print("Checking planning requirements...")
    data = load_data()
    print(data.keys())

    has_issues = False

    # Check for duplicates
    has_duplicates = check_requirements_for_duplicates(data['requirements'])
    if has_duplicates:
        has_issues = True

    # Check references
    has_invalid_refs = check_valid_requirement_references(
        data['national-requirements'],
        data['app-types'], 
        data['sub-types'],
        data['requirements']
    )
    if has_invalid_refs:
        has_issues = True

    if not has_issues:
        print("\nAll checks passed!")