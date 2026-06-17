from click.testing import CliRunner

import spec
from planning_application_specification.models import ComponentDef, ComponentUsage, FieldDef, FieldUsage


def test_report_summary_command_prints_loaded_record_counts(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "load_content",
        lambda: {
            "application": {"a": {}, "b": {}},
            "module": {"m1": {}, "m2": {}, "m3": {}},
            "field": {"f1": {}},
            "component": {"c1": {}, "c2": {}},
            "codelist": {"cl1": {}},
            "dataset": {"d1": {}, "d2": {}, "d3": {}, "d4": {}},
            "specification": {"s1": {}},
        },
    )

    result = runner.invoke(spec.cli, ["report", "summary"])

    assert result.exit_code == 0
    assert result.output == (
        "applications: 2\n"
        "modules: 3\n"
        "fields: 1\n"
        "components: 2\n"
        "codelists: 1\n"
        "datasets: 4\n"
        "specifications: 1\n"
    )


def test_report_summary_command_supports_markdown_output(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "load_content",
        lambda: {
            "application": {"a": {}},
            "module": {"m1": {}},
            "field": {"f1": {}, "f2": {}},
            "component": {},
            "codelist": {"cl1": {}, "cl2": {}},
            "dataset": {"d1": {}},
            "specification": {"s1": {}, "s2": {}},
        },
    )

    result = runner.invoke(spec.cli, ["report", "summary", "--markdown"])

    assert result.exit_code == 0
    assert result.output == (
        "# Specification summary\n\n"
        "- **Applications**: 1\n"
        "- **Modules**: 1\n"
        "- **Fields**: 2\n"
        "- **Components**: 0\n"
        "- **Codelists**: 2\n"
        "- **Datasets**: 1\n"
        "- **Specifications**: 2\n"
    )


def test_report_decision_summary_lists_covered_needs(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "load_needs",
        lambda: {
            "need": {
                "need-1": {"need": "need-1", "name": "First need"},
                "need-2": {"need": "need-2", "name": "Second need"},
                "need-3": {"need": "need-3"},
            },
            "justification": {
                "just-1": {"needs": ["need-1", "need-2"]},
                "just-2": {"needs": ["need-2"]},
            },
        },
    )

    result = runner.invoke(spec.cli, ["report", "decision", "summary", "--list"])

    assert result.exit_code == 0
    assert "Decision-stage needs covered by justifications: 2/3" in result.output
    assert "Covered needs:" in result.output
    assert "• need-1: First need (just-1)" in result.output
    assert "• need-2: Second need (just-1, just-2)" in result.output


def test_report_completeness_summary_command_prints_scope_totals(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "calculate_scope_summary",
        lambda input_path: {
            "input": str(input_path),
            "total_rows": 10,
            "in_scope_rows": 7,
            "out_of_scope_rows": 3,
            "total_2024_volume": 1000,
            "in_scope_2024_volume": 900,
            "covered_2024_volume": 750,
            "completeness_pct": 75.0,
        },
    )

    result = runner.invoke(spec.cli, ["report", "completeness", "summary"])

    assert result.exit_code == 0
    assert "Completeness summary" in result.output
    assert "Total rows: 10" in result.output
    assert "In-scope rows: 7" in result.output
    assert "Out-of-scope rows: 3" in result.output
    assert "Total 2024 volume: 1000" in result.output
    assert "In-scope 2024 volume: 900" in result.output
    assert "Volume covered by spec: 750" in result.output
    assert "Completeness: 75.0%" in result.output


def test_forms_command_lists_matching_2025_forms(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_forms_by_app_type",
        lambda app_type: [
            {
                "name": "Householder application form",
                "reference": "form-hh",
                "document-url": "https://example.com/form-hh.pdf",
            },
            {
                "name": "Householder larger homes form",
                "reference": "form-hh-large",
                "document-url": "https://example.com/form-hh-large.pdf",
            },
        ]
        if app_type == "hh"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "list", "hh"])

    assert result.exit_code == 0
    assert "Found 2 matching 2025 forms for application type 'hh':" in result.output
    assert "- Householder application form (form-hh)" in result.output
    assert "https://example.com/form-hh.pdf" in result.output
    assert "- Householder larger homes form (form-hh-large)" in result.output


