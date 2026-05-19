#!/usr/bin/env python3
"""Generate documentation for field datatypes used by this specification."""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

FIELD_DIR = Path("specification/field")
OUTPUT_PATH = Path("documentation/field-datatypes.md")
GITHUB_API_URL = (
    "https://api.github.com/repos/digital-land/specification/contents/"
    "content/datatype?ref=main"
)
UPSTREAM_BROWSE_URL = (
    "https://github.com/digital-land/specification/blob/main/content/datatype"
)

LOCAL_DATATYPES = {"boolean", "number", "object", "enum"}

EXAMPLES = {
    "blob": "SGVsbG8=",
    "boolean": "true",
    "curie": "prefix:reference",
    "datetime": "2026-05-19",
    "decimal": "51.5074",
    "enum": "owner",
    "flag": "yes",
    "hash": "sha-256:abc123",
    "integer": "12",
    "json": '{"reference":"abc"}',
    "latitude": "51.5074",
    "longitude": "-0.1278",
    "number": "12.5",
    "object": '{"reference":"abc"}',
    "string": "Example text",
    "text": "Longer free text",
    "url": "https://www.example.com/document.pdf",
    "wkt": "POINT(-0.1278 51.5074)",
}


@dataclass(frozen=True)
class FieldUsage:
    ref: str
    name: str
    datatype: str
    path: Path


