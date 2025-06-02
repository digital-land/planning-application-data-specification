---
reference: affordable-housing-statement
local-authority: CMD
required-if:
  any:
    - all:
        - condition:
            field: dwelling-count
            operator: ">="
            value: 1
            description: The proposal includes at least one new dwelling.
        - condition:
            field: housing-floorspace
            operator: ">="
            value: 100
            description: The total new housing floorspace is at least 100 square metres.
    - condition:
        field: housing-type
        value: student
        description: The proposal includes student accommodation.
    - condition:
        field: housing-type
        value: shared
        description: The proposal includes shared housing.
    - condition:
        field: housing-type
        value: older-people
        description: The proposal includes housing for older people.
---
