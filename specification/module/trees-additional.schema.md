---
module: trees-additional
name: Trees additional information
description: |
  Additional information about trees on the site, including condition concerns, 
  damage reports, and supporting documentation
fields:
  - field: advice-from-authority
  - field: condition-concerns
    required: true
    applies-if:
      application-type:
        in: [consent-under-tpo]
  - field: causing-subsidence
    required: true
    applies-if:
      application-type:
        in: [consent-under-tpo]
  - field: causing-structural-damage
    required: true
    applies-if:
      application-type:
        in: [consent-under-tpo]
  - field: supporting-documents
    description: Documents supporting the work required to trees
    required: true
rules:
  - rule: "If condition-concerns is true then Arboricultural impact assessment document is required"
  - rule: "If causing-subsidence is true then Subsidence Report is required" 
  - rule: "If causing-structural-damage is true then a Structural damage report is required"
  - rule: "supporting-documents must include sketch plan, supporting documents, reports, or photographs"
  - rule: "supporting-documents must include any documents required based on condition concerns, subsidence, or structural damage"
entry-date: 2025-07-01
end-date: ''
---
