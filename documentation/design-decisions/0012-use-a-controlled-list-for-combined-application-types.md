## Decision: Use a controlled list for combined application types

**Date:** 2026-04-14  
**Status:** Proposed  

**Context:**  

Some planning application forms cover more than one application type in a single submission, for example householder planning permission and listed building consent.

We needed to decide whether the specification should allow application types to be combined freely, or whether only a limited set of combinations should be supported.

DM policy advice was that these cases are linked because the applicant would need the separate connected Planning Acts consent in order to implement the development.

We also needed a mechanism that avoids duplicating large application definitions for each recognised combination.

**Decision:**  

- Treat combined applications as a controlled list of policy-approved combinations.  
- Store that controlled list in `specification/combined-application-types.csv`.  
- Keep single application types as the canonical source definitions.  
- Derive a combined application dynamically from the member application types rather than hand-authoring combined records in `specification/application/`.  
- Resolve combinations only when explicitly requested.  
- Reject combinations that are not active in the controlled list.  
- Treat module ordering as out of scope for the specification.  

**Rationale:**  

Using a controlled list:

- matches the policy basis that these are connected-consent cases, not an open-ended composition feature
- keeps policy control over which combinations are recognised
- avoids creating and maintaining separate full application definitions for each allowed combination
- lets the specification reuse existing single application definitions and shared modules
- keeps ordering out of the core model, where it is better handled by downstream UX or implementation choices

This gives a clear policy boundary with low duplication and predictable runtime behaviour.

**Consequences:**  

- Combined application support depends on an explicit row being present and active in `combined-application-types.csv`.  
- Tooling must normalise member order before lookup, for example `lbc;hh` resolves as `hh;lbc`.  
- Combined applications derive a deduped union of member modules and merged application-level items.  
- `application-type` applicability checks for combined selections use OR semantics across the component application types.   

**Alternatives considered:**  

- Allow any sensible combination of application types -> rejected because it does not match the policy framing and would weaken control over what counts as a valid combined application.  
- Hand-author each combined application in `specification/application/` -> rejected because it duplicates the canonical single application definitions and increases maintenance overhead.  
- Include ordering rules in the specification -> rejected because ordering is a presentation or implementation concern, not part of the core combination model.
