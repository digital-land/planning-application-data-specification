---
component: non-residential-use
name: Non-residential use
description: |
  Structure for defining non-residential use amounts, which can be expressed as 
  floorspace or site area with exact values or ranges
fields:
  - field: non-residential-measurement-type
    required: true
    description: Type of measurement being provided (floorspace or site-area)
  - field: exact-value
    description: Exact figure of non-residential use
  - field: min
    description: Lower bound of non-residential use for ranges
  - field: max
    description: Upper bound of non-residential use for ranges
rules:
  - rule: either `extact-value` or `min` and `max` to be provided
entry-date: 2025-06-26
end-date: ''
---
