from bin.render_static_site import (
    build_need_maps,
    design_decision_feedback_url,
    extract_dataset_only_refs,
    parse_design_decision,
)
from bin.renderer import url_for


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


def test_parse_design_decision_extracts_metadata_and_renders_body(tmp_path):
    decision_path = tmp_path / "0012-use-a-controlled-list.md"
    decision_path.write_text(
        "## Decision: Use a controlled list\n\n"
        "**Date:** 2026-04-14  \n"
        "**Status:** Proposed  \n\n"
        "**Context:**\n\n"
        "Some context.\n",
        encoding="utf-8",
    )

    decision = parse_design_decision(decision_path)

    assert decision["decision_id"] == "0012"
    assert decision["slug"] == "0012-use-a-controlled-list"
    assert decision["title"] == "Use a controlled list"
    assert decision["date"] == "2026-04-14"
    assert decision["status"] == "Proposed"
    assert "Decision: Use a controlled list" not in decision["body"]
    assert "2026-04-14" not in decision["body"]
    assert '<p class="govuk-body"><strong>Context:</strong></p>' in decision["body"]


def test_design_decision_feedback_url_includes_decision_number_and_title():
    result = design_decision_feedback_url(
        {
            "decision_id": "0012",
            "title": "Use a controlled list for combined application types",
        }
    )

    assert result == (
        "https://github.com/digital-land/planning-application-data-specification/"
        "issues/new?title=%5B0012%5D%20Feedback%20on%20design%20decision%3A%20"
        "Use%20a%20controlled%20list%20for%20combined%20application%20types"
    )
