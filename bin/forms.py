from csv_helpers import read_csv
from utils import split_field_in_dicts


def load_2025_form_data():
    # use read_csv from csv_helpers to load from filepath
    forms_2025_filepath = "data/planning-application-form.csv"
    data = read_csv(forms_2025_filepath, as_dict=True)
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
