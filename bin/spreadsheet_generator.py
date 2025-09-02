import os

from csv_helpers import write_csv
from forms import get_2025_forms_by_app_type
from loader import load_content
from utils import make_hyperlink_cell


def _get_module_ref(module_obj, key=None):
    # try common keys for a module reference
    if key and isinstance(key, str):
        return key
    if not isinstance(module_obj, dict):
        return ""
    return (
        module_obj.get("module")
        or module_obj.get("reference")
        or module_obj.get("id")
        or module_obj.get("ref")
        or ""
    )


def _format_form_link(form):
    if isinstance(form, dict):
        form_url = form.get("document-url")
        form_name = form.get("name") or form.get("title") or form_url or ""
    else:
        return ""

    if form_url:
        return make_hyperlink_cell(form_name, form_url)
    return form_name


def module_list(app):
    if "modules" not in app.keys():
        return []
    modules_dict = app.get("modules", {})
    return [m["module"] for m in modules_dict]


def get_apps_with_module(module_ref, applications):
    return [
        app_ref
        for app_ref, app in applications.items()
        if module_ref in module_list(app)
    ]


def get_forms(app_types):
    forms = []
    for app_type in app_types:
        forms.extend(get_2025_forms_by_app_type(app_type))
    # de duplicate the forms before returning
    return list({form["reference"]: form for form in forms}.values())


def generate_spreadsheet_all_modules(
    specification, output_path: str = "tmp/module_spreadsheet.csv"
):
    """
    Generate a CSV string containing one row per module with columns:
    - module reference
    - module name
    - current description
    - new description (blank)
    - forms (form name displayed as a markdown link to the form)

    `modules` may be either a dict (mapping reference->module) or a list of module objects.
    Each module object is expected to be a dict that may contain `name`, `description`,
    and `forms` (a list of strings or dicts).
    """
    modules = specification.get("module")
    applications = specification.get("application")

    highest_form_count = 0
    rows = []
    for ref, module in modules.items():
        module_name = module.get("name", "")
        description = module.get("description", "")
        row = {
            "reference": ref,
            "name": module_name,
            "current-description": description,
            "new-description": "",
        }
        used_in = get_apps_with_module(ref, applications)
        forms = get_forms(used_in)
        formatted_forms = [f for f in (_format_form_link(f) for f in forms) if f]
        print(ref, len(formatted_forms))
        if len(formatted_forms) == 0:
            row["form0"] = ""
        else:
            highest_form_count = max(highest_form_count, len(formatted_forms))
            for i, form in enumerate(formatted_forms, start=0):
                row[f"form{i}"] = form
        rows.append(row)

    folder = os.path.dirname(output_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    # place the the forms headers at the end
    final_headers = []
    for i in range(highest_form_count):
        final_headers.append(f"form{i}")
    write_csv(rows, output_file=output_path, final_headers=final_headers)

    return output_path


if __name__ == "__main__":
    specification = load_content()
    out = generate_spreadsheet_all_modules(specification)
    print(f"Wrote spreadsheet to: {out}")
