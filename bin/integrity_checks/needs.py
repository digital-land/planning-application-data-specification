from integrity_checks.utils import has_reference_error, print_error

# NEEDS (.md files under user-needs/need)
# =======================================
#
# 1. need identifier must be string, kebab-case and unique
# 2. status is one of draft | proposed | accepted | retired
# 3. priority is one of high | medium | low
# 4. name is a non-empty string
# 5. statement is a non-empty string
# 6. variations, if present, each value should be an identifier for another need
# 7. next_step is optional but if present should be review | rewrite | split | retire


VALID_STATUSES = {"draft", "proposed", "accepted", "retired"}
VALID_PRIORITIES = {"high", "medium", "low"}
VALID_NEXT_STEPS = {"review", "rewrite", "split", "retire"}


def check_need_identifiers(needs):
    """Rule 1: validate need identifier."""
    seen = set()
    has_errors = False
    for need_id, need in needs.items():
        has_errors |= has_reference_error(need_id, "need", seen)
        seen.add(need_id)

        # Ensure frontmatter value matches dict key
        fm_need = need.get("need") or need.get("id")
        if fm_need and fm_need != need_id:
            print_error(
                "need",
                need_id,
                f"frontmatter identifier '{fm_need}' does not match filename key",
            )
            has_errors = True
    return not has_errors


def check_status(needs):
    """Rule 2: status in allowed values."""
    has_errors = False
    for need_id, need in needs.items():
        status = need.get("status")
        if status not in VALID_STATUSES:
            print_error(
                "need",
                need_id,
                f"invalid status '{status}'; expected one of {sorted(VALID_STATUSES)}",
            )
            has_errors = True
    return not has_errors


def check_priority(needs):
    """Rule 3: priority in allowed values."""
    has_errors = False
    for need_id, need in needs.items():
        priority = need.get("priority")
        if priority not in VALID_PRIORITIES:
            print_error(
                "need",
                need_id,
                f"invalid priority '{priority}'; expected one of {sorted(VALID_PRIORITIES)}",
            )
            has_errors = True
    return not has_errors


def check_name(needs):
    """Rule 4: name is non-empty string."""
    has_errors = False
    for need_id, need in needs.items():
        name = need.get("name")
        if not isinstance(name, str) or not name.strip():
            print_error("need", need_id, "name is missing or empty")
            has_errors = True
    return not has_errors


def check_statement(needs):
    """Rule 5: statement is non-empty string."""
    has_errors = False
    for need_id, need in needs.items():
        statement = need.get("statement")
        if not isinstance(statement, str) or not statement.strip():
            print_error("need", need_id, "statement is missing or empty")
            has_errors = True
    return not has_errors


def check_variations(needs):
    """Rule 6: variations reference other needs."""
    has_errors = False
    all_ids = set(needs.keys())
    for need_id, need in needs.items():
        variations = need.get("variations") or []
        if variations is None:
            continue
        if not isinstance(variations, list):
            print_error(
                "need",
                need_id,
                f"variations must be a list of identifiers, got {type(variations).__name__}",
            )
            has_errors = True
            continue
        for var in variations:
            if var not in all_ids:
                print_error(
                    "need",
                    need_id,
                    f"variation '{var}' not found among needs identifiers",
                )
                has_errors = True
    return not has_errors


def check_next_step(needs):
    """Rule 7: next_step is optional but if present must be valid."""
    has_errors = False
    for need_id, need in needs.items():
        next_step = need.get("next_step")
        if next_step is None or next_step == "":
            continue
        if next_step not in VALID_NEXT_STEPS:
            print_error(
                "need",
                need_id,
                f"invalid next_step '{next_step}'; expected one of {sorted(VALID_NEXT_STEPS)}",
            )
            has_errors = True
    return not has_errors


def check_all(needs):
    """Run all need integrity checks."""
    checks_with_args = [
        (check_need_identifiers, [needs]),
        (check_status, [needs]),
        (check_priority, [needs]),
        (check_name, [needs]),
        (check_statement, [needs]),
        (check_variations, [needs]),
        (check_next_step, [needs]),
    ]

    all_passed = True
    for check, args in checks_with_args:
        print(f"\nRunning {check.__name__}...")
        if not check(*args):
            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = check_all({})
    exit(0 if success else 1)
