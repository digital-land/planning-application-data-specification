---
description: Details of any 'designated area' the develpoment site is on, such as
  a Conservation Area or National Park.
end-date: ''
entry-date: 2025-01-02
fields:
- field: designations
  required: true
module: designated-areas
name: Designated areas
rules:
- Multiple selections allowed from the designation codelist
- If none of the designated areas apply to the site, the array should be empty
- Each designation in the array must be unique (no duplicates)
---