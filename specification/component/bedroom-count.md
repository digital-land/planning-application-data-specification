---
component: bedroom-count
name: Bedroom count
description: |
  Structure for counting units by bedroom number, allowing for unknown bedroom counts
fields:
  - field: no-bedrooms-unknown
    required: true
  - field: no-of-bedrooms
    required-if:
      - field: no-bedrooms-unknown
        value: false
  - field: units
    required: true
entry-date: 2025-07-17
end-date: ''
---
