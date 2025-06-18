---
module: site-visit
name: Site Visit Details
description: |
  Details needed to support a site visit by the planning authority
fields:
  - field: can-be-seen-from
    required: true
  - field: contact-type
    required: true
  - field: contact
    required-if:
      - field: contact-type
        in: [applicant, agent]
  - field: other-contact
    required-if:
      - field: contact-type
        value: other
rules:
  - rule: "contact must match agent name details if contact-type is agent"
  - rule: "contact must match applicant name if contact-type is applicant"
  - rule: "When contact-type is other, full contact details must be provided"

entry-date: 2025-06-12
end-date: ''
---
