---
module: processes-machinery-waste-outline
name: Processes machinery waste
description: |
  Information about site activities, processes, and waste management development
  including facility types, capacities, and throughput details. Specifically for outline applications
fields:
  - field: site-activity-details
    required: true
  - field: proposal-waste-management-outline
    required: true
  - field: waste-management-outline
  - field: waste-streams
rules:
  - description: "waste-management-outline is required when proposal-waste-management-outline is true"
    rule: "if proposal-waste-management-outline == true then waste-management-outline is required"
  - description: "waste-streams is required when proposal-waste-management-outline is true"
    rule: "if proposal-waste-management-outline == true then waste-streams is required"
entry-date: 2025-07-14
end-date: ''
---
