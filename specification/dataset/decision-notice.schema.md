---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: decision-notice
description: 'The decision notice dataset records the issued decision for a planning application'
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: '2025-12-18'
fields:
- field: decision
  requirement-level: MUST
  description: "The decision outcome for the planning application"
- field: decision-date
  requirement-level: MUST
  description: "The date the decision notice was issued"
- field: organisation
  requirement-level: MUST
  description: "Identifier of the organisation issuing the decision notice (planning authority, Planning Inspectorate or Secretary of State)"
- field: decision-maker
  requirement-level: MUST
  description: "The category of person or body that formally made the decision"
- field: planning-officer-recommendation
  requirement-level: SHOULD
  description: "The recommendation made by the planning officer for this application"
- field: document-url
  requirement-level: SHOULD
  description: "The URL to the published decision notice"
- field: documentation-url
  requirement-level: MUST
  description: "The URL of the page where the decision notice can be found"
- field: notes
  requirement-level: MAY
  description: Optional notes that provide additional context about the decision notice
- field: planning-application
  dataset: planning-application
  requirement-level: MUST
  description: "The reference for the related planning application"
- field: reference
  requirement-level: MUST
  description: "The reference for the decision notice"
key-field: ''
licence: ogl3
name: Decision notice
notes: 
phase: alpha
plural: Decision notices
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
    - iri: "https://schema.org/Decision"
      relation: "closeMatch"
      description: >
        A planning decision represents the outcome of a planning application,
        made by a planning authority, determining whether permission is granted,
        refused, or otherwise disposed of.
  links:
    - predicate: "https://schema.org/result"
      target_dataset: planning-application
      via_field: planning-application
      target_field: reference
      description: "This decision notice relates to the planning application it determines."
---
