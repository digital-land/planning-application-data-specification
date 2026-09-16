---
module: ma-proposal-eligibility
name: Class MA proposed change eligibility
description: Article 4 restrictions, space standards and continued residential use for a proposed Class MA change of use from commercial, business and service use to dwellinghouses.
entry-date: 2026-09-16
end-date: ''
fields:
  - field: article-4-restriction
    required: true
  - field: meets-space-standard
    required: true
  - field: dwellinghouse-use
    description: Whether every dwellinghouse in the building will remain in Use Class C3 following the change of use, with no other use except purposes ancillary to its use as a dwellinghouse.
    required: true
---

This module captures section 4b of the [Class MA application form, version ECAB 2024.1](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form064_england_en.pdf).

The Article 4 question concerns applications submitted before 1 August 2022 proposing a change of use from offices (Use Class E(g)(i), previously Use Class B1(a)) to dwellinghouses (Use Class C3). Record `not-applicable` where the application falls outside that scope.

Applicants should not continue with this application route and should seek legal advice if they answer:

- `yes` to `article-4-restriction`.
- `false` to `meets-space-standard`.
- `false` to `dwellinghouse-use`.
