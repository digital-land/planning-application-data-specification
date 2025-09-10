---
description: Details of any conflict of interest that may exist between the applicant
  and planning authority.
end-date: ''
entry-date: 2025-06-16
fields:
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - reserved-matters
      - demolition-con-area
      - lbc
      - advertising
      - ldc
      - consent-under-tpo
      - non-material-amendment
      - pip
      - extraction-oil-gas
      - notice-trees-in-con-area
  field: conflict-to-declare
  required: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - reserved-matters
      - demolition-con-area
      - lbc
      - advertising
      - ldc
      - consent-under-tpo
      - non-material-amendment
      - pip
      - extraction-oil-gas
      - notice-trees-in-con-area
  field: conflict-person-name
  required-if:
  - field: conflict-to-declare
    value: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - reserved-matters
      - demolition-con-area
      - lbc
      - advertising
      - ldc
      - consent-under-tpo
      - non-material-amendment
      - pip
      - extraction-oil-gas
      - notice-trees-in-con-area
  field: conflict-details
  required-if:
  - field: conflict-to-declare
    value: true
module: conflict-of-interest
name: Conflict of interest
rules:
- rule: conflict-person-name must match a name provided in applicants or agent sections
---