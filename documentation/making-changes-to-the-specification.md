# Making changes to the specification

This guide explains how to make deliberate, traceable changes to the planning application data specification. It is for contributors changing the model, its supporting needs and justifications, or its documentation and examples.

## Principles for making a change

- Start with a user need, policy requirement, delivery problem or other clearly stated reason for the change. Do not add data only because it might be useful one day.
- Prefer reuse where the existing element has the same meaning. Do not reuse an element simply because it has a similar label or datatype.
- Keep the meaning of established elements stable. Where a proposed change would alter an element's meaning, prefer a new element or deliberately generalise it with the impact made clear.
- Make linked changes together. A change to a canonical field, codelist or dataset may require changes to its usages, justification, examples, generated outputs and documentation.
- Keep the model independent of a particular form, screen or supplier implementation. Capture the information that needs to be exchanged or maintained, rather than presentation details.
- Make the rationale reviewable. Record why the change exists and what need it helps meet.
- Make small, coherent changes that can be reviewed and tested independently.

## High-level workflow

1. Describe the problem and identify the relevant user need, or create one if needed.
2. Identify the kind of model change needed and check whether an existing element can be reused without changing its meaning.
3. Update the canonical definition and every relevant usage of it in the specification.
4. Update or add justifications, examples and source documentation where they are affected. Regenerate derived outputs through the normal workflow where needed; do not edit them directly.
5. Run `make checks`, review the generated and rendered outputs where relevant, and make the change available for review.

## Change types

