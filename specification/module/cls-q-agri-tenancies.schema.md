---
module: cls-q-agri-tenancies
name: Class Q agricultural tenancies
description: Current agricultural tenancy consent and agreements about agricultural need following recent tenancy termination for a prior approval change of use from agricultural buildings to dwellinghouses.
entry-date: 2026-10-20
end-date: ''
fields:
  - field: agricultural-tenants
    description: Whether the site is currently occupied under any agricultural tenancy agreements.
    required: true
  - field: tenancy-parties-consent
    required: true
    applies-if:
      field: agricultural-tenants
      value: true
  - field: cls-q-tenancy-terminated
    required: true
  - field: cls-q-agri-use-not-required
    required: true
    applies-if:
      field: cls-q-tenancy-terminated
      value: true
---

This module captures section 5 of the [prior approval application form for agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf).

The form introduces the consent question with “If yes”, referring to current agricultural tenancy agreements. It separately introduces the agreement about agricultural need with “If yes”, referring to the recent termination question. Each follow-up is applicable and required only when its preceding answer is true. The current-tenancy and recent-termination questions are independent and both must be answered.

If current agricultural tenancy agreements exist and all parties consent to the change of use, the form requires copies of written confirmations from all relevant landlords and tenants stating their consent with the application.

If relevant agricultural tenancy agreements have been terminated and all parties agree that the site is no longer required for agricultural use, the form requires copies of written confirmations from all relevant landlords and tenants stating that agreement with the application.

Applicants should not continue with this application route and should seek advice from the local planning authority if they answer:

- `true` to `agricultural-tenants` and `false` to `tenancy-parties-consent`.
- `true` to `cls-q-tenancy-terminated` and `false` to `cls-q-agri-use-not-required`.
