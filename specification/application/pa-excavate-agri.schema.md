---
application: pa-excavate-agri
extends: prior-approval
name: 'Prior approval: Excavations or waste deposits for agriculture'
description: Prior approval for excavations or deposits of waste material reasonably necessary for the purposes of agriculture.
notes: Classes A and B (agricultural development) and Class E (forestry development)
entry-date: 2026-11-24
start-date: ''
end-date: ''
legislation:
  - https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/6
fields:
  - field: submission-details
    required: true
  - field: additional-data
modules:
  - module: agri-excavation-works
  - module: agri-forest-dev-elig
  - module: site-visit
allow-additional-properties: false
---

This definition covers the [prior approval form for excavations or deposits of waste material reasonably necessary for the purposes of agriculture, ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form018_england_en.pdf).
