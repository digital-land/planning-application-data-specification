from bin.csv_helpers import read_csv


def load_app_types():
    return read_csv("../data/planning-application-type.csv", as_dict=True)


def load_forms():
    return read_csv("../data/planning-application-form.csv", as_dict=True)


def load_modules():
    modules = read_csv("../data/planning-application-module.csv", as_dict=True)
    return sorted(modules, key=lambda x: x["name"])


def load_app_modules():
    joins = read_csv("../data/application-type-module.csv", as_dict=True)
    return joins


def load_all():
    return load_app_types(), load_forms(), load_modules(), load_app_modules()
