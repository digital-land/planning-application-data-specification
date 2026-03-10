#!/usr/bin/env python3
"""Completeness scope calculations for submission-specification coverage."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

# TODO: derive inheritance-only references from application-type parent relationships.
INHERITANCE_ONLY_REFS = {"outline", "ldc", "prior-approval"}
DEFAULT_INPUT = Path("bin/admin_data/2024-application-volumes.csv")


def parse_application_types(value: str) -> list[str]:
    if not value:
        return []
    normalised = value.replace(";", ",")
    return [part.strip() for part in normalised.split(",") if part.strip()]


def parse_volume(value: str) -> int:
    if not value:
        return 0
    value = value.strip()
    if not value:
        return 0
    try:
        return int(float(value))
    except ValueError:
        return 0


def append_note(existing: str, extra: str) -> str:
    existing = (existing or "").strip()
    extra = extra.strip()
    if existing and extra:
        return f"{existing}; {extra}"
    return existing or extra


def in_scope_name(row: dict[str, str], app_types: list[str]) -> str:
    application_name = (row.get("application-name") or "").strip()
    form_name = (row.get("form-name") or "").strip()
    stats_name = (row.get("stats-app-name") or "").strip()
    app_types_display = ",".join(app_types)

    if application_name:
        return application_name
    if form_name:
        return f"Form: {form_name} ({app_types_display})"
    if stats_name:
        return f"PP stats: {stats_name}"
    return f"Application types: {app_types_display}"


def out_scope_name(row: dict[str, str], app_types: list[str]) -> str:
    application_name = (row.get("application-name") or "").strip()
    stats_name = (row.get("stats-app-name") or "").strip()
    app_types_display = ",".join(app_types)

    if application_name:
        return application_name
    if stats_name:
        return f"PP stats: {stats_name}"
    return f"Application types: {app_types_display}"


def calculate_total_volume(items: list[dict[str, Any]]) -> int:
    return sum(int(item.get("volume", 0) or 0) for item in items)


def evaluate_scope(
    input_path: Path, inheritance_only_refs: set[str] | None = None
) -> dict[str, Any]:
    inheritance_only_refs = inheritance_only_refs or INHERITANCE_ONLY_REFS

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    in_scope: list[dict[str, Any]] = []
    out_of_scope: list[dict[str, Any]] = []

    for row in rows:
        app_types = parse_application_types(row.get("applications-types", ""))
        volume = parse_volume(row.get("2024-total", ""))
        form_name = (row.get("form-name") or "").strip()
        notes = (row.get("notes") or "").strip()

        has_form = bool(form_name)
        has_positive_volume = volume > 0
        is_inheritance_only = len(app_types) == 1 and app_types[0] in inheritance_only_refs

        if is_inheritance_only:
            notes = append_note(
                notes,
                "Inheritance-only application type (included in scope but not a standalone submission type)",
            )

        item = {
            "type": "combined" if len(app_types) > 1 else "single",
            "application-types": app_types,
            "volume": volume,
            "notes": notes,
        }

        if has_form or has_positive_volume or is_inheritance_only:
            item["name"] = in_scope_name(row, app_types)
            in_scope.append(item)
        else:
            item["name"] = out_scope_name(row, app_types)
            out_of_scope.append(item)

    total_volume = calculate_total_volume(in_scope + out_of_scope)
    in_scope_volume = calculate_total_volume(in_scope)
    completeness_pct = (in_scope_volume / total_volume * 100) if total_volume else 0.0

    return {
        "summary": {
            "input": str(input_path),
            "total_rows": len(rows),
            "in_scope_rows": len(in_scope),
            "out_of_scope_rows": len(out_of_scope),
            "total_2024_volume": total_volume,
            "in_scope_2024_volume": in_scope_volume,
            "completeness_pct": round(completeness_pct, 2),
            "volume_treatment": "shared",
            "scope_rules": {
                "has_form": "form-name is non-empty",
                "has_positive_volume": "2024-total > 0",
                "inheritance_only_refs": sorted(inheritance_only_refs),
            },
        },
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
    }


def main() -> None:
    result = evaluate_scope(DEFAULT_INPUT)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
