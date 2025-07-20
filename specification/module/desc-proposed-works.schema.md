---
module: desc-proposed-works
name: Description of proposed works
description: |
  Description of proposed development works including extension measurements
  and detailed work specifications for planning applications
fields:
  - field: proposed-works-details
    required: true
  - field: extension-depth
    required: true
  - field: max-extension-height
    required: true
  - field: eaves-height
    required: true
rules:
  - description: "All measurements must be positive values in metres"
    rule: "extension-depth > 0 AND max-extension-height > 0 AND eaves-height > 0"
  - description: "Eaves height should typically be less than maximum height"
    rule: "eaves-height <= max-extension-height"
  - description: "Extension depth must be measured externally"
    rule: "extension-depth measurement taken from external face of existing rear wall"
  - description: "Height measurements must be from natural ground level"
    rule: "max-extension-height and eaves-height measured from natural ground level"
  - description: "Proposed works details must be comprehensive and clear"
    rule: "proposed-works-details.length > 10"
entry-date: 2025-07-14
end-date: ''
---