def test_forms_command_handles_no_matches(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_forms_by_app_type", lambda app_type: [])

    result = runner.invoke(spec.cli, ["analysis", "forms", "list", "unknown"])

    assert result.exit_code == 0
    assert "No 2025 forms found for application type 'unknown'" in result.output


def test_form_command_shows_core_2025_form_details(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_form",
        lambda form_ref: {
            "name": "Application for planning permission",
            "reference": "form-app-for-pp",
            "application-types": ["full", "outline-all", "outline-some"],
            "document-url": "https://example.com/form-app-for-pp.pdf",
        }
        if form_ref == "form-app-for-pp"
        else None,
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "show", "form-app-for-pp"])

    assert result.exit_code == 0
    assert "Form: Application for planning permission" in result.output
    assert "Reference: form-app-for-pp" in result.output
    assert "Application types: full, outline-all, outline-some" in result.output
    assert "Document URL: https://example.com/form-app-for-pp.pdf" in result.output


def test_form_command_handles_missing_form(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_form", lambda form_ref: None)

    result = runner.invoke(spec.cli, ["analysis", "forms", "show", "missing-form"])

    assert result.exit_code == 0
    assert "No 2025 form found with reference 'missing-form'" in result.output


def test_form_url_command_supports_combined_application_type(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_forms_by_app_type",
        lambda application_type: [
            {
                "application-types": ["hh", "lbc"],
                "document-url": "https://example.com/form-hh-lbc.pdf",
            }
        ]
        if application_type == "hh;lbc"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "urls", "hh;lbc"])

    assert result.exit_code == 0
    assert "application-type: hh + lbc" in result.output
    assert "https://example.com/form-hh-lbc.pdf" in result.output


def test_form_url_command_normalises_combined_application_type_order(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_forms_by_app_type",
        lambda application_type: [
            {
                "application-types": ["hh", "lbc"],
                "document-url": "https://example.com/form-hh-lbc.pdf",
            }
        ]
        if application_type == "lbc;hh"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "urls", "lbc;hh"])

    assert result.exit_code == 0
    assert "application-type: hh + lbc" in result.output
    assert "https://example.com/form-hh-lbc.pdf" in result.output


def test_inspect_application_command_shows_single_application_summary(monkeypatch):
    runner = CliRunner()

    class StubApplication:
        ref = "hh"
        name = "Householder planning application"
        description = "Single application description"
        application_types = ["hh"]
        is_combined = False
        notes = ""
        items = [
            FieldUsage(
                original=FieldDef(ref="submission-details", name="Submission details"),
                overrides={"required": True},
            )
        ]
        modules = [type("ModuleDef", (), {"ref": "site-details", "name": "Site details"})()]

    class StubSpecification:
        def application(self, application_ref):
            assert application_ref == "hh"
            return StubApplication()

    monkeypatch.setattr(spec, "Specification", type("SpecificationModule", (), {"load": staticmethod(lambda path=None: StubSpecification())}))

    result = runner.invoke(spec.cli, ["inspect", "application", "hh"])

    assert result.exit_code == 0
    assert "Application: hh" in result.output
    assert "Name: Householder planning application" in result.output
    assert "Description: Single application description" in result.output
    assert "Application types: hh" in result.output
    assert "Combined: no" in result.output
    assert "Application items:" in result.output
    assert "- field: submission-details (required)" in result.output
    assert "Modules:" in result.output
    assert "- site-details: Site details" in result.output


