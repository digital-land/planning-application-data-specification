---
application: pa-road-agri-forest
extends: prior-approval
name: 'Prior approval: Private roads for agricultural or forestry use'
description: Prior approval for the formation, alteration or maintenance of private ways for agricultural or forestry use.
notes: Classes A and B (agricultural development) and Class E (forestry development)
entry-date: 2026-11-23
start-date: ''
end-date: ''
legislation:
  - https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/6
fields:
  - field: submission-details
    required: true
  - field: additional-data
modules:
  - module: agri-forest-dev-elig
  - module: agri-road-works
  - module: site-visit
allow-additional-properties: false
---

This definition covers the [prior approval form for the formation, alteration or maintenance of private ways for agricultural or forestry use, ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form017_england_en.pdf), under GPDO Schedule 2, Part 6, Classes A/B/E.
