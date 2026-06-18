from bin.render_static_site import (
    build_codelist_usage_view,
    build_component_usage_view,
    build_field_usage_view,
    build_module_usage_view,
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


def test_build_module_usage_view_uses_package_applications_with_links():
    applications = [
        type(
            "StubApplication",
            (),
            {
                "ref": "full",
                "name": "Full planning permission",
                "is_combined": False,
            },
        )(),
        type(
            "StubApplication",
            (),
            {
                "ref": "hh;lbc",
                "name": "Householder planning permission and listed building consent",
                "is_combined": True,
            },
        )(),
    ]

    class StubSpec:
        def applications_with_module(self, module_ref):
            assert module_ref == "proposal-details"
            return applications

    class StubRenderer:
        def url_for(self, path):
            return f"/base{path}"

    usage = build_module_usage_view(StubSpec(), "proposal-details", StubRenderer())

    assert usage == {
        "applications": [
            {
                "ref": "full",
                "name": "Full planning permission",
                "href": "/base/application-type/full",
                "is_combined": False,
            },
            {
                "ref": "hh;lbc",
                "name": "Householder planning permission and listed building consent",
                "href": "/base/application-type/hh;lbc",
                "is_combined": True,
            },
        ]
    }


def test_build_field_usage_view_uses_direct_modules_and_components_with_links():
    dataset_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubDataset",
                (),
                {"ref": "planning-application", "name": "Planning application"},
            )()
        },
    )()
    module_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubModule",
                (),
                {"ref": "proposal-details", "name": "Proposal details"},
            )()
        },
    )()
    component_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubComponent",
                (),
                {"ref": "site-location", "name": "Site location"},
            )()
        },
    )()
    usages = type(
        "StubFieldUsages",
        (),
        {
            "datasets": [dataset_match],
            "modules": [module_match],
            "components": [component_match],
        },
    )()

    class StubSpec:
        def field_usages(self, field_ref):
            assert field_ref == "description"
            return usages

    class StubRenderer:
        def url_for(self, path):
            return f"/base{path}"

    usage = build_field_usage_view(StubSpec(), "description", StubRenderer())

    assert usage == {
        "datasets": [
            {
                "ref": "planning-application",
                "name": "Planning application",
                "href": "/base/dataset/planning-application",
            }
        ],
        "modules": [
            {
                "ref": "proposal-details",
                "name": "Proposal details",
                "href": "/base/module/proposal-details",
            }
        ],
        "components": [
            {
                "ref": "site-location",
                "name": "Site location",
                "href": "/base/component/site-location",
            }
        ],
    }


def test_build_component_usage_view_uses_fields_and_modules_with_links():
    module_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubModule",
                (),
                {"ref": "applicant-details", "name": "Applicant details"},
            )()
        },
    )()
    usages = type(
        "StubComponentUsages",
        (),
        {
            "fields": [
                type(
                    "StubField",
                    (),
                    {"ref": "applicants", "name": "Applicants"},
                )()
            ],
            "modules": [module_match],
        },
    )()

    class StubSpec:
        def component_usages(self, component_ref):
            assert component_ref == "applicant"
            return usages

    class StubRenderer:
        def url_for(self, path):
            return f"/base{path}"

    usage = build_component_usage_view(StubSpec(), "applicant", StubRenderer())

    assert usage == {
        "fields": [
            {
                "ref": "applicants",
                "name": "Applicants",
                "href": "/base/field/applicants",
            }
        ],
        "modules": [
            {
                "ref": "applicant-details",
                "name": "Applicant details",
                "href": "/base/module/applicant-details",
            }
        ],
    }


def test_build_codelist_usage_view_uses_fields_modules_and_components_with_links():
    module_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubModule",
                (),
                {"ref": "interest-details", "name": "Interest details"},
            )(),
            "usage": type(
                "StubFieldUsage",
                (),
                {"original": type("StubField", (), {"ref": "applicant-interest-type"})()},
            )(),
        },
    )()
    component_match = type(
        "StubContainerUsage",
        (),
        {
            "container": type(
                "StubComponent",
                (),
                {"ref": "waste-management", "name": "Waste management"},
            )(),
            "usage": type(
                "StubFieldUsage",
                (),
                {"original": type("StubField", (), {"ref": "unit-type"})()},
            )(),
        },
    )()
    usages = type(
        "StubCodelistUsages",
        (),
        {
            "fields": [
                type(
                    "StubField",
                    (),
                    {"ref": "applicant-interest-type", "name": "Applicant interest type"},
                )()
            ],
            "modules": [module_match],
            "components": [component_match],
        },
    )()

    class StubSpec:
        def codelist_usages(self, codelist_ref):
            assert codelist_ref == "applicant-interest-type"
            return usages

    class StubRenderer:
        def url_for(self, path):
            return f"/base{path}"

    usage = build_codelist_usage_view(
        StubSpec(), "applicant-interest-type", StubRenderer()
    )

    assert usage == {
        "fields": [
            {
                "ref": "applicant-interest-type",
                "name": "Applicant interest type",
                "href": "/base/field/applicant-interest-type",
            }
        ],
        "modules": [
            {
                "ref": "interest-details",
                "name": "Interest details",
                "href": "/base/module/interest-details",
                "field_ref": "applicant-interest-type",
            }
        ],
        "components": [
            {
                "ref": "waste-management",
                "name": "Waste management",
                "href": "/base/component/waste-management",
                "field_ref": "unit-type",
            }
        ],
    }


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
