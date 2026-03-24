## Decision: Use explicit schedule days for hours of operation

**Date:** 2026-03-24  
**Status:** Proposed  

**Context:**  

The previous hours of operation model used a `day-type` codelist with grouped values such as:

- `monday-friday`
- `saturday`
- `sunday`
- `bank-holiday`

This was too limiting for common real cases, for example:

- Monday to Thursday one pattern, Friday another
- Tuesday only late opening
- separate bank holiday hours

The issue and working discussion are captured in [issue #357](https://github.com/digital-land/planning-application-data-specification/issues/357).

We need a simple structure that is more flexible than grouped day buckets, without adopting a complex schedule syntax.

**Decision:**  

- Replace the grouped `day-type` approach for hours of operation with explicit day selection.  
- Use a `schedule-day` codelist containing individual days plus `bank-holiday`.  
- Use a multi-value `schedule-days` field on each `operational-times` entry.  
- Keep the existing `closed` and `time-ranges` pattern.  

**Rationale:**  

Using explicit schedule days:

- allows common patterns to be represented without adding complex syntax
- keeps the model closer to established patterns such as [schema.org `OpeningHoursSpecification`](https://schema.org/OpeningHoursSpecification)
- avoids forcing users into a small set of grouped day buckets
- supports clearer validation and more predictable downstream use

This gives more flexibility while keeping the model simple enough for planning forms and examples.

**Consequences:**  

- Hours of operation entries can now apply to one or more explicit days.  
- The old `day-type` field and codelist are retired in favour of `schedule-days` and `schedule-day`.  
- Examples and related component documentation need to use the new structure.  

**Alternatives considered:**  

- Keep the grouped `day-type` codelist -> rejected because it is too limited for common scheduling cases.  
- Adopt a compact schedule syntax similar to OpenStreetMap `opening_hours` -> rejected as more complexity than is needed for this specification.  
- Use free text only for hours of operation -> rejected because it reduces structure, validation and reuse.  
