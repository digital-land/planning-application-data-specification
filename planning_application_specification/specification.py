from __future__ import annotations

import csv

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .loader import _resolve_repo_root, load_specification_model
from .models import ComponentUsage, FieldUsage


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


@dataclass(frozen=True)
class ResolvedFieldUsage:
    overrides: dict
    applies_if: dict | list | None
    required_if: dict | list | None


@dataclass(frozen=True)
class ResolvedField:
    ref: str
    name: str
    description: str
    datatype: str
    required: bool
    notes: str
    component: Optional[str]
    cardinality: str
    applies: bool
    applies_if: dict | list | None
    required_if: dict | list | None
    base: object
    usage: ResolvedFieldUsage
    container_ref: str
    container_kind: str


@dataclass(frozen=True)
class ResolvedComponentReference:
    ref: str
    name: str
    description: str
    datatype: str
    required: bool
    notes: str
    component_ref: str
    cardinality: str
    applies: bool
    applies_if: dict | list | None
    required_if: dict | list | None
    base: object
    usage: ResolvedFieldUsage
    component: object
    container_ref: str
    container_kind: str


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

    def field(self, ref: str):
        field = self.fields.get(ref)
        if not field:
            raise KeyError(f"Unknown field: {ref}")
        return field

    def component(self, ref: str):
        component = self.components.get(ref)
        if not component:
            raise KeyError(f"Unknown component: {ref}")
        return component

    def module(self, ref: str):
        module = self.modules.get(ref)
        if not module:
            raise KeyError(f"Unknown module: {ref}")
        return module

    def resolve_field(
        self,
        ref: str,
        module: str | None = None,
        component: str | None = None,
        selection: SelectionContext | None = None,
    ) -> ResolvedField:
        if not module and not component:
            raise ValueError("resolve_field(...) requires module=... or component=...")

        if module:
            module_def = self.module(module)
            if component:
                component_usage = self._find_component_usage(module_def.items, component)
                if not component_usage:
                    raise KeyError(
                        f"Component '{component}' not found in module '{module}'"
                    )
                field_usage = self._find_field_usage(component_usage.component.items, ref)
                if not field_usage:
                    raise KeyError(
                        f"Field '{ref}' not found in component '{component}' within module '{module}'"
                    )
                return self._build_resolved_field(
                    field_usage=field_usage,
                    container_ref=component,
                    container_kind="component",
                    selection=selection,
                )

            field_usage = self._find_field_usage(module_def.items, ref)
            if not field_usage:
                raise KeyError(f"Field '{ref}' not found in module '{module}'")
            return self._build_resolved_field(
                field_usage=field_usage,
                container_ref=module,
                container_kind="module",
                selection=selection,
            )

        component_def = self.component(component)
        field_usage = self._find_field_usage(component_def.items, ref)
        if not field_usage:
            raise KeyError(f"Field '{ref}' not found in component '{component}'")
        return self._build_resolved_field(
            field_usage=field_usage,
            container_ref=component,
            container_kind="component",
            selection=selection,
        )

    def resolve_container_items(
        self,
        module: str | None = None,
        component: str | None = None,
        selection: SelectionContext | None = None,
    ) -> tuple[ResolvedField | ResolvedComponentReference, ...]:
        if bool(module) == bool(component):
            raise ValueError(
                "resolve_container_items(...) requires exactly one of module=... or component=..."
            )

        if module:
            container_def = self.module(module)
            container_ref = module
            container_kind = "module"
        else:
            container_def = self.component(component)
            container_ref = component
            container_kind = "component"

        resolved_items = []

        for item in container_def.items:
            if isinstance(item, FieldUsage):
                resolved_items.append(
                    self._build_resolved_field(
                        field_usage=item,
                        container_ref=container_ref,
                        container_kind=container_kind,
                        selection=selection,
                    )
                )
            elif isinstance(item, ComponentUsage):
                resolved_items.append(
                    self._build_resolved_component_reference(
                        component_usage=item,
                        container_ref=container_ref,
                        container_kind=container_kind,
                        selection=selection,
                    )
                )

        return tuple(resolved_items)

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

    def _find_field_usage(self, items, ref: str) -> FieldUsage | None:
        for item in items:
            if isinstance(item, FieldUsage) and item.original.ref == ref:
                return item
            if isinstance(item, ComponentUsage):
                match = self._find_field_usage(item.component.items, ref)
                if match:
                    return match
        return None

    def _find_component_usage(self, items, component_ref: str) -> ComponentUsage | None:
        for item in items:
            if isinstance(item, ComponentUsage):
                if item.component.ref == component_ref:
                    return item
                match = self._find_component_usage(item.component.items, component_ref)
                if match:
                    return match
        return None

    def _usage_applies(
        self, usage: FieldUsage, selection: SelectionContext | None
    ) -> bool:
        applies_if = usage.overrides.get("applies-if")
        if not applies_if or not selection:
            return True
        if not isinstance(applies_if, dict):
            return True

        if selection.application_type:
            app_type_condition = applies_if.get("application-type")
            if isinstance(app_type_condition, dict):
                allowed = app_type_condition.get("in")
                if isinstance(allowed, list):
                    return selection.application_type in allowed
        return True

    def _build_resolved_field(
        self,
        field_usage: FieldUsage,
        container_ref: str,
        container_kind: str,
        selection: SelectionContext | None,
    ) -> ResolvedField:
        base = field_usage.original
        overrides = field_usage.overrides or {}
        applies_if = overrides.get("applies-if")
        required_if = overrides.get("required-if")
        return ResolvedField(
            ref=base.ref,
            name=overrides.get("name") or base.name,
            description=overrides.get("description") or base.description,
            datatype=overrides.get("datatype") or base.datatype,
            required=overrides.get("required", base.required),
            notes=overrides.get("notes") or base.notes,
            component=overrides.get("component", base.component),
            cardinality=str(overrides.get("cardinality", base.cardinality)),
            applies=self._usage_applies(field_usage, selection),
            applies_if=applies_if,
            required_if=required_if,
            base=base,
            usage=ResolvedFieldUsage(
                overrides=overrides,
                applies_if=applies_if,
                required_if=required_if,
            ),
            container_ref=container_ref,
            container_kind=container_kind,
        )

    def _build_resolved_component_reference(
        self,
        component_usage: ComponentUsage,
        container_ref: str,
        container_kind: str,
        selection: SelectionContext | None,
    ) -> ResolvedComponentReference:
        referenced_by_field = component_usage.referenced_by_field
        if not isinstance(referenced_by_field, FieldUsage):
            raise ValueError("Component usage is missing the referencing field usage")

        base = referenced_by_field.original
        overrides = referenced_by_field.overrides or {}
        applies_if = overrides.get("applies-if")
        required_if = overrides.get("required-if")

        return ResolvedComponentReference(
            ref=base.ref,
            name=overrides.get("name") or base.name,
            description=overrides.get("description") or base.description,
            datatype=overrides.get("datatype") or base.datatype,
            required=overrides.get("required", base.required),
            notes=overrides.get("notes") or base.notes,
            component_ref=component_usage.component.ref,
            cardinality=str(overrides.get("cardinality", base.cardinality)),
            applies=self._usage_applies(referenced_by_field, selection),
            applies_if=applies_if,
            required_if=required_if,
            base=base,
            usage=ResolvedFieldUsage(
                overrides=overrides,
                applies_if=applies_if,
                required_if=required_if,
            ),
            component=component_usage.component,
            container_ref=container_ref,
            container_kind=container_kind,
        )
