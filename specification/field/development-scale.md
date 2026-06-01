---
cardinality: 1
codelist: development-scale
datatype: enum
description: The local planning authority's classification of a full or outline planning application by development scale
end-date: ''
entry-date: 2026-06-01
field: development-scale
name: Development scale
notes: >
  Used for the local planning authority's recorded classification at decision point.
  This is not automatically derived from proposal thresholds in the specification.
---

Although major development criteria can often be described using thresholds such as dwelling count, site area and floorspace, the classification is assigned by the local planning authority. It may involve judgement for mixed-use, borderline or changed proposals, and the value needed for reporting is the classification at decision point. The specification therefore records the LPA classification directly rather than treating it as automatically derived from submitted proposal data.

The field is only applicable to full and outline planning applications. The name `development-scale` is used instead of `major-minor` so the codelist can be extended if policy introduces additional categories, such as medium development.
