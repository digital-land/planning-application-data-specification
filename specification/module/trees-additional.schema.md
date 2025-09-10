---
description: Further details of any issues relating to trees on the site
end-date: ''
entry-date: 2025-07-01
fields:
- field: advice-from-authority
- applies-if:
    application-type:
      in:
      - consent-under-tpo
  field: condition-concerns
  required: true
- applies-if:
    application-type:
      in:
      - consent-under-tpo
  field: causing-subsidence
  required: true
- applies-if:
    application-type:
      in:
      - consent-under-tpo
  field: causing-structural-damage
  required: true
- description: Documents supporting the work required to trees
  field: supporting-documents
  required: true
module: trees-additional
name: Trees additional information
rules:
- rule: If condition-concerns is true then Arboricultural impact assessment document
    is required
- rule: If causing-subsidence is true then Subsidence Report is required
- rule: If causing-structural-damage is true then a Structural damage report is required
- rule: supporting-documents must include sketch plan, supporting documents, reports,
    or photographs
- rule: supporting-documents must include any documents required based on condition
    concerns, subsidence, or structural damage
---