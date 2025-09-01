import pytest
from bin.utils import split_field_in_dicts, split_string, to_anchor


@pytest.fixture
def sample_dicts():
    # returned value is recreated for each test (function scope)
    return [{"tags": "a;b", "a-list": ["already", "list"]}, {"tags": ""}]


def test_to_anchor_simple():
    assert to_anchor("Site constraint") == "site-constraint"


def test_to_anchor_non_alnum():
    assert to_anchor("Site: Constraint / Area") == "site-constraint-area"


def test_to_anchor_trims_hyphens():
    assert to_anchor("  --Example!! ") == "example"


def test_to_anchor_empty():
    assert to_anchor("") == ""
    assert to_anchor(None) == ""


def test_split_string_semicolon():
    assert split_string("hh;full") == ["hh", "full"]


def test_split_string_single():
    assert split_string("hh") == ["hh"]


def test_split_string_empty():
    assert split_string("") == []


def test_split_string_other_separator():
    assert split_string("test,string", ",") == ["test", "string"]


def test_split_field_in_dicts_in_place_mutates(sample_dicts):
    data = sample_dicts
    res = split_field_in_dicts(data, "tags", ";", in_place=True)
    assert res is data
    assert data[0]["tags"] == ["a", "b"]


def test_split_field_in_dicts_copy_does_not_mutate_original(sample_dicts):
    data = sample_dicts
    original = [d.copy() for d in data]
    res = split_field_in_dicts(data, "tags", ";", in_place=False)
    # original must be unchanged
    assert data == original
    # result has the split values
    assert res[0]["tags"] == ["a", "b"]
    assert res[1]["tags"] == []


def test_split_field_in_dicts_non_string_value_ignored(sample_dicts):
    data = sample_dicts
    res = split_field_in_dicts(data, "a-list", ";", in_place=False)
    # non-string values should be left as-is
    assert res[0]["a-list"] == ["already", "list"]


def test_split_field_in_dicts_invalid_dicts_type_raises():
    import pytest

    with pytest.raises(TypeError):
        split_field_in_dicts("not-a-list", "no-list")
