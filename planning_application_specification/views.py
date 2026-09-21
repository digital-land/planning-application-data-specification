"""Explicit selections of existing datasets, without record evaluation."""
from copy import deepcopy
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .specification import Specification


def view_errors(ref, definition, datasets):
    """Shared authoring validation; return contextual errors without raising."""
    errors = []
    prefix = f"specification/{ref}.schema.md"
    selected = definition.get("datasets", [])
    if not isinstance(selected, list):
        return [f"{prefix}: datasets must be a list"]
    seen = set()
    for entry in selected:
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: dataset entry must be a mapping")
            continue
        dataset = entry.get("dataset")
        context = f"{prefix}: dataset {dataset!r}"
        if not isinstance(dataset, str) or dataset not in datasets:
            errors.append(f"{context}: unknown dataset")
            continue
        if dataset in seen:
            errors.append(f"{context}: duplicate selection")
        seen.add(dataset)
        defined = {field['field'] for field in datasets[dataset].get('fields', [])}
        fields = entry.get('fields', [])
        if not isinstance(fields, list):
            errors.append(f"{context}: fields must be a list")
            continue
        field_seen = set()
        for field in fields:
            if not isinstance(field, dict):
                errors.append(f"{context}: field entry must be a mapping")
                continue
            name = field.get('field')
            location = f"{context}: field {name!r}"
            if not isinstance(name, str) or name not in defined:
                errors.append(f"{location}: field is not defined in the dataset")
                continue
            if name in field_seen:
                errors.append(f"{location}: duplicate selection")
            field_seen.add(name)
            for key in ('datatype', 'cardinality', 'required', 'required-if'):
                if key in field:
                    errors.append(f"{location}: {key} is not permitted in a view")
            if 'requirement-level' in field and field['requirement-level'] not in ('MUST', 'SHOULD', 'MAY'):
                errors.append(f"{location}: invalid requirement-level")
            for key in ('name', 'description'):
                if key in field and not isinstance(field[key], str):
                    errors.append(f"{location}: {key} must be a string")
        if 'record-inclusion' in entry:
            rule = entry['record-inclusion']
            if not isinstance(rule, dict):
                errors.append(f"{context}: record-inclusion must be a mapping")
                continue
            controlling = rule.get('field')
            if not isinstance(controlling, str) or controlling not in defined:
                errors.append(f"{context}: record-inclusion field must belong to the dataset")
            values = rule.get('include-values')
            literal = isinstance(values, list) and bool(values) and all(isinstance(v, str) and bool(v) for v in values)
            profile = isinstance(values, dict) and all(isinstance(values.get(k), str) and bool(values[k]) for k in ('codelist', 'specification-profile'))
            if not (literal or profile):
                errors.append(f"{context}: include-values must be a non-empty string list or a codelist/profile mapping")
    return errors


@dataclass(frozen=True)
class ViewDataset:
    ref: str
    name: str
    description: str
    base: object
    record_inclusion: dict | None


class View:
    def __init__(self, specification: 'Specification', ref: str, definition: dict):
        errors = view_errors(ref, definition, specification.tables['dataset'])
        if errors:
            raise ValueError('\n'.join(errors))
        self.specification = specification
        self.ref = ref
        self.name = definition.get('name', ref)
        self._entries = {entry['dataset']: deepcopy(entry) for entry in definition.get('datasets', [])}

    def dataset(self, ref):
        if ref not in self._entries:
            raise KeyError(f"Dataset '{ref}' is not selected by view '{self.ref}'")
        entry = self._entries[ref]
        base = self.specification.dataset(ref)
        return ViewDataset(ref, entry.get('name', base.name), entry.get('description', base.description), base, deepcopy(entry.get('record-inclusion')))

    def datasets(self):
        return tuple(self.dataset(ref) for ref in self._entries)

    def resolve_field(self, ref, *, dataset):
        from .specification import ResolvedFieldUsage, ResolvedViewField
        self.dataset(dataset)
        entry = next((field for field in self._entries[dataset].get('fields', []) if field['field'] == ref), None)
        if entry is None:
            raise KeyError(f"Field '{ref}' is not selected in dataset '{dataset}' by view '{self.ref}'")
        underlying = self.specification.resolve_field(ref, dataset=dataset)
        overrides = deepcopy({key: value for key, value in entry.items() if key != 'field'})
        values = dict(underlying.__dict__)
        values.update(name=entry.get('name', underlying.name), description=entry.get('description', underlying.description),
                      usage=ResolvedFieldUsage(overrides, deepcopy(entry.get('applies-if')), None))
        return ResolvedViewField(**values, dataset_field=underlying, view_ref=self.ref)

    def resolve_container_items(self, *, dataset):
        self.dataset(dataset)
        return tuple(self.resolve_field(field['field'], dataset=dataset) for field in self._entries[dataset].get('fields', []))
