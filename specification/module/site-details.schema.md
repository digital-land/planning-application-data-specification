---
description: Where the proposed development will be built.
end-date: ''
entry-date: 2025-06-13
fields:
- field: site-locations
  required: true
module: site-details
name: Site details
rules:
- rule:
    description: At least one site-location must be provided for tree works applications
    field: site-locations
    require:
      min: 1
    type: count-constraint
    when:
      application-type:
        in:
        - tree-works
- rule:
    description: Exactly one site-location for all other applications types
    field: site-locations
    require:
      exact: 1
    type: count-constraint
    when:
      application-type:
        not:
        - tree-works
- rule: If easting is provided, northing must also be provided and vice versa
- rule: If latitude is provided, longitude must also be provided and vice versa
- rule: Each site-location must include a site boundary and site address
- rule: The planning authority must translate site information received on a paper form into the required structured site-location data, including the site boundary
- rule: Site boundary must be valid WKT
- rule: UPRNs must be valid format
- rule: USRNs must be 8-digit strings
- rule: Post code must be valid UK format
---
