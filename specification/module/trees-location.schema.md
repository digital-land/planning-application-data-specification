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
- rule: Each site-location must include a site boundary and site address
- rule: If easting is provided, northing must also be provided and vice versa
- rule: Online services can send the boundary supplied by the applicant/agent
- rule: The planning authority must translate site information received on a paper form into the required structured site-location data, including the site boundary
---
