def print_all_forms(forms, markdown=False):
    for form in forms:
        if markdown:
            print(f"* [{form['name']}]({form['document-url']})")
        else:
            print(f"{form['name']} (ref: {form['reference']})")
            print(f"Covers app-types: {form['application-types']}")
            print(f"URL: {form['document-url']}\n")
    print("================================================")
    app_types = [form['application-types'] for form in forms]
    flattened_app_types = sorted(set([app_type for types in app_types for app_type in types.split(';')]))
    print(f"Application types covered by forms: {';'.join(flattened_app_types)}")


def form_details(form, modules=None):
    print("===")
    print("Form")
    print("===")

    print(f"{form['name']} (ref: {form['reference']})")

    print("\nCovers")
    print("===")
    app_types = form['application-types'].split(";")
    for _t in app_types:
        print(_t)

    print("\nLink")
    print("===")
    print(form['document-url'])

    if modules:
        print(f"\n{len(modules)} Sections (in form)")
        print("===")
        for module in modules:
            print(f"'{module['name']}'")



def get_forms_by_app_type(app_type, forms):
    return [form for form in forms if app_type in form['application-types'].split(';')]


def get_form(ref, forms):
    matches = [form for form in forms if ref == form['reference']]
    if matches:
        return matches[0]
    return None


def get_forms(refs, forms):
    matched_forms = [get_form(ref, forms) for ref in refs]
    return matched_forms


def get_app_types_covered(forms):
    app_types = [form['application-types'] for form in forms]
    flattened_app_types = sorted(set([app_type for types in app_types for app_type in types.split(';')]))
    return flattened_app_types
