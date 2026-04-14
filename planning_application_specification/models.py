from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union


@dataclass
class FieldDef:
    ref: str
    name: str
    datatype: str = "string"
    required: bool = False
    description: str = ""
    notes: str = ""
    component: Optional[str] = None
    resolved_component: Optional["ComponentUsage"] = None
    cardinality: str = "1"
    entry_date: Optional[str] = None
    end_date: Optional[str] = None

    @classmethod
    def from_spec(cls, spec: Any) -> "FieldDef":
        if isinstance(spec, FieldDef):
            return spec
        if isinstance(spec, str):
            return cls(ref=spec, name=spec)
        if not isinstance(spec, dict):
            return cls(ref=str(spec), name=str(spec))
        ref = spec.get("field") or spec.get("ref") or ""
        name = spec.get("name") or spec.get("title") or ref
        datatype = spec.get("datatype") or spec.get("type") or "string"
        required = bool(spec.get("required", False))
        description = spec.get("description", "") or ""
        notes = spec.get("notes", "") or ""
        component = spec.get("component")
        cardinality = str(spec.get("cardinality", "1"))
        entry_date = spec.get("entry-date") or spec.get("entry_date")
        end_date = spec.get("end-date") or spec.get("end_date")
        return cls(
            ref=ref,
            name=name,
            datatype=datatype,
            required=required,
            description=description,
            notes=notes,
            component=component,
            cardinality=cardinality,
            entry_date=entry_date,
            end_date=end_date,
        )


@dataclass
class FieldUsage:
    original: FieldDef
    overrides: Dict[str, Any]


@dataclass
class ComponentUsage:
    component: "ComponentDef"
    referenced_by_field: Optional[Union["FieldUsage", FieldDef]] = None


@dataclass
class ComponentDef:
    ref: str
    name: str
    description: str = ""
    items: List[Any] = field(default_factory=list)
    field_usages: List[FieldUsage] = field(default_factory=list)
    component_usages: List["ComponentUsage"] = field(default_factory=list)
    entry_date: Optional[str] = None
    end_date: Optional[str] = None

    @classmethod
    def from_spec(
        cls,
        component_def: Any,
        field_defs: Dict[str, FieldDef],
        component_index: Dict[str, object],
    ) -> "ComponentDef":
        if isinstance(component_def, ComponentDef):
            return component_def
        if isinstance(component_def, str):
            return cls(ref=component_def, name=component_def)
        ref = component_def.get("component") or ""
        name = component_def.get("name") or ref
        description = component_def.get("description", "") or ""
        raw_fields = component_def.get("fields") or []
        items: List[Any] = []

        for field_item in raw_fields:
            field_ref = field_item.get("field")
            original_field_def = field_defs.get(field_ref) if field_defs else None

            if original_field_def:
                field_usage = FieldUsage(
                    original=original_field_def, overrides=field_item
                )
                if original_field_def.component:
                    component_item = dict(
                        component_index.get(original_field_def.component)
                    )
                    if component_item:
                        items.append(
                            ComponentUsage(
                                component=cls.from_spec(
                                    component_item, field_defs, component_index
                                ),
                                referenced_by_field=field_usage,
                            )
                        )
                else:
                    items.append(field_usage)

        field_usages = [item for item in items if isinstance(item, FieldUsage)]
        component_usages = [item for item in items if isinstance(item, ComponentUsage)]

        entry_date = component_def.get("entry-date")
        end_date = component_def.get("end-date")
        return cls(
            ref=ref,
            name=name,
            description=description,
            items=items,
            field_usages=field_usages,
            component_usages=component_usages,
            entry_date=entry_date,
            end_date=end_date,
        )


@dataclass
class ModuleDef:
    ref: str
    name: str
    description: str = ""
    items: List[Any] = field(default_factory=list)
    field_usages: List[FieldUsage] = field(default_factory=list)
    component_usages: List[ComponentUsage] = field(default_factory=list)
    entry_date: Optional[str] = None
    end_date: Optional[str] = None

    @classmethod
    def from_spec(
        cls,
        module_content: Any,
        field_defs: Dict[str, FieldDef],
        component_defs: Dict[str, ComponentDef],
    ) -> "ModuleDef":
        if isinstance(module_content, ModuleDef):
            return module_content
        ref = module_content.get("module") or ""
        name = module_content.get("name") or ""
        description = module_content.get("description") or ""

        raw_fields = module_content.get("fields") or []
        items = resolve_items(raw_fields, field_defs, component_defs)

        field_usages = [item for item in items if isinstance(item, FieldUsage)]
        component_usages = [item for item in items if isinstance(item, ComponentUsage)]

        entry_date = module_content.get("entry-date")
        end_date = module_content.get("end-date")

        return cls(
            ref=ref,
            name=name,
            description=description,
            items=items,
            field_usages=field_usages,
            component_usages=component_usages,
            entry_date=entry_date,
            end_date=end_date,
        )


