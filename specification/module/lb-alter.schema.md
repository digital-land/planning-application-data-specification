---
description: Details of any changes being made to a listed building as part of development
  works
end-date: ''
entry-date: 2025-07-08
fields:
- field: proposal-alter-lb
  required: true
- field: proposal-alter-lb-types
  required-if:
    field: proposal-alter-lb
    value: true
- field: document-reference
  required-if:
    field: proposal-alter-lb
    value: true
module: lb-alter
name: Listed building alterations
rules:
- rule: each document in document-reference must have a `reference` that matches a document in application.documents
---

This module captures information about proposed alterations to listed buildings. The `proposal-alter-lb` field determines whether the proposal includes any alterations to listed buildings. When this is true, applicants must specify the types of alterations using the `proposal-alter-lb-types` field and provide supporting documentation through the `document-reference` field.

The alteration types are defined in the lb-alteration-type codelist and include:
- Interior works
- Exterior works
- Fixed structures or objects
- Stripping out of internal finishes

Supporting documents should provide detailed information about the proposed alterations to help assess their impact on the listed building's special architectural or historic interest.
