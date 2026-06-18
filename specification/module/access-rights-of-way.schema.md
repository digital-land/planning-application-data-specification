---
description: Details of any changes the proposed development would make to existing
  access arrangements or public rights of way
end-date: ''
entry-date: 2025-06-13
fields:
- field: new-altered-vehicle
  required: true
- field: new-altered-pedestrian
  required: true
- field: change-right-of-way
  applies-if:
    application-type:
      in:
      - full
      - hh
      - outline
      - technical-details-consent
  required: true
- field: new-right-of-way
  applies-if:
    application-type:
      in:
      - full
      - extraction-oil-gas
      - outline
      - technical-details-consent
  required: true
- field: new-public-road
  applies-if:
    application-type:
      in:
      - full
      - extraction-oil-gas
      - outline
      - technical-details-consent
  required: true
- field: temp-right-of-way
  applies-if:
    application-type:
      in:
      - extraction-oil-gas
  required: true
- field: future-new-right-of-way
  applies-if:
    application-type:
      in:
      - extraction-oil-gas
  required: true
- field: supporting-documents
  required-if:
  - any:
    - field: new-altered-vehicle
      value: true
    - field: new-altered-pedestrian
      value: true
    - field: change-right-of-way
      value: true
    - field: new-right-of-way
      value: true
    - field: new-public-road
      value: true
    - field: temp-right-of-way
      value: true
    - field: future-new-right-of-way
      value: true
module: access-rights-of-way
name: Access and rights of way
rules:
- rule: All fields must use values from rights-of-way-answer codelist
- rule: If new-altered-vehicle is true, details must be provided
- rule: If change-right-of-way is true, separate rights of way order may be needed
- rule: If temp-right-of-way is true, details of temporary diversions must be provided
- rule: each document in supporting-documents must have a `reference` that matches a document in application.documents
---
