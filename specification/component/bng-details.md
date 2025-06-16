---
component: bng-details
name: Biodiversity net gain details
description: |
  Details about the biodiversity net gain assessment including pre-development value,
  habitat loss information, and required supporting documents
fields:
  - field: pre-development-date
    required: true
  - field: pre-development-biodiversity-value
    required: true
  - field: earlier-date-reason
    required-if:
      - field: pre-development-date
        description: "earlier than application submission"
  - field: habitat-loss-after-2020
  - field: habitat-loss-details
    required-if:
      - field: habitat-loss-after-2020
        value: true
  - field: metric-publication-date
    required: true
  - field: irreplaceable-habitats
    required: true
  - field: irreplaceable-habitats-details
    required-if:
      - field: irreplaceable-habitats
        value: true
  - field: supporting-documents
    required: true
entry-date: 2025-06-16
end-date: ''
---
