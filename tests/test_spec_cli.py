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

    result = runner.invoke(spec.cli, ["forms", "hh"])

    assert result.exit_code == 0
    assert "Found 2 matching 2025 forms for application type 'hh':" in result.output
    assert "- Householder application form (form-hh)" in result.output
    assert "https://example.com/form-hh.pdf" in result.output
    assert "- Householder larger homes form (form-hh-large)" in result.output


def test_forms_command_handles_no_matches(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_forms_by_app_type", lambda app_type: [])

    result = runner.invoke(spec.cli, ["forms", "unknown"])

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

    result = runner.invoke(spec.cli, ["form", "form-app-for-pp"])

    assert result.exit_code == 0
    assert "Form: Application for planning permission" in result.output
    assert "Reference: form-app-for-pp" in result.output
    assert "Application types: full, outline-all, outline-some" in result.output
    assert "Document URL: https://example.com/form-app-for-pp.pdf" in result.output


def test_form_command_handles_missing_form(monkeypatch):
    runner = CliRunner()

    monkeypatch.setattr(spec, "get_2025_form", lambda form_ref: None)

    result = runner.invoke(spec.cli, ["form", "missing-form"])

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

    result = runner.invoke(spec.cli, ["form-url", "hh;lbc"])

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

    result = runner.invoke(spec.cli, ["form-url", "lbc;hh"])

    assert result.exit_code == 0
    assert "application-type: hh + lbc" in result.output
    assert "https://example.com/form-hh-lbc.pdf" in result.output


def test_find_application_command_shows_single_application_summary(monkeypatch):
    runner = CliRunner()

    class StubApplication:
        ref = "hh"
        name = "Householder planning application"
        description = "Single application description"
        application_types = ["hh"]
        is_combined = False
        notes = ""
        items = [FieldUsage(original=FieldDef(ref="application", name="Application"), overrides={"required": True})]
        modules = [type("ModuleDef", (), {"ref": "site-details", "name": "Site details"})()]

    class StubSpecification:
        def application(self, application_ref):
            assert application_ref == "hh"
            return StubApplication()

    monkeypatch.setattr(spec, "Specification", type("SpecificationModule", (), {"load": staticmethod(lambda path=None: StubSpecification())}))

    result = runner.invoke(spec.cli, ["find", "application", "hh"])

    assert result.exit_code == 0
    assert "Application: hh" in result.output
    assert "Name: Householder planning application" in result.output
    assert "Description: Single application description" in result.output
    assert "Application types: hh" in result.output
    assert "Combined: no" in result.output
    assert "Application items:" in result.output
    assert "- field: application (required)" in result.output
    assert "Modules:" in result.output
    assert "- site-details: Site details" in result.output


def test_find_application_command_shows_combined_application_summary(monkeypatch):
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
                component=ComponentDef(ref="application", name="Application"),
                referenced_by_field=FieldUsage(
                    original=FieldDef(ref="application", name="Application"),
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

    result = runner.invoke(spec.cli, ["find", "application", "hh;lbc"])

    assert result.exit_code == 0
    assert "Application: hh;lbc" in result.output
    assert "Name: Householder planning permission and listed building consent" in result.output
    assert "Application types: hh, lbc" in result.output
    assert "Combined: yes" in result.output
    assert "Notes: Connected consent case" in result.output
    assert "Application items:" in result.output
    assert "- component: application (via field: application)" in result.output
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

    result = runner.invoke(spec.cli, ["find", "modules-in-application", "hh;lbc"])

    assert result.exit_code == 0
    assert "Modules in application 'hh;lbc' (2):" in result.output
    assert "site-details: Site details" in result.output
    assert "lb-grade: Listed building grade" in result.output


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

    result = runner.invoke(spec.cli, ["module-forms", "agent-contact"])

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

    result = runner.invoke(spec.cli, ["module-forms", "missing-module"])

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

    result = runner.invoke(spec.cli, ["form-modules", "form-app-for-pp"])

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

    result = runner.invoke(spec.cli, ["form-modules", "missing-form"])

    assert result.exit_code == 0
    assert "No analysed 2025 modules found for form 'missing-form'" in result.output


def test_form_analysis_list_command_reuses_forms_output(monkeypatch):
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

    result = runner.invoke(spec.cli, ["form-analysis", "list", "hh"])

    assert result.exit_code == 0
    assert "Found 1 matching 2025 forms for application type 'hh':" in result.output
    assert "- Householder application form (form-hh)" in result.output


def test_form_analysis_modules_command_reuses_module_output(monkeypatch):
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

    result = runner.invoke(spec.cli, ["form-analysis", "modules", "form-app-for-pp"])

    assert result.exit_code == 0
    assert "Found 1 analysed 2025 modules for form 'form-app-for-pp':" in result.output
    assert "- Agent contact details (agent-contact)" in result.output
