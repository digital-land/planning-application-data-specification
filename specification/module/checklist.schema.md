---
description: Checking whether all the requirements of the form have been met, such
  as proof of payment or supporting documentation.
end-date: ''
entry-date: 2025-06-12
fields:
- field: national-req-types
  required: true
module: checklist
name: Checklist
rules:
- rule: All values must be from the national-requirement-type codelist
- rule: Values must be valid for the current application type
---