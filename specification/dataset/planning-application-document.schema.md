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
  - field: document-url
  - field: documentation-url
entry-date: 2026-01-28
end-date: ''
entity-maximum: ''
entity-minimum: ''
key-field: ''
licence: ogl3
notes: 
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
---

A record of a document submitted as part of a planning application
One row per file
Plans, reports, statements, drawings, notices, certificates, etc.
