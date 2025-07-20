---
module: plans-drawings-supporting-materials
name: Plans, drawings and supporting materials
description: |
  Specification for plans, drawings, and supporting documents required for
  planning applications, including document references and inspection details
fields:
  - field: plans-documents
    required: true
  - field: inspection-address
    required: true
rules:
  - description: "At least one document must be provided"
    rule: "plans-documents.length >= 1"
  - description: "Each document must have a unique reference number within the application"
    rule: "plans-documents[].reference-number must be unique"
  - description: "Document names must be descriptive and non-empty"
    rule: "plans-documents[].name.length > 0"
  - description: "Inspection address must be a complete postal address"
    rule: "inspection-address must include street, town/city, and postcode"
entry-date: 2025-07-14
end-date: ''
---
