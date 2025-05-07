def display_requirements(requirements, app_type=None, sub_type=None):
    """Display requirements in a formatted way to the terminal."""
    # Print header
    if app_type and sub_type:
        print(f"\nRequirements for {app_type} -> {sub_type}:")
    elif app_type:
        print(f"\nBase requirements for {app_type}:")
    else:
        print(f"\nRequirements for {sub_type}:")
    print("---")
    
    if not requirements:
        print("\nNo requirements found")
        return
        
    for req in sorted(requirements, key=lambda x: x['name']):
        print(f"\n{req['name']}")
        if req.get('description'):
            print(f"  {req['description']}")
        print(f"  Reference: {req['reference']}")


def get_requirement(ref, requirements):
    """Get a single requirement by its reference"""
    return next((req for req in requirements if req['reference'] == ref), None)


def get_requirements(refs, requirements, sort_by="name"):
    """Get multiple requirements by their references"""
    matched = []
    for ref in refs:
        req = get_requirement(ref, requirements)
        if req:
            matched.append(req)
    return sorted(matched, key=lambda x: x[sort_by])