# Required national public view output and rules for deriving it

The national public view is a defined extraction from the wider planning
application data standard. It says what must be published, without prescribing
how a planning authority or supplier stores or processes the underlying data.

The entry point is
[`national-public-view.schema.md`](../specification/national-public-view.schema.md).
It lists the datasets and fields in the view and, where necessary, the rules
for deciding which records to include.

## Why use an extraction

An extraction is safer than treating the public view as a complete record with
some parts hidden. Nothing enters the national public view unless the standard
explicitly says it should be extracted.

The schema reuses the canonical dataset and field definitions. Those definitions
remain the source of datatypes and relationships; the public-view schema selects
what is published. A supplier can derive that output from a database, document
register, event log, validated payload or another internal representation.

## What the schema includes

- A dataset is included when it appears in `national-public-view.schema.md`.
- Within an included dataset, only the fields listed in the schema are included.
- A dataset with no `record-inclusion` rule contributes all of its records.

For example, `planning-application` is listed without a record rule, so every
planning-application record is included with only its listed fields. A dataset
that is not listed is not part of the output.

## Record inclusion

`record-inclusion` is a special attribute that filters the records within a dataset so that only certain records are included in the "view".

- **No rule:** include every record from that dataset, but only its listed fields.
- **Literal values:** include a record only when the value in a controlling
  field matches one of the values listed in the rule.
- **Codelist values:** include a record only when the value in a controlling
  field is allowed by a codelist usage profile.

Record inclusion is opt-in: if a rule is present, a record is excluded unless it
matches the rule.

### Pattern 1: Include records by matching field values (literal values)

This pattern uses a field on each source record as the controlling field. The idea is to read
its value and include the record only when it matches one of the literal values
in `include-values`.

Use it whenever the record itself holds the decision or status that controls
inclusion. For example, the following rule includes a document only when its
`public-register-status` is `publish`. Blank, `withhold` and any other value
do not match, so the document stays out of the view.

```yaml
record-inclusion:
  description: Include only documents the planning authority has decided may appear on the public register.
  field: public-register-status
  include-values:
    - publish
```

The controlling field is input to the extraction, not automatically part of its
output. `public-register-status` need not be published merely because it is used
to decide whether to publish a document.

### Pattern 2: Include records using a codelist usage profile (codelist values)

This pattern also uses a controlling field on each source record. Instead of
listing literal values, the rule names a canonical codelist and a specification
profile. Resolve the values allowed by that profile in the codelist's usage
table, then include only records whose controlling-field value matches one of
those values.

Use it when inclusion depends on whether a category of record belongs in the
view. For example, the following rule includes timeline records only when their
`permission-process-event` is selected for the `national-public-view` profile.

```yaml
record-inclusion:
  description: Include only permission process events selected for the national public view.
  field: permission-process-event
  include-values:
    codelist: permission-process-event
    specification-profile: national-public-view
```

The canonical codelist defines the possible values, and the usage table defines
which values are allowed for the specified profile. The profile belongs inside
the rule because it resolves that specific codelist selection. This keeps the
rule self-contained and allows a future view to use different profiles for
different rules if needed.

This reuses the existing [codelist usage pattern](codelist-usage.md): codelists
define concepts, while usage tables define context-specific subsets.

## Extraction steps

1. Open `national-public-view.schema.md`.
2. For each listed dataset, find the corresponding source records.
3. Retain only the listed fields.
4. Include all records if there is no `record-inclusion` rule.
5. For literal `include-values`, include only records whose controlling field has one of those values.
6. For a codelist `include-values`, use that rule's `codelist` and `specification-profile` to find the allowed values in the usage table, then include only matching records.
7. Produce an output containing only the datasets, records and fields selected by these rules.

## Document publication status

`planning-application-document` uses `public-register-status` to record whether
each document is suitable for public availability. It is part of the planning
application data, not just extraction metadata, because the decision needs to
travel with the application when data moves between systems or authorities.

The field is an enum rather than a boolean so that it distinguishes an actively
withheld document from one that has not yet been assessed:

- `publish`: the record can be made public
- `withhold`: the record should not be made public
- `not-assessed`: no decision has yet been recorded

If a sensitive document can be published after redaction, model the original and
redacted version as separate document records. Mark the original `withhold` and
the redacted document `publish`.

`public-register-status` is the proposed solution for [Record document
publication decisions](../user-needs/need/dd-need-103.md).

## Current decisions

- Use `national-public-view.schema.md` as the entry point for the national public view.
- Treat its listed datasets and fields as the publication boundary.
- Use `record-inclusion` where only some records in an included dataset should be extracted.
- For the MVP, support one controlling field per `record-inclusion` rule.
- Put a plain-English `description` on each rule.
- Put the profile used for a codelist selection inside that rule's `include-values`.
- Exclude document records unless `public-register-status` is `publish`.

## Remaining questions

- Should the public-view schema duplicate selected field descriptions or refer to canonical dataset fields more tersely?
- Is `record-inclusion` the clearest name for the rule?
- Is the national public view always a subset of the local authority's public view, or can it require something that the authority would not otherwise publish locally?
