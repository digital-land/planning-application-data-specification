---
module: checklist
name: Checklist
description: |
  Identifies the national requirement types that apply to this application type
fields:
  - field: national-req-types
    required: true
rules:
  - rule: "All values must be from the national-requirement-type codelist"
  - rule: "Values must be valid for the current application type"
entry-date: 2025-06-12
end-date: ''
---
