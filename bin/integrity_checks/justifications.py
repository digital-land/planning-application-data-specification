from integrity_checks.utils import has_reference_error, print_error

# JUSTIFICATIONS (.md files under user-needs/justification)
# =========================================================
# - id must be present, string, kebab-case, and unique
# - status is one of draft | proposed | accepted | retired
# - need references (need_id or needs list) must point to known needs
# - satisfaction is full | partial
# - confidence is high | medium | low
# - body/content must be non-empty
# - satisfied_by references (datasets/fields) should exist in the specification

VALID_STATUSES = {"draft", "proposed", "accepted", "retired"}
VALID_SATISFACTION = {"full", "partial"}
VALID_CONFIDENCE = {"high", "medium", "low"}


def check_ids(justifications):
    """ID must be string, kebab-case and unique."""
    seen = set()
    has_errors = False
    for just_id, just in justifications.items():
        has_errors |= has_reference_error(just_id, "justification", seen)
        seen.add(just_id)

        fm_id = just.get("id")
        if fm_id and fm_id != just_id:
            print_error(
                "justification",
                just_id,
                f"frontmatter id '{fm_id}' does not match filename key",
            )
            has_errors = True
    return not has_errors


def check_status(justifications):
    """Status must be allowed."""
    has_errors = False
    for just_id, just in justifications.items():
        status = just.get("status")
        if status not in VALID_STATUSES:
            print_error(
                "justification",
                just_id,
                f"invalid status '{status}'; expected one of {sorted(VALID_STATUSES)}",
            )
            has_errors = True
    return not has_errors


def check_need_refs(justifications, needs):
    """need_id or needs list must reference known needs."""
    has_errors = False
    known_needs = set(needs.keys())

    for just_id, just in justifications.items():
        need_id = just.get("need_id")
        need_list = just.get("needs")

        # at least one of need_id/needs should exist
        if not need_id and not need_list:
            print_error(
                "justification",
                just_id,
                "missing need reference (need_id or needs list)",
            )
            has_errors = True
            continue

        # check singular
        if need_id and need_id not in known_needs:
            print_error(
                "justification",
                just_id,
                f"need_id '{need_id}' not found among needs",
            )
            has_errors = True

        # check list
        if need_list is not None:
            if not isinstance(need_list, list):
                print_error(
                    "justification",
                    just_id,
                    f"needs must be a list, got {type(need_list).__name__}",
                )
                has_errors = True
            else:
                for ref in need_list:
                    if ref not in known_needs:
                        print_error(
                            "justification",
                            just_id,
                            f"need reference '{ref}' not found among needs",
                        )
                        has_errors = True
    return not has_errors


def check_satisfaction(justifications):
    """Satisfaction must be full or partial."""
    has_errors = False
    for just_id, just in justifications.items():
        sat = just.get("satisfaction")
        if sat not in VALID_SATISFACTION:
            print_error(
                "justification",
                just_id,
                f"invalid satisfaction '{sat}'; expected one of {sorted(VALID_SATISFACTION)}",
            )
            has_errors = True
    return not has_errors


def check_confidence(justifications):
    """Confidence must be high/medium/low."""
    has_errors = False
    for just_id, just in justifications.items():
        conf = just.get("confidence")
        if conf not in VALID_CONFIDENCE:
            print_error(
                "justification",
                just_id,
                f"invalid confidence '{conf}'; expected one of {sorted(VALID_CONFIDENCE)}",
            )
            has_errors = True
    return not has_errors


def check_body_present(justifications):
    """Body text must be present (outside frontmatter)."""
    has_errors = False
    for just_id, just in justifications.items():
        content = getattr(just, "content", None)
        if content is None:
            # fallback: frontmatter stored as dict with "content"
            content = just.get("content")
        if not content or not str(content).strip():
            print_error("justification", just_id, "body/content is missing or empty")
            has_errors = True
    return not has_errors


def _walk_satisfied_by(node):
    """
    Yield dataset/field references from a satisfied_by structure.
    Supports nested dicts/lists (allOf/anyOf, rule.requires, etc.).
    """
    if isinstance(node, dict):
        ds = node.get("dataset")
        field = node.get("field")
        if ds or field:
            yield ds, field
        # recurse into nested structures
        for key in ["allOf", "anyOf", "requires"]:
            if key in node:
                yield from _walk_satisfied_by(node[key])
        # also dive into values that are dict/list
        for val in node.values():
            if isinstance(val, (dict, list)):
                yield from _walk_satisfied_by(val)
    elif isinstance(node, list):
        for item in node:
            yield from _walk_satisfied_by(item)


def check_satisfied_by_refs(justifications, datasets, fields):
    """Ensure satisfied_by references point to known datasets/fields."""
    has_errors = False
    dataset_ids = set(datasets.keys())
    field_ids = set(fields.keys())
    dataset_field_map = {
        name: {
            f.get("field")
            for f in (dataset.get("fields") or [])
            if isinstance(f, dict) and f.get("field")
        }
        for name, dataset in datasets.items()
    }

    for just_id, just in justifications.items():
        sb = just.get("satisfied_by")
        if not sb:
            # optional but warn about missing satisfied_by
            print(f"Warning in justification '{just_id}': satisfied_by is missing")
            continue
        for ds, field in _walk_satisfied_by(sb):
            if ds and ds not in dataset_ids:
                print_error(
                    "justification",
                    just_id,
                    f"dataset '{ds}' in satisfied_by not found in datasets",
                )
                has_errors = True
            if field and field not in field_ids:
                print_error(
                    "justification",
                    just_id,
                    f"field '{field}' in satisfied_by not found in fields",
                )
                has_errors = True
            if (
                ds
                and field
                and ds in dataset_ids
                and field in field_ids
                and field not in dataset_field_map.get(ds, set())
            ):
                print_error(
                    "justification",
                    just_id,
                    f"field '{field}' is not listed for dataset '{ds}'",
                )
                has_errors = True
    return not has_errors


def check_all(justifications, needs, datasets, fields):
    """Run all justification integrity checks."""
    checks_with_args = [
        (check_ids, [justifications]),
        (check_status, [justifications]),
        (check_need_refs, [justifications, needs]),
        (check_satisfaction, [justifications]),
        (check_confidence, [justifications]),
        (check_body_present, [justifications]),
        (check_satisfied_by_refs, [justifications, datasets, fields]),
    ]

    all_passed = True
    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = check_all({}, {}, {}, {})
    exit(0 if success else 1)
