---
component: existing-use-detail
name: Existing use detail
description: |
  Information about a specific existing use on the site, including use class,
  additional details, and which part of the land it relates to
fields:
  - field: use
    required: true
  - field: use-details
    required-if:
      - field: use
        value: "sui"
      - field: use
        value: "other"
  - field: land-part
    required: true
entry-date: 2025-07-09
end-date: ''
notes: use-details conditions needs to be an or condition not an and condition
---
