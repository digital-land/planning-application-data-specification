"""Named specifications composing independently defined datasets."""
from copy import deepcopy
from dataclasses import dataclass
from .views import view_errors


@dataclass(frozen=True)
class SpecificationDataset:
    ref: str
    name: str
    description: str
    base: object


class SpecificationDefinition:
    def __init__(self, repository, ref, definition):
        self.repository = repository
        self.ref = ref
        self.name = definition.get('name', ref)
        self._definition = deepcopy(dict(definition))
        # Reuse selection validation without applying view-only structural rules.
        selection = deepcopy(self._definition)
        for dataset in selection.get('datasets', []) if isinstance(selection.get('datasets', []), list) else []:
            if not isinstance(dataset, dict):
                continue
            for field in dataset.get('fields', []) if isinstance(dataset.get('fields', []), list) else []:
                if isinstance(field, dict):
                    field.pop('datatype', None)
                    field.pop('cardinality', None)
        errors = view_errors(ref, selection, repository.tables['dataset'])
        if errors:
            raise ValueError('\n'.join(errors))
        self._entries = {entry['dataset']: entry for entry in self._definition.get('datasets', [])}
        for dataset, entry in self._entries.items():
            if 'record-inclusion' in entry:
                raise ValueError(f"Specification '{ref}', dataset '{dataset}': record filters belong in views")
            for field in self._fields(dataset):
                resolved = repository.resolve_field(field['field'], dataset=dataset)
                for key, actual in [('datatype', resolved.datatype), ('cardinality', resolved.cardinality), ('codelist', resolved.codelist), ('dataset', resolved.target_dataset)]:
                    if key in field and (str(field[key]) if key == 'cardinality' else field[key]) != actual:
                        raise ValueError(f"Specification '{ref}', dataset '{dataset}', field '{field['field']}': conflicting {key}")

    def dataset(self, ref):
        if ref not in self._entries:
            raise KeyError(f"Dataset '{ref}' is not included in specification '{self.ref}'")
        entry = self._entries[ref]
        base = self.repository.dataset(ref)
        return SpecificationDataset(ref, entry.get('name', base.name), entry.get('description', base.description), base)

    def datasets(self):
        return tuple(self.dataset(ref) for ref in self._entries)

    def _fields(self, dataset):
        self.dataset(dataset)
        entry = self._entries[dataset]
        if 'fields' in entry:
            return entry['fields']
        return [{'field': field['field']} for field in self.repository.tables['dataset'][dataset].get('fields', [])]

    def resolve_field(self, ref, *, dataset):
        from .specification import ResolvedSpecificationField, ResolvedFieldUsage
        entry = next((field for field in self._fields(dataset) if field['field'] == ref), None)
        if entry is None:
            raise KeyError(f"Field '{ref}' is not included in dataset '{dataset}' of specification '{self.ref}'")
        underlying = self.repository.resolve_field(ref, dataset=dataset)
        overrides = deepcopy({key: value for key, value in entry.items() if key != 'field'})
        values = dict(underlying.__dict__)
        values.update(name=entry.get('name', underlying.name), description=entry.get('description', underlying.description),
                      usage=ResolvedFieldUsage(overrides, deepcopy(entry.get('applies-if', underlying.applies_if)), underlying.required_if),
                      applies_if=deepcopy(entry.get('applies-if', underlying.applies_if)))
        return ResolvedSpecificationField(**values, dataset_field=underlying, specification_ref=self.ref)

    def resolve_container_items(self, *, dataset):
        return tuple(self.resolve_field(field['field'], dataset=dataset) for field in self._fields(dataset))
