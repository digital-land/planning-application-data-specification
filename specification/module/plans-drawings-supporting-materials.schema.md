---
description: Additional materials and specifications that form part of the planning
  application
end-date: ''
entry-date: 2025-07-14
fields:
- field: supporting-documents
  required: true
- field: inspection-address
  required: true
module: plans-drawings-supporting-materials
name: Plans, drawings and supporting materials
rules:
- description: At least one document must be provided
  rule: supporting-documents.length >= 1
- description: Inspection address must be a complete postal address
  rule: inspection-address must include street, town/city, and postcode
- description: Each plan or document reference must match a document uploaded with the application
  rule: each document in supporting-documents must have a `reference` that matches a document in application.documents
---
