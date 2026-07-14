# Required national public view output and rules for deriving it

This note describes a proposed way to define the national public view as a specific output from the wider planning application data standard.

The proposal is to create `national-public-view.schema.md`. That schema would state which datasets and fields make up the national public view, and include the small number of rules needed to decide which records from those datasets are extracted.

## Context

The national public view is best framed as an extraction from the wider planning application data standard.

This is a useful framing because it separates:

- the data a planning authority must be able to accept and hold
- the way a supplier stores or processes that data internally
- the data that must be published openly in the national public view

The standard should define conformant data at the boundaries. It should not prescribe the supplier's internal architecture.

In plain English:

- authorities must be able to hold and maintain conformant planning application data
- authorities must be able to accept conformant submission data
- authorities must be able to publish conformant national public view data
- authorities must be able to share conformant data as required (e.g. to PINs)
- how their back office system gets from one to the other is implementation detail

The national public view is built from records defined in the planning application data specification. Some values may originate in the submission, some may be recorded by officers and some may come from later process activity.

## Why "extraction" is a useful framing

"Extraction" works better than "filter" or "redaction".

Filtering implies the public view is produced by taking a complete record and hiding bits of it. That is risky because the default mental model becomes "publish unless removed".

Extraction implies the safer model:

> Nothing enters the national public view unless the standard explicitly says it should be extracted.

