from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class FieldDef:
    ref: str
    name: str
    datatype: str = "string"
    required: bool = False
    description: str = ""
    notes: str = ""
    # If this field is an object that references a component, `component` will
    # contain the component ref (string) from the spec. After resolving, the
    # `resolved_component` attribute may hold a ComponentInstance wrapper which
    # preserves the calling field context while referencing the shared
    # ComponentDef.
    component: Optional[str] = None
    resolved_component: Optional["ComponentInstance"] = None
    # cardinality in the spec is typically '1' or 'n'
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
class FieldInstance:
    """
    Lightweight wrapper used when a field is instantiated. For example for a specific component or module
    """

    original: FieldDef
    overrides: Dict[str, Any]


@dataclass
class ComponentInstance:
    """
    Lightweight wrapper used when a field references a component.
    Keeps the shared ComponentDef unchanged while preserving the
    calling field reference (FieldDef) for traversal/output.
    """

    component: ComponentDef
    referenced_by_field: Optional[FieldInstance] = None


@dataclass
class ComponentDef:
    ref: str
    name: str
    description: str = ""
    # Preserve original author-specified order by storing an `items` list
    # which can contain FieldDef and ComponentDef instances.
    items: List[Any] = field(default_factory=list)
    # Keep convenience lists (derived from items) for backward compatibility
    fields: List[FieldDef] = field(default_factory=list)
    components: List["ComponentDef"] = field(default_factory=list)
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

        # loop over fields listed in component
        for field_item in raw_fields:
            field_ref = field_item.get("field")
            original_field_def = field_defs.get(field_ref) if field_defs else None

            if original_field_def:
                field_instance = FieldInstance(
                    original=original_field_def, overrides=field_item
                )
                if original_field_def.component:
                    # resolve this component def
                    component_item = dict(
                        component_index.get(original_field_def.component)
                    )
                    if component_item:
                        items.append(
                            ComponentInstance(
                                component=cls.from_spec(
                                    component_item, field_defs, component_index
                                ),
                                referenced_by_field=field_instance,
                            )
                        )
                else:
                    items.append(field_instance)

        # easy access attrs
        fields = [i for i in items if isinstance(i, FieldDef)]
        components = [i for i in items if isinstance(i, ComponentDef)]

        entry_date = component_def.get("entry-date")
        end_date = component_def.get("end-date")
        return cls(
            ref=ref,
            name=name,
            description=description,
            items=items,
            fields=fields,
            components=components,
            entry_date=entry_date,
            end_date=end_date,
        )


@dataclass
class ModuleDef:
    ref: str
    name: str
    description: str = ""
    # Preserve original order of fields/components
    items: List[Any] = field(default_factory=list)
    fields: List[FieldDef] = field(default_factory=list)
    components: List[ComponentDef] = field(default_factory=list)
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
        items: List[Any] = []

        items.extend(resolve_items(raw_fields, field_defs, component_defs))

        fields = [i for i in items if isinstance(i, FieldDef)]
        components = [i for i in items if isinstance(i, ComponentDef)]

        entry_date = module_content.get("entry-date")
        end_date = module_content.get("end-date")

        return cls(
            ref=ref,
            name=name,
            description=description,
            items=items,
            fields=fields,
            components=components,
            entry_date=entry_date,
            end_date=end_date,
        )


@dataclass
class DatasetDef:
    dataset: str
    ref: str
    name: str
    description: str = ""
    # Preserve original order of fields/components; items may contain FieldInstance
    # or ComponentInstance objects.
    items: List[Any] = field(default_factory=list)
    # Datasets list fields directly; they can be plain fields or fields that
    # resolve to components, so we keep the resolved items here.
    fields: List[Any] = field(default_factory=list)
    components: List[ComponentDef] = field(default_factory=list)
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

        components = [i.component for i in items if isinstance(i, ComponentInstance)]

        entry_date = dataset_content.get("entry-date")
        start_date = dataset_content.get("start-date")
        end_date = dataset_content.get("end-date")

        return cls(
            dataset=dataset,
            ref=dataset,
            name=name,
            description=description,
            items=items,
            fields=items,
            components=components,
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
    extends: Optional[str] = None
    allow_additional_properties: Optional[bool] = False
    synonyms: List[str] = field(default_factory=list)
    legislation: List[str] = field(default_factory=list)
    notes: str = ""
    entry_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    # items can mix FieldDef and ComponentDef at app-level
    items: List[Any] = field(default_factory=list)
    fields: List[FieldDef] = field(default_factory=list)
    components: List[ComponentDef] = field(default_factory=list)
    # module refs (as strings)
    modules: List[str] = field(default_factory=list)
    # resolved ModuleDef objects (populated by resolve_application_modules)
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

        # start with fields specific to application
        raw_fields = app_content.get("fields") or []
        items: List[Any] = []
        items.extend(resolve_items(raw_fields, field_defs, component_defs))

        fields = [i for i in items if isinstance(i, FieldDef)]
        components = [i for i in items if isinstance(i, ComponentDef)]

        modules = [
            module_defs.get(m["module"]) for m in (app_content.get("modules") or [])
        ]

        return cls(
            application=app,
            ref=app,
            name=name,
            description=description,
            extends=extends,
            allow_additional_properties=allow_additional_properties,
            synonyms=synonyms,
            legislation=legislation,
            notes=notes,
            entry_date=entry_date,
            start_date=start_date,
            end_date=end_date,
            items=items,
            fields=fields,
            components=components,
            modules=modules,
        )


def resolve_items(raw_fields, field_defs, component_defs):
    items = []
    # loop over fields listed in element
    for field_item in raw_fields:
        field_ref = field_item.get("field")
        original_field_def = field_defs.get(field_ref) if field_defs else None

        if original_field_def:
            field_instance = FieldInstance(
                original=original_field_def, overrides=field_item
            )
            if original_field_def.component:
                # resolve this component def
                component_def = component_defs.get(original_field_def.component)
                if component_def:
                    items.append(
                        ComponentInstance(
                            component=component_def,
                            referenced_by_field=field_instance,
                        )
                    )
            else:
                # we might want to do overrides here
                items.append(field_instance)
    return items
