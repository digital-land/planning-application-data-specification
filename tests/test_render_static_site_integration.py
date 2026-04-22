import os
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

    dataset_page = output_dir / "decision-stage" / "dataset" / "section-106" / "index.html"
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

    module_page = output_dir / "submission" / "module" / "interest-details" / "index.html"
    module_html = module_page.read_text(encoding="utf-8")
    assert 'href="/codelist/applicant-interest-type"' in module_html

    dataset_page = output_dir / "decision-stage" / "dataset" / "decision-notice" / "index.html"
    dataset_html = dataset_page.read_text(encoding="utf-8")
    assert 'href="/codelist/decision-maker"' in dataset_html
