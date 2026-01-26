## Decision: Record date precision explicitly using a separate `date_precision` attribute

**Date:** 2026-01-26 
**Status:** Under review

**Context:**  

Several fields in the specification use a date or datetime datatype, but the required level of precision varies by use case. In some cases only a year or month is known or meaningful, while in others a full calendar date or timestamp is required.

Although ISO 8601 supports reduced precision formats (for example `YYYY` or `YYYY-MM`), mixing multiple representations into a single field makes validation, interpretation, and schema generation more complex. It also blurs the difference between the value of a date and the certainty or precision with which it is known.

We need a clear and consistent way to express date precision without overloading the date value itself.

**Decision:**  

We will represent date precision using a separate attribute alongside the date field.

Fields will use a full ISO 8601 date or datetime format for their value, and an additional attribute (for example `date_precision`) will indicate the level of precision required or provided.

For example:

```
datatype: datetime
date_precision: month
```

**Rationale:**  

Separating the date value from its precision:
- keeps the date format consistent and predictable
- avoids relying on reduced ISO 8601 formats to imply meaning
- makes precision an explicit, machine readable part of the model
- simplifies schema generation and validation
- allows future extension without changing how date values are stored

It also reflects a clear conceptual distinction:
- the date field represents what the date is
- the precision attribute represents how precisely it is known or required

This makes the model easier to reason about for both humans and machines.

**Alternatives considered:**  

- Using reduced ISO 8601 formats only (for example `YYYY-MM`) in the date field → rejected because precision becomes implicit and harder to validate consistently.
- Encoding precision in field names (for example `decision-month`) → rejected as it leads to field proliferation and reduces flexibility.
- Creating separate datatypes for each precision level → rejected as unnecessary complexity at this stage.
- Storing the date format itself in `date_precision` (for example `YYYY-MM` or `YYYY-MM-DD`) → considered, but not adopted as this describes representation rather than meaning. We want `date_precision` to express semantic intent (year, month, day, time) rather than mirror formatting rules, which are already handled by the date datatype.

