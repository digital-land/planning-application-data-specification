from integrity_checks.utils import has_reference_error, print_error

# SPECIFICATIONS (.schema.md files in specification/)
# ==================================================
#
# 1. specification attr must be string, kebab-case and unique across all specifications
# 2. each dataset listed must exist in dataset definitions
# 3. every field listed under a dataset must be defined on that dataset


def check_specification_names(specifications):
    """
    Check rule 1: specification attr must be string, kebab-case and unique
    """
    seen_specifications = set()
    has_errors = False

    for specification_name, specification in specifications.items():
        has_errors |= has_reference_error(
            specification_name, "specification", seen_specifications
        )
        seen_specifications.add(specification_name)

    return not has_errors


def check_datasets_exist(specifications, datasets):
    """
    Check rule 2: each dataset listed must exist in dataset definitions
    """
    has_errors = False

    for specification_name, specification in specifications.items():
        for dataset in specification.get("datasets", []):
            dataset_name = dataset.get("dataset")
            if not dataset_name:
                print_error(
                    "specification",
                    specification_name,
                    "dataset entry missing dataset attribute",
                )
                has_errors = True
                continue
            if dataset_name not in datasets:
                print_error(
                    "specification",
                    specification_name,
                    f"dataset '{dataset_name}' not found in dataset definitions",
                )
                has_errors = True

    return not has_errors


def check_dataset_fields(specifications, datasets):
    """
    Check rule 3: every field listed under a dataset must be defined on that dataset
    """
    has_errors = False

    for specification_name, specification in specifications.items():
        for dataset in specification.get("datasets", []):
            dataset_name = dataset.get("dataset")
            if not dataset_name or dataset_name not in datasets:
                # handled in check_datasets_exist
                continue

            dataset_definition = datasets.get(dataset_name, {})
            defined_fields = {
                field.get("field") for field in dataset_definition.get("fields", [])
            }

            for field in dataset.get("fields", []):
                field_name = field.get("field")
                if not field_name:
                    print_error(
                        "specification",
                        specification_name,
                        f"dataset '{dataset_name}' has field entry missing field attribute",
                    )
                    has_errors = True
                    continue
                if field_name not in defined_fields:
                    print_error(
                        "specification",
                        specification_name,
                        f"field '{field_name}' not defined in dataset '{dataset_name}'",
                    )
                    has_errors = True

    return not has_errors


def check_all(specifications, datasets):
    """Run all specification integrity checks."""
    checks_with_args = [
        (check_specification_names, [specifications]),
        (check_datasets_exist, [specifications, datasets]),
        (check_dataset_fields, [specifications, datasets]),
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
