---
description: How long the proposed advertisement will be shown.
end-date: ''
entry-date: 2025-07-07
fields:
- field: advert-start-date
  required: true
- field: advert-end-date
  required: true
module: advert-period
name: Advert period
rules:
- rule: advert-start-date must be a valid date in YYYY-MM-DD format
- rule: advert-end-date must be a valid date in YYYY-MM-DD format
- rule: advert-end-date must be after advert-start-date
---