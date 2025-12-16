## Decision: Explicitly set if application payloads can contain additional properties

**Date:** 2025-01-07  
**Status:** Under review  

**Context:**  
When generating JSON Schemas from the declarative application definitions, we need a clear and explicit way to control whether application payloads may include properties beyond those defined by the specification.  

By default, JSON Schema allows additional properties unless explicitly restricted. This implicit behaviour is easy to miss and can lead to inconsistent validation, unclear contracts with suppliers, and accidental data drift over time.  

We also need a simple mechanism that proovides flexibility so that some application types can be strictly closed if desired, while others can remain extensible, without introducing premature complexity into the declarative model.

**Decision:**  
We will introduce a top-level attribute on application definitions named `allow-additional-properties`.  

This flag will be used by schema generation tooling to explicitly set the `additionalProperties` behaviour on the root JSON Schema for that application type.

**Rationale:**  
Placing the flag at the application level makes the extensibility of each application type explicit, intentional, and easy to reason about. It reflects the fact that this is a rule about the *overall shape of the submission payload*, rather than a property of any individual field or module.  

Using a simple boolean keeps the declarative model approachable and avoids over-engineering at an early stage. It allows us to:
- make schema openness a conscious design choice
- generate schemas that are explicit rather than relying on JSON Schema defaults
- vary strictness between application types as desired

This approach supports clearer governance, better validation behaviour, and more predictable downstream use of the data.

**Alternatives Considered:**  
- Relying on JSON Schema defaults → rejected because openness would be implicit and easy to overlook.  
- Defining extensibility only at module level → rejected for now as it does not address top-level payload shape and adds complexity early.  
- Introducing a richer extensibility model (e.g. open / closed / namespaced modes) → deferred to a later iteration once real extension needs emerge.
