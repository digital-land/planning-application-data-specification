from csv_helpers import read_csv
from utils import split_field_in_dicts

FORMS_2025_FILEPATH = "data/analysis/2025-planning-application-form.csv"


def load_2025_form_data():
    data = read_csv(FORMS_2025_FILEPATH, as_dict=True)
    return split_field_in_dicts(data, "application-types")


def get_2025_forms_by_app_type(app_type):
    if not app_type:
        return None
    forms = load_2025_form_data()

    filtered_forms = [form for form in forms if app_type in form["application-types"]]

    return filtered_forms


def get_2025_form(form_ref, forms=None):
    if not form_ref:
        return None

    forms = forms if forms is not None else load_2025_form_data()
    matches = [form for form in forms if form_ref == form.get("reference")]
    if matches:
        return matches[0]
    return None


def get_2025_forms_by_refs(form_refs, forms=None):
    if not form_refs:
        return []

    forms = forms if forms is not None else load_2025_form_data()
    return [form for form_ref in form_refs if (form := get_2025_form(form_ref, forms))]


# add main
if __name__ == "__main__":
    app_type = "hh"
    forms = get_2025_forms_by_app_type(app_type)
    print(forms)
