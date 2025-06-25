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
  - field: contact-reference
    required-if:
      - field: contact-type
        in: [applicant, agent]
  - field: other-contact
    required-if:
      - field: contact-type
        value: other
rules:
  - rule: "contact-reference must match agent-details.agent.reference details if contact-type is agent"
  - rule: "contact-reference must match one of the references in applicant-details.applicants if contact-type is applicant"
  - rule: "When contact-type is other, full contact details must be provided"

entry-date: 2025-06-12
end-date: ''
---
