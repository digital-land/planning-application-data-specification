## Decision: Reference authoritative application artefacts without prescribing storage

**Date:** 2026-06-04  
**Status:** draft  

**Context:**  

Later procedural, appeal or enforcement questions may depend on recovering the
application data exactly as it existed at an important point in the planning
process.

The specification needs to ensure this data remains identifiable and
retrievable without prescribing how authorities and suppliers store it.

**Decision:**  

Where application data has procedural, evidential or legal significance at a
defined point, the specification will reference the authoritative artefact using
a URI.

The URI must allow an authorised user or system to identify and retrieve the
artefact. It does not imply public access or require a particular storage
approach.

The first uses of this pattern are:

- `submitted-data-uri`: application data as first received by the planning
  authority
- `validated-data-uri`: application data accepted through planning validation

Documents remain separate records in `planning-application-document`.

**Rationale:**  

Referencing the artefact rather than embedding it:

- ensures significant earlier states are not silently overwritten
- supports controlled access to potentially sensitive data
- allows implementations to store the artefact, expose it through an API or
  construct it when requested
- avoids prescribing supplier or authority system design

**Consequences:**  

- The URI must continue to resolve to the correct authoritative artefact.
- The artefact must not change to represent a later point in the process.
- Access control and storage remain implementation concerns.
- Open-data views are defined separately and are not authoritative
  point-in-process artefacts.

**Alternatives considered:**  

- Embed the application data -> rejected because it may be large and sensitive.
- Require public URLs -> rejected because access may need to be restricted.
- Require stored immutable files -> rejected because this unnecessarily
  prescribes implementation.
