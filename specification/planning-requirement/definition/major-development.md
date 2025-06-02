---
definition:
  major-development:
    description: A standard definition of major development for residential or non-residential proposals.
    any:
      - condition:
          field: dwelling-count
          operator: ">="
          value: 10
      - condition:
          field: site-area-residential
          operator: ">="
          value: 0.5
      - condition:
          field: site-area-non-residential
          operator: ">="
          value: 1
      - condition:
          field: floorspace-non-residential
          operator: ">="
          value: 1000
---
