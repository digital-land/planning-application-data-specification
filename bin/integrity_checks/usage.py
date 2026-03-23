from pathlib import Path

from csv_helpers import read_csv_with_headers
from integrity_checks.utils import print_error, run_checks
from utils import check_kebab_case


def _declared_field_names(meta):
    names = []
    for field in meta.get("fields", []):
        if isinstance(field, dict):
            name = field.get("field") or field.get("ref")
        else:
            name = field
        if name:
            names.append(name)
    return names


def _source_path(meta):
    source = meta.get("source", "")
    if not (
        isinstance(source, str)
        and source.startswith("data/")
        and source.endswith(".csv")
    ):
        return None

    project_root = Path(__file__).resolve().parents[2]
    return project_root / source


def _iter_local_usage_tables(usage_tables):
    for path, meta in usage_tables.items():
        source_path = _source_path(meta)
        if not source_path or not source_path.exists():
            continue

        headers, rows = read_csv_with_headers(source_path)
        yield path, meta, source_path, headers, rows


def _load_codelist_keys(codelists, codelist_name):
    for _path, meta in codelists.items():
        if meta.get("codelist") != codelist_name:
            continue

        source_path = _source_path(meta)
        if not source_path or not source_path.exists():
            return set()

        headers, rows = read_csv_with_headers(source_path)
        key_field = meta.get("key-field")
        if not key_field or key_field not in headers:
            return set()

        return {
            (row.get(key_field) or "").strip()
            for row in rows
            if (row.get(key_field) or "").strip()
        }

    return set()


def check_usage_names(usage_tables):
    seen = set()
    has_errors = False

    for path, meta in usage_tables.items():
        usage_name = meta.get("data")
        if not isinstance(usage_name, str) or not check_kebab_case(usage_name):
            print_error("usage", path, f"data '{usage_name}' must be kebab-case string")
            has_errors = True
        elif usage_name in seen:
            print_error("usage", path, f"duplicate data '{usage_name}'")
            has_errors = True
        seen.add(usage_name)

    return not has_errors


def check_usage_source_exists(usage_tables):
    has_errors = False

    for path, meta in usage_tables.items():
        source_path = _source_path(meta)
        if not source_path:
            print_error(
                "usage", path, f"source is missing or invalid: {meta.get('source')}"
            )
            has_errors = True
        elif not source_path.exists():
            print_error("usage", path, f"source does not exist: {meta.get('source')}")
            has_errors = True

    return not has_errors


def check_usage_declared_fields_exist(usage_tables):
    has_errors = False

    project_root = Path(__file__).resolve().parents[2]
    for path, meta, source_path, headers, _rows in _iter_local_usage_tables(usage_tables):
        declared_fields = _declared_field_names(meta)
        for field_name in declared_fields:
            if field_name not in headers:
                print_error(
                    "usage",
                    path,
                    f"declared field '{field_name}' missing from source CSV {source_path.relative_to(project_root)}",
                )
                has_errors = True

    return not has_errors


def check_usage_key_field_values(usage_tables):
    has_errors = False

    for path, meta, source_path, headers, rows in _iter_local_usage_tables(usage_tables):
        key_field = meta.get("key-field")
        if not key_field or key_field not in headers:
            continue

        seen = {}
        for row_num, row in enumerate(rows, start=2):
            key = (row.get(key_field) or "").strip()
            if not key:
                print_error(
                    "usage",
                    path,
                    f"blank key-field '{key_field}' in {source_path.name} row {row_num}",
                )
                has_errors = True
                continue
            if key in seen:
                print_error(
                    "usage",
                    path,
                    f"duplicate key '{key}' in {source_path.name} rows {seen[key]} and {row_num}",
                )
                has_errors = True
            else:
                seen[key] = row_num

    return not has_errors


def check_specification_profiles_exist(usage_tables, codelists):
    valid_profiles = _load_codelist_keys(codelists, "specification-profile")
    has_errors = False

    for path, _meta, source_path, headers, rows in _iter_local_usage_tables(usage_tables):
        if "specification-profile" not in headers:
            continue

        for row_num, row in enumerate(rows, start=2):
            profile = (row.get("specification-profile") or "").strip()
            if profile and profile not in valid_profiles:
                print_error(
                    "usage",
                    path,
                    f"unknown specification-profile '{profile}' in {source_path.name} row {row_num}",
                )
                has_errors = True

    return not has_errors


def check_application_types_exist(usage_tables, applications):
    valid_application_types = set(applications.keys())
    has_errors = False

    for path, _meta, source_path, headers, rows in _iter_local_usage_tables(usage_tables):
        if "application-types" not in headers:
            continue

        for row_num, row in enumerate(rows, start=2):
            raw_value = (row.get("application-types") or "").strip()
            if not raw_value:
                continue

            for application_type in raw_value.split(";"):
                application_type = application_type.strip()
                if application_type and application_type not in valid_application_types:
                    print_error(
                        "usage",
                        path,
                        f"unknown application-type '{application_type}' in {source_path.name} row {row_num}",
                    )
                    has_errors = True

    return not has_errors


def check_all(usage_tables, codelists, applications):
    checks_with_args = [
        (check_usage_names, [usage_tables]),
        (check_usage_source_exists, [usage_tables]),
        (check_usage_declared_fields_exist, [usage_tables]),
        (check_usage_key_field_values, [usage_tables]),
        (check_specification_profiles_exist, [usage_tables, codelists]),
        (check_application_types_exist, [usage_tables, applications]),
    ]

    return run_checks(checks_with_args)


if __name__ == "__main__":
    check_all()
