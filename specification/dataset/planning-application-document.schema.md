---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: planning-application-document
name: Planning application document
description: Links a planning application to the documents submitted with it.
fields:
  - field: reference
    description: Unique identifier for the document record
  - field: planning-application
    description: Reference to the planning application this document relates to
  - field: name
    description: Title or label used to identify the document
  - field: replaces
    description: Reference to an earlier document record replaced by this document
    dataset: planning-application-document
  - field: document-url
  - field: documentation-url
entry-date: 2026-01-28
end-date: ''
entity-maximum: ''
entity-minimum: ''
key-field: ''
licence: ogl3
notes: |
  `replaces` is a self-reference within the `planning-application-document` dataset.
  The explicit `dataset: planning-application-document` on the field usage is
  intentional and shows that the field must reference another document record in
  the same dataset, rather than an arbitrary string or a record from a different
  dataset.
phase: alpha
plural: Planning application document
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- administrative
- development
typology: document
version:

semantics:
  aligns_to:
    - iri: "https://schema.org/DigitalDocument"
      relation: "closeMatch"
      description: >
        Each record represents a digital document submitted as part of a planning
        application.

    - iri: "https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/OWL#IfcDocumentInformation"
      relation: "closeMatch"
      description: >
        This dataset corresponds to the IFC idea of document information, but in a
        lighter form, focused on identifying and referencing planning application
        documents rather than managing their full lifecycle.
    
  links:
    - predicate: "https://schema.org/isPartOf"
      target_dataset: planning-application
      via_field: planning-application
      target_field: reference
      description: >
        Each document is part of a planning application and supports its assessment.
    - predicate: "http://purl.org/dc/terms/replaces"
      target_dataset: planning-application-document
      via_field: replaces
      target_field: reference
      description: >
        Where present, this document replaces an earlier planning-application-document
        record for the same planning application.
---

A record of a document submitted as part of a planning application
One row per file
Plans, reports, statements, drawings, notices, certificates, etc.

Example:

```yaml
dataset: planning-application-document
reference: doc-002
planning-application: pa-1001
name: Proposed plans revision B
document-url: https://example.org/documents/proposed-plans-v2.pdf
documentation-url: https://example.org/applications/pa-1001/documents/doc-002
replaces: doc-001
```

In this example `doc-002` is the newer document record and it replaces the
earlier document record `doc-001` for the same planning application. The `name`
field gives a readable title so users can recognise the document without having
to inspect the file directly.
