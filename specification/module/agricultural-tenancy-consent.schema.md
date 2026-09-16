---
module: agricultural-tenancy-consent
name: Agricultural tenancy consent
description: Whether land is occupied under agricultural tenancy agreements and all parties have consented to the proposed change of use.
entry-date: 2026-09-16
end-date: ''
fields:
  - field: agricultural-tenants
    description: Whether any part of the land covered by or within the curtilage of the building is occupied under any agricultural tenancy agreements.
    required: true
  - field: tenancy-parties-consent
    required-if:
      - field: agricultural-tenants
        value: true
---

This module captures section 5 of the [Class MA application form, version ECAB 2024.1](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form064_england_en.pdf). It establishes consent to the change of use from all parties to agricultural tenancy agreements.

If agricultural tenancy agreements exist and all parties have consented, copies of written confirmations from all relevant parties stating their consent should accompany the application.

Applicants should not continue with this application route and should seek legal advice if they answer:

- `true` to `agricultural-tenants` and `false` to `tenancy-parties-consent`.
