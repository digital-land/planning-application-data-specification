#!/usr/bin/env python3
"""
Fetch organisation datasets and build the planning-authority codelist CSV.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Sequence
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from csv_helpers import write_csv

DATASETS: Sequence[tuple[str, str]] = (
    (
        "local-authority",
        "https://files.planning.data.gov.uk/dataset/local-authority.json",
    ),
    (
        "national-park-authority",
        "https://files.planning.data.gov.uk/dataset/national-park-authority.json",
    ),
    (
        "development-corporation",
        "https://files.planning.data.gov.uk/dataset/development-corporation.json",
    ),
)

OUTPUT_PATH = Path("data/codelist/planning-authority.csv")


ALL_ORGANISATION_DATASETS: Sequence[tuple[str, str]] = DATASETS + (
    (
        "government-organisation",
        "https://files.planning.data.gov.uk/dataset/government-organisation.json",
    ),
    (
        "passenger-transport-executives",
        "https://files.planning.data.gov.uk/dataset/passenger-transport-executive.json",
    ),
)
ORGS_OUTPUT_PATH = Path("data/codelist/organisations.csv")


def fetch_entities(url: str) -> List[dict]:
    """Fetch the JSON payload from the given URL and return the entities list."""
    try:
        with urlopen(url) as response:
            payload = json.load(response)
            entities = payload.get("entities", [])
            if not isinstance(entities, list):
                raise ValueError(f"Invalid 'entities' content from {url}")
            return entities
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"Failed to fetch {url}: {exc}") from exc


def iter_rows() -> Iterable[dict]:
    """Yield rows ready for CSV writing from each dataset."""
    for dataset_name, url in DATASETS:
        entities = fetch_entities(url)
        for entity in entities:
            yield {
                "entity": entity.get("entity", ""),
                "reference": f"{dataset_name}:{entity.get('reference' , '')}",
                "name": entity.get("name", ""),
                "planning-data-reference": entity.get("reference", ""),
                "dataset": entity.get("dataset", dataset_name),
                "prefix": entity.get("prefix", ""),
                "local-planning-authority": entity.get("local-planning-authority", ""),
                "entry-date": entity.get("entry-date", ""),
                "start-date": entity.get("start-date", ""),
                "end-date": entity.get("end-date", ""),
            }


def iter_organisation_rows() -> Iterable[dict]:
    """Yield rows ready for CSV writing from each organisation dataset."""
    for dataset_name, url in ALL_ORGANISATION_DATASETS:
        entities = fetch_entities(url)
        for entity in entities:
            yield {
                "entity": entity.get("entity", ""),
                "reference": f"{dataset_name}:{entity.get('reference' , '')}",
                "name": entity.get("name", ""),
                "planning-data-reference": entity.get("reference", ""),
                "dataset": entity.get("dataset", dataset_name),
                "prefix": entity.get("prefix", ""),
                "entry-date": entity.get("entry-date", ""),
                "start-date": entity.get("start-date", ""),
                "end-date": entity.get("end-date", ""),
            }


def build_planning_authority_csv() -> None:
    rows = list(iter_rows())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(
        rows,
        output_file=str(OUTPUT_PATH),
        first_headers=[
            "entity",
            "reference",
            "name",
            "planning-data-reference",
            "dataset",
            "prefix",
            "local-planning-authority",
        ],
        final_headers=["entry-date", "start-date", "end-date"],
    )


def build_organisations_csv() -> None:
    rows = list(iter_organisation_rows())
    ORGS_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(
        rows,
        output_file=str(ORGS_OUTPUT_PATH),
        first_headers=[
            "entity",
            "reference",
            "name",
            "planning-data-reference",
            "dataset",
            "prefix",
        ],
        final_headers=["entry-date", "start-date", "end-date"],
    )


def main() -> None:
    build_planning_authority_csv()
    build_organisations_csv()


if __name__ == "__main__":
    main()
