---
description: |
  How waste will be managed on the site
end-date: ''
entry-date: 2025-07-09
fields:
- field: site-activity-details
  required: true
- field: proposal-waste-management
  required: true
- field: waste-management
- field: waste-streams
module: processes-machinery-waste
name: Processes machinery waste
notes: |
  If no waste management facility is applicable, the applicant answers that at section level.
  If waste management is applicable, they add one or more entries only for the facilities they need to describe.
  They should not be expected to work through the full codelist and mark each remaining facility not applicable.
rules:
- description: waste-management must contain one or more applicable facility entries
    when proposal-waste-management is true
  rule: if proposal-waste-management == true then waste-management is required
- description: waste-streams is required when proposal-waste-management is true
  rule: if proposal-waste-management == true then waste-streams is required
- description: is-total-capacity-known and is-annual-throughput-known are only applicable
    for outline applications
  rule: is-total-capacity-known and is-annual-throughput-known only apply to outline
    applications
---
