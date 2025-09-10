---
description: Any additional relevant information about the development site.
end-date: ''
entry-date: 2025-06-26
fields:
- field: site-area
  required: true
- field: existing-use
  required: true
- field: known-constraints
  required: true
- field: supporting-documents
  required-if:
  - field: known-constraints
    operator: not_empty
module: site-info
name: Site information
rules:
- rule: supporting-documents is required if known-constraints is not empty
- rule: site-area value should ideally be calculated from site boundary
- rule: 'site-area unit must be one of: m2, hectares'
- rule: 'provided-by must be one of: Applicant, System/Service'
- rule: use must reference valid use class or be 'other' or 'sui'
- rule: specified-use is required if use is 'sui' or 'other'
- rule: floorspace must be numeric value in m2
---