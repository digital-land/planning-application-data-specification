---
module: processes-machinery-waste
name: Processes machinery waste
description: |
  Information about site activities, processes, and waste management development
  including facility types, capacities, and throughput details
fields:
  - field: site-activity-details
    required: true
  - field: proposal-waste-management
    required: true
  - field: waste-management
  - field: waste-streams
rules:
  - description: "waste-management is required when proposal-waste-management is true"
    rule: "if proposal-waste-management == true then waste-management is required"
  - description: "waste-streams is required when proposal-waste-management is true"
    rule: "if proposal-waste-management == true then waste-streams is required"
  - description: "total-capacity is required when not-applicable is false"
    rule: "if not-applicable == false then total-capacity is required"
  - description: "annual-throughput is required when not-applicable is false"
    rule: "if not-applicable == false then annual-throughput is required"
  - description: "is-total-capacity-known and is-annual-throughput-known are only applicable for outline applications"
    rule: "is-total-capacity-known and is-annual-throughput-known only apply to outline applications"
entry-date: 2025-07-09
end-date: ''
---
