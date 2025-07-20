---
module: haz-substances
name: Hazardous substances
description: |
  Information about hazardous substances involved in the proposal,
  including substance types, quantities, and consent requirements
fields:
  - field: involves-hazardous-substances
    required: true
  - field: substance-types
    required-if:
      - field: involves-hazardous-substances
        value: "yes"
  - field: hazardous-sub-consent-req
    required: true
  - field: hazardous-sub-consent-details
    required-if:
      - field: hazardous-sub-consent-req
        value: true
rules:
  - description: "substance-types is required when involves-hazardous-substances is 'yes'"
    rule: "if involves-hazardous-substances == 'yes' then substance-types is required"
  - description: "hazardous-sub-consent-details is required when hazardous-sub-consent-req is true"
    rule: "if hazardous-sub-consent-req == true then hazardous-sub-consent-details is required"
  - description: "name is required when hazardous-substance-type is 'other'"
    rule: "if hazardous-substance-type == 'other' then name is required"
  - description: "amount must be greater than 0"
    rule: "amount > 0"
entry-date: 2025-07-09
end-date: ''
---
