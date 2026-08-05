## Decision: Use text, identifiers and site boundaries for addresses

**Date:** 2026-08-05  
**Status:** Proposed

**Context:**

Planning applications need two distinct kinds of address information:

- a correspondence address for a person or notification recipient; and
- a readable description of the development site.

Neither an address string nor a property or street identifier is sufficient to
describe the extent of a development site, particularly for unaddressed land or
sites containing multiple premises. The working discussion is captured in
[issue #307](https://github.com/digital-land/planning-application-data-specification/issues/307).

**Decision:**

Use a `contact-address` component for correspondence. It contains required
`address-text`, with optional `postcode` and singular `uprn`.

Use a `site-address` component for a development site. It contains required
`address-text`, with optional `postcode`, plural `uprns` for existing premises
within the site boundary, and plural `usrns` for associated streets.

Each `site-location` must contain both a readable `site-address` and required
`geometry`, presented as **Site boundary** in this context. The geometry is
authoritative for the extent of the application site. The planning authority
must translate paper-form information into this structured representation.

**Consequences:**

- Services can use an address lookup, GOV.UK address pattern or free text,
  provided they produce the standard data shape.
- UPRNs and USRNs enrich an address where they are known; they do not replace
  address text or a site boundary.
- UPRNs created by the development are output information and are not
  recorded during submission as the existing premises to which the application applies.
