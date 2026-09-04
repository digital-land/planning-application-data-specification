from pathlib import Path

from bin.render_static_site import build_site, parse_args
from planning_application_specification import Guidance, Specification


def test_render_site_builds_section_106_dataset(tmp_path, monkeypatch):
    # Run build_site against the existing specification as a sanity check.
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    # Ensure we run from project root so relative specs resolve
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    dataset_page = output_dir / "dataset" / "section-106" / "index.html"
    assert dataset_page.exists(), "section-106 dataset page should be rendered"
    html = dataset_page.read_text(encoding="utf-8")
    # Basic smoke checks: title and at least one linked need/justification section
    assert "section 106 agreement" in html
    assert "Needs satisfied by this dataset" in html
    assert (
        'href="/static/vendor/govuk/govuk-frontend-6.4.0.min.css"' in html
    )
    assert "design.planning.data.gov.uk/static/stylesheets/application.css" not in html
    assert 'import { initAll } from "/static/vendor/govuk/' in html
    assert (
        "design.planning.data.gov.uk/static/javascripts/digital-land-frontend.js"
        in html
    )

    govuk_css = (
        output_dir / "static" / "vendor" / "govuk" / "govuk-frontend-6.4.0.min.css"
    ).read_text(encoding="utf-8")
    assert '--govuk-frontend-version:"6.4.0"' in govuk_css
    assert "url(/assets/" not in govuk_css

    application_css = (
        output_dir / "static" / "stylesheets" / "application.css"
    ).read_text(encoding="utf-8")
    assert ".js-enabled .js-hidden" in application_css


