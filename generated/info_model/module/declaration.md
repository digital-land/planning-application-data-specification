# Declaration

Signed and dated verification of the application's accuracy.

**Declaration module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| person-reference | Person reference | Declaration must be made by an applicant or agent making the application |  | MUST | Used to link named individuals from the form to a particular declaration or confirmation statement, for example in the declaration module.
 |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application |  | MUST |  |
| declaration-date | Declaration date | The date the declaration was made |  | MUST |  |

**Validation rules**

- person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future
- declaration-confirmed must be `true` for a submission to be valid