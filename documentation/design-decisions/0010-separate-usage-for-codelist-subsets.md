## Decision: Use separate usage tables when codelists need context-specific subsets

**Date:** 2026-03-19  
**Status:** Proposed  

**Context:**  

Some codelists need to support different valid subsets in different contexts, while still representing one coherent set of concepts.

The immediate need is `tenure-type`:

- MHCLG uses a smaller set of high-level tenure values
- GLA uses a more granular set of tenure values
- both are describing the same field
- the allowed values vary by context

This is not a unique problem. It is a common standards pattern.

Examples:

- [HL7 FHIR](https://www.hl7.org/fhir/) separates `CodeSystem` from `ValueSet`
- [SDMX](https://sdmx.org/) separates code lists from constraint artefacts
- [GS1 code lists guidance](https://www.gs1.org/edi-xml/technical-user-guide/code-lists) recognises context-specific subsets of broader code lists

Within this repository there is also a local precedent for separate relationship tables such as `data/application-type-module.csv`.

We need a clear pattern that keeps:

- the codelist concepts themselves
- any hierarchy between those concepts
- the rules about where each value is allowed

separate from each other.

**Decision:**  

- When a codelist needs context-specific subsets, keep one canonical codelist for the concepts.  
- Use `parent` in that codelist where a hierarchy or roll-up relationship is needed.  
- Define context-specific allowed values in a separate codelist-specific usage table.  
- Document profile or context selection in prose unless a more formal routing mechanism becomes necessary.  

For `tenure-type`, this means:

- the codelist defines the tenure values and any parent-child roll-up
- a separate `tenure-type-usage` table defines which values are allowed in which context

**Rationale:**  

Using a separate usage table:

- keeps codelists focused on what each value means
- keeps hierarchy focused on roll-up relationships
- allows applicability rules to vary without changing the concept model
- makes the pattern reusable for other codelists if needed
- matches a common approach used in established standards

This gives a clearer model with lower long-term maintenance cost than trying to encode context rules directly into the codelist file.

**Consequences:**  

- The model now uses more than one file.  
- People using the data need to look in one place for the codelist meanings and another for where each value is allowed.  
- Routing logic may need documenting separately if profile selection becomes more complex.  

**Alternatives considered:**  

- Keep usage rules inside the codelist itself -> rejected because it mixes concept definition, hierarchy and context rules in one file.  
- Create one generic usage table for every codelist -> rejected for now because it introduces abstraction before we know that different codelists need exactly the same rule structure.  
- Create separate codelists for MHCLG and GLA tenure values -> rejected because the field is the same field and the values need a shared canonical source and roll-up structure.  
