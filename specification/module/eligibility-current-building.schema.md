---
module: eligibility-current-building
name: Eligibility current building
description: |
  Eligibility criteria related to current building status including construction period,
  storey additions, permitted development use, and site location constraints
fields:
  - field: was-constructed-btw-1948-2018
    required: true
  - field: has-additional-storeys
    required: true
  - field: was-use-granted-by-pdr
    required: true
  - field: is-site-in-restricted-area
    required: true
rules:
  - description: "Building must be constructed in eligible construction period"
    rule: "was-constructed-btw-1948-2018 == true (required for application to proceed)"
  - description: "No additional storeys should have been previously added"
    rule: "has-additional-storeys == false (required for application to proceed)"
  - description: "Current use must not be from permitted development rights"
    rule: "was-use-granted-by-pdr == false (required for application to proceed)"
  - description: "Site must not be in restricted area"
    rule: "is-site-in-restricted-area == false (required for application to proceed)"
  - description: "All eligibility criteria must be met for application to proceed"
    rule: "was-constructed-btw-1948-2018 == true AND has-additional-storeys == false AND was-use-granted-by-pdr == false AND is-site-in-restricted-area == false"
entry-date: 2025-07-15
end-date: ''
---
