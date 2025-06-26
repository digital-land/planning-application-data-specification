---
component: use
name: Use
description: |
  A specific use class or type of use for a site or building
fields:
  - field: use
    required: true
  - field: specified-use
    required-if:
      - field: use
        value: "sui"
      - field: use
        value: "other"
entry-date: 2025-06-26
end-date: ''
---
