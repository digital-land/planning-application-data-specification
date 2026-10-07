---
description: The grade of any listed building affected by the proposed development.
end-date: ''
entry-date: 2025-01-05
fields:
- field: listed-building-grade-known
  required: true
- field: listed-building-grade
  required: true
  applies-if:
    field: listed-building-grade-known
    value: true
- field: listed-building
- description: Source of the listed building grade information
  field: provided-by
module: lb-grade
name: Listed building grade
rules:
- rule: If listed-building-grade-known is true, supply a grade from the listed-building-grade codelist
- rule: If listed-building-grade-known is false, the applicant is declaring that they do not know the grade and must not supply listed-building-grade
- rule: If listed-building is provided, it must reference a valid listed building
---
