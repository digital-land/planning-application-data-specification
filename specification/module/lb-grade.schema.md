---
description: The grade of any listed building affected by the proposed development.
end-date: ''
entry-date: 2025-01-05
fields:
- field: listed-building-grade
  required: true
  applies-if:
    field: listed-building-grade-unknown
    operator: empty
- field: listed-building-grade-unknown
  required: true
  fixed-value: true
  applies-if:
    field: listed-building-grade
    operator: empty
- field: listed-building
- description: Source of the listed building grade information
  field: provided-by
module: lb-grade
name: Listed building grade
rules:
- rule: Supply either a grade from the listed-building-grade codelist or listed-building-grade-unknown set to true, but not both
- rule: Omit the unknown flag when supplying a grade. Omitting both fields is not an answer
- rule: If listed-building is provided, it must reference a valid listed building
---