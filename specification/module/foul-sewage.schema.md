---
module: foul-sewage
name: Foul sewage disposal
description: |
  Information about foul sewage disposal methods and connection to existing 
  drainage systems for development proposals
fields:
  - field: has-new-disposal-arrangements
    required: true
  - field: foul-sewage-disposal-types
    required-if:
      field: has-new-disposal-arrangements
      value: true
  - field: produce-foul-sewage
    required: true
    applies-if:
      - application-types: 
          in: [extraction-oil-gas]
  - field: connect-to-drainage-system
    required: true
  - field: drainage-system-details
rules:
  - description: "drainage-system-details is required when connect-to-drainage-system is true"
    rule: "if connect-to-drainage-system == true then drainage-system-details is required"
  - description: "drainage-system-details is required for extraction-oil-gas applications"
    rule: "if application-type includes 'extraction-oil-gas' then drainage-system-details is required"
entry-date: 2025-07-09
end-date: ''
---
