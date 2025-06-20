---
component: file
name: File
description: |
  Structure for digital files or references to stored files,
  including metadata and validation information
fields:
  - field: url
    description: A URL pointing to the stored file
  - field: base64-content
  - field: filename
    required: true
    description: Name of the file being uploaded
  - field: mime-type
  - field: checksum
  - field: file-size
entry-date: 2025-06-20
end-date: ''
---
