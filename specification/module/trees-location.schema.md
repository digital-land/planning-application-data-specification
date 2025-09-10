---
description: Where trees affected by the proposed development are located.
end-date: ''
entry-date: 2025-07-01
fields:
- field: is-site-different
  required: true
- description: Details of the sites on which the tree(s) are located
  field: site-locations
  required-if:
  - field: is-site-different
    value: true
module: trees-location
name: Trees location
rules:
- rule: site-locations only required if the site is different from the applicant's
    address
- rule: 'At least one location method must be provided per site: site-boundary, address-text,
    or easting+northing'
- rule: If easting is provided, northing must also be provided and vice versa
- rule: Online services can send the boundary supplied by the applicant/agent
- rule: Paper forms would need other fields translated into site-boundary
---