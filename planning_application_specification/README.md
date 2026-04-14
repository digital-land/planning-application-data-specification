# planning_application_specification

Python package for loading and querying the planning application specification from a local checkout of this repository.

This package is being introduced gradually so existing `/bin` scripts can move onto it in small safe steps. The current interface is intentionally small.

The current package has three kinds of query:

- canonical lookup for definitions as they exist in the source data
- applicable views for codelists filtered by selection context
- resolved views for fields as used within a module or component
- application lookup for canonical single application types and controlled combined application types

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

householder = spec.application("hh")
print(householder.name)
print(householder.application_types)

householder_listed = spec.application(["hh", "lbc"])
print(householder_listed.name)
print(householder_listed.application_types)
```

You can also load from an explicit repo path:

```python
spec = Specification.load("/path/to/planning-application-data-specification")
```

If the package cannot detect the repository root automatically, `Specification.load(...)` raises `FileNotFoundError`.

## Current scope

The implemented package currently supports:

- loading the specification model from a local repo checkout
- canonical single-application lookup and controlled combined-application lookup
- canonical codelist lookup
- canonical field, component and module lookup
- applicable codelist filtering using selection context
- resolved field lookup for module or component context with static override merging
- resolved container item lookup that preserves mixed authored order for plain fields and component-reference rows

Current V1 boundary:

- works against a local checkout of this repository
- evaluates codelist applicability from usage data using selection context
- evaluates field `applies-if` only for `application-type` conditions
- exposes `required-if` as raw rule data and does not execute answer-dependent rules

## Combined applications

Combined applications are supported as a controlled list of active combinations defined in `specification/combined-application-types.csv`.

Use:

- `spec.application("hh")` for a canonical single application type
- `spec.application(["hh", "lbc"])` for a controlled combined application type

Combined applications currently:

- normalise member order before lookup
- reject unknown combinations with `KeyError`
- reject recognised but inactive combinations with `ValueError`
- expose a deduped union of member modules
- expose merged application-level items

Example:

```python
householder = spec.application("hh")
householder_listed = spec.application(["hh", "lbc"])

print(householder.ref)  # hh
print(householder_listed.ref)  # hh;lbc
print(householder_listed.is_combined)  # True
```

## Choosing the right method

Use canonical lookup when you want the base definition:

- `spec.application(ref)` for an application view over a canonical single application definition
- `spec.codelist(ref)` for the source codelist
- `spec.field(ref)`, `spec.component(ref)` and `spec.module(ref)` for canonical definitions

Use contextual lookup when you want the specification as it applies in a particular situation:

- `spec.application([ref1, ref2])` for an active controlled combined application type using the same public shape
- `spec.codelist(ref).applicable(selection=...)` when codelist items may vary by profile or application type
- `spec.resolve_field(...)` when a field may carry local usage overrides or conditional applicability inside a module or component
- `spec.resolve_container_items(...)` when you need the ordered mixed rows of a module or component as authored

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

This returns the source codelist definition without applying usage rules. To get the filtered set of items for a particular profile or application type, call `.applicable(selection=...)` on the returned object.

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

### `Specification.application(ref: str | list[str])`

Return an application view for either a canonical single application or a derived controlled combined application.

Arguments:

- `ref`: a single application type reference such as `"hh"`, or a list of application type references such as `["hh", "lbc"]`

Returns:

- an `ApplicationDef` view for a single or combined application
- `application_types`, `name`, `description` and `modules` are available in both cases
- combined applications set `is_combined=True`
- combined applications also expose lifecycle metadata carried in `combined-application-types.csv`, such as `entry_date`, `start_date`, `end_date`, and `notes`
- combined applications derive `allow_additional_properties` with AND semantics across member applications
- combined applications expose a deduped union of application-level `items`, `field_usages`, and `component_usages`
- input order does not matter for combined applications, so `["lbc", "hh"]` resolves as `hh;lbc`

Raises:

- `KeyError` if the single application or combined application is unknown
- `ValueError` if the combined application is recognised but not yet active

Example:

```python
householder = spec.application("hh")
householder_listed = spec.application(["hh", "lbc"])
```

### `Specification.field(ref: str)`

Return a canonical field definition by reference.

This does not apply module or component usage overrides. Use `spec.resolve_field(...)` when you need the field as used in context.

Arguments:

- `ref`: field reference, for example `"description"`

Returns:

- the compiled field definition object

Raises:

- `KeyError` if the field is not defined

Example:

```python
field = spec.field("description")
```

### `Specification.component(ref: str)`

Return a canonical component definition by reference.

Arguments:

- `ref`: component reference, for example `"bedroom-count"`

Returns:

- the compiled component definition object

Raises:

- `KeyError` if the component is not defined

Example:

```python
component = spec.component("bedroom-count")
```

Returned component definitions currently expose:

- `items`: ordered mixed usage list
- `field_usages`: field usages contained by the component
- `component_usages`: nested component usages contained by the component

### `Specification.module(ref: str)`

Return a canonical module definition by reference.

Arguments:

- `ref`: module reference, for example `"proposal-details"`

Returns:

- the compiled module definition object

Raises:

- `KeyError` if the module is not defined

Example:

```python
module = spec.module("proposal-details")
```

Returned module definitions currently expose:

- `items`: ordered mixed usage list
- `field_usages`: field usages contained by the module
- `component_usages`: component usages contained by the module

### `Specification.resolve_field(ref: str, module: str | None = None, component: str | None = None, selection: SelectionContext | None = None) -> ResolvedField`

Return a resolved field view for a specific structural context.

Use this when canonical lookup is not enough and you need the field as used within a module or component.

Arguments:

- `ref`: field reference
- `module`: optional module reference
- `component`: optional component reference
- `selection`: optional selection context used for `applies-if`

Rules:

- at least one of `module` or `component` must be provided
- if `module` is provided, the field is resolved in that module context
- if `component` is provided without a module, the field is resolved in that canonical component context
- if both are provided, the field is resolved in that component as reached within the module

Current behaviour:

- merges static override attributes from the field usage on top of the canonical field definition
- returns `required-if` as raw rule data
- evaluates `applies-if` only for `application-type` conditions
- returns a resolved field even when it does not apply, with `applies=False`

This method currently aims to answer: "what does this field look like here?" It does not yet answer answer-dependent questions such as whether the field becomes required based on other submitted values.

Examples:

```python
resolved = spec.resolve_field(
    "description",
    module="tree-work-details",
)

