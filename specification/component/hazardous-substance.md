---
component: hazardous-substance
name: Hazardous substance
description: |
  Information about a specific hazardous substance including its type,
  name (if other), and quantity in tonnes
fields:
  - field: hazardous-substance-type
    required: true
  - field: hazardous-substance-other
    required-if:
      - field: hazardous-substance-type
        value: "other"
  - field: amount
    required: true
entry-date: 2025-07-09
end-date: ''
---
