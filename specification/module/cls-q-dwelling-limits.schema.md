---
module: cls-q-dwelling-limits
name: Class Q dwellinghouses and floor space
description: Proposed net dwelling increase, individual dwelling size and cumulative dwelling counts and floor space for prior approval of agricultural buildings to dwellinghouses.
entry-date: 2026-10-20
end-date: ''
fields:
  - field: net-dwellings-increase
    description: The number of dwellinghouses proposed by the development additional to the number on the site immediately prior to development.
    required: true
  - field: single-dwelling-over-150sqm
    required: true
  - field: cls-q-previous-dwellings
    required: true
  - field: floorspace
    description: Total combined floor space, in square metres, previously and now proposed to be changed to dwellinghouses under Class Q on this established or former agricultural unit.
    required: true
notes: |
  The source form states the following eligibility limits, including dwellinghouses previously developed under this permitted development right:
  - No more than a total of 10 dwellinghouses can be developed.
  - The floor space of any single dwellinghouse developed cannot exceed 150 square metres.
  - The cumulative floor space of all dwellinghouses developed cannot exceed 1,000 square metres.
  If proposals exceed any of these limits, the form advises applicants not to continue and to seek advice from the local planning authority. These are policy notes, not automatic submission blocks.
---

This module captures section 6 of the [prior approval application form for agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf). All four questions are asked without conditional qualifiers. The field bodies preserve the source questions and the note defining net increase.
