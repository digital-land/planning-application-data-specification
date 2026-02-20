#!/usr/bin/env python3
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "bin"))

import argparse

from csv_helpers import csvs_to_excel, write_csv  # noqa: E402
from loader import load_specification_model  # noqa: E402

OUTPUT_DIR = Path("data/element-index")


def export_fields(model):
    fields = []
    for f in model.get("fields", {}).values():
        fields.append(
            {
                "reference": f.ref,
                "name": f.name,
                "description": f.description,
                "datatype": f.datatype,
                "cardinality": f.cardinality,
                "codelist": getattr(f, "codelist", ""),
                "component": f.component or "",
                "notes": getattr(f, "notes", ""),
                "entry-date": getattr(f, "entry_date", ""),
                "end-date": getattr(f, "end_date", ""),
            }
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(fields, output_file=OUTPUT_DIR / "fields.csv")


def export_modules(model):
    modules = []
    for m in model.get("modules", {}).values():
        modules.append(
            {
                "reference": m.ref,
                "name": m.name,
                "description": m.description,
                "entry-date": getattr(m, "entry_date", ""),
                "end-date": getattr(m, "end_date", ""),
                "field-count": len(getattr(m, "items", []) or []),
            }
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(modules, output_file=OUTPUT_DIR / "modules.csv")


def export_components(model):
    components = []
    for c in model.get("components", {}).values():
        components.append(
            {
                "reference": c.ref,
                "name": c.name,
                "description": c.description,
                "entry-date": getattr(c, "entry_date", ""),
                "end-date": getattr(c, "end_date", ""),
                "field-count": len(getattr(c, "items", []) or []),
            }
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(components, output_file=OUTPUT_DIR / "components.csv")


def export_codelists(model, sort=True):
    codelists = []
    for c in model.get("tables", {}).get("codelist", {}).values():
        codelists.append(
            {
                "reference": c.get("codelist"),
                "name": c.get("name", c.get("codelist")),
                "description": c.get("description", ""),
                "source": c.get("source", ""),
                "key-field": c.get("key-field", ""),
                "entry-date": c.get("entry-date", ""),
                "end-date": c.get("end-date", ""),
            }
        )

    if sort:
        codelists = sorted(codelists, key=lambda c: c.get("reference") or "")

    if codelists:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        write_csv(codelists, output_file=OUTPUT_DIR / "codelists.csv")


def main():
    parser = argparse.ArgumentParser(
        description="Export elements to CSV (and optional Excel)"
    )
    parser.add_argument(
        "--xlsx",
        help="Optional path to write a combined Excel workbook of the CSV outputs",
        default=None,
    )
    parser.add_argument(
        "--no-sort-codelists",
        help="Do not sort codelists alphabetically by reference",
        action="store_true",
    )
    args = parser.parse_args()

    model = load_specification_model()
    export_fields(model)
    export_modules(model)
    export_components(model)
    export_codelists(model, sort=not args.no_sort_codelists)

    if args.xlsx:
        csvs = [
            OUTPUT_DIR / "fields.csv",
            OUTPUT_DIR / "modules.csv",
            OUTPUT_DIR / "components.csv",
            OUTPUT_DIR / "codelists.csv",
        ]
        csvs_to_excel(csvs, args.xlsx)


if __name__ == "__main__":
    main()
