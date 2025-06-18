---
module: site-details
name: Site details
description: |
  Information about the location and extent of the site where development 
  or works are proposed
fields:
  - field: site-locations
    required: true
rules:
  - rule: "At least one site-location must be provided for tree works applications"
  - rule: "Exactly one site-location for all other applications types"
  - rule: "If easting is provided, northing must also be provided and vice versa"
  - rule: "If latitude is provided, longitude must also be provided and vice versa"
  - rule: "Site boundary must be valid GeoJSON"
  - rule: "UPRNs must be valid format"
  - rule: "Post code must be valid UK format"
entry-date: 2025-06-13
end-date: ''
---
