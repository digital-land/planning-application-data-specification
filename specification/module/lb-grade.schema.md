---
module: lb-grade
name: Listed building grade
description: |
  Information about the grade of listed buildings affected by the planning application
fields:
  - field: listed-building-grade
    required: true
  - field: listed-building
  - field: provided-by
    description: Source of the listed building grade information
rules:
  - rule: "listed-building-grade must be selected from the listed-building-grade codelist or 'don't know'"
  - rule: "If listed-building is provided, it must reference a valid listed building"
entry-date: 2025-01-05
end-date: ''
---
