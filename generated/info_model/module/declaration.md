# Declaration

Signed and dated verification of the application's accuracy.

**Declaration module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| name | Name | A name of a person |  | MUST |  |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application |  | MUST |  |
| declaration-date | Declaration date | The date the declaration was made |  | MUST |  |

**Validation rules**

- name must match one of the named individuals in the application
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future