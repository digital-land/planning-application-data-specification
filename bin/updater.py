from pathlib import Path

import frontmatter
from loader import load_content

application_dir = Path("specification") / "application"
module_dir = Path("specification") / "module"


def save_frontmatter_obj(obj, output_file_path):
    try:
        with output_file_path.open("w", encoding="utf-8") as fh:
            fh.write(frontmatter.dumps(obj))
        print(f"Wrote updated to {output_file_path}")
    except Exception as exc:
        print(f"Failed to write file {output_file_path}: {exc}")


def update_application(ref, field, value):
    specification = load_content()
    # Perform update logic here
    print(f"Updating application {ref}: setting {field} to {value}")
    application = specification["application"].get(ref)
    if application:
        application[field] = value
        post = application
    else:
        print(f"Application {ref} not found.")

    # save the file back to the markdown file
    application_dir.mkdir(parents=True, exist_ok=True)
    out_path = application_dir / f"{ref}.schema.md"

    save_frontmatter_obj(post, out_path)


def update_module(ref, field, value):
    specification = load_content()
    # Perform update logic here
    print(f"Updating module {ref}: setting {field} to {value}")
    module = specification["module"].get(ref)
    if module:
        module[field] = value
        post = module
    else:
        print(f"Module {ref} not found.")

    # save the file back to the markdown file
    module_dir.mkdir(parents=True, exist_ok=True)
    out_path = module_dir / f"{ref}.schema.md"

    save_frontmatter_obj(post, out_path)


def batch_update(element: str, field: str, updates: list):
    for update in updates:
        ref = update.get("reference")
        value = update.get(field)
        if element == "application":
            update_application(ref, field, value)
        elif element == "module":
            update_module(ref, field, value)
        else:
            print(f"Unknown element type: {element}")


if __name__ == "__main__":
    from csv_helpers import read_csv

    updates = read_csv("tmp/app_updates.csv", as_dict=True)
    batch_update("application", "name", updates)
