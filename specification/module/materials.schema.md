---
description: What materials are being used for the proposed development
end-date: ''
entry-date: 2025-06-13
fields:
- field: proposal-material-details
  required: true
- field: building-elements
  required-if:
  - field: proposal-material-details
    value: true
- field: providing-additional-material-information
  required: true
- field: supporting-documents
  required-if:
  - field: providing-additional-material-information
    value: true
module: materials
name: Materials
notes: |
  If no material details are applicable to the proposal, the applicant answers that at section level.
  If material details are applicable, they add entries only for the relevant building elements.
  They should not be expected to work through every building element and mark each remaining one not applicable.
rules:
- rule: Each building-element must have a unique building-element-type
- rule: 'At least one of: existing-materials, proposed-materials or materials-not-known
    must be provided for each building-element'
- rule: materials-not-known cannot be true if existing-materials or proposed-materials
    is provided
- rule: supporting-documents must reference valid documents in the application
---
