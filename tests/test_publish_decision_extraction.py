"""Tests for the decision-stage extractor publisher."""

import importlib.util
from pathlib import Path


PUBLISHER_PATH = Path(
    ".codex/skills/decision-stage-extractor/scripts/publish_decision_extraction.py"
)


def load_publisher_module():
    spec = importlib.util.spec_from_file_location("decision_publisher", PUBLISHER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_load_existing_migrates_known_legacy_headers(tmp_path):
    publisher = load_publisher_module()
    path = tmp_path / "planning-application.csv"
    path.write_text(
        "reference,description,application-types,site,received-date,planning-authority,development-scale,planning-performance-agreement,withdrawn-date,linked-applications,document-url,documentation-url\n"
        "2011/0734,Example,full,site-1,2011-03-15,local-authority:HCK,,,,,,\n"
    )
    fields = [
        "reference", "name", "description", "application-types", "site", "received-date",
        "planning-authority", "development-scale", "planning-performance-agreement",
        "withdrawn-date", "linked-applications", "document-url", "documentation-url",
    ]

    assert publisher.load_existing("planning-application", path, fields) == [
        {
            "reference": "2011/0734",
            "name": "",
            "description": "Example",
            "application-types": "full",
            "site": "site-1",
            "received-date": "2011-03-15",
            "planning-authority": "local-authority:HCK",
            "development-scale": "",
            "planning-performance-agreement": "",
            "withdrawn-date": "",
            "linked-applications": "",
            "document-url": "",
            "documentation-url": "",
        }
    ]


def test_load_existing_preserves_site_boundary_when_migrating_to_geometry(tmp_path):
    publisher = load_publisher_module()
    path = tmp_path / "site.csv"
    path.write_text(
        "reference,name,address-text,postcode,description,site-boundary\n"
        "site-1,Example,,,,\"{\"\"type\"\": \"\"Polygon\"\"}\"\n"
    )

    assert publisher.load_existing(
        "site",
        path,
        ["reference", "name", "address-text", "postcode", "description", "geometry"],
    )[0]["geometry"] == '{"type": "Polygon"}'


def test_load_existing_adds_blank_section_106_name(tmp_path):
    publisher = load_publisher_module()
    path = tmp_path / "section-106.csv"
    path.write_text(
        "reference,decision-notice,document-url,documentation-url\n"
        "agreement-1,notice-1,,https://example.com/documents\n"
    )

    assert publisher.load_existing(
        "section-106",
        path,
        ["reference", "name", "decision-notice", "document-url", "documentation-url"],
    ) == [
        {
            "reference": "agreement-1",
            "name": "",
            "decision-notice": "notice-1",
            "document-url": "",
            "documentation-url": "https://example.com/documents",
        }
    ]
