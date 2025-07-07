---
module: adj-premises
name: Adjacent premises
description: |
  Information about addresses of properties adjacent to the development site
fields:
  - field: addresses
    required: true
rules:
  - rule: "At least one address must be provided"
  - rule: "Each address must have address-text as minimum requirement"
  - rule: "UPRN should be provided where known for accurate property identification"
entry-date: 2025-07-07
end-date: ''
---
