---
description: Who will be affected by the proposal and whether they have been notified,
  such as agricultural tenants
end-date: ''
entry-date: 2025-06-13
fields:
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: sole-owner
  required: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
  field: agricultural-tenants
  required: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
  field: owners-and-tenants
- applies-if:
    application-type:
      in:
      - lbc
  field: lbc-owners
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: steps-taken
  notes: Required for Certificate-C or Certificate-D
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: newspaper-notices
  notes: Required for Certificate-C or Certificate-D
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: ownership-cert-option
  notes: Certificate type determined by ownership and notification status
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: applicant-signature
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: agent-signature
- applies-if:
    application-type:
      in:
      - hh
      - full
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: signature-date
module: ownership-certs
name: Ownership certificates and agricultural land declaration
---