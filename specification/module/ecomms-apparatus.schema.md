---
module: ecomms-apparatus
name: Electronic communications apparatus
description: Details of proposed and existing electronic communications apparatus and supporting technical documents.
entry-date: 2026-11-24
end-date: ''
fields:
  - field: apparatus-type-details
    required: true
  - field: proposal-description
    description: Details of the electronic communications apparatus to be installed or altered, including height, size, colour and other relevant characteristics.
    required: true
  - field: replaces-installation
    required: true
  - field: description
    name: Existing apparatus details
    description: Details of the existing electronic communications apparatus being replaced, including height, size, colour and other relevant characteristics.
    required-if:
      - field: replaces-installation
        value: true
  - field: icnirp-declaration-provided
    required: true
  - field: icnirp-declaration-document
    required-if:
      - field: icnirp-declaration-provided
        value: true
  - field: ecomms-template-provided
    required: true
  - field: ecomms-template-document
    required-if:
      - field: ecomms-template-provided
        value: true
---

This module captures apparatus and supplementary information from sections 5 and 6 of the [prior approval form for electronic communications network development, ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form020_england_en.pdf).

Source questions for the reused description fields:

- Please provide further details of the apparatus (e.g. height, size, colour, etc):
- If Yes, please provide further details of the existing apparatus (e.g. height, size, colour etc):
