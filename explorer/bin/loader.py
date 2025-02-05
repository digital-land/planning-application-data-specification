from bin.csv_helpers import read_csv


def load_app_types():
    return read_csv("../data/planning-application-type.csv", as_dict=True)


def load_forms():
    return read_csv("../data/planning-application-form.csv", as_dict=True)


def load_all():
    return load_app_types(), load_forms()
