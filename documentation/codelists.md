# Codelists

A codelist is a controlled list of valid values for a particular field. 

Each codelist definition file describes what the list is for, where the source data comes from, and the structure of the codes.

This helps standardise terminology, improve validation, and make it easier to integrate systems.

## Why

We get several benefits from defining codelists, including:

* **Consistency and reuse**  
  Ensures the same values are used everywhere, avoiding subtle variations.
* **Easier validation**  
  Fields referencing a codelist can be checked automatically against a known set of codes.
* **Easier to maintain**  
  One place to update the list and its metadata, rather than chasing copies in multiple specs.
* **Clear provenance**  
  Source and licensing information are explicit, so consumers know where the data came from.
* **Declarative, not procedural**  
  Defined as structured data, so the list is format-neutral and can be processed by different tools and languages.

## Decisions

**Each codelist has a single canonical definition**  
The definition lives in this shared planning application specification repository

**The data can be defined in the repo or elsewhere**
Some codelists are specific to this specification so the CSV (or other format) containing the actual codes will be included in this repository. Other codelists have wider applicability so they will be elsewhere for wider use.

**Attributes of codelist definitions**

* `codelist` — short, stable identifier (lowercase kebab-case)
* `name` — singular display name
* `plural` — plural display name
* `description` — purpose and scope
* `organisation` — identifier for the owning organisation
* `licence` — licence for reuse (e.g. `ogl3`)
* `source` — URL to the authoritative source data (CSV or API)
* `fields` — list of column names in the codelist data file
* `key-field` — column containing the unique identifier for codes
* `entry-date` — when this codelist definition was first added
* `end-date` — when this codelist definition was withdrawn (if applicable)
* `notes` — any extra context or implementation guidance
* `github-discussion` — link or ID for relevant discussion thread

**The codelist definition is metadata only**  
It describes the list and its columns but does not include the rows themselves.

**Fields in a codelist CSV should match the `fields` attribute**  
This allows automated validation to check that the source file has the expected structure.

## Still to decide

* Should codelist definitions include version information beyond `entry-date` and `end-date`?  
* Should we require `status` (e.g. active, deprecated, experimental)?   
* Do the fields need to be defined? 

## Example

Codelist definition:
```yaml
---
codelist: development-phase
name: Development phase
plural: Development phases
description: |
  The development phase codelist defines the various stages or phases that an extraction of oil and gas project may progress through, such as exploratory and production. This helps standardize the terminology used to describe the status of projects.
organisation: government-organisation:D1342
licence: ogl3
entry-date: 2025-08-13
end-date:
fields:
  - field: reference
  - field: name
  - field: description
key-field: reference
source:
notes:
github-discussion: 194
---
```

### Validation rules for codelist definitions

* codelist, name, description, fields, source and key-field must be present
* every field in fields must appear as a column in the source data
* the key-field must be unique within the source data
* if end-date is present, it must be on or after entry-date
* `source` must be a valid URL
