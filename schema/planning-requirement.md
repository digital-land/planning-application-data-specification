---
dataset: planning-requirement
description: "a dataset of planning requirements, usually documents that are required along side a planning application"
fields:
- field: reference
  description: the reference for the specific planning requirement
- field: name
  description: Human-readable title of the planning requirement
- field: description
  description: Summary or explanation of  the planning requirement
- field: synonyms
  description: Alternative names or terms for the requirement, separated by semicolons.
- field: document-type
  description: Classification or grouping of the requirement (e.g. report, statement). Groupings tbc
- field: notes
  description: Any additional notes or context
- field: entry-date
  description: Date the requirement was added (ISO 8601 format, e.g. 2020-01-01).
- field: end-date
  description: Date the requirement ended or was superseded (if applicable, ISO 8601 format).
name: Planning requirement
plural: Planning requirements
---