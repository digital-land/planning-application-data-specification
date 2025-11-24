---
description: Additional materials and specifications that form part of the planning
  application
end-date: ''
entry-date: 2025-07-14
fields:
- field: plans-documents
  required: true
- field: inspection-address
  required: true
module: plans-drawings-supporting-materials
name: Plans, drawings and supporting materials
rules:
- description: At least one document must be provided
  rule: plans-documents.length >= 1
- description: Each document must have a unique reference number within the application
  rule: plans-documents[].reference-number must be unique
- description: Document names must be descriptive and non-empty
  rule: plans-documents[].name.length > 0
- description: Inspection address must be a complete postal address
  rule: inspection-address must include street, town/city, and postcode
- rule: each document in plans-document must have a `reference` that matches a document in application.documents
---
