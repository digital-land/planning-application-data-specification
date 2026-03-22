# Codelist usage pattern

## Summary

This note describes a general pattern for defining how to use subsets of codelists.

This will apply in cases where:

- one codelist defines the values for a field
- different contexts allow different subsets of that codelist
- some contexts need more granular values than others

The pattern is simple:

1. keep one canonical codelist for the values
2. keep usage or context rules in a separate table

If the codelist needs hierarchy, that hierarchy stays in the codelist.

## Why this pattern is needed

Without a clear pattern, a codelist can end up doing two jobs at once:

- defining the values, and any hierarchy between them
- defining where those values are allowed

This makes the codelist harder to understand and harder to maintain.

This pattern keeps the roles clear:

- the codelist defines the values, their meaning and any roll-up relationship
- the usage table defines where those values are allowed

## How the pattern works

### Canonical codelist

The canonical codelist is the source of truth for the values.

It should contain:

- the values themselves
- the meaning of each value
- any hierarchy or roll-up relationship, using `parent` where needed

It should not contain context rules about where each value is allowed.

### Usage table

The usage table says where a codelist value is allowed.

Each row says that one value is allowed in one context.

A first version for `tenure-type` could include:

- `reference`
- `tenure-type`
- `profile`
- `application-type`
- `module`
- `entry-date`
- `start-date`
- `end-date`
- `notes`

Example:

| reference | tenure-type | profile | application-type | module | entry-date | start-date | end-date | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mhclg-full-market-housing` | `market-housing` | `mhclg-core` | `full` | `res-units` | `2026-03-18` |  |  | Used in the national full permission context. |
| `mhclg-ldc-social-rented` | `social-rented` | `mhclg-core` | `ldc` | `res-units` | `2026-03-18` |  |  | Used in the national lawful development certificate context. |
| `gla-full-market-for-sale` | `market-for-sale` | `gla` | `full` | `res-units` | `2026-03-18` |  |  | Used when the GLA profile applies. |
| `gla-full-london-affordable-rent` | `london-affordable-rent` | `gla` | `full` | `res-units` | `2026-03-18` |  |  | Used when the GLA profile applies. |

For example, `market-for-sale` is to be used by GLA profiles in `full` applications as part of the `res-units` module.

The initial recommendation is to use separate usage tables for separate codelists, for example:

- `tenure-type-usage.csv`
- `housing-type-usage.csv`

This is clearer and easier to maintain than one generic usage table.

## Routing rules

The usage table says which values are allowed for a given profile or context.

There may also need to be a short explanation of how an application ends up on that profile.

In plain English:

- the usage table answers: what is allowed once you are in profile `X`?
- the routing rule answers: how do you know you are in profile `X`?

Examples:

- today: if `planning-authority` is in GLA jurisdiction, use profile `gla`; otherwise use `mhclg-core`
- possible future: if the application uses a GLA replacement module, use profile `gla`; otherwise use `mhclg-core`

For now, this can stay as a short prose explanation rather than a formal artefact.

## Where it should sit

The canonical codelist remains in `data/codelist/`.

The usage table should sit in `data/`, for example:

- `data/tenure-type-usage.csv`

Its definition should sit in `specification/data/`, for example:

- `specification/data/tenure-type-usage.schema.md`

If needed, a short explanation of routing rules can be added to the usage-table schema note or to `specification/README.md`.

## Recommendation

- adopt the pattern as a general codelist pattern
- use `tenure-type` as the first concrete implementation
- keep usage tables codelist-specific rather than generic
- keep routing rules as prose unless the need becomes more complex

## Why we need this now

We are rolling this pattern out first for `tenure-type`.

That is the case that made the need clear because:

- MHCLG has its tenure types
- GLA uses more granular tenure types for the same field
- the values need to sit in one coherent codelist
- the allowed subsets vary by context

So `tenure-type` is the first implementation of a general pattern, not a one-off special case.

---

## Examples from other standards

This is a common standards pattern. It is not something unique to this work.

### HL7 FHIR

[HL7 FHIR](https://www.hl7.org/fhir/) separates:

- `CodeSystem`, which defines the codes and their meaning
- `ValueSet`, which defines which codes are allowed in a particular context

Further reading:

- [FHIR CodeSystem](https://www.hl7.org/fhir/codesystem.html)
- [FHIR ValueSet](https://www.hl7.org/fhir/valueset.html)

### SDMX

[SDMX](https://sdmx.org/) separates code lists from constraint artefacts that describe which subsets are valid in a particular data flow or context.

Further reading:

- [SDMX for Education](https://sdmx.org/sdmx-for-education/)

### GS1

[GS1 code lists guidance](https://www.gs1.org/edi-xml/technical-user-guide/code-lists) also recognises the need to work with subsets of broader code lists for particular business contexts.
