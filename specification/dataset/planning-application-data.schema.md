---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: planning-application-data
description: Links a planning application to authoritative structured application data as submitted and, where applicable, as validated.
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: 2026-06-04
fields:
  - field: reference
    description: Unique identifier for the planning application data record
  - field: planning-application
    description: Reference to the planning application this data relates to
  - field: submitted-data-uri
  - field: validated-data-uri
key-field: ''
licence: ogl3
name: Planning application data
notes: |
  There should be one planning-application-data record for each planning
  application.

  `submitted-data-uri` is required for every record.

  `validated-data-uri` is required when the related planning application has a
  planning-permission-timeline record with the `found-valid` process event. It
  may be empty where an application has not been found valid.
phase: alpha
plural: Planning application data
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
  - administrative
  - development
typology: document
version: ''

semantics:
  links:
    - predicate: "https://schema.org/about"
      target_dataset: planning-application
      via_field: planning-application
      target_field: reference
      description: >
        Each record identifies authoritative structured data for the referenced
        planning application.
---

The dataset records the source data artefacts from which different views can be
constructed. It identifies the application data as first received and, where
the application was found valid, the data accepted through planning validation.

The URI fields do not prescribe how the artefacts are stored or produced. They
must allow an authorised user or system to identify and retrieve the correct
authoritative artefact.

See [Decision: Reference authoritative application artefacts without prescribing
storage](../../documentation/design-decisions/0018-reference-authoritative-application-artefacts-without-prescribing-storage.md).
