from click.testing import CliRunner

import spec


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
