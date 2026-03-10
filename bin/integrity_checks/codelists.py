from pathlib import Path

from csv_helpers import read_csv_with_headers
import yaml
from integrity_checks.utils import print_error, print_warning, run_checks
from utils import check_kebab_case


def check_codelist_names(codelists):
    """
    Check rule 1 & 3: codelist attr must be string, kebab-case and unique across all codelists
    """
    seen = set()
    has_errors = False
    for path, meta in codelists.items():
        codelist = meta.get("codelist")
        if not isinstance(codelist, str) or not check_kebab_case(codelist):
            print_error(
                "codelist", path, f"codelist '{codelist}' must be kebab-case string"
            )
            has_errors = True
        if codelist in seen:
            print_error("codelist", path, f"duplicate codelist '{codelist}'")
            has_errors = True
        seen.add(codelist)
    return not has_errors


def check_codelist_source(codelists):
    """
    Check rule 2: source is empty = error, should be either path or url
    """
    has_errors = False
    for path, meta in codelists.items():
        source = meta.get("source", "")
        valid_source = (
            source
            and isinstance(source, str)
            and (source.startswith("http") or source.startswith("data/"))
        )
        if not valid_source:
            print_error(
                "codelist", path, f"source is missing or not a valid url/path: {source}"
            )
            has_errors = True
    return not has_errors


def check_codelist_github_discussion(codelists):
    """
    Check rule 3: warning if github discussion number is empty
    """
    for path, meta in codelists.items():
        if not meta.get("github-discussion"):
            print_warning("codelist", path, "github-discussion is empty")
    return True


def check_codelist_entry_date(codelists):
    """
    Check rule 4: entry-date should not be blank
    """
    has_errors = False
    for path, meta in codelists.items():
        if not meta.get("entry-date"):
            print_error("codelist", path, "entry-date is missing or blank")
            has_errors = True
    return not has_errors


def check_codelist_name_plural(codelists):
    """
    Check rule 9: warn if name or plural is missing or not capitalised correctly
    """
    for path, meta in codelists.items():
        for key in ["name", "plural"]:
            val = meta.get(key)
            if not val:
                print(f"Warning in {path}: {key} is missing")
            elif not val[0].isupper():
                print(f"Warning in {path}: {key} should start with a capital letter")
    return True


def check_codelist_end_date(codelists):
    """
    Check rule 10: warn if end-date is missing (should be present, even if blank)
    """
    for path, meta in codelists.items():
        if "end-date" not in meta:
            print(f"Warning in {path}: end-date is missing")
    return True


def _declared_field_names(meta):
    fields = meta.get("fields", [])
    names = []
    for field in fields:
        if isinstance(field, dict):
            name = field.get("field") or field.get("ref")
        else:
            name = field
        if name:
            names.append(name)
    return names


def _iter_local_csv_codelists(codelists):
    project_root = Path(__file__).resolve().parents[2]
    for path, meta in codelists.items():
        source = meta.get("source")
        if not (
            isinstance(source, str)
            and source.startswith("data/")
            and source.endswith(".csv")
        ):
            continue

        source_path = project_root / source
        if not source_path.exists():
            continue

        try:
            headers, rows = read_csv_with_headers(source_path)
        except Exception:
            continue

        yield path, meta, source, headers, rows


def check_codelist_key_field_present(codelists):
    has_errors = False
    for path, meta, source, headers, _rows in _iter_local_csv_codelists(codelists):
        key_field = meta.get("key-field")
        if key_field and key_field not in headers:
            print_error(
                "codelist",
                path,
                f"key-field '{key_field}' missing from source CSV {source}",
            )
            has_errors = True
    return not has_errors


def check_codelist_blank_keys(codelists):
    has_errors = False
    for path, meta, source, headers, rows in _iter_local_csv_codelists(codelists):
        key_field = meta.get("key-field")
        if not key_field or key_field not in headers:
            continue

        for row_num, row in enumerate(rows, start=2):
            key = (row.get(key_field) or "").strip()
            if not key:
                print_error(
                    "codelist",
                    path,
                    f"blank key-field '{key_field}' in {source} row {row_num}",
                )
                has_errors = True
    return not has_errors


def check_codelist_duplicate_keys(codelists):
    has_errors = False
    for path, meta, source, headers, rows in _iter_local_csv_codelists(codelists):
        key_field = meta.get("key-field")
        if not key_field or key_field not in headers:
            continue

        seen_keys = {}
        for row_num, row in enumerate(rows, start=2):
            key = (row.get(key_field) or "").strip()
            if not key:
                continue
            if key in seen_keys:
                print_error(
                    "codelist",
                    path,
                    f"duplicate key '{key}' in {source} rows {seen_keys[key]} and {row_num}",
                )
                has_errors = True
            else:
                seen_keys[key] = row_num
    return not has_errors


def check_codelist_parent_column(codelists):
    has_errors = False
    for path, meta, source, headers, _rows in _iter_local_csv_codelists(codelists):
        declared_fields = _declared_field_names(meta)
        if "parent" not in declared_fields:
            continue

        if "parent" not in headers:
            print_error(
                "codelist",
                path,
                f"declares a parent field but source CSV {source} does not include a parent column",
            )
            has_errors = True
    return not has_errors


def check_codelist_parent_references(codelists):
    """
    Check local CSV-backed codelists that declare `parent` use valid same-codelist parent references.
    """
    has_errors = False
    for path, meta, source, headers, rows in _iter_local_csv_codelists(codelists):
        declared_fields = _declared_field_names(meta)
        if "parent" not in declared_fields:
            continue

        key_field = meta.get("key-field")
        if not key_field or key_field not in headers or "parent" not in headers:
            continue

        valid_parents = {
            (row.get(key_field) or "").strip()
            for row in rows
            if (row.get(key_field) or "").strip()
        }

        for row_num, row in enumerate(rows, start=2):
            ref = (row.get(key_field) or "").strip()
            parent = (row.get("parent") or "").strip()
            if not parent:
                continue
            if parent == ref:
                print_error(
                    "codelist",
                    path,
                    f"row {row_num} in {source} cannot use itself as parent",
                )
                has_errors = True
            elif parent not in valid_parents:
                print_error(
                    "codelist",
                    path,
                    f"row {row_num} in {source} references unknown parent '{parent}'",
                )
                has_errors = True

    return not has_errors


def check_all(codelists):
    checks_with_args = [
        (check_codelist_names, [codelists]),
        (check_codelist_source, [codelists]),
        (check_codelist_github_discussion, [codelists]),
        (check_codelist_entry_date, [codelists]),
        (check_codelist_name_plural, [codelists]),
        (check_codelist_end_date, [codelists]),
        (check_codelist_key_field_present, [codelists]),
        (check_codelist_blank_keys, [codelists]),
        (check_codelist_duplicate_keys, [codelists]),
        (check_codelist_parent_column, [codelists]),
        (check_codelist_parent_references, [codelists]),
    ]
    return run_checks(checks_with_args)


if __name__ == "__main__":
    check_all()