- [Fields](#fields)
  - [Adding a field](#adding-a-field)
  - [Removing a field](#removing-a-field)
  - [Changing a field](#changing-a-field)
- Components (needs content)
- Modules (needs content)
- Datasets (needs content)
  - Adding a dataset (needs content)
  - Removing a dataset (needs content)
  - Changing a dataset (needs content)
  - [Adding a field to a dataset](#adding-a-field-to-a-dataset)
- [National public view](#national-public-view)
- Codelists (needs content)
- Codelist values (needs content)
- [Application types](#application-types)
  - [Allowed combined application types](#allowed-combined-application-types)
- [User needs](#user-needs)
  - [Adding a user need](#adding-a-user-need)
- [Justifications](#justifications)
  - [Adding a justification](#adding-a-justification)

## Fields

Fields are canonical definitions of individual data points. They are reused in modules and datasets where their semantic meaning holds. See [Fields](fields.md) for the field model and reuse principles.

### Adding a field

1. Identify the user need or other reason for the information.
2. Search the existing fields and reuse one only if it describes the same real-world concept. If an existing field is too narrow but can safely be generalised, assess every current usage before changing it.
3. If the field does not already exist, add its canonical definition in `specification/field/`. Give it a stable `field` reference, a concise `name`, a plain-language `description`, an appropriate `datatype`, cardinality and entry date.
4. Add the field to the relevant module, dataset or other usage by following the workflow for that change type.
5. Run `make checks`.

### Removing a field


### Changing a field

First decide whether the proposed change preserves the field's meaning.

For a non-semantic change, such as clearer wording, a corrected datatype constraint or improved guidance:

1. Update the canonical field definition.
2. Review every usage to decide whether a context-specific override, description or validation rule also needs changing.
3. Update affected examples, documentation and justifications.
4. Run `make checks`

For a semantic change, such as changing what information the field represents:

1. ...

## Application types

Application type definitions are the files in `specification/application/`.
Before adding or changing one, identify the user need and legal basis, then
check whether an existing application type can be extended (the new one has a parent type) and build out from there.

### Adding a new application

An application definition should include a stable reference, name,
description, legislation, dates as properties.
The fields property MUST include `submission-details`.
The modules property is where to list the expected modules.

Keep conditional questions in the relevant module or component, and set
`allow-additional-properties` explicitly.

If the change adds a new concept, define the field, component or module in its canonical location before referencing it from the application. 

Update any affected codelists, codelist usage and examples.

Always run `make checks` and review the compiled application view, spreadsheet and JSON Schema before submitting the change for review.

[THIS CONTENT NEEDS FLESHING OUT]

### Allowed combined application types

A combined application type is only allowed where the applicant needs more
than one connected consent to carry out the development. These must be agreed with the Development Management Policy team in MHCLG.

Do not create a separate application definition for a combination.

First confirm the policy basis for the combination and that each member
application type already has an active canonical definition. Then add the
combination to `specification/combined-application-types.csv`, using the
application-type references in a consistent order.

The specification derives the combined application from its member application types. Its modules and application-level fields are the combined, de-duplicated set from those definitions. Do not copy modules or fields into a new combined application file.

Run `make checks` and review the generated output to confirm that the
combination is recognised and has the expected payload shape.

## Datasets

### Adding a field to a dataset

1. Identify the need that the field will help meet.
2. Search `specification/field/` for a field with the same meaning. Reuse it if the meaning is the same. If no suitable field exists, follow [Adding a field](#adding-a-field) before continuing.
3. Identify the canonical dataset in `specification/dataset/` and confirm that the information describes that dataset's subject. Do not add a field to a convenient dataset if it belongs to a different record.
4. Add the field reference to the dataset's `fields` property. Set `requirement-level` to `MUST`, `SHOULD` or `MAY` when that expectation has been decided. Existing usages may omit it while levels are introduced progressively. See [Required fields and requirement levels](requirement-levels.md).
5. Add a context-specific description only where it makes the field clearer in this dataset. Use overrides or applicability rules only when they are necessary and do not change the canonical meaning.
6. Search for every specification or view that includes the dataset. Add the field to each specification where it belongs. For the planning-application-data model, this normally includes [planning-application-data.schema.md](../specification/planning-application-data.schema.md).
7. Make an explicit decision about whether the field should be included in the [national public view](#national-public-view). Do not assume that adding it to the wider specification means it should also be made available as open data.
8. Add or update a justification linking the dataset field to the need it helps satisfy. (See creating justification records)
9. Update affected source documentation and examples. Do not edit generated outputs directly.
10. Run `make checks` and review the complete diff to confirm that the canonical dataset, wider specification, public view decision and justification agree.

## National public view

The [national public view schema](../specification/national-public-view.schema.md) is an explicit open-data extraction from the wider planning application data specification. Nothing is included unless that schema lists it.

When adding or changing a dataset field:

1. Decide whether there is a clear public need for the information and whether publishing it supports transparency, discovery, accountability or reuse.
2. Assess the publication risk. Consider personal data, commercially sensitive information, private or security-sensitive information, free text and fields whose contents cannot be reliably controlled.
3. Check whether the entire dataset is public or whether it has a `record-inclusion` rule. A field should not bypass a rule that excludes sensitive or unpublished records.
4. If the field should be open, add it under the relevant dataset in `specification/national-public-view.schema.md`, with a description suitable for the public view. Set its publication `requirement-level` independently from its dataset level. See [Required fields and requirement levels](requirement-levels.md).
5. If it only applies to certain application types, such as `development-scale`, add that condition
6. Use `MUST`, `SHOULD` or `MAY` to state the publication expectation. Do not use `required` or `required-if` in a publication view.
7. If the field should not be open, leave it out.
8. Update the readable publication summary and any affected notes in [national-public-view.md](national-public-view.md). The schema remains the definitive contract.
9. Mention the publication decision in the relevant justification where it is material to how the need is met.
10. Run `make checks` and confirm that the national public view remains a deliberate subset of the wider specification.

## User needs

User needs describe the problem to solve, not the proposed field, dataset or other implementation. Read [Needs and justifications](../user-needs/README.md), [User groups](user-groups.md) and the working [User needs writing playbook](../tmp/user-needs-writing-playbook.md) before adding one.

### Adding a user need

1. Start with the evidence or observation that prompted the need. Ask who needs the information, what they are trying to do and why it matters. An existing form, public register or common data item is evidence of a practice, but does not by itself prove the underlying user need.
2. Search `user-needs/need/` for an existing or overlapping need. Reuse or refine an existing need when the actor, motivation and outcome are substantially the same.
3. Choose the most specific canonical actor from [User groups](user-groups.md) that explains the motivation. Use `planning-system-user` only when the same motivation genuinely applies across several planning user groups. Use a data-domain actor for needs about general properties of the data rather than a planning task.
4. Draft a solution-free statement in the form: “As a [user], I need [need], so that [outcome].” Do not name the proposed field, dataset, API, page or other implementation in the statement.
5. Give the need the next available identifier and create one Markdown file in `user-needs/need/`. Complete its status, priority, name, statement, actors, scope, themes, source, variations, next step and notes.
6. Record the source accurately. Distinguish direct user research, legislation and reporting requirements from needs inferred through data design or observation.
7. If the need is inferred or uncertain, use `status: proposed`, record the confidence and verification questions in `notes`, and set an allowed `next_step`, normally `review` or `rewrite`. Do not present an observed implementation pattern as confirmed user evidence.
8. Use `variations` to identify nearby needs where that will help reviewers assess overlap, splitting or rationalisation.
9. Run `make checks` and review the statement again for a clear user, purpose and outcome without prescribing the solution.

## Justifications

A justification records the claim that one or more specification elements help satisfy a need. It connects the reason for a change to the implemented model without putting implementation details into the need itself.

### Adding a justification

1. Confirm that the need exists and that the model elements named in the justification have been defined.
2. Choose the next available `just-NNNN` identifier and create a Markdown file in `user-needs/justification/`.
3. Reference one or more needs in `needs`.
4. Describe the exact dataset, field, codelist value or combination in `satisfied_by`. Use `allOf` when the elements are useful only together and `anyOf` only where genuinely alternative implementations meet the same need.
5. Set `satisfaction` to `full` only when the named elements meet the stated need. Use `partial` when important information or capability remains outside the current model.
6. Set the confidence independently from satisfaction. Confidence describes how strong the evidence is for the claim, not how complete the model is.
7. Explain in the body how the elements help meet the need, what would be missing without them, any limits on how they should be used and any relevant national-public-view decision.
8. Run `make checks` to confirm that the need and every referenced specification element exist.
