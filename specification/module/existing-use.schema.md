---
module: existing-use
name: Existing use
description: |
  Information about the current and previous use of the site, including contamination status and supporting documents.
fields:
  - field: existing-use-details
    required: true
  - field: site-vacant
    required: true
  - field: last-use-details
    required: false
    required-if:
      - field: site-vacant
        value: true
  - field: last-use-end-date
    required: false
    required-if:
      - field: site-vacant
        value: true
  - field: is-contaminated-land
    required: true
  - field: is-suspected-contaminated-land
    required: true
  - field: proposed-use-contamination-risk
    required: true
  - field: contamination-assessment
    required: false
    required-if:
      any:
        - field: is-contaminated-land
          value: true
        - field: is-suspected-contaminated-land
          value: true
        - field: proposed-use-contamination-risk
          value: true
rules:
  - rule: "last-use-details and last-use-end-date are required if site-vacant is true"
  - rule: "contamination-assessment is required if any of is-contaminated-land, is-suspected-contaminated-land, or proposed-use-contamination-risk is true"
entry-date: 2025-08-18
end-date: ''
---
