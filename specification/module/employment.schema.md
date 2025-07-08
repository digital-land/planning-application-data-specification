---
module: employment
name: Employment
description: |
  Module for capturing information about employment impacts of a development 
  proposal, including existing and proposed employee counts
fields:
  - field: existing-employees
    required: true
  - field: proposed-employees
    required: true
  - field: employment-impact
rules:
  - "Existing-employees is required for all non-residential applications"
  - "Proposed-employees is required if the proposal affects employment capacity"
  - "Employment-impact is calculated based on existing and proposed values"
  - "Full-time and part-time employee counts must be positive integers or 0"
  - "FTE is calculated as full-time + (part-time ÷ 2)"
entry-date: 2025-07-08
end-date: ''
---
