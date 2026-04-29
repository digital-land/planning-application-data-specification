## Decision: When to use explicit not applicable fields

**Date:** 2026-04-22  
**Status:** Proposed  

**Context:**  

Some legacy planning application forms include explicit `not applicable` tick boxes alongside many individual options or sub-fields.

That works on paper forms because a blank space can be ambiguous. It may mean:

- not relevant
- no change
- none or zero
- not answered

In a digital form, that same explicit pattern can become burdensome if applicants are asked to tick `not applicable` repeatedly across a long list of options.

Recent examples include:

- [issue #358](https://github.com/digital-land/planning-application-data-specification/issues/358) on waste management facilities
- [issue #360](https://github.com/digital-land/planning-application-data-specification/issues/360) on non-residential floorspace rows

Feedback from DM policy is that the legacy form pattern was mainly there to elicit a response, but that digital forms should not preserve every explicit `not applicable` field where this adds unnecessary burden. Planning Portal feedback also supports treating omitted entries as implicitly not applicable in digital flows where relevance is established through earlier questions or interface logic.

We need a clear rule for when to keep an explicit `not applicable` field and when blank input can be interpreted as meaning not applicable.

**Decision:**  

- Do not carry over every legacy paper-form `not applicable` field into the digital specification by default.  
- Keep an explicit `not applicable` field only where it materially helps distinguish between `not relevant`, `no change`, `none or zero`, and `not answered`.  
- Where the digital flow can establish relevance through earlier questions, conditional logic, or the absence of any selected option, blank input may be treated as implying `not applicable`.  
- Avoid explicit per-item `not applicable` fields where they would mainly force applicants to repeat the same response across many options without improving interpretation.  

**Rationale:**  

Using explicit `not applicable` fields selectively:

- preserves clarity where applicant intent would otherwise be ambiguous
- reduces unnecessary applicant burden in digital forms
- allows digital interfaces to use branching and conditional logic rather than reproducing paper-form mechanics
- gives a reusable rule for resolving similar questions across modules

This gives a better balance than either extreme of always requiring explicit `not applicable` or always inferring it from missing data.

**Consequences:**  

- Some existing paper-form `not applicable` fields will not be modelled directly in the digital specification.  
- Module and field design should consider whether ambiguity is real before adding explicit `not applicable` values or booleans.  
- Digital implementations may need upstream logic or clearer section-level questions so that omitted entries can be interpreted safely.  
- Similar issues should be resolved against this rule rather than decided ad hoc each time.  

**Alternatives considered:**  

- Keep every explicit `not applicable` field from the paper forms -> rejected because it reproduces paper-form burden in digital services and can add many superfluous inputs.  
- Always infer `not applicable` from blank input -> rejected because in some cases blank data is genuinely ambiguous and an explicit declaration is still useful.  
- Use a simple numeric threshold, such as removing explicit `not applicable` when there are many options -> rejected because burden matters, but the main test should be ambiguity versus usefulness rather than count alone.  

**Where this pattern is used:**  

- [Processes machinery waste](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/processes-machinery-waste.schema.md) and [outline variant](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/processes-machinery-waste-outline.schema.md): applicants only provide entries for relevant waste management facilities. They do not work through all 21 facility types marking each remaining one `not applicable`, because that would be unnecessarily burdensome.  
- [Materials](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/materials.schema.md): applicants answer at section level whether material details need to be provided. If they do, they only provide entries for the relevant building elements. They do not work through each remaining building element marking it `not applicable`, and omitted building elements are not recorded as inferred `not applicable` answers.  
