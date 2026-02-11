---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-conditions
dataset: decision-condition
description: Records each planning condition attached to a decision so the decision record reflects all legal requirements
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: 2026-01-08
fields:
- field: reference
- field: decision-notice
- field: planning-condition
  description: Reference to the planning condition record linked to the decision
- field: organisation
  description: Identifier of the organisation responsible for this condition within the decision
- field: requested-by
- field: discharged-by
key-field: ''
licence: ogl3
name: Decision condition
paint-options: ''
phase: alpha
plural: Decision conditions
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- administrative
typology: value
version: 
wikidata: ''
wikipedia: ''
notes: ''

semantics:
  aligns_to:
    - iri: "https://schema.org/LegalAction"
      relation: "closeMatch"
      description: >
        Each record represents the application of a planning condition to a specific
        decision, making that condition legally binding for a particular development.
  
  links:
    - predicate: "https://schema.org/isPartOf"
      target_dataset: decision-notice
      via_field: decision-notice
      target_field: reference
      description: >
        Each decision condition forms part of the decision notice and contributes to
        the legal effect of the permission.

    - predicate: "https://schema.org/about"
      target_dataset: planning-condition
      via_field: planning-condition
      target_field: reference
      description: >
        Each decision condition applies a specific planning condition clause to
        a particular decision.
---
