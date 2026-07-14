# Submission details

This is a working note on the `submission-details` part of the planning application payload.

## Purpose

`submission-details` describes the submission itself: how it is identified, routed, validated, handled and traced.

It should not become a general metadata or catalogue section. It should only contain information needed to process, validate, route, trace or interpret the submitted payload.

The current specification has a component called `submission-details` which contains the current submission-level information. This replaces the earlier `application` component name, which was easy to confuse with the planning application itself.

Source issue: [planning-data-design #140](https://github.com/digital-land/planning-data-design/issues/140)

## Inclusion test

A field belongs in `submission-details` if it supports at least one of these purposes:

- identifying the submission
- routing the submission
- validating the payload
- recording provenance
- supporting audit
- detecting duplicates, retries, corrections or resubmissions
- passing the payload between systems without relying on transport headers or private supplier context

If a candidate field does not meet one of these purposes, it should usually stay out for now.

## Needs

### Confident needs, currently covered

These are needs we are confident belong in `submission-details` and are already represented by fields in the component.

| Need | Current field or model | Notes |
| --- | --- | --- |
| Identify the submission itself | `submission-reference` | Identifies the submitted payload. This should mean the submission reference, not the planning authority's application reference or a generic supplier transaction reference. |
| Identify the application type or types for approved combinations | `application-types` | Needed to know which application specification applies. A submission may contain one application type or an approved combination of application types, so this needs to support a list rather than a single value. The value drives module selection, validation rules and any downstream interpretation of what has been submitted. |
| Identify which planning authority the submission will be sent to | `planning-authority` | Needed to route the submission to the intended authority and to check that the receiving system is handling a submission meant for it. This should identify the authority responsible for receiving the application, not the applicant, agent or software supplier. |
| Provide the context needed for regional codelist variants | `specification-profile` | Used where a codelist has different allowed values for different specification profiles. This lets validation filter the codelist to the values that apply to the specified profile. |
| Identify included documents | `documents` | Provides a single source of truth for uploaded files in the payload. The document list is submission-level payload information: it tells the receiver what files are included and gives the structured payload a way to reference uploaded documents. |
| Record when the application was submitted | `submitted-at` | Records the date and time the application was submitted. |
| Record when the payload was created | `created-at` | Records the date and time the submission payload was created by the originating system. This is separate from the submitted date because the payload may be prepared before it is submitted. |
| Record fee information where relevant | `fee` | Optional. Wider fee modelling is separate future work. |

### Confident needs, not fully covered

These are needs we are confident matter, but where the current model only partly addresses the need or the exact field pattern still needs more work.

| Need | Current gap | Possible way to satisfy it |
| --- | --- | --- |
| Identify the ruleset or regulatory regime the submission was made under | `specification-profile` gives some context, but does not by itself identify the exact version of the specification, ruleset or regulatory regime used when the submission was prepared. | Add a specification, ruleset or version identifier so receiving systems can interpret and validate the payload against the rules it was submitted under, rather than inferring that from dates or local knowledge. |
| Support deduplication and idempotency | `submission-reference` may help, but the retry and duplicate-handling model is not yet clear. | Decide whether `submission-reference` is enough or whether separate retry, correlation or idempotency fields are needed. |

### Captured needs, not yet settled

These are possible needs that have been raised or identified during the work. They are not yet settled because we need more evidence, a clearer process model or a decision about where the information belongs.

| Need | Why it may matter | Why it is not settled |
| --- | --- | --- |
| Identify the submitting organisation or origin system | Could support provenance, accountability, support, debugging, duplicate detection and understanding how a payload was produced. | The role is ambiguous: applicant, agent, supplier, service operator, integration point and system owner are different things. This is also difficult without a controlled list or identifier scheme for supplier systems, submission services or organisations. A free-text value would be easy to populate inconsistently and hard to use reliably. |
| Record corrections, replacements or resubmissions | Needed if the payload needs to describe whether it replaces or amends an earlier submission. | Correction and resubmission flows are not yet clearly in scope. |
| Link related submissions | Could connect a correction or resubmission to an earlier payload. | Depends on the correction/resubmission model. |
| Record the submission purpose | Could distinguish new applications, corrections, test payloads or replacements. | Needs evidence that these flows should be represented inside the payload. |
| Identify modules included in the payload | Could provide an explicit manifest of intended module inclusions, including declared-but-empty modules or partial submissions. | Modules are already represented as top-level objects in the payload, so a separate `modules` list may duplicate information unless a clear manifest need is confirmed. |
| Record when the payload was received by the planning authority | This may matter once a planning authority receives the submission and creates its own records. | This belongs more naturally in the planning application data specification as a receiving-authority record, rather than in the applicant or agent submission payload. |
| Identify PINS references | May matter for some routes or later stages. | Need to confirm when PINS references exist, who assigns them and whether they belong in the submission payload. |
| Record destination beyond planning authority | Could matter if a submission is routed to PINS, an intermediary or more than one body. | For the baseline, `planning-authority` may be enough. |
| Persist transport or correlation identifiers | Could help with support and troubleshooting after API receipt. | Many transport values may belong outside the domain payload unless systems need them later. |
