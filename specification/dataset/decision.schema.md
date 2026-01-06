---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: decision
description: 'The decision dataset records what decision was made on a planning application'
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: '2025-12-18'
fields:
- field: decision
- field: decision-date
- field: organisation
  description: Identifier of the organisation issuing the decision notice (planning authority, Planning Inspectorate, or Secretary of State)
- field: planning-application
- field: reference
key-field: ''
licence: ogl3
name: Decision
paint-options: ''
phase: alpha
plural: Decisions
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- administrative
- development
typology: document
version: 
wikidata: ''
wikipedia: ''

semantics:
  aligns_to:
    - iri: "https://schema.org/Decision"
      relation: "closeMatch"
      description: >
        A planning decision represents the outcome of a planning application,
        made by a planning authority, determining whether permission is granted,
        refused, or otherwise disposed of.
  links:
    - predicate: "https://schema.org/result"   # decision -> (thing it results in / relates to)
      target_dataset: planning-application
      via_field: planning-application
      target_field: reference
      description: "This decision relates to the planning application it determines."
---
