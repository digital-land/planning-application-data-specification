# Interest in land

Whether the applicant owns or has permission to use the land where the proposed advertisement will be placed

**Interest in land module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-owns-land | Applicant owns land | True or False indicating whether the applicant owns the land where the advertisement will be displayed |  | MUST |  |
| permission-obtained | Permission obtained | True or False indicating whether permission of the owner for the display of an advertisement has been obtained |  | MAY | Rule: is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Permission not obtained details | Details explaining why permission from the land owner has not been obtained for the advertisement display |  | MAY |  |

**Validation rules**

- permission-obtained must be provided when applicant-owns-land is false
- permission-not-obtained-details must be provided when applicant-owns-land is false and permission-obtained is false
- No advertisement to be displayed without permission of owner or person with interest entitled to grant permission