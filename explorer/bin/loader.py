from bin.csv_helpers import read_csv


def load_app_types():
    return read_csv("../data/planning-application-type.csv", as_dict=True)


def load_sub_types():
    joins = read_csv("../data/planning-application-sub-type.csv", as_dict=True)
    return joins


def load_forms():
    return read_csv("../data/planning-application-form.csv", as_dict=True)


def load_modules():
    modules = read_csv("../data/planning-application-module.csv", as_dict=True)
    return sorted(modules, key=lambda x: x["name"])


def load_app_modules():
    joins = read_csv("../data/application-type-module.csv", as_dict=True)
    return joins


def load_requirements():
    planning_requirements = read_csv("../data/planning-requirement.csv", as_dict=True)
    return planning_requirements


def load_national_requirements():
    national_requirements = read_csv("../data/national-planning-requirement.csv", as_dict=True)
    return national_requirements


def load_all():
    return load_app_types(), load_forms(), load_modules(), load_app_modules(), load_sub_types()


def load_data():
    return {
        "app-types": load_app_types(),
        "forms": load_forms(),
        "modules": load_modules(),
        "app-modules": load_app_modules(),
        "sub-types": load_sub_types(),
        "requirements": load_requirements(),
        "national-requirements": load_national_requirements(),
    }
