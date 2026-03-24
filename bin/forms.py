from csv_helpers import read_csv
from utils import split_field_in_dicts

FORMS_2025_FILEPATH = "data/analysis/2025-planning-application-form.csv"


def load_2025_form_data():
    data = read_csv(FORMS_2025_FILEPATH, as_dict=True)
    return split_field_in_dicts(data, "application-types")


def get_2025_forms_by_app_type(app_type):
    if not app_type:
        return None
    # get form data
    forms = load_2025_form_data()

    # filter forms that cover the specified application type using in form['application-types']
    filtered_forms = [form for form in forms if app_type in form["application-types"]]

    return filtered_forms


# add main
if __name__ == "__main__":
    app_type = "hh"
    forms = get_2025_forms_by_app_type(app_type)
    print(forms)
