import pytest

from bin.render_static_site import (
    build_need_maps,
    extract_dataset_only_refs,
    url_for,
)


def test_url_for_handles_base_url():
    assert url_for("", "/decision-stage") == "/decision-stage"
    assert url_for("http://example.com", "/decision-stage") == "http://example.com/decision-stage"
    # ensure leading slash is added if missing
    assert url_for("", "decision-stage") == "/decision-stage"


def test_extract_dataset_only_refs_filters_out_field_pairs():
    blob = [
        {"dataset": "section-106"},
        {"dataset": "decision-notice", "field": "reference"},
        {"field": "only-field"},
        {"dataset": "site"},
    ]
    assert extract_dataset_only_refs(blob) == ["section-106", "site"]


def test_build_need_maps_dataset_only_mapping():
    needs_data = {
        "need": {},
        "justification": {
            "just-1": {
                "needs": ["dd-need-001"],
                "satisfied_by": [{"dataset": "section-106"}],
            }
        },
    }
    need_to_just, dataset_to_need = build_need_maps(needs_data)
    assert list(need_to_just.keys()) == ["dd-need-001"]
    assert dataset_to_need.get("section-106") is not None
    assert dataset_to_need["section-106"][0]["need"] == "dd-need-001"
    assert dataset_to_need["section-106"][0]["justification"]["needs"] == ["dd-need-001"]


def test_build_need_maps_excludes_dataset_field_pairs():
    needs_data = {
        "need": {},
        "justification": {
            "just-2": {
                "needs": ["dd-need-002"],
                "satisfied_by": [{"dataset": "section-106", "field": "decision-notice"}],
            }
        },
    }
    _, dataset_to_need = build_need_maps(needs_data)
    # dataset+field pairs should not be treated as dataset-only satisfaction
    assert dataset_to_need.get("section-106") is None


def test_build_need_maps_handles_dict_satisfied_by():
    needs_data = {
        "need": {},
        "justification": {
            "just-3": {
                "needs": ["dd-need-003"],
                "satisfied_by": {"dataset": "section-106"},
            }
        },
    }
    _, dataset_to_need = build_need_maps(needs_data)
    assert dataset_to_need.get("section-106") is not None
    assert dataset_to_need["section-106"][0]["need"] == "dd-need-003"
