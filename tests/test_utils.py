from bin.utils import to_anchor


def test_to_anchor_simple():
    assert to_anchor("Site constraint") == "site-constraint"


def test_to_anchor_non_alnum():
    assert to_anchor("Site: Constraint / Area") == "site-constraint-area"


def test_to_anchor_trims_hyphens():
    assert to_anchor("  --Example!! ") == "example"


def test_to_anchor_empty():
    assert to_anchor("") == ""
    assert to_anchor(None) == ""
