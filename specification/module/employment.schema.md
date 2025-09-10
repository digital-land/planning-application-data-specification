---
description: How the proposed development will impact employment, including existing
  and proposed employee numbers
end-date: ''
entry-date: 2025-07-08
fields:
- field: existing-employees
  required: true
- field: proposed-employees
  required: true
- field: employment-impact
module: employment
name: Employment
rules:
- Existing-employees is required for all non-residential applications
- Proposed-employees is required if the proposal affects employment capacity
- Employment-impact is calculated based on existing and proposed values
- Full-time and part-time employee counts must be positive integers or 0
- FTE is calculated as full-time + (part-time ÷ 2)
---