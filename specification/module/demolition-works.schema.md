---
module: demolition-works
name: Proposed demolition works
description: Buildings, reasons, methods, site restoration, expected dates and effects of proposed demolition works.
entry-date: 2026-11-27
end-date: ''
fields:
  - field: description
    description: Description of the buildings to be demolished.
    required: true
  - field: reason
    description: Reason why demolition needs to take place.
    required: true
  - field: demolition-method
    required: true
  - field: site-restoration-details
    required: true
  - field: expected-works-start-date
    required: true
  - field: expected-works-end-date
    required: true
  - field: has-public-right-of-way
    required: true
  - field: later-redevelopment-proposed
    required: true
  - field: tree-removal
    description: Whether the proposal involves the felling or pruning of any trees.
    required: true
  - field: supporting-documents
    description: References to plans showing details of the proposed tree felling or pruning.
    required-if:
      - field: tree-removal
        value: true
  - field: demolition-spoil-disposal
    required: true
rules:
  - rule: '`expected-works-start-date` and `expected-works-end-date` must both be after the application submission date.'
---

This module captures section 5 of the [prior approval form for demolition of buildings, version ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form022_england_en.pdf).

