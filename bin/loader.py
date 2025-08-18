from glob import glob

import frontmatter

tables = {
    "application": {},
    "codelist": {},
    "component": {},
    "field": {},
    "module": {},
    # "planning-requirement": {},
}


def load_table_content(table):
    file_path = "*.md"
    if table in ["application", "module", "codelist"]:
        file_path = "*.schema.md"

    for path in glob(f"specification/{table}/{file_path}"):
        post = frontmatter.load(path)
        tables[table][post[table]] = post


def load_content():
    for table in tables.keys():
        load_table_content(table)
    return tables


if __name__ == "__main__":
    tables = load_content()
    print(tables["application"].keys())
