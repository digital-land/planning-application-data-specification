---
description: Whether the applicant has obtained a Certificate of Immunity (COI) meaning
  the building in question cannot be listed
end-date: ''
entry-date: 2025-07-01
fields:
- field: cert-of-immunity-sought
  required: true
- field: application-result
  required-if:
  - equals: 'yes'
    field: cert-of-immunity-sought
module: immunity-from-listing
name: Immunity from listing
rules:
- rule: application-result is required when cert-of-immunity-sought is 'yes'
---