def test_inspect_field_command_shows_canonical_field_summary(monkeypatch):
    runner = CliRunner()

    class StubField:
        ref = "description"
        name = "Description"
        datatype = "string"
        required = True
        cardinality = "1"
        component = None
        description = "Describe the proposal."
        notes = "Keep this concise."
        entry_date = "2026-01-01"
        end_date = ""

    class StubSpecification:
        def field(self, field_ref):
            assert field_ref == "description"
            return StubField()

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "field", "description"])

    assert result.exit_code == 0
    assert "Field: description" in result.output
    assert "Name: Description" in result.output
    assert "Datatype: string" in result.output
    assert "Required: yes" in result.output
    assert "Cardinality: 1" in result.output
    assert "Description: Describe the proposal." in result.output
    assert "Notes: Keep this concise." in result.output
    assert "Entry date: 2026-01-01" in result.output


def test_inspect_module_command_shows_canonical_module_summary(monkeypatch):
    runner = CliRunner()

    module = type(
        "StubModule",
        (),
        {
            "ref": "proposal-details",
            "name": "Proposal details",
            "description": "Information about the proposal.",
            "field_usages": [
                FieldUsage(
                    original=FieldDef(ref="description", name="Description"),
                    overrides={},
                )
            ],
            "component_usages": [
                ComponentUsage(
                    component=ComponentDef(ref="site-area", name="Site area"),
                    referenced_by_field=FieldUsage(
                        original=FieldDef(ref="site-area", name="Site area"),
                        overrides={},
                    ),
                )
            ],
            "entry_date": "2026-01-01",
            "end_date": "",
            "items": [
                FieldUsage(
                    original=FieldDef(ref="description", name="Description"),
                    overrides={},
                ),
                ComponentUsage(
                    component=ComponentDef(ref="site-area", name="Site area"),
                    referenced_by_field=FieldUsage(
                        original=FieldDef(ref="site-area", name="Site area"),
                        overrides={},
                    ),
                ),
            ],
        },
    )()

    class StubSpecification:
        def module(self, module_ref):
            assert module_ref == "proposal-details"
            return module

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "module", "proposal-details"])

    assert result.exit_code == 0
    assert "Module: proposal-details" in result.output
    assert "Name: Proposal details" in result.output
    assert "Description: Information about the proposal." in result.output
    assert "Field usages: 1" in result.output
    assert "Component usages: 1" in result.output
    assert "Entry date: 2026-01-01" in result.output
    assert "Top-level items:" in result.output
    assert "- field: description (Description)" in result.output
    assert "- component: site-area (Site area) (via field: site-area)" in result.output


def test_inspect_component_command_shows_canonical_component_summary(monkeypatch):
    runner = CliRunner()

    component = type(
        "StubComponent",
        (),
        {
            "ref": "site-area",
            "name": "Site area",
            "description": "Measurements for the site.",
            "field_usages": [
                FieldUsage(
                    original=FieldDef(ref="area", name="Area"),
                    overrides={},
                )
            ],
            "component_usages": [],
            "entry_date": "2026-01-01",
            "end_date": "",
            "items": [
                FieldUsage(
                    original=FieldDef(ref="area", name="Area"),
                    overrides={},
                )
            ],
        },
    )()

    class StubSpecification:
        def component(self, component_ref):
            assert component_ref == "site-area"
            return component

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "component", "site-area"])

    assert result.exit_code == 0
    assert "Component: site-area" in result.output
    assert "Name: Site area" in result.output
    assert "Description: Measurements for the site." in result.output
    assert "Field usages: 1" in result.output
    assert "Component usages: 0" in result.output
    assert "Entry date: 2026-01-01" in result.output
    assert "Top-level items:" in result.output
    assert "- field: area (Area)" in result.output


