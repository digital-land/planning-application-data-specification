from csv_helpers import read_csv
from utils import get_record, split_field_in_dicts, split_string

FORMS_2025_FILEPATH = "data/analysis/2025-planning-application-form.csv"
MODULES_2025_FILEPATH = "data/analysis/2025-planning-application-module.csv"


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
    return get_record(forms, form_ref)


def get_2025_forms_by_refs(form_refs, forms=None):
    if not form_refs:
        return []

    forms = forms if forms is not None else load_2025_form_data()
    return [form for form_ref in form_refs if (form := get_2025_form(form_ref, forms))]


def load_2025_module_analysis_data():
    return read_csv(MODULES_2025_FILEPATH, as_dict=True)


def get_2025_forms_for_module(module_ref, forms=None, modules=None):
    if not module_ref:
        return []

    forms = forms if forms is not None else load_2025_form_data()
    modules = modules if modules is not None else load_2025_module_analysis_data()

    module = get_record(modules, module_ref)
    if not module:
        return []

    raw_form_refs = module.get("application-forms", "")
    form_refs = split_string(raw_form_refs)
    return get_2025_forms_by_refs(form_refs, forms)


def get_2025_modules_for_form(form_ref, modules=None):
    if not form_ref:
        return []

    modules = modules if modules is not None else load_2025_module_analysis_data()
    matching_modules = [
        module
        for module in modules
        if form_ref in split_string(module.get("application-forms", ""))
    ]
    return sorted(matching_modules, key=lambda module: module.get("name", ""))


# add main
if __name__ == "__main__":
    app_type = "hh"
    forms = get_2025_forms_by_app_type(app_type)
    print(forms)
