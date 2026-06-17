from __future__ import annotations

import csv

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .application_types import canonical_application_ref, normalise_application_types
from .applications import resolve_application
from .loader import _resolve_repo_root, load_specification_model
from .models import ApplicationDef, ComponentUsage, FieldDef, FieldUsage


@dataclass(frozen=True)
class SelectionContext:
    specification_profile: Optional[str] = None
    application_type: Optional[str | list[str] | tuple[str, ...] | set[str]] = None

    def application_types(self) -> tuple[str, ...]:
        return normalise_application_types(self.application_type)


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
class FieldUsageMatch:
    container_type: str
    container: object
    usage: FieldUsage


@dataclass(frozen=True)
class FieldUsages:
    modules: tuple[FieldUsageMatch, ...]
    components: tuple[FieldUsageMatch, ...]


@dataclass(frozen=True)
class ComponentUsages:
    fields: tuple[FieldDef, ...]
    modules: tuple[FieldUsageMatch, ...]


@dataclass(frozen=True)
class CodelistUsages:
    fields: tuple[FieldDef, ...]
    modules: tuple[FieldUsageMatch, ...]
    components: tuple[FieldUsageMatch, ...]


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
    source: str
    usage: str
    items: tuple[CodelistItem, ...]

    def applicable(self, selection: SelectionContext | None = None) -> ApplicableCodelist:
        usage_source = self.usage or self.specification._conventional_usage_source(
            self.ref
        )
        if not usage_source:
            return ApplicableCodelist(
                canonical=self,
                items=self.items,
                selection=selection,
                usage_rules_applied=False,
            )

        usage_rows = self.specification._load_csv_rows(usage_source)
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
            source=codelist_meta.get("source", "") or "",
            usage=codelist_meta.get("usage", "") or "",
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

    def application(self, ref: str | list[str]) -> ApplicationDef:
        application = resolve_application(ref, self.tables)
        if not application:
            raise KeyError(f"Unknown application: {ref}")
        if isinstance(application, ApplicationDef):
            return application
        if hasattr(application, "get") and callable(getattr(application, "get")):
            return self._build_application_view(application)
        raise TypeError(f"Unexpected application shape for {ref!r}")

    def applications_with_module(self, ref: str) -> tuple[ApplicationDef, ...]:
        self.module(ref)
        matching_applications = []
        for application in self.applications.values():
            if any(module.ref == ref for module in application.modules):
                matching_applications.append(application)
        return tuple(sorted(matching_applications, key=lambda application: application.ref))

    def field_usages(self, ref: str) -> FieldUsages:
        self.field(ref)
        module_matches = self._collect_field_usage_matches(self.modules.values(), ref, "module")
        component_matches = self._collect_field_usage_matches(
            self.components.values(), ref, "component"
        )
        return FieldUsages(modules=module_matches, components=component_matches)

    def component_usages(self, ref: str) -> ComponentUsages:
        self.component(ref)
        fields = tuple(
            sorted(
                (
                    field
                    for field in self.fields.values()
                    if field.component == ref
                ),
                key=lambda field: field.ref,
            )
        )
        module_matches = self._collect_component_usage_matches(
            self.modules.values(), ref, "module"
        )
        return ComponentUsages(fields=fields, modules=module_matches)

    def codelist_usages(self, ref: str) -> CodelistUsages:
        self.codelist(ref)
        fields = tuple(
            sorted(
                (
                    field
                    for field in self.fields.values()
                    if field.codelist == ref
                ),
                key=lambda field: field.ref,
            )
        )
        module_matches = self._collect_codelist_usage_matches(
            self.modules.values(), ref, "module"
        )
        component_matches = self._collect_codelist_usage_matches(
            self.components.values(), ref, "component"
        )
        return CodelistUsages(
            fields=fields,
            modules=module_matches,
            components=component_matches,
        )

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

    def _conventional_usage_source(self, codelist_ref: str) -> str:
        usage_schema_ref = f"{codelist_ref}-usage"
        usage_schema = self.tables.get("usage", {}).get(usage_schema_ref)
        if not usage_schema:
            return ""
        return usage_schema.get("source", "") or ""

    def _build_application_view(self, application: dict) -> ApplicationDef:
        application_types = application.get("application-types") or []
        if isinstance(application_types, str):
            application_types = [item for item in application_types.split(";") if item]

        if not application_types:
            application_ref = application.get("application") or application.get("ref") or ""
            if application_ref:
                application_types = [application_ref]

        if len(application_types) == 1:
            canonical_application = self.applications.get(application_types[0])
            if canonical_application:
                return canonical_application

        return self._build_combined_application_view(application, application_types)

    def _build_combined_application_view(
        self, application: dict, application_types: list[str]
    ) -> ApplicationDef:
        canonical_ref = canonical_application_ref(application_types)
        member_applications = [
            self.applications[app_type]
            for app_type in application_types
            if app_type in self.applications
        ]
        module_defs = []
        for module_entry in application.get("modules") or []:
            if isinstance(module_entry, str):
                module_ref = module_entry
            elif isinstance(module_entry, dict):
                module_ref = module_entry.get("module")
            else:
                module_ref = None

            if not module_ref:
                continue

            module = self.modules.get(module_ref)
            if module:
                module_defs.append(module)

        items = self._merge_application_items(member_applications)
        field_usages = [item for item in items if isinstance(item, FieldUsage)]
        component_usages = [item for item in items if isinstance(item, ComponentUsage)]

        if member_applications:
            allow_additional_properties = all(
                bool(app.allow_additional_properties) for app in member_applications
            )
        else:
            allow_additional_properties = bool(
                application.get("allow-additional-properties", False)
            )

        return ApplicationDef(
            application=canonical_ref,
            ref=canonical_ref,
            name=application.get("name") or canonical_ref,
            description=application.get("description", "") or "",
            application_types=list(application_types),
            is_combined=len(application_types) > 1,
            notes=application.get("notes", "") or "",
            entry_date=application.get("entry-date"),
            start_date=application.get("start-date"),
            end_date=application.get("end-date"),
            allow_additional_properties=allow_additional_properties,
            items=items,
            field_usages=field_usages,
            component_usages=component_usages,
            modules=module_defs,
        )

    def _merge_application_items(
        self, applications: list[ApplicationDef]
    ) -> list[FieldUsage | ComponentUsage]:
        merged_items = []
        seen_keys = set()

        for application in applications:
            for item in application.items:
                item_key = self._application_item_key(item)
                if item_key in seen_keys:
                    continue
                seen_keys.add(item_key)
                merged_items.append(item)

        return merged_items

    def _application_item_key(self, item: FieldUsage | ComponentUsage) -> tuple:
        if isinstance(item, FieldUsage):
            return ("field", item.original.ref)
        if isinstance(item, ComponentUsage):
            referenced_by_field = item.referenced_by_field
            field_ref = None
            if isinstance(referenced_by_field, FieldUsage):
                field_ref = referenced_by_field.original.ref
            return ("component", item.component.ref, field_ref)
        return ("other", id(item))

    def _row_matches_selection(
        self, row: dict, selection: SelectionContext | None
    ) -> bool:
        if not selection:
            return True

        if selection.specification_profile:
            profile = row.get("specification-profile")
            if profile and profile != selection.specification_profile:
                return False

        selection_application_types = selection.application_types()
        if selection_application_types:
            allowed = set(normalise_application_types(row.get("application-types")))
            if allowed and not any(
                app_type in allowed for app_type in selection_application_types
            ):
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

    def _collect_field_usage_matches(
        self, containers, field_ref: str, container_type: str
    ) -> tuple[FieldUsageMatch, ...]:
        matches = []
        for container in containers:
            usage = self._find_direct_field_usage(container.items, field_ref)
            if usage:
                matches.append(
                    FieldUsageMatch(
                        container_type=container_type,
                        container=container,
                        usage=usage,
                    )
                )
        return tuple(sorted(matches, key=lambda match: match.container.ref))

    def _collect_codelist_usage_matches(
        self, containers, codelist_ref: str, container_type: str
    ) -> tuple[FieldUsageMatch, ...]:
        matches = []
        for container in containers:
            for usage in self._find_direct_codelist_usages(container.items, codelist_ref):
                matches.append(
                    FieldUsageMatch(
                        container_type=container_type,
                        container=container,
                        usage=usage,
                    )
                )
        return tuple(
            sorted(
                matches,
                key=lambda match: (
                    match.container.ref,
                    match.usage.original.ref,
                ),
            )
        )

    def _collect_component_usage_matches(
        self, containers, component_ref: str, container_type: str
    ) -> tuple[FieldUsageMatch, ...]:
        matches = []
        for container in containers:
            usage = self._find_direct_component_field_usage(
                container.items, component_ref
            )
            if usage:
                matches.append(
                    FieldUsageMatch(
                        container_type=container_type,
                        container=container,
                        usage=usage,
                    )
                )
        return tuple(sorted(matches, key=lambda match: match.container.ref))

    def _find_direct_field_usage(self, items, ref: str) -> FieldUsage | None:
        for item in items:
            if isinstance(item, FieldUsage) and item.original.ref == ref:
                return item
        return None

    def _find_direct_component_field_usage(
        self, items, component_ref: str
    ) -> FieldUsage | None:
        for item in items:
            if (
                isinstance(item, ComponentUsage)
                and item.component.ref == component_ref
                and isinstance(item.referenced_by_field, FieldUsage)
            ):
                return item.referenced_by_field
        return None

    def _find_direct_codelist_usages(
        self, items, codelist_ref: str
    ) -> tuple[FieldUsage, ...]:
        return tuple(
            item
            for item in items
            if isinstance(item, FieldUsage)
            and self._field_usage_codelist(item) == codelist_ref
        )

    def _field_usage_codelist(self, usage: FieldUsage) -> str | None:
        return usage.overrides.get("codelist", usage.original.codelist)

    def _usage_applies(
        self, usage: FieldUsage, selection: SelectionContext | None
    ) -> bool:
        applies_if = usage.overrides.get("applies-if")
        if not applies_if or not selection:
            return True
        if not isinstance(applies_if, dict):
            return True

        selection_application_types = selection.application_types()
        if selection_application_types:
            app_type_condition = applies_if.get("application-type")
            if isinstance(app_type_condition, dict):
                allowed = normalise_application_types(app_type_condition.get("in"))
                if allowed:
                    return any(app_type in allowed for app_type in selection_application_types)
        return True

    def _build_resolved_field(
        self,
        field_usage: FieldUsage,
        container_ref: str,
        container_kind: str,
        selection: SelectionContext | None,
    ) -> ResolvedField:
        base = field_usage.original
        resolved_usage = self._build_resolved_usage(field_usage)
        overrides = resolved_usage.overrides
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
            applies_if=resolved_usage.applies_if,
            required_if=resolved_usage.required_if,
            base=base,
            usage=resolved_usage,
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
        resolved_usage = self._build_resolved_usage(referenced_by_field)
        overrides = resolved_usage.overrides

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
            applies_if=resolved_usage.applies_if,
            required_if=resolved_usage.required_if,
            base=base,
            usage=resolved_usage,
            component=component_usage.component,
            container_ref=container_ref,
            container_kind=container_kind,
        )

    def _build_resolved_usage(self, field_usage: FieldUsage) -> ResolvedFieldUsage:
        overrides = field_usage.overrides or {}
        return ResolvedFieldUsage(
            overrides=overrides,
            applies_if=overrides.get("applies-if"),
            required_if=overrides.get("required-if"),
        )
