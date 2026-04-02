from click.testing import CliRunner

import spec


def test_summary_command_prints_loaded_record_counts(monkeypatch):
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

    result = runner.invoke(spec.cli, ["summary"])

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


def test_summary_command_supports_markdown_output(monkeypatch):
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

    result = runner.invoke(spec.cli, ["summary", "--markdown"])

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
