---
reference: design-and-access-statement
name: Design and access statement
description: >
  A report accompanying and supporting a planning application that explains how a proposed development is a suitable response to the site and its setting, and demonstrates that it can be adequately accessed by prospective users.
synonyms: 
requirement-type: document
source: "Article 9, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended)"
entry-date: 2025-03-30
end-date: ''

required-if:
  any:
    - ref: major-development
    - all:
        - site:
            in: [conservation-area, world-heritage-site]
            description: Site lies within a conservation area or world heritage site.
        - any:
            - condition:
                field: dwelling-count
                operator: ">="
                value: 1
                description: Development provides one or more dwellings.
            - condition:
                field: floorspace
                operator: ">="
                value: 100
                description: Development provides 100 square metres or more of floorspace.
---
