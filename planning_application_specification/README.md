# planning_application_specification

Python package for loading and querying the planning application specification from a local checkout of this repository.

This package is being introduced gradually so existing `/bin` scripts can move onto it in small safe steps. The current interface is intentionally small.

## Getting started

For now, the package works against a local checkout of this repository.

From the repo root:

```python
from planning_application_specification import Specification
from planning_application_specification.specification import SelectionContext

spec = Specification.load()

tenure_type = spec.codelist("tenure-type")
print(tenure_type.name)
print(len(tenure_type.items))

gla_full_tenure_type = tenure_type.applicable(
    selection=SelectionContext(
        specification_profile="gla",
        application_type="full",
    )
)
print(len(gla_full_tenure_type.items))
```

You can also load from an explicit repo path:

```python
spec = Specification.load("/path/to/planning-application-data-specification")
```

If the package cannot detect the repository root automatically, `Specification.load(...)` raises `FileNotFoundError`.

## Current scope

The implemented package currently supports:

- loading the specification model from a local repo checkout
- canonical codelist lookup
- applicable codelist filtering using selection context

It does not yet provide the planned field, component, module or resolved field query APIs.

## API index

## `Specification`

Defined in [specification.py](/Users/colm/code/mhclg/digital-land/planning-application-data-specification/planning_application_specification/specification.py).

### `Specification.load(path: str | Path | None = None) -> Specification`

Load the specification from a local checkout of this repository.

Arguments:

- `path`: optional path to the repo root. If omitted, the loader tries to detect the repo root from the current working directory and its parents.

Returns:

- a `Specification` instance with loaded tables and compiled indexes

Raises:

- `FileNotFoundError` if the repository root cannot be found

Example:

```python
spec = Specification.load()
spec = Specification.load("/path/to/repo")
```

### `Specification.codelist(ref: str) -> Codelist`

Return a canonical codelist by reference.

Arguments:

- `ref`: codelist reference, for example `"tenure-type"`

Returns:

- a `Codelist` object

Raises:

- `KeyError` if the codelist is not defined

Example:

```python
tenure_type = spec.codelist("tenure-type")
```

### `Specification` attributes

These are currently available on the loaded object:

- `source_path`: resolved repo root path used for loading
- `tables`: raw frontmatter tables
- `modules`: compiled module index
- `components`: compiled component index
- `applications`: compiled application index
- `fields`: compiled field index

These are available because they are useful during migration. They should be treated as provisional rather than polished public API.

## `SelectionContext`

Defines selection context for context-sensitive queries.

Fields:

- `specification_profile: str | None = None`
- `application_type: str | None = None`

Example:

```python
selection = SelectionContext(
    specification_profile="gla",
    application_type="full",
)
```

## `Codelist`

Represents the canonical codelist.

Attributes:

- `specification`: parent `Specification`
- `ref`: codelist reference
- `name`: human-readable name
- `description`: schema description text
- `items`: tuple of canonical `CodelistItem` objects

### `Codelist.applicable(selection: SelectionContext | None = None) -> ApplicableCodelist`

Return an applicable codelist view for a given selection context.

Behaviour:

- if no usage rules are defined for the codelist, returns all canonical items
- if usage rules exist, filters items using the available selection context
- current filtering understands:
  - `specification-profile`
  - `application-types`

Example:

```python
gla_full_tenure_type = spec.codelist("tenure-type").applicable(
    selection=SelectionContext(
        specification_profile="gla",
        application_type="full",
    )
)
```

## `ApplicableCodelist`

Represents a codelist view after applying usage rules.

Attributes:

- `canonical`: the canonical `Codelist`
- `items`: tuple of applicable `CodelistItem` objects
- `selection`: the `SelectionContext` used
- `usage_rules_applied`: `True` if a matching `*-usage` data schema exists, otherwise `False`

## `CodelistItem`

Represents one row from a codelist CSV.

Attributes:

- `reference`
- `name`
- `description`
- `notes`
- `parent`
- `row`: original CSV row as a dict

## Loading internals

The main loading support currently lives in:

- [loader.py](/Users/colm/code/mhclg/digital-land/planning-application-data-specification/planning_application_specification/loader.py)
- [models.py](/Users/colm/code/mhclg/digital-land/planning-application-data-specification/planning_application_specification/models.py)

These modules are currently part of the implementation surface for migration work. They may be refined as the package grows.

## Planned next areas

Expected next additions include:

- canonical `field`, `component` and `module` lookups
- `spec.resolve_field(...)`
- clearer public distinction between canonical definitions, usages and resolved views
