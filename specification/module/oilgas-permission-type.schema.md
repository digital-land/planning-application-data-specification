---
module: oilgas-permission-type
name: Oil and gas permission types
description: |
  Module for details about types of onshore oil and gas extraction permissions already received and applying for
fields:
  - field: oilgas-permission-types
    required: true
  - field: related-permissions
    require-if:
  - field: other-details
  - field: will-consolidate-permissions
    required: true
  - field: details
    description: Details about the consolidation or update of permissions
    required-if:
      - field: will-consolidate-permissions
        value: true
  - field: related-proposals
    description: Previous permissions for minerals development on the site (if any)
entry-date: 2025-09-09
end-date: ''
---