def test_inspect_codelist_command_shows_canonical_codelist_summary(monkeypatch):
    runner = CliRunner()

    codelist = type(
        "StubCodelist",
        (),
        {
            "ref": "tenure-type",
            "name": "Tenure type",
            "description": "Types of housing tenure.",
            "items": [
                type(
                    "StubCodelistItem",
                    (),
                    {
                        "reference": "market-housing",
                        "name": "Market housing",
                        "parent": None,
                    },
                )(),
                type(
                    "StubCodelistItem",
                    (),
                    {
                        "reference": "london-affordable-rent",
                        "name": "London affordable rent",
                        "parent": "affordable-housing",
                    },
                )(),
            ],
        },
    )()

    class StubSpecification:
        def codelist(self, codelist_ref):
            assert codelist_ref == "tenure-type"
            return codelist

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "codelist", "tenure-type"])

    assert result.exit_code == 0
    assert "Codelist: tenure-type" in result.output
    assert "Name: Tenure type" in result.output
    assert "Description: Types of housing tenure." in result.output
    assert "Items: 2" in result.output
    assert "Items preview:" in result.output
    assert "- market-housing: Market housing" in result.output
    assert (
        "- london-affordable-rent: London affordable rent (parent: affordable-housing)"
        in result.output
    )


def test_field_usage_command_uses_canonical_summary_shape(monkeypatch):
    runner = CliRunner()

    usage = type(
        "StubFieldUsageResult",
        (),
        {
            "modules": [
                type(
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
            ],
            "components": [
                type(
                    "StubContainerUsage",
                    (),
                    {
                        "container": type(
                            "StubComponent",
                            (),
                            {"ref": "site-area", "name": "Site area"},
                        )()
                    },
                )()
            ],
        },
    )()

    class StubSpecification:
        def field_usages(self, field_ref):
            assert field_ref == "description"
            return usage

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "uses", "field", "description"])

    assert result.exit_code == 0
    assert "Field: description" in result.output
    assert "Modules: 1" in result.output
    assert "- proposal-details: Proposal details" in result.output
    assert "Components: 1" in result.output
    assert "- site-area: Site area" in result.output


def test_codelist_usage_command_uses_package_query(monkeypatch):
    runner = CliRunner()

    usages = type(
        "StubCodelistUsages",
        (),
        {
            "fields": [
                FieldDef(
                    ref="decision-maker",
                    name="Decision maker",
                    codelist="decision-maker",
                )
            ],
            "modules": [
                type(
                    "StubContainerUsage",
                    (),
                    {
                        "container": type(
                            "StubModule",
                            (),
                            {"ref": "decision-notice", "name": "Decision notice"},
                        )(),
                        "usage": FieldUsage(
                            original=FieldDef(ref="decision-maker", name="Decision maker"),
                            overrides={"field": "decision-maker"},
                        ),
                    },
                )()
            ],
            "components": [
                type(
                    "StubContainerUsage",
                    (),
                    {
                        "container": type(
                            "StubComponent",
                            (),
                            {"ref": "decision-summary", "name": "Decision summary"},
                        )(),
                        "usage": FieldUsage(
                            original=FieldDef(ref="decision-maker", name="Decision maker"),
                            overrides={
                                "field": "decision-maker",
                                "codelist": "decision-maker",
                            },
                        ),
                    },
                )()
            ],
        },
    )()

    class StubSpecification:
        def codelist_usages(self, codelist_ref):
            assert codelist_ref == "decision-maker"
            return usages

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "uses", "codelist", "decision-maker"])

    assert result.exit_code == 0
    assert "Codelist: decision-maker" in result.output
    assert "Fields: 1" in result.output
    assert "- decision-maker: Decision maker" in result.output
    assert "Modules: 1" in result.output
    assert "- decision-notice: Decision notice (field: decision-maker)" in result.output
    assert "Components: 1" in result.output
    assert "- decision-summary: Decision summary (field: decision-maker)" in result.output


def test_codelist_usage_command_handles_no_matches(monkeypatch):
    runner = CliRunner()

    usages = type(
        "StubCodelistUsages",
        (),
        {
            "fields": [],
            "modules": [],
            "components": [],
        },
    )()

    class StubSpecification:
        def codelist_usages(self, codelist_ref):
            assert codelist_ref == "unused-codelist"
            return usages

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(spec.cli, ["inspect", "uses", "codelist", "unused-codelist"])

    assert result.exit_code == 0
    assert "No fields, modules or components found using codelist 'unused-codelist'" in result.output


