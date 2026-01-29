---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: planning-permission-timeline
description: Records key events in the processing of a planning application.
start-date: ''
end-date: ''
entry-date: 2026-01-28
entity-minimum: ''
entity-maximum: ''
fields:
  - field: reference
    description: Unique identifier for the timeline entry
  - field: planning-application
  - field: permission-process-event
  - field: event-date
key-field: ''
licence: ogl3
name: Planning permission timeline
phase: alpha
plural: Planning permission timeline
prefix: ''
realm: dataset
replacement-dataset: ''
themes:
  - development
  - administrative
typology: administrative
version: ''
notes: 

semantics:
  aligns_to:
    - iri: "https://schema.org/Event"
      relation: "closeMatch"
      description: >
        Each record represents a dated event in the processing of a planning application.

    - iri: "https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcEvent.htm"
      relation: "closeMatch"
      description: >
        This dataset is conceptually aligned with the IFC IfcEvent concept, but focused on
        planning permission process events rather than BIM work plans.
      
  links:
    - predicate: "https://schema.org/about"
      target_dataset: planning-application
      via_field: planning-application
      target_field: reference
      description: >
        Each timeline entry is about the referenced planning application.
---
