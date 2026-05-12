# Fields

A consistent structure for how fields are described and reused across modules, enabling shared definitions, clarity, and better validation

### Why

We'll get lots of benefits from defining fields, including:

* field reuse
  Avoids defining the same field multiple times with subtle differences
* easier validation
  Shared field types and constraints make conformance easier to check across systems
* easier to change
  Single place to update a field instead of across multiple modules
* easier to maintain
  Simpler to build tooling to support maintaining the specs - like auto generating human readable versions and documentation
* declarative, not procedural
  By defining fields as structured data, not logic, the spec becomes easier to read, validate, and integrate across languages and tools — it’s format-neutral and implementation-agnostic

### Decisions

**Fields should be defined centrally**
Each field has a canonical definition in a shared repository.

**Attributes of field definitions**

* `field`
* `name`
* `description`
* `datatype`
* `component`
* `cardinality`
* `entry-date`
* `end-date` - for deprecating fields

**`required` is specified in the module, not the field**
Avoids context-dependent logic in the field definition

**Modules can override field attributes**
But this should be done sparingly. It's better to create distinct field names for significantly different uses. [Example needed]

In practice this is most useful for presentation text:

* override `name` when a reused field needs a different label in a specific module
* override `description` when the module needs tighter context-specific guidance
* use `notes` for extra implementation guidance rather than for labels

For example, a shared `description` field can be reused in different modules while each module supplies the label and wording that fit that context.

**Reuse fields when the semantic meaning holds**
Reuse a field when it describes the same real-world concept, not just when the wording on a form overlaps.

This means an existing field can be reused where only the label, description, guidance, requiredness, validation, cardinality or presentation changes in a particular module. Those differences should be handled with module-level field attributes or overrides.

Do not reuse a field where its current meaning is tied to a different domain and would import the wrong assumptions. In that case, either generalise the existing field deliberately or create a new field with a clearer meaning.

For example, a generic `addresses` field can be reused where a form asks for multiple premises addresses, with the module making the context and `cardinality: n` explicit. However, an advertisement-specific `height` field should not be reused for telecommunications apparatus just because both forms ask for a height.

**Use `component` for substructures**
Semantically accurate for nested objects (like Person, Document, etc.)

**Make dataset-constrained field usage explicit**
When a field usage in a dataset is constrained to records from a specific dataset,
include `dataset:` explicitly on that field usage.

This includes self-references. For example, if a field in
`planning-application-document` must point to another record in the same dataset,
that dataset constraint should still be written explicitly rather than left implicit.

This makes it clear that the field is not just a free string and helps readers and
tooling understand the intended target of the reference.


### Still to decide

* would `codelist` be a useful attribute?
  It would allow us to be more explicit about which codelist is used for a given field
* where should constraints if applicable go? For example, `min`, `max`
  Should constraints be defined at the field level (reused everywhere) or module level (context-specific)? Or both? Needs to be worked through
* should we version fields?
  Already included `end-date` to deprecate fields. But do we need `version` too? Will the fields change?


### Examples

Field definition for a simple field:
```
---
cardinality: '1'
datatype: boolean
description: ''
entry-date: ''
end-date: ''
field: is-advert-in-place
name: Is the advert in place
---
```

Field definition for a field with substructure:
```
---
cardinality: 'n'
datatype: object
description: ''
entry-date: ''
end-date: ''
field: applicants
name: Applicants
component: Applicant
---
```

### Validation rules for field definitions

* every field of datatype `object` must have a `component` attribute
* every field of datatype `enum` must have a `codelist` attribute
* cardinality must be `1` or `n`
