---
module: flood-risk-assessment
name: Flood risk assessment
description: |
  Information about flood risk assessments for planning applications including flood risk area status, 
  data sources, assessment documents, watercourse proximity, flood risk impacts, and surface water disposal methods
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
rules:
  - rule: "flood-risk-assessment document reference is required when flood-risk-area is true"
  - rule: "surface-water-disposal must contain at least one disposal method"
entry-date: 2025-07-17
end-date: ''
---
