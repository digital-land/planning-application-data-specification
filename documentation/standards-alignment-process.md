# Standards alignment process

This note explains how we identify standards, vocabularies and data models that may be relevant to the planning application specifications, and how we record alignment where it is useful.

## Intent

The intent is to make sure the specification is not designed in isolation.

Where an existing standard or vocabulary is relevant, we should:

- consider whether it helps explain or structure the planning data
- align where the meaning is genuinely close
- record the relationship clearly
- avoid claiming conformance where we are only using a concept as a reference point

The planning application specification still needs to model the planning process in a way that works for planning authorities, applicants, agents and downstream users. Alignment with another standard should support that aim, not override it.

## How alignment should be handled

When a potentially relevant standard is found:

1. Capture it as a candidate reference.
2. Record what concept, field, dataset or codelist it may relate to.
3. Decide whether the relationship is useful enough to record.
4. If it is useful, add a short semantic note to the relevant schema or documentation.
5. If it affects the model shape, record the decision in a design decision note.
6. If it is not useful now, leave it as a candidate rather than forcing alignment.

Where we record semantic alignment in schemas, we should be clear about the relationship. For example, use `closeMatch` where the concepts are similar but not identical.

## Candidate standards and vocabularies

These are standards, vocabularies and sources that may be relevant in different parts of the specification.

| Candidate | Possible relevance | Current position |
| --- | --- | --- |
| `schema.org` | Common vocabulary for actions, decisions, documents, events and legal concepts. | Used in semantic notes for some decision-stage datasets. |
| buildingSMART IFC | Built environment concepts such as sites, documents and events. | Used as a conceptual reference where it helps explain decision-stage datasets. |
| WGS84 / UK government location point standard | Coordinates and location exchange. | Used for latitude and longitude fields and location decisions. |
| OGC Well-known text / ISO geometry conventions | Geometry representation for boundaries and spatial data. | Reflected in field datatype documentation for geometry-like values. |
| JSON Schema | Machine-readable validation of generated schemas. | Used for generated JSON Schema, currently Draft-07 for compatibility. |
| planning.data.gov.uk specification | Existing planning data conventions, datatypes and codelists. | Reused where possible, with further datatype alignment still being reviewed. |

This list is not exhaustive. It is a working list of potentially relevant references, not a claim that the specification conforms to each one.

## Alignment captured so far

Some alignment has already been captured in the specification, mainly through semantic notes in decision-stage dataset schemas.

Examples include:

- `planning-application` aligns to `schema.org` `ApplyAction` as a close match.
- `decision-notice` aligns to `schema.org` `Decision`, with a link back to the application it determines.
- `planning-application-document` aligns to `schema.org` `DigitalDocument` and buildingSMART IFC `IfcDocumentInformation`.
- `planning-permission-timeline` aligns to `schema.org` `Event` and is conceptually aligned with IFC `IfcEvent`.
- `planning-condition` aligns to `schema.org` `Legislation` as a close match for reusable condition clauses.
- `decision-condition` aligns to `schema.org` `LegalAction` for applying a condition to a specific decision.
- `site` aligns to IFC `IfcSite`, while noting that a planning site is an administrative and legal grouping rather than only a physical construction site.
- `section-106` aligns to `schema.org` `LegalDocument`.

There are also design decisions and field notes that align with existing conventions:

- location coordinate decisions use WGS84 and reference the UK government location point standard
- geometry datatype documentation references Well-known text and ISO geometry conventions
- generated JSON Schema documentation explains the use of JSON Schema Draft-07
- codelist and datatype work reuses planning.data.gov.uk conventions where practical

## What this process is not

This process does not mean:

- every external standard must be adopted
- every field needs a semantic mapping
- a loose conceptual similarity is enough to change the planning model
- semantic notes are a substitute for clear field names, descriptions and validation rules

The aim is pragmatic alignment: use existing standards where they help, record useful relationships and keep the planning specification clear in its own terms.

## Next steps

- Keep a lightweight list of candidate standards or vocabularies when they are raised.
- Add semantic notes only where the relationship is clear and useful.
- Use design decision records when alignment affects the model shape.
- Review candidate references as part of future iterations, especially where decision-stage datasets mature or new publication requirements emerge.

## Suggesting standards to consider

We welcome issues that point us to relevant standards, vocabularies or existing data models that we should consider.

When raising an issue, it helps to include:

- the standard, vocabulary or model being suggested
- which part of the specification it may relate to
- what alignment or connection you think we should consider
- any practical reason this would help implementers, planning authorities or data users

Suggestions do not need to prove that the specification should adopt the standard. They can simply flag something relevant that we should assess.
