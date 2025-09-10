---
description: What materials are being used for the proposed development
end-date: ''
entry-date: 2025-06-13
fields:
- field: building-elements
  required: true
- field: additional-material-information
  required: true
- field: supporting-documents
  required-if:
  - field: additional-material-information
    value: true
module: materials
name: Materials
rules:
- rule: Each building-element must have a unique building-element-type
- rule: 'At least one of: existing-materials, proposed-materials, materials-not-applicable
    or materials-not-known must be provided for each building-element'
- rule: materials-not-applicable cannot be true if existing-materials or proposed-materials
    is provided
- rule: materials-not-known cannot be true if existing-materials or proposed-materials
    is provided
- rule: supporting-documents must reference valid documents in the application
---