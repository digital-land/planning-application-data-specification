---
description: Results of any flood risk assessments made for the development site
end-date: ''
entry-date: 2025-07-17
fields:
- field: flood-risk-area
  required: true
- field: data-provided-by
- field: flood-risk-assessment
  required-if:
  - field: flood-risk-area
    value: true
- field: within-20m-watercourse
  required: true
- field: increases-flood-risk
  required: true
- field: surface-water-disposal
  required: true
module: flood-risk-assessment
name: Flood risk assessment
rules:
- rule: flood-risk-assessment document reference is required when flood-risk-area
    is true
- rule: surface-water-disposal must contain at least one disposal method
---