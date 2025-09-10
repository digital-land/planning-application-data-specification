---
description: The grade of any listed building affected by the proposed development.
end-date: ''
entry-date: 2025-01-05
fields:
- field: listed-building-grade
  required: true
- field: listed-building
- description: Source of the listed building grade information
  field: provided-by
module: lb-grade
name: Listed building grade
rules:
- rule: listed-building-grade must be selected from the listed-building-grade codelist
    or 'don't know'
- rule: If listed-building is provided, it must reference a valid listed building
---