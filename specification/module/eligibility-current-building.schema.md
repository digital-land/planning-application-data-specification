---
module: eligibility-current-building
name: Eligibility current building
description: |
  Eligibility criteria related to current building status including construction period,
  storey additions, permitted development use, and site location constraints
fields:
  - field: in-building-construction-period
    required: true
  - field: has-additional-storeys
    required: true
  - field: was-use-granted-by-pdr
    required: true
  - field: site-location-constraint
    required: true
validation:
  - description: "Building must be constructed in eligible construction period"
    rule: "in-building-construction-period == true (required for application to proceed)"
  - description: "No additional storeys should have been previously added"
    rule: "has-additional-storeys == false (required for application to proceed)"
  - description: "Current use must not be from permitted development rights"
    rule: "was-use-granted-by-pdr == false (required for application to proceed)"
  - description: "Site must not be in restricted area"
    rule: "site-location-constraint == false (required for application to proceed)"
  - description: "All eligibility criteria must be met for application to proceed"
    rule: "in-building-construction-period == true AND has-additional-storeys == false AND was-use-granted-by-pdr == false AND site-location-constraint == false"
entry-date: 2025-07-15
end-date: ''
---
