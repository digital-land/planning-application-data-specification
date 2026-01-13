## Decision: Use enum field instead of nullable boolean

**Date:** 2025-07-01  
**Status:** Under review  
**Context:**  
We needed to model fields where the answer may be "yes", "no", or explicitly "unknown" — such as [cert-of-im-sought].

**Decision:**  
We will define an explicit three-valued enum with allowed values: `yes`, `no`, and `unknown`.

**Rationale:**  
Using an enum avoids the ambiguity of a `null` value in a boolean field, which can be interpreted in multiple ways (missing, not applicable, unknown, or simply not filled in). An enumerated type makes the allowed values crystal clear and ensures that "unknown" is explicitly stated by the applicant where relevant, rather than implied through absence.  

This mirrors best practice from HL7 FHIR and other schemas (e.g., Minnesota damage assessment), where `YesNoUnknown` is treated as a distinct, codified field type. It improves data quality and semantic clarity.

**Alternatives Considered:**  
- Boolean field allowing null → rejected due to ambiguity.
- Free-text field → rejected due to lack of validation and consistency.