resolved = spec.resolve_field(
    "no-bedrooms-unknown",
    component="bedroom-count",
)

resolved = spec.resolve_field(
    "related-application",
    module="proposal-details",
    selection=SelectionContext(application_type="full"),
)
```

### `Specification.resolve_container_items(module: str | None = None, component: str | None = None, selection: SelectionContext | None = None) -> tuple[ResolvedField | ResolvedComponentReference, ...]`

Return the ordered resolved items for a module or component.

Use this when you need the container as authored, rather than a direct lookup by field reference.

Current behaviour:

- requires exactly one of `module` or `component`
- preserves authored item order
- returns a mixed tuple of `ResolvedField` and `ResolvedComponentReference`
- applies the same `application-type` based `applies-if` handling used by `resolve_field(...)`
- keeps component-reference rows visible as first-class items rather than dropping them during resolution

Example:

```python
items = spec.resolve_container_items(
    module="tree-work-details",
    selection=SelectionContext(application_type="notice-trees-in-con-area"),
)

items = spec.resolve_container_items(
    component="bedroom-count",
)
```

## `ResolvedField`

Represents a field definition resolved in a usage context.

This is a contextual view. It combines the canonical field definition with the usage-level override and condition data for the selected module or component context.

Attributes:

- `ref`
- `name`
- `description`
- `datatype`
- `required`
- `notes`
- `component`
- `cardinality`
- `applies`
- `applies_if`
- `required_if`
- `base`: canonical field definition
- `usage`: slim public usage view containing override and condition data
- `container_ref`
- `container_kind`

## `ResolvedFieldUsage`

Represents the usage-specific part of a resolved field without repeating the canonical base definition.

Attributes:

- `overrides`
- `applies_if`
- `required_if`

## `ResolvedComponentReference`

Represents a container row that points to a nested component.

This is a contextual view of the referencing field usage plus the target component definition.

Attributes:

- `ref`
- `name`
- `description`
- `datatype`
- `required`
- `notes`
- `component_ref`
- `cardinality`
- `applies`
- `applies_if`
- `required_if`
- `base`: canonical field definition
- `usage`: slim public usage view containing override and condition data
- `component`: canonical component definition reached by this row
- `container_ref`
- `container_kind`

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
- `application_type: str | list[str] | tuple[str, ...] | set[str] | None = None`

Example:

```python
selection = SelectionContext(
    specification_profile="gla",
    application_type="full",
)
```

`application_type` may be:

- a single application type string such as `"hh"`
- a semicolon-delimited combined string such as `"hh;lbc"`
- a Python collection such as `["hh", "lbc"]`

For combined application selections, `application-type` checks use OR semantics. A row or field applies if it matches at least one of the selected application types.

Examples:

```python
selection = SelectionContext(application_type="hh;lbc")
selection = SelectionContext(application_type=["hh", "lbc"])
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

Use this when the canonical codelist exists globally but the allowed items vary by usage context.

Behaviour:

- if no usage rules are defined for the codelist, returns all canonical items
- if usage rules exist, filters items using the available selection context
- current filtering understands:
  - `specification-profile`
  - `application-types`

This is a selection-time filter over the canonical codelist. It does not change the underlying canonical definition.

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

- clearer public distinction between canonical definitions, usages and resolved views
