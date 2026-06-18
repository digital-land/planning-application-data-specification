from pathlib import Path

from bin.render_static_site import build_site, parse_args


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

    dataset_page = output_dir / "dataset" / "decision-notice" / "index.html"
    dataset_html = dataset_page.read_text(encoding="utf-8")
    assert 'href="/codelist/decision-maker"' in dataset_html


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