@dataclass
class DatasetDef:
    dataset: str
    ref: str
    name: str
    description: str = ""
    items: List[Any] = field(default_factory=list)
    field_usages: List[Any] = field(default_factory=list)
    component_usages: List[ComponentUsage] = field(default_factory=list)
    entry_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    @classmethod
    def from_spec(
        cls,
        dataset_content: Any,
        field_defs: Dict[str, FieldDef],
        component_defs: Dict[str, ComponentDef],
    ) -> "DatasetDef":
        if isinstance(dataset_content, DatasetDef):
            return dataset_content

        dataset = dataset_content.get("dataset") or ""
        name = dataset_content.get("name") or dataset
        description = dataset_content.get("description") or ""

        raw_fields = dataset_content.get("fields") or []
        items = resolve_items(raw_fields, field_defs, component_defs)

        component_usages = [
            item for item in items if isinstance(item, ComponentUsage)
        ]

        entry_date = dataset_content.get("entry-date")
        start_date = dataset_content.get("start-date")
        end_date = dataset_content.get("end-date")

        return cls(
            dataset=dataset,
            ref=dataset,
            name=name,
            description=description,
            items=items,
            field_usages=items,
            component_usages=component_usages,
            entry_date=entry_date,
            start_date=start_date,
            end_date=end_date,
        )


@dataclass
class ApplicationDef:
    application: str
    ref: str
    name: str
    description: str = ""
    application_types: List[str] = field(default_factory=list)
    is_combined: bool = False
    extends: Optional[str] = None
    allow_additional_properties: Optional[bool] = False
    synonyms: List[str] = field(default_factory=list)
    legislation: List[str] = field(default_factory=list)
    notes: str = ""
    entry_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    items: List[Any] = field(default_factory=list)
    field_usages: List[FieldUsage] = field(default_factory=list)
    component_usages: List[ComponentUsage] = field(default_factory=list)
    modules: List[str] = field(default_factory=list)
    resolved_modules: List[ModuleDef] = field(default_factory=list)

    @classmethod
    def from_spec(
        cls,
        app_content: Any,
        field_defs: Dict[str, FieldDef],
        component_defs: Dict[str, ComponentDef],
        module_defs: Dict[str, ModuleDef],
    ) -> "ApplicationDef":
        app = app_content.get("application")
        name = app_content.get("name") or app
        description = app_content.get("description") or ""
        extends = app_content.get("extends")
        allow_additional_properties = app_content.get(
            "allow-additional-properties", False
        )
        synonyms = app_content.get("synonyms") or []
        legislation = app_content.get("legislation") or []
        notes = app_content.get("notes") or ""
        entry_date = app_content.get("entry-date")
        start_date = app_content.get("start-date")
        end_date = app_content.get("end-date")

        raw_fields = app_content.get("fields") or []
        items = resolve_items(raw_fields, field_defs, component_defs)

        field_usages = [item for item in items if isinstance(item, FieldUsage)]
        component_usages = [item for item in items if isinstance(item, ComponentUsage)]

        modules = [
            module_defs.get(module["module"]) for module in (app_content.get("modules") or [])
        ]

        return cls(
            application=app,
            ref=app,
            name=name,
            description=description,
            application_types=[app] if app else [],
            is_combined=False,
            extends=extends,
            allow_additional_properties=allow_additional_properties,
            synonyms=synonyms,
            legislation=legislation,
            notes=notes,
            entry_date=entry_date,
            start_date=start_date,
            end_date=end_date,
            items=items,
            field_usages=field_usages,
            component_usages=component_usages,
            modules=modules,
        )


def resolve_items(raw_fields, field_defs, component_defs):
    items = []
    for field_item in raw_fields:
        field_ref = field_item.get("field")
        original_field_def = field_defs.get(field_ref) if field_defs else None

        if original_field_def:
            field_usage = FieldUsage(
                original=original_field_def, overrides=field_item
            )
            if original_field_def.component:
                component_def = component_defs.get(original_field_def.component)
                if component_def:
                    items.append(
                        ComponentUsage(
                            component=component_def,
                            referenced_by_field=field_usage,
                        )
                    )
            else:
                items.append(field_usage)
    return items


# Temporary aliases while the package surface settles.
FieldInstance = FieldUsage
ComponentInstance = ComponentUsage
