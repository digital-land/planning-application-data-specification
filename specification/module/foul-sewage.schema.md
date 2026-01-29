---
description: How waste water will leave the property as part of the proposed development
end-date: ''
entry-date: 2025-07-09
fields:
- field: has-new-disposal-arrangements
  required: true
- field: foul-sewage-disposal-types
  required-if:
    - field: has-new-disposal-arrangements
      value: true
- field: produce-foul-sewage
  applies-if:
    application-type:
      in:
        - extraction-oil-gas
  required: true
- field: connect-to-drainage-system
  applies-if:
    application-type:
      in:
        - full
        - outline-some
        - technical-details-consent
  required: true
- field: connect-to-drainage-system-oil-gas
  applies-if:
    application-type:
      in:
        - extraction-oil-gas
  required: true
- field: supporting-documents
  description: References to plans or drawings showing details of the existing drainage
    system
module: foul-sewage
name: Foul sewage disposal
rules:
- description: supporting-documents is required when connect-to-drainage-system is
    true
  rule: if connect-to-drainage-system == true then supporting-documents is required
- description: supporting-documents is required for extraction-oil-gas applications
  rule: if application-type includes 'extraction-oil-gas' then supporting-documents
    is required
- description: supporting-documents is required when connect-to-drainage-system-oil-gas
    is yes
  rule: if connect-to-drainage-system-oil-gas == 'yes' then supporting-documents
    is required
- description: each document in supporting-documents must have a `reference` that
    matches a document in application.documents
  rule: each document in supporting-documents must have a `reference` that matches
    a document in application.documents
---
