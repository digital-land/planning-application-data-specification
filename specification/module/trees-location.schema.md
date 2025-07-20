---
module: trees-location
name: Trees location
description: |
  Location information for trees affected by the proposed works, required when the site is different from the applicant's address
fields:
  - field: is-site-different
    required: true
  - field: site-locations
    description: Details of the sites on which the tree(s) are located
    required-if:
      - field: is-site-different
        value: true
rules:
  - rule: "site-locations only required if the site is different from the applicant's address"
  - rule: "At least one location method must be provided per site: site-boundary, address-text, or easting+northing"
  - rule: "If easting is provided, northing must also be provided and vice versa"
  - rule: "Online services can send the boundary supplied by the applicant/agent"
  - rule: "Paper forms would need other fields translated into site-boundary"
entry-date: 2025-07-01
end-date: ''
---
