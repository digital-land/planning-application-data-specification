from __future__ import annotations

import csv

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .loader import _resolve_repo_root, load_specification_model


@dataclass(frozen=True)
class SelectionContext:
    specification_profile: Optional[str] = None
    application_type: Optional[str] = None


@dataclass(frozen=True)
class CodelistItem:
    reference: str
    name: str
    description: str = ""
    notes: str = ""
    parent: Optional[str] = None
    row: dict | None = None


@dataclass(frozen=True)
class ApplicableCodelist:
    canonical: "Codelist"
    items: tuple[CodelistItem, ...]
    selection: SelectionContext | None
    usage_rules_applied: bool


@dataclass
class Codelist:
    specification: "Specification"
    ref: str
    name: str
    description: str
    items: tuple[CodelistItem, ...]

    def applicable(self, selection: SelectionContext | None = None) -> ApplicableCodelist:
        usage_schema_ref = f"{self.ref}-usage"
        usage_schema = self.specification.tables.get("data", {}).get(usage_schema_ref)
        if not usage_schema:
            return ApplicableCodelist(
                canonical=self,
                items=self.items,
                selection=selection,
                usage_rules_applied=False,
            )

        usage_rows = self.specification._load_csv_rows(usage_schema["source"])
        item_key = self.ref
        allowed_refs = set()
        for row in usage_rows:
            if not self.specification._row_matches_selection(row, selection):
                continue
            item_ref = row.get(item_key)
            if item_ref:
                allowed_refs.add(item_ref)

        applicable_items = tuple(
            item for item in self.items if item.reference in allowed_refs
        )
        return ApplicableCodelist(
            canonical=self,
            items=applicable_items,
            selection=selection,
            usage_rules_applied=True,
        )


@dataclass
class Specification:
    source_path: Path
    tables: dict
    modules: dict
    components: dict
    applications: dict
    fields: dict

    @classmethod
    def load(cls, path: str | Path | None = None) -> "Specification":
        source_path = _resolve_repo_root(path)
        model = load_specification_model(source_path)
        return cls(
            source_path=source_path,
            tables=model["tables"],
            modules=model["modules"],
            components=model["components"],
            applications=model["applications"],
            fields=model["fields"],
        )

    def codelist(self, ref: str) -> Codelist:
        codelist_meta = self.tables.get("codelist", {}).get(ref)
        if not codelist_meta:
            raise KeyError(f"Unknown codelist: {ref}")

        rows = self._load_csv_rows(codelist_meta["source"])
        items = tuple(
            CodelistItem(
                reference=row.get("reference", ""),
                name=row.get("name", "") or row.get("reference", ""),
                description=row.get("description", "") or "",
                notes=row.get("notes", "") or "",
                parent=row.get("parent") or None,
                row=row,
            )
            for row in rows
            if row.get("reference")
        )
        return Codelist(
            specification=self,
            ref=ref,
            name=codelist_meta.get("name", ref),
            description=codelist_meta.get("description", "") or "",
            items=items,
        )

    def _load_csv_rows(self, relative_path: str) -> list[dict]:
        csv_path = self.source_path / relative_path
        with csv_path.open(newline="", encoding="utf-8") as csv_file:
            return list(csv.DictReader(csv_file))

    def _row_matches_selection(
        self, row: dict, selection: SelectionContext | None
    ) -> bool:
        if not selection:
            return True

        if selection.specification_profile:
            profile = row.get("specification-profile")
            if profile and profile != selection.specification_profile:
                return False

        if selection.application_type:
            app_types = row.get("application-types")
            if app_types:
                allowed = {value.strip() for value in app_types.split(";") if value.strip()}
                if selection.application_type not in allowed:
                    return False

        return True