def test_render_site_dataset_index_links_to_github_feedback(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    dataset_index = (output_dir / "dataset" / "index.html").read_text(
        encoding="utf-8"
    )
    assert (
        'href="https://github.com/digital-land/planning-application-data-specification/issues/new"'
        in dataset_index
    )


def test_render_site_shows_contextual_field_guidance(tmp_path, monkeypatch):
    package_guidance = Specification.guidance

    def guidance_for_renderer(
        specification,
        *,
        dataset=None,
        module=None,
        component=None,
        field=None,
    ):
        examples = {
            ("site", None, None, None): "Site dataset guidance",
            (None, "proposal-details", None, None): "Proposal module guidance",
            (None, "proposal-details", None, "description"): (
                "Proposal description guidance"
            ),
            (None, None, "site-address", None): "Site address component guidance",
            (None, None, "site-address", "address-text"): (
                "Site address text guidance"
            ),
        }
        content = examples.get((dataset, module, component, field))
        if content:
            return Guidance(content=content)
        return package_guidance(
            specification,
            dataset=dataset,
            module=module,
            component=component,
            field=field,
        )

    monkeypatch.setattr(Specification, "guidance", guidance_for_renderer)

    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    site_page = output_dir / "dataset" / "site" / "index.html"
    html = site_page.read_text(encoding="utf-8")

    guidance_position = html.index("Guidance")
    needs_position = html.index("Needs this field satisfies", guidance_position)
    assert "Former Riverside Mill" in html
    assert guidance_position < needs_position
    assert '<p class="govuk-body"><p>Plain-language name' not in html
    assert (
        '<p class="govuk-body">The <a class="govuk-link" href="#reference">'
        "reference</a> for the site</p>"
    ) in html
    assert "Site dataset guidance" in html

    module_html = (
        output_dir / "module" / "proposal-details" / "index.html"
    ).read_text(encoding="utf-8")
    assert "Proposal module guidance" in module_html
    assert "Proposal description guidance" in module_html

    component_html = (
        output_dir / "component" / "site-address" / "index.html"
    ).read_text(encoding="utf-8")
    assert "Site address component guidance" in component_html
    assert "Site address text guidance" in component_html


def test_render_site_shows_need_satisfied_by_single_field_in_all_of(
    tmp_path, monkeypatch
):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    html = (
        output_dir / "dataset" / "planning-application" / "index.html"
    ).read_text(encoding="utf-8")
    field_start = html.index('id="officer-name"')
    field_end = html.index('id="development-scale"', field_start)
    officer_name_html = html[field_start:field_end]

    assert 'href="/user-need/dd-need-115"' in officer_name_html
    assert "This field helps satisfy need" in officer_name_html
    assert "No needs satisfied by this field" not in officer_name_html


def test_render_site_links_codelists_on_module_and_dataset_detail_pages(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    module_page = output_dir / "module" / "interest-details" / "index.html"
    module_html = module_page.read_text(encoding="utf-8")
    assert 'href="/codelist/applicant-interest-type"' in module_html
    assert ">Allowed values</dt>" in module_html

    dataset_page = output_dir / "dataset" / "decision-notice" / "index.html"
    dataset_html = dataset_page.read_text(encoding="utf-8")
    assert 'href="/codelist/decision-maker"' in dataset_html
    assert ">Allowed values</dt>" in dataset_html
    assert ">Decision maker codelist</a>" in dataset_html
    assert "Codelist:" not in dataset_html

    planning_application_page = (
        output_dir / "dataset" / "planning-application" / "index.html"
    )
    planning_application_html = planning_application_page.read_text(encoding="utf-8")
    assert ">Related dataset</dt>" in planning_application_html
    assert ">Site dataset</a>" in planning_application_html
    assert "Links to dataset:" not in planning_application_html

    component_page = output_dir / "component" / "waste-management" / "index.html"
    component_html = component_page.read_text(encoding="utf-8")
    assert 'href="/codelist/waste-throughput-unit"' in component_html
    assert ">Waste throughput unit codelist</a>" in component_html


def test_render_site_shows_dataset_examples(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    html = (
        output_dir / "dataset" / "planning-application" / "index.html"
    ).read_text(encoding="utf-8")

    assert "Basic planning application" in html
    assert 'data-module="govuk-tabs"' in html
    assert 'class="govuk-tabs__list"' in html
    assert 'class="govuk-tabs__tab"' in html
    assert '<p class="govuk-body"><div class="govuk-tabs' not in html
    assert 'href="#basic-planning-application-table"' in html
    assert 'href="#basic-planning-application-json"' in html
    assert "2026/0123/FUL" in html
    assert "application-types" in html
    assert html.index(">Fields</h2>") < html.index('id="examples"')
    assert html.index('id="examples"') < html.index(
        ">Needs satisfied by this dataset</h2>"
    )
    assert (
        'class="govuk-section-break govuk-section-break--visible '
        'govuk-section-break--l app-strong-section-break"' in html
    )


def test_render_site_shows_complete_householder_example(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    index_html = (output_dir / "example" / "index.html").read_text(
        encoding="utf-8"
    )
    assert "Planning application records" in index_html
    assert (
        'href="/example/planning-application-data/householder-application/"'
        in index_html
    )
    assert "Download the complete example" not in index_html

    detail_path = (
        output_dir
        / "example"
        / "planning-application-data"
        / "householder-application"
        / "index.html"
    )
    detail_html = detail_path.read_text(encoding="utf-8")
    assert "Example householder application" in detail_html
    assert (
        "This example shows a straightforward householder application from "
        "receipt and validation through consultation and a delegated decision."
        in detail_html
    )
    assert 'class="govuk-!-width-two-thirds app-example-introduction"' in detail_html
    assert "confidential supporting information" in detail_html.lower()
    assert 'href="/dataset/planning-application/"' in detail_html
    assert 'href="/dataset/site/"' in detail_html
    assert (
        'href="/example/planning-application-data/'
        'householder-application/example.json" download'
        in detail_html
    )
    assert 'class="app-example-json app-complete-example-json"' in detail_html
    assert 'data-module="govuk-tabs"' not in detail_html
    assert "<table" not in detail_html
    assert "&#34;planning-application&#34;" in detail_html

    source_example = Path(
        "specification/example/planning-application-data/householder-application.json"
    )
    downloaded_example = detail_path.parent / "example.json"
    assert downloaded_example.read_bytes() == source_example.read_bytes()


def test_render_site_shows_submission_examples(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    examples = {
        "full": "full--ex1001.json",
        "outline-some": "outline-some--ex1002.json",
        "reserved-matters": "reserved-matters--ex1003.json",
        "approval-condition": "approval-condition--ex1004.json",
        "advertising": "advertising--ex1005.json",
        "non-material-amendment": "non-material-amendment--ex1006.json",
    }
    index_html = (output_dir / "example" / "index.html").read_text(
        encoding="utf-8"
    )
    assert "Submission payloads" in index_html
    assert index_html.index("Submission payloads") < index_html.index(
        "Planning application records"
    )

    for slug, filename in examples.items():
        example_url = f"/example/submission/{slug}/"
        assert f'href="{example_url}"' in index_html

        detail_path = output_dir / example_url.removeprefix("/") / "index.html"
        detail_html = detail_path.read_text(encoding="utf-8")
        assert 'class="app-example-json app-complete-example-json"' in detail_html
        assert (
            f'href="{example_url}example.json" download' in detail_html
        )
        assert "<table" not in detail_html

        source_path = Path("specification/example/application-type") / filename
        downloaded_path = detail_path.parent / "example.json"
        assert downloaded_path.read_bytes() == source_path.read_bytes()


def test_render_site_shows_requirement_levels_for_datasets_and_public_view(
    tmp_path, monkeypatch
):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    dataset_html = (output_dir / "dataset" / "site" / "index.html").read_text(
        encoding="utf-8"
    )
    public_view_html = (
        output_dir / "view" / "national-public" / "index.html"
    ).read_text(encoding="utf-8")

    documentation_href = (
        "https://github.com/digital-land/planning-application-data-specification/"
        "blob/main/documentation/requirement-levels.md"
    )
    assert "Requirement level" in dataset_html
    assert "Not specified" in dataset_html
    assert f'href="{documentation_href}"' not in dataset_html
    assert "Requirement level" in public_view_html
    assert "Not specified" in public_view_html
    assert f'href="{documentation_href}"' in public_view_html


def test_render_site_shows_where_module_is_used(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    module_page = output_dir / "module" / "proposal-details" / "index.html"
    html = module_page.read_text(encoding="utf-8")

    assert "Where this is used" in html
    assert "This module is used in 14 application types:" in html
    assert 'href="/application-type/hh"' in html
    assert 'href="/application-type/hh;lbc"' in html
    assert ">outline<" not in html


def test_render_site_shows_where_field_is_used(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    field_page = output_dir / "field" / "description" / "index.html"
    html = field_page.read_text(encoding="utf-8")

    assert "Where this is used" in html
    assert "This field is used in" in html
    assert "datasets:" in html
    assert 'href="/dataset/planning-application"' in html
    assert "modules:" in html
    assert 'href="/module/proposal-details"' in html
    assert "components:" in html
    assert 'href="/component/site-location"' in html


def test_render_site_renders_field_notes_as_markdown(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    field_page = output_dir / "field" / "document-url" / "index.html"
    html = field_page.read_text(encoding="utf-8")

    assert 'Use <code class="app-code">document-url</code>' in html
    assert 'href="/field/documentation-url"' in html
    assert '>documentation-url</code></a>' in html
    assert "Use `document-url`" not in html


def test_render_site_shows_where_component_is_used(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    component_page = output_dir / "component" / "applicant" / "index.html"
    html = component_page.read_text(encoding="utf-8")

    assert "Where this is used" in html
    assert "This component is used in 1 field:" in html
    assert 'href="/field/applicants"' in html
    assert "This component is used in 1 module:" in html
    assert 'href="/module/applicant-details"' in html


def test_render_site_shows_where_codelist_is_used(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    codelist_page = output_dir / "codelist" / "applicant-interest-type" / "index.html"
    html = codelist_page.read_text(encoding="utf-8")

    assert "Where this is used" in html
    assert "This codelist is used in 1 field:" in html
    assert 'href="/field/applicant-interest-type"' in html
    assert "This codelist is used in 2 modules:" in html
    assert 'href="/module/interest-details"' in html
    assert 'href="/module/ldc-interest"' in html
    assert "(field: applicant-interest-type)" in html


def test_render_site_uses_local_root_links_when_base_url_is_empty(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    index_html = (output_dir / "index.html").read_text(encoding="utf-8")
    assert 'href="/application-type/"' in index_html
    assert 'href="/planning-application-data-specification/application-type/"' not in index_html

    application_html = (
        output_dir / "application-type" / "full" / "index.html"
    ).read_text(encoding="utf-8")
    assert 'href="/module/agent-details"' in application_html
    assert 'href="/planning-application-data-specification/module/agent-details"' not in application_html

    module_html = (
        output_dir / "module" / "agent-details" / "index.html"
    ).read_text(encoding="utf-8")
    assert 'href="/module"' in module_html
    assert 'href="/submission"' not in module_html


def test_render_site_uses_base_url_for_github_pages_links(tmp_path, monkeypatch):
    output_dir = tmp_path / "site"
    args = parse_args([
        "--output",
        str(output_dir),
        "--base-url",
        "/planning-application-data-specification",
        "--spec-root",
        "specification",
        "--needs-root",
        "user-needs",
    ])
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(args)

    index_html = (output_dir / "index.html").read_text(encoding="utf-8")
    assert 'href="/planning-application-data-specification/application-type/"' in index_html

    application_html = (
        output_dir / "application-type" / "full" / "index.html"
    ).read_text(encoding="utf-8")
    assert (
        'href="/planning-application-data-specification/module/agent-details"'
        in application_html
    )
