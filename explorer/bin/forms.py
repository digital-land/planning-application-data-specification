def print_all_forms(forms):
    for form in forms:
        print(f"{form['name']} (ref: {form['reference']}) - for app-types: {form['application-types']}")
        print(f"{form['document-url']}\n")


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
        print("\nModules (in form)")
        print("===")
        for module in modules:
            print(module['name'])



def get_forms_by_app_type(app_type, forms):
    return [form for form in forms if app_type in form['application-types'].split(';')]


def get_form(ref, forms):
    matches = [form for form in forms if ref == form['reference']]
    if matches:
        return matches[0]
    return None

