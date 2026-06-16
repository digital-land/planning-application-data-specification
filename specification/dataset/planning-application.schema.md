---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: planning-application
description: 'Records of applications submitted to planning authorities'
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: '2025-12-18'
fields:
- field: document-url
  description: A url to the completed application form
- field: documentation-url
  description: URL where supporting documents for the application can be accessed
- field: description
  description: The description of the proposed development
- field: application-types
- field: site
- field: received-date
  description: Date the planning authority received the application
- field: planning-authority
  description: Identifier of the planning authority that received this planning application
- field: development-scale
  applies-if:
    application-types:
      in:
      - full
      - outline-all
      - outline-some
- field: planning-performance-agreement
- field: withdrawn-date
- field: linked-applications
- field: reference
key-field: ''
licence: ogl3
name: Planning application
notes: 
phase: alpha
plural: Planning applications
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- administrative
- development
- housing
typology: document
version: 

semantics:
  aligns_to:
    - iri: "https://schema.org/ApplyAction"
      relation: "closeMatch"
      description: "A planning application represents a request to a public authority for permission to carry out development."
---
