---
module: advert-period
name: Advert period
description: |
  Module for capturing the time period that consent to advertisement is sought
fields:
  - field: advert-start-date
    required: true
  - field: advert-end-date
    required: true
rules:
  - rule: "advert-start-date must be a valid date in YYYY-MM-DD format"
  - rule: "advert-end-date must be a valid date in YYYY-MM-DD format"
  - rule: "advert-end-date must be after advert-start-date"
entry-date: 2025-07-07
end-date: ''
---
