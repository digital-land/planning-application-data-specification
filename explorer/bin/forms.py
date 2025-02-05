def print_all_forms(forms):
    for form in forms:
        print(f"{form['name']} (ref: {form['reference']}) - for app-types: {form['application-types']}")
        print(f"{form['document-url']}\n")


def form_details(form):
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


def get_forms_by_app_type(app_type, forms):
    return [form for form in forms if app_type in form['application-types'].split(';')]

