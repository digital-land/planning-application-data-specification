# Permission type module

Information about the permissions being applied for


**Permission type module module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| permission-types | Permission types[] | List of permission types being applied for |  | MUST | Select from the **permission-type** enum |
| related-proposals | Related proposals[]{} | A set of related proposals with application type and decision date |  | MAY |  |
| other-details | Other details | Explanation if other ground is selected |  | MAY |  |
| will-consolidate-permissions | Will consolidate permissions | Is the applicant looking to consolidate permissions? |  | MUST |  |
| details | Details | Details about the consolidation or update of permissions |  | MAY | Rule: is a MUST if `will-consolidate-permissions` is `True` |


**Related proposal component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST | 
application-type | Application type | The type of planning application | MUST | Select from the **application-type** enum
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MUST | 

