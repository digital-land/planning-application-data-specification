---
component: site-location
name: Site location
description: |
  Details about the location of a development site, including its boundary,
  site address and coordinates.
fields:
  - field: geometry
    required: true
    name: Site boundary
  - field: site-address
    required: true
    notes: UPRNs are not needed in case of notification for work to trees in conservation area
  - field: easting
  - field: northing
  - field: latitude
  - field: longitude
entry-date: 2025-06-13
end-date: ''
notes: |
  The UK government standard for exchange of location
  data is WGS84 (latitude/longitude). Easting/northing (British National Grid) may
  be supplied additionally; one can be derived from the other where needed.
---
