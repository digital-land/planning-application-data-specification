from integrity_checks.utils import has_reference_error, print_error

# DATASETS (.schema.md files)
# ===========================
#
# 1. dataset attr must be string, kebab-case and unique across all datasets
# 2. each field in fields attr must be a field reference in /fields
# 3. every dataset must have entry-date and end-date attrs
# 4. only expected attributes should be present (helps catch typos)


def check_dataset_names(datasets):
    """
    Check rule 1: dataset attr must be string, kebab-case and unique across all datasets
    """
    seen_datasets = set()
    has_errors = False

    for dataset_name, dataset in datasets.items():
        has_errors |= has_reference_error(dataset_name, "dataset", seen_datasets)

        if dataset.get("dataset") and dataset.get("dataset") != dataset_name:
            print_error(
                "dataset",
                dataset_name,
                f"frontmatter dataset '{dataset.get('dataset')}' does not match filename key",
            )
            has_errors = True

        seen_datasets.add(dataset_name)

    return not has_errors


def check_field_references(datasets, fields):
    """
    Check rule 2: each field in fields attr must be a field reference in /fields
    """
    has_errors = False

    for dataset_name, dataset in datasets.items():
        dataset_fields = dataset.get("fields", [])

        for field_def in dataset_fields:
            field_name = field_def.get("field")
            if not field_name:
                print_error(
                    "dataset", dataset_name, "missing field name in fields list"
                )
                has_errors = True
                continue

            if field_name not in fields:
                print_error(
                    "dataset",
                    dataset_name,
                    f"referenced field '{field_name}' not found in field definitions",
                )
                has_errors = True

    return not has_errors


def check_dates(datasets):
    """
    Check rule 3: every dataset must have entry-date and end-date attrs
    """
    has_errors = False

    for dataset_name, dataset in datasets.items():
        if "entry-date" not in dataset:
            print_error("dataset", dataset_name, "missing entry-date")
            has_errors = True
        if "end-date" not in dataset:
            print_error("dataset", dataset_name, "missing end-date")
            has_errors = True

    return not has_errors


def check_attrs(datasets):
    """
    Check rule 4: each dataset has the expected attributes; warn on extras
    """
    has_errors = False

    expected_attrs = {
        "attribution",
        "collection",
        "consideration",
        "dataset",
        "description",
        "end-date",
        "entity-maximum",
        "entity-minimum",
        "entry-date",
        "fields",
        "key-field",
        "licence",
        "name",
        "notes",
        "phase",
        "plural",
        "prefix",
        "realm",
        "replacement-dataset",
        "start-date",
        "themes",
        "typology",
        "version",
        "semantics",
    }

    for dataset_name, dataset in datasets.items():
        # Robustly get keys from dict or frontmatter.Post
        if hasattr(dataset, "keys"):
            keys = dataset.keys()
        elif hasattr(dataset, "metadata"):
            keys = dataset.metadata.keys()
        else:
            keys = []
        missing_attrs = expected_attrs.difference(keys)
        extra_attrs = set(keys).difference(expected_attrs)

        for attr in sorted(missing_attrs):
            print_error("dataset", dataset_name, f"missing attribute '{attr}'")
            has_errors = True

        for attr in sorted(extra_attrs):
            print(f"Warning in dataset '{dataset_name}': unexpected attribute '{attr}'")

    return not has_errors


def check_all(datasets, fields):
    """Run all dataset integrity checks."""
    checks_with_args = [
        (check_dataset_names, [datasets]),
        (check_field_references, [datasets, fields]),
        (check_dates, [datasets]),
        (check_attrs, [datasets]),
    ]

    all_passed = True
    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = check_all()
    exit(0 if success else 1)
