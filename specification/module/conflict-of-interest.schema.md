---
module: conflict-of-interest
name: Conflict of interest
description: |
  Information about any conflicts of interest between the applicant/agent and the planning authority,
  including relationships with staff or elected members
fields:
  - field: conflict-to-declare
    required: true
    applies-if:
      - application-type:
          in: [hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area]
  - field: conflict-person-name
    required-if:
      - field: conflict-to-declare
        value: true
    applies-if:
      - application-type:
          in: [hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area]
  - field: conflict-details
    required-if:
      - field: conflict-to-declare
        value: true
    applies-if:
      - application-type:
          in: [hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area]
rules:
  - rule: "conflict-person-name must match a name provided in applicants or agent sections"
entry-date: 2025-06-16
end-date: ''
---
