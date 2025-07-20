---
module: immunity-from-listing
name: Immunity from listing
description: |
  Details about certificate of immunity applications and their results
fields:
  - field: cert-of-immunity-sought
    required: true
  - field: application-result
    required-if:
      - field: cert-of-immunity-sought
        equals: "yes"
rules:
  - rule: "application-result is required when cert-of-immunity-sought is 'yes'"
entry-date: 2025-07-01
end-date: ''
---
