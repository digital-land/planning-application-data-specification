from pathlib import Path

from generate_info_model import generate_module
from loader import load_content
from utils import save_string_to_file

OUTPUT_DIR = "generated"
INFO_MODULE_OUTPUT_DIR = f"{OUTPUT_DIR}/info_modules"


def build():
    # check output_dir exists, if not make it
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    # load specification data
    specification = load_content()
    # check INFO_MODULE_OUTPUT_DIR exists, if not make it
    Path(INFO_MODULE_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    # loop over modules and generate markdown files, placing generated markdown in INFO_MODULE_OUTPUT_DIR
    modules = specification.get("module", {})
    for module_ref, module_def in modules.items():
        print(f"Generating info model for: {module_def['name']}")
        # generate markdown for each module
        md = generate_module(module_ref, specification)
        # filenames should be {module['module']}.md
        out_path = f"{INFO_MODULE_OUTPUT_DIR}/module/{module_ref}.md"
        save_string_to_file(md, out_path)


if __name__ == "__main__":
    print("Running build script...")
    build()
    print("Build script completed.")
