---
module: permission-type
name: Permission type module
description: |
  Information about the permissions being applied for
fields:
  - field: permission-types
    required: true
  - field: related-proposals
  - field: other-details
  - field: will-consolidate-permissions
    required: true
  - field: details
    description: Details about the consolidation or update of permissions
    required-if:
      - field: will-consolidate-permissions
        value: true
entry-date: 2025-09-09
end-date: ''
---