def test_component_usage_command_uses_canonical_summary_shape(monkeypatch):
    runner = CliRunner()

    usages = type(
        "StubComponentUsages",
        (),
        {
            "fields": [
                FieldDef(ref="floor-area", name="Floor area"),
                FieldDef(ref="site-area", name="Site area"),
            ],
            "modules": [
                type(
                    "StubContainerUsage",
                    (),
                    {
                        "container": type(
                            "StubModule",
                            (),
                            {"ref": "proposal-details", "name": "Proposal details"},
                        )(),
                    },
                )(),
                type(
                    "StubContainerUsage",
                    (),
                    {
                        "container": type(
                            "StubModule",
                            (),
                            {"ref": "site-details", "name": "Site details"},
                        )(),
                    },
                )(),
            ],
        },
    )()

    class StubSpecification:
        def component_usages(self, component_ref):
            assert component_ref == "site-dimensions"
            return usages

    monkeypatch.setattr(
        spec,
        "Specification",
        type(
            "SpecificationModule",
            (),
            {"load": staticmethod(lambda path=None: StubSpecification())},
        ),
    )

    result = runner.invoke(
        spec.cli, ["inspect", "uses", "component", "site-dimensions"]
    )

    assert result.exit_code == 0
    assert "Component: site-dimensions" in result.output
    assert "Fields: 2" in result.output
    assert "- floor-area: Floor area" in result.output
    assert "- site-area: Site area" in result.output
    assert "Modules: 2" in result.output
    assert "- proposal-details: Proposal details" in result.output
    assert "- site-details: Site details" in result.output


def test_inspect_application_command_shows_combined_application_summary(monkeypatch):
    runner = CliRunner()

    class StubApplication:
        ref = "hh;lbc"
        name = "Householder planning permission and listed building consent"
        description = "Combined application description"
        application_types = ["hh", "lbc"]
        is_combined = True
        notes = "Connected consent case"
        items = [
            ComponentUsage(
                component=ComponentDef(ref="submission-details", name="Submission details"),
                referenced_by_field=FieldUsage(
                    original=FieldDef(ref="submission-details", name="Submission details"),
                    overrides={},
                ),
            )
        ]
        modules = [
            type("ModuleDef", (), {"ref": "site-details", "name": "Site details"})(),
            type("ModuleDef", (), {"ref": "lb-grade", "name": "Listed building grade"})(),
        ]

    class StubSpecification:
        def application(self, application_ref):
            assert application_ref == "hh;lbc"
            return StubApplication()

    monkeypatch.setattr(spec, "Specification", type("SpecificationModule", (), {"load": staticmethod(lambda path=None: StubSpecification())}))

    result = runner.invoke(spec.cli, ["inspect", "application", "hh;lbc"])

    assert result.exit_code == 0
    assert "Application: hh;lbc" in result.output
    assert "Name: Householder planning permission and listed building consent" in result.output
    assert "Application types: hh, lbc" in result.output
    assert "Combined: yes" in result.output
    assert "Notes: Connected consent case" in result.output
    assert "Application items:" in result.output
    assert "- component: submission-details (via field: submission-details)" in result.output
    assert "Modules:" in result.output
    assert "- site-details: Site details" in result.output
    assert "- lb-grade: Listed building grade" in result.output


def test_modules_in_application_command_supports_combined_application_type(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "load_content",
        lambda: {
            "module": {
                "site-details": {"name": "Site details"},
                "lb-grade": {"name": "Listed building grade"},
            }
        },
    )
    monkeypatch.setattr(
        spec,
        "get_application_module_refs",
        lambda application_ref, specification: ["site-details", "lb-grade"]
        if application_ref == "hh;lbc"
        else [],
    )

    result = runner.invoke(spec.cli, ["inspect", "uses", "application", "hh;lbc"])

    assert result.exit_code == 0
    assert "Application type: hh;lbc" in result.output
    assert "Modules: 2" in result.output
    assert "- site-details: Site details" in result.output
    assert "- lb-grade: Listed building grade" in result.output


