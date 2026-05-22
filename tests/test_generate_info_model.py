from loader import load_content
from generate_info_model import generate_application, generate_module


def test_generate_module_uses_resolved_field_name_for_top_level_rows():
    specification = load_content()

    module_markdown = generate_module("desc-proposed-works-lb-ldc", specification)

    assert (
        "| description | Description of Proposed Works |" in module_markdown
    )


def test_generate_module_keeps_component_reference_rows():
    specification = load_content()

    module_markdown = generate_module("tree-work-details", specification)

    assert "| tree-details | Tree details[]{} |" in module_markdown


def test_generate_module_keeps_component_table_application_conditions():
    specification = load_content()

    module_markdown = generate_module("tree-work-details", specification)

    assert "reason | Reason | Explain the reason for the work | MAY |  | consent-under-tpo" in module_markdown


def test_generate_module_keeps_validation_rules_section():
    specification = load_content()

    module_markdown = generate_module("con-remove-vary", specification)

    assert "**Validation rules**" in module_markdown
    assert (
        "- Reason must explain why the applicant wishes condition(s) to be removed or changed"
        in module_markdown
    )


def test_generate_application_keeps_application_field_codelists_and_rules():
    specification = load_content()

    application_markdown = generate_application("advertising", specification)

    assert "application-types | Application types[] |" in application_markdown
    assert "Select from the **application-type** enum" in application_markdown
    assert "**Validation rules**" in application_markdown
    assert "- submission-reference must identify the submitted payload" in application_markdown


def test_generate_application_keeps_required_codelist_section():
    specification = load_content()

    application_markdown = generate_application("advertising", specification)

    assert "## Required codelists" in application_markdown
    assert "### Advertisement type" in application_markdown
    assert "| fascia | Fascia |" in application_markdown
