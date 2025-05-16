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

**Use `component` for substructures**
Semantically accurate for nested objects (like Person, Document, etc.)


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
