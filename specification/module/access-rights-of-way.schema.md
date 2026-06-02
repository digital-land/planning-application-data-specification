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
  - any: true
    field:
    - new-altered-vehicle
    - new-altered-pedestrian
    - change-right-of-way
    - new-right-of-way
    - new-public-road
    - temp-right-of-way
    - future-new-right-of-way
module: access-rights-of-way
name: Access and rights of way
rules:
- rule: All fields must use values from rights-of-way-answers codelist
- rule: If new-altered-vehicle is yes, details must be provided
- rule: If change-right-of-way is yes, separate rights of way order may be needed
- rule: If temp-right-of-way is yes, details of temporary diversions must be provided
- rule: each document in supporting-documents must have a `reference` that matches a document in application.documents
---
