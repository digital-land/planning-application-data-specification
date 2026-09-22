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
  requirement-level: SHOULD
  description: "A URL to the completed application form"
- field: documentation-url
  requirement-level: MUST
  description: "The URL where supporting documents for the application can be accessed"
- field: notes
  requirement-level: MAY
  description: Optional notes that provide additional context about the planning application
- field: description
  requirement-level: MUST
  description: "The description of the proposed development"
- field: name
  requirement-level: SHOULD
  description: A plain-language label for the planning application so it can be identified without relying on its reference
- field: application-types
  requirement-level: MUST
  description: "One or more codelist values describing the application type"
- field: site
  dataset: site
  requirement-level: MUST
  description: "The reference for the related site"
- field: received-date
  requirement-level: MUST
  description: "The date the planning authority received the application"
- field: planning-authority
  requirement-level: MUST
  description: Identifier of the planning authority that received this planning application
- field: officer-name
  name: Case officer
  description: Name of the planning officer responsible for handling the application
- field: development-scale
  requirement-level: SHOULD
  applies-if:
    application-types:
      in:
      - full
      - outline-all
      - outline-some
  description: "The local planning authority's classification of a full or outline planning application by development scale"
- field: planning-performance-agreement
  requirement-level: MUST
  description: "Whether the application was subject to a Planning Performance Agreement"
- field: withdrawn-date
  requirement-level: SHOULD
  description: "The date the planning application was withdrawn"
- field: linked-applications
  dataset: planning-application
  requirement-level: MUST
  description: "References to earlier applications this application directly links to"
- field: reference
  requirement-level: MUST
  description: "The reference for the planning application"
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
