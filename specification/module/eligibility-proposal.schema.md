---
module: eligibility-proposal
name: Eligibility proposal
description: |
  Eligibility criteria related to proposal design and construction including storey construction,
  height restrictions, roof specifications, and material requirements
fields:
  - field: principal-part-only
    required: true
  - field: ceiling-height-exceeds-3m
    required: true
  - field: existing-ceiling-height-exceeds-3m
    required: true
  - field: building-height-exceeds-18m
    required: true
  - field: roof-height-exceeds-3-5m
    required: true
  - field: roof-height-exceeds-7m
    required: true
  - field: is-dwelling-detached
    required: true
  - field: extension-on-attached-dwelling
    required-if:
      - field: is-dwelling-detached
        value: false
  - field: extension-below-terrace-roof
    required-if:
      - field: is-dwelling-detached
        value: false
  - field: roof-pitch-matching
    required: true
  - field: window-on-side-elevation
    required: true
  - field: materials-similar-exterior
    required: true
  - field: dwellinghouse-use
    required: true
rules:
  - description: "Additional storeys must be on principal part only"
    rule: "principal-part-only == true (required for application to proceed)"
  - description: "Ceiling height of additional storeys must not exceed 3m"
    rule: "ceiling-height-exceeds-3m == false (required for application to proceed)"
  - description: "Existing ceiling height must not exceed 3m"
    rule: "existing-ceiling-height-exceeds-3m == false (required for application to proceed)"
  - description: "Extended building height must not exceed 18m"
    rule: "building-height-exceeds-18m == false (required for application to proceed)"
  - description: "Roof height must not exceed 3.5m above existing"
    rule: "roof-height-exceeds-3-5m == false (required for application to proceed)"
  - description: "Roof height must not exceed 7m above existing"
    rule: "roof-height-exceeds-7m == false (required for application to proceed)"
  - description: "Roof pitch must match existing"
    rule: "roof-pitch-matching == true (required for application to proceed)"
  - description: "Side elevation windows require further assessment"
    rule: "window-on-side-elevation == false (if true, further assessment required)"
  - description: "Exterior materials must be similar to existing"
    rule: "materials-similar-exterior == true (required for application to proceed)"
  - description: "Extended dwelling must remain Class C3 use"
    rule: "dwellinghouse-use == true (required for application to proceed)"
  - description: "Extension height restrictions for attached dwellings"
    rule: "if is-dwelling-detached == false, then extension-on-attached-dwelling should be considered"
  - description: "Terrace roof height restrictions for attached dwellings"
    rule: "if is-dwelling-detached == false, then extension-below-terrace-roof should be considered"
entry-date: 2025-07-18
end-date: ''
---