@dataclass(frozen=True)
class UpstreamDatatype:
    datatype: str
    name: str
    description: str
    source_url: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse the simple key-value front matter used by specification markdown."""
    if not text.startswith("---\n"):
        return {}, text

    lines = text.splitlines()
    metadata: dict[str, str] = {}
    end_index = None

    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            end_index = index
            break
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip("'\"")
        metadata[key.strip()] = value

    if end_index is None:
        return metadata, ""

    body = "\n".join(lines[end_index + 1 :]).strip()
    return metadata, body


def load_field_usages(field_dir: Path = FIELD_DIR) -> list[FieldUsage]:
    usages: list[FieldUsage] = []
    for path in sorted(field_dir.glob("*.md")):
        metadata, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        datatype = metadata.get("datatype")
        field_ref = metadata.get("field")
        if not datatype or not field_ref:
            continue
        usages.append(
            FieldUsage(
                ref=field_ref,
                name=metadata.get("name") or field_ref,
                datatype=datatype,
                path=path,
            )
        )
    return usages


def group_field_usages(usages: Iterable[FieldUsage]) -> dict[str, list[FieldUsage]]:
    grouped: dict[str, list[FieldUsage]] = defaultdict(list)
    for usage in usages:
        grouped[usage.datatype].append(usage)
    return {
        datatype: sorted(items, key=lambda item: item.ref)
        for datatype, items in grouped.items()
    }


def fetch_json(url: str) -> object:
    request = Request(
        url, headers={"User-Agent": "planning-application-data-specification"}
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"Failed to fetch {url}: {exc}") from exc


def fetch_text(url: str) -> str:
    request = Request(
        url, headers={"User-Agent": "planning-application-data-specification"}
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"Failed to fetch {url}: {exc}") from exc


def extract_description(body: str) -> str:
    paragraphs = [
        paragraph.strip() for paragraph in body.split("\n\n") if paragraph.strip()
    ]
    if not paragraphs:
        return ""
    return " ".join(paragraphs[0].split())


def parse_upstream_datatype(text: str, source_url: str) -> UpstreamDatatype:
    metadata, body = parse_frontmatter(text)
    datatype = metadata.get("datatype") or Path(source_url).stem
    return UpstreamDatatype(
        datatype=datatype,
        name=metadata.get("name") or datatype,
        description=extract_description(body),
        source_url=source_url,
    )


def load_upstream_datatypes(api_url: str = GITHUB_API_URL) -> list[UpstreamDatatype]:
    payload = fetch_json(api_url)
    if not isinstance(payload, list):
        raise RuntimeError(f"Expected a list from {api_url}")

    datatypes: list[UpstreamDatatype] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        name = item.get("name", "")
        download_url = item.get("download_url")
        if not name.endswith(".md") or not download_url:
            continue
        datatypes.append(
            parse_upstream_datatype(fetch_text(download_url), download_url)
        )

    return sorted(datatypes, key=lambda item: item.datatype.lower())


def escape_table_value(value: object) -> str:
    text = str(value).replace("\n", " ").replace("|", r"\|")
    return text


def markdown_table(headers: Sequence[str], rows: Iterable[Sequence[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append(
            "| " + " | ".join(escape_table_value(value) for value in row) + " |"
        )
    return "\n".join(lines)


def markdown_link(text: str, url: str) -> str:
    return f"[{text}]({url})"


def source_for_datatype(
    datatype: str, upstream_index: dict[str, UpstreamDatatype]
) -> str:
    if datatype in upstream_index:
        return "Upstream"
    if datatype in LOCAL_DATATYPES:
        return "Local to this specification"
    return "Unknown / check"


def notes_for_datatype(
    datatype: str, upstream_index: dict[str, UpstreamDatatype]
) -> str:
    if datatype in upstream_index:
        return upstream_index[datatype].description
    if datatype == "boolean":
        return "JSON boolean used in local payload structures."
    if datatype == "number":
        return "JSON number used in local payload structures."
    if datatype == "object":
        return "JSON object used for fields that reference a component."
    if datatype == "enum":
        return "Controlled value from a local codelist."
    return "Not found in upstream datatypes or local datatype conventions."


def build_used_datatypes_rows(
    grouped_usages: dict[str, list[FieldUsage]],
    upstream_datatypes: Sequence[UpstreamDatatype],
) -> list[list[object]]:
    upstream_index = {item.datatype: item for item in upstream_datatypes}
    rows: list[list[object]] = []
    for datatype in sorted(grouped_usages, key=str.lower):
        usages = grouped_usages[datatype]
        example = usages[0]
        rows.append(
            [
                datatype,
                source_for_datatype(datatype, upstream_index),
                len(usages),
                markdown_link(example.name, f"../{example.path.as_posix()}"),
                notes_for_datatype(datatype, upstream_index),
            ]
        )
    return rows


def build_upstream_rows(
    upstream_datatypes: Sequence[UpstreamDatatype],
) -> list[list[object]]:
    rows: list[list[object]] = []
    for datatype in upstream_datatypes:
        source_url = f"{UPSTREAM_BROWSE_URL}/{datatype.datatype}.md"
        rows.append(
            [
                datatype.datatype,
                datatype.description,
                EXAMPLES.get(datatype.datatype, ""),
                markdown_link("planning.data.gov.uk specification", source_url),
            ]
        )
    return rows


def render_document(
    grouped_usages: dict[str, list[FieldUsage]],
    upstream_datatypes: Sequence[UpstreamDatatype],
) -> str:
    used_rows = build_used_datatypes_rows(grouped_usages, upstream_datatypes)
    upstream_rows = build_upstream_rows(upstream_datatypes)

    return "\n".join(
        [
            "# Field datatypes",
            "",
            "This page is generated from the field definitions in this specification and the upstream planning.data.gov.uk datatype definitions.",
            "",
            "Field datatypes should reuse the planning.data.gov.uk datatypes where possible. Datatypes that only exist for this specification's JSON payload structures are marked as local, and datatype values that do not match either source are marked for checking.",
            "",
            "Regenerate this page with `make field-datatypes`.",
            "",
            "## Datatypes used in this specification",
            "",
            markdown_table(
                ["Datatype", "Source", "Field count", "Example field", "Notes"],
                used_rows,
            ),
            "",
            "## Upstream datatypes available to reuse",
            "",
            markdown_table(
                ["Datatype", "Description", "Example", "Source"],
                upstream_rows,
            ),
            "",
        ]
    )


def generate(
    field_dir: Path = FIELD_DIR,
    output_path: Path = OUTPUT_PATH,
    upstream_datatypes: Sequence[UpstreamDatatype] | None = None,
) -> str:
    usages = load_field_usages(field_dir)
    grouped = group_field_usages(usages)
    upstream = (
        list(upstream_datatypes)
        if upstream_datatypes is not None
        else load_upstream_datatypes()
    )
    document = render_document(grouped, upstream)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")
    return document


def main() -> None:
    generate()


if __name__ == "__main__":
    main()