This matches the emerging security position and the [NPSA planning process security guidance](https://www.npsa.gov.uk/security-best-practices/build-it-secure/security-considerations-planning-process).

## Proposal: define `national-public-view.schema.md`

Create a separate schema file that directly describes the national public view. A separate schema is clearer and safer than trying to explain a distributed set of properties across the canonical datasets, fields and codelists.

It also gives a direct answer to a developer:

> To publish the national public view, produce data conforming to `national-public-view.schema.md`.

This would use the same dataset and field definitions as `planning-application-data.schema.md`, but would be explicitly named for the view being published:

```yaml
specification: national-public-view
specification-profile: national-public-view
name: National public view
datasets:
  - dataset: planning-application
    name: planning application
    fields:
      - field: reference
      - field: description
      - field: application-types
      - field: site
        dataset: site
      - field: received-date

  - dataset: planning-application-document
    name: planning application document
    record-inclusion:
      field: public-register-status
      include-values:
        - publish
    fields:
      - field: reference
      - field: planning-application
        dataset: planning-application
      - field: document-url
      - field: documentation-url
      - field: name
      - field: replaces
        dataset: planning-application-document
```

This is easier to explain to implementers because it starts with the output:

> These are the datasets and fields that make up the national public view.

The canonical dataset schemas remain the source of field definitions, datatypes and relationships. The public-view schema says which parts are extracted.

Note the top-level `specification-profile: national-public-view`. This says the whole schema is the national public view profile. That *profile* is used when resolving codelists.

## Mechanisms needed

With this proposal, presence in `national-public-view.schema.md` is the main inclusion mechanism.

This means:

- a dataset is in the national public view if it appears in `national-public-view.schema.md`
- a dataset is not in the national public view if it does not appear
- a field is in the national public view if it is listed under a dataset in `national-public-view.schema.md`
- a field is not in the national public view if it is not listed

So the public-view schema itself handles dataset and field inclusion.

The only extra mechanisms needed are:

- codelist-value inclusion, where only some values in a codelist are part of the public view
- row-by-row inclusion, where only some records in a listed dataset are part of the public view

### Codelist-value inclusion

For codelists, reuse the existing [codelist usage pattern](../documentation/codelist-usage.md).

The canonical codelist defines all possible values. A usage table defines which values are valid for `specification-profile: national-public-view`.

Example:

- `permission-process-event` remains the full codelist
- `permission-process-event-usage.csv` or equivalent says which events are included in `national-public-view`
- the public-view extraction includes timeline rows only where `permission-process-event` is one of those values

Because `national-public-view.schema.md` has `specification-profile: national-public-view` at the top level, a resolver uses that profile when checking a codelist usage table.

### Row-by-row inclusion based on a field value

Some datasets appear in `national-public-view.schema.md`, but not every record in those datasets should be extracted.

For example, the document dataset can contain records that the planning authority has decided should not be made public.

For those datasets, the schema needs a `record-inclusion` rule. The rule says which field controls inclusion and which values qualify a record for extraction.

The simplest form is:

```yaml
record-inclusion:
  field: public-register-status
  include-values:
    - publish
```

This means:

- inspect the `public-register-status` field on each source record
- include only records where the value is `publish`
- exclude records with any other value, including blank or unassessed values

The important point is that row inclusion is opt-in. A record is not extracted unless it has a value that the public-view schema explicitly includes.

## Examples of `record-inclusion`

There are two cases the schema needs to support.

### Case 1: include records by literal field values

This is the document publication decision case.

```yaml
specification: national-public-view
specification-profile: national-public-view
name: National public view
datasets:
  - dataset: planning-application-document
    name: planning application document
    record-inclusion:
      field: public-register-status
      include-values:
        - publish
    fields:
      - field: reference
      - field: planning-application
        dataset: planning-application
      - field: document-url
      - field: documentation-url
      - field: name
      - field: replaces
        dataset: planning-application-document
```

This matches the security position: a document enters the public view only when the planning authority has positively recorded that it is suitable for public availability.

The `public-register-status` field itself does not need to be included in the national public view output. It is a control field used to derive the output. It should only be included if there is a user need for the public to see status metadata for withheld documents.

### Case 2: include records by codelist profile

This is the timeline event case.

For `planning-permission-timeline`, the relevant question is not whether a planning officer approved each row for publication. The question is whether the event type is part of the national public view.

The cleaner shape is:

```yaml
specification: national-public-view
specification-profile: national-public-view
name: National public view
datasets:
  - dataset: planning-permission-timeline
    name: planning permission timeline
    record-inclusion:
      field: permission-process-event
      include-values:
        codelist: permission-process-event
    fields:
      - field: reference
      - field: planning-application
        dataset: planning-application
      - field: permission-process-event
      - field: event-date
```

This says:

- look at the `permission-process-event` field
- use the `permission-process-event` codelist
- because the schema has `specification-profile: national-public-view`, include only values allowed for that profile

### Schema-level `specification-profile`

The `specification-profile` is a top-level property on `national-public-view.schema.md`.

In this proposal, `specification-profile` identifies the controlled context used to resolve profile-specific rules. For the national public view, it tells the resolver to use codelist usage rows for `national-public-view`.

Why it makes sense here:

- the whole schema is the national public view
- the profile should be available to every codelist usage lookup
- it avoids repeating the same profile on every dataset or rule
- it keeps `record-inclusion` focused on the inclusion condition

The pattern is:

```yaml
specification: national-public-view
specification-profile: national-public-view
name: National public view
datasets:
  - dataset: planning-permission-timeline
    record-inclusion:
      field: permission-process-event
      include-values:
        codelist: permission-process-event
```

This means "use the named codelist and the schema's top-level `specification-profile`".

## Proposed extraction algorithm

An implementer should be able to extract the national public view by following the public-view schema, without needing to know how the source system stores its internal data.

The steps are:

1. Open `national-public-view.schema.md`.
2. Read the top-level `specification-profile`. For this view it is `national-public-view`.
3. For each dataset listed in `datasets`, find the corresponding source data held by the planning authority or supplier.
4. Ignore any source dataset that is not listed in `national-public-view.schema.md`.
5. For each listed dataset, extract only the fields listed under that dataset.
6. Ignore any source field that is not listed under the dataset in `national-public-view.schema.md`.
7. If the dataset has no `record-inclusion` rule, include every source record for that dataset.
8. If the dataset has `record-inclusion.include-values` as a literal list, include only records where the named field has one of those values.
9. If the dataset has `record-inclusion.include-values.codelist`, use the named codelist and the schema's top-level `specification-profile` to find the allowed values, then include only records where the named field has one of those values.
10. Produce an output payload containing only the datasets, records and fields resolved by those rules.

For example:

- `planning-application` appears in the schema with no `record-inclusion`, so all matching `planning-application` records are included with only the listed fields.
- `planning-application-data` does not appear in the schema, so it is not extracted.
- `planning-application-document` appears in the schema with `record-inclusion.field: public-register-status` and `include-values: [publish]`, so only document records marked `publish` are extracted.
- `planning-permission-timeline` can use `record-inclusion` with `permission-process-event` and the `permission-process-event` codelist, so only event values allowed for `national-public-view` are extracted.

The extraction process can source the data from a database, document register, event log, validated payload or another internal representation. The standard defines the required output and rules, not the internal implementation.

---

## Annex: document publication status

The main example of row-by-row inclusion is `planning-application-document`. The standard records whether each document is suitable for public availability using `public-register-status`.

This status is part of the planning application data, not just metadata in the extraction schema, because the decision has value beyond the national public view. It needs to travel with the application record when data moves between systems or authorities.

The field is `public-register-status`, because it describes the authority's decision about whether the document is available through the public register, without making it sound specific only to the national public view.

This field is the proposed solution for [Record document publication decisions](../user-needs/need/dd-need-103.md).

The field is an enum rather than a boolean so the data can distinguish a document that has been actively withheld from a document that has not yet been assessed.

The codelist values are:

- `publish`: the record can be made public
- `withhold`: the record should not be made public
- `not-assessed`: no decision has yet been recorded

Redaction does not need a separate public-register status. If an original document is sensitive but a redacted version can be published, model that as separate document records:

```csv
reference,public-register-status
doc-1,withhold
doc-1-redacted,publish
doc-2,publish
```

The potential follow-up is a field such as `redacted-from`, so the redacted public document can point back to the withheld original.

## Current decisions

- Use `national-public-view.schema.md` as the entry point for the national public view.
- Put `specification-profile: national-public-view` at the top level.
- Treat presence in `national-public-view.schema.md` as the inclusion mechanism for datasets and fields.
- Use `record-inclusion` for datasets where only some records should be extracted.
- For the MVP, support `record-inclusion` with a single controlling field.
- Put `public-register-status` on `planning-application-document` for the MVP.
- Exclude `withhold` document records from the national public view entirely.
- Do not track who made the publication decision or when unless verified needs show this is required.

## Remaining questions

- Should `national-public-view.schema.md` duplicate selected field descriptions, as `planning-application-data.schema.md` does, or should it reference canonical dataset fields more tersely?
- Should the rule be called `record-inclusion`, `include-if`, `where` or something else?
- Is the national public view always a subset of the local authority's public view, or can the national view require something that the authority would not otherwise publish locally?
