---
module: tree-work-details
name: Identification of tree(s) and description of works
description: |
  Details of trees and proposed work to them, including identification, 
  species and work descriptions
fields:
  - field: description
    description: Description of work applicant wishes to carry out, including identifying the trees, species and setting out the work
    required: true
  - field: tree-details
    description: Details of each tree that is part of the proposal
rules:
  - rule: "Tree identifiers should use TPO reference numbers where applicable"
  - rule: "Description must include tree identification, species and work details"
entry-date: 2025-06-30
end-date: ''
---
