---
description: Where the advertisement being applied to be built will be located
end-date: ''
entry-date: 2025-07-09
fields:
- field: is-advert-in-place
  required: true
- field: advert-placed-date
  required-if:
  - field: is-advert-in-place
    value: true
- field: is-replacement-advert
  required: true
- field: document-reference
  required-if:
  - field: is-advert-in-place
    value: true
  - field: is-replacement-advert
    value: true
- field: is-advert-overhanging
  required: true
module: advert-location
name: Advertisement location
rules:
- description: advert-placed-date is required when is-advert-in-place is true
  rule: if is-advert-in-place == true then advert-placed-date is required
- description: document-reference is required when is-advert-in-place OR is-replacement-advert
    is true
  rule: if (is-advert-in-place == true OR is-replacement-advert == true) then document-reference
    is required
---