def test_applications_with_module_command_uses_new_inspect_output_shape(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "load_content",
        lambda: {
            "application": {
                "hh": {"name": "Householder planning application"},
                "full": {"name": "Full planning application"},
            }
        },
    )
    monkeypatch.setattr(
        spec,
        "get_applications_with_module",
        lambda module_ref, specification: ["hh", "full"]
        if module_ref == "site-details"
        else [],
    )

    result = runner.invoke(spec.cli, ["inspect", "uses", "module", "site-details"])

    assert result.exit_code == 0
    assert "Module: site-details" in result.output
    assert "Applications: 2" in result.output
    assert "- hh: Householder planning application" in result.output
    assert "- full: Full planning application" in result.output


def test_module_forms_command_lists_analysed_2025_forms(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_forms_for_module",
        lambda module_ref: [
            {
                "name": "Application for planning permission",
                "reference": "form-app-for-pp",
                "document-url": "https://example.com/form-app-for-pp.pdf",
            },
            {
                "name": "Outline application",
                "reference": "form-outline",
                "document-url": "https://example.com/form-outline.pdf",
            },
        ]
        if module_ref == "agent-contact"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "for-module", "agent-contact"])

    assert result.exit_code == 0
    assert "Found 2 analysed 2025 forms for module 'agent-contact':" in result.output
    assert (
        "These results come from the 2025 forms analysis data, not the specification model."
        in result.output
    )
    assert "- Application for planning permission (form-app-for-pp)" in result.output
    assert "- Outline application (form-outline)" in result.output


def test_module_forms_command_handles_no_matches(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_forms_for_module", lambda module_ref: [])

    result = runner.invoke(spec.cli, ["analysis", "forms", "for-module", "missing-module"])

    assert result.exit_code == 0
    assert "No analysed 2025 forms found for module 'missing-module'" in result.output


def test_form_modules_command_lists_analysed_2025_modules(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_modules_for_form",
        lambda form_ref: [
            {"name": "Agent contact details", "reference": "agent-contact"},
            {"name": "Site address", "reference": "site-address"},
        ]
        if form_ref == "form-app-for-pp"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "modules", "form-app-for-pp"])

    assert result.exit_code == 0
    assert "Found 2 analysed 2025 modules for form 'form-app-for-pp':" in result.output
    assert (
        "These results come from the 2025 forms analysis data, not the specification model."
        in result.output
    )
    assert "- Agent contact details (agent-contact)" in result.output
    assert "- Site address (site-address)" in result.output


def test_form_modules_command_handles_no_matches(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_modules_for_form", lambda form_ref: [])

    result = runner.invoke(spec.cli, ["analysis", "forms", "modules", "missing-form"])

    assert result.exit_code == 0
    assert "No analysed 2025 modules found for form 'missing-form'" in result.output


def test_analysis_forms_list_command_reuses_forms_output(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_forms_by_app_type",
        lambda app_type: [
            {
                "name": "Householder application form",
                "reference": "form-hh",
                "document-url": "https://example.com/form-hh.pdf",
            }
        ]
        if app_type == "hh"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "list", "hh"])

    assert result.exit_code == 0
    assert "Found 1 matching 2025 forms for application type 'hh':" in result.output
    assert "- Householder application form (form-hh)" in result.output


def test_analysis_forms_modules_command_reuses_module_output(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(
        spec,
        "get_2025_modules_for_form",
        lambda form_ref: [
            {"name": "Agent contact details", "reference": "agent-contact"}
        ]
        if form_ref == "form-app-for-pp"
        else [],
    )

    result = runner.invoke(spec.cli, ["analysis", "forms", "modules", "form-app-for-pp"])

    assert result.exit_code == 0
    assert "Found 1 analysed 2025 modules for form 'form-app-for-pp':" in result.output
    assert "- Agent contact details (agent-contact)" in result.output
