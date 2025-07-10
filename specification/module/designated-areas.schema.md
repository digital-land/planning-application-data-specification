---
module: designated-areas
name: Designated areas
description: |
  Module for capturing information about designated areas that apply to a development site
fields:
  - field: designations
    required: true
rules:
  - "Multiple selections allowed from the designation codelist"
  - "If none of the designated areas apply to the site, the array should be empty"
  - "Each designation in the array must be unique (no duplicates)"
entry-date: 2025-01-02
end-date: ''
---
