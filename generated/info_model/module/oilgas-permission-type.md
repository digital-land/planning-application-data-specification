# Oil and gas permission types

Module for details about types of onshore oil and gas extraction permissions already received and applying for


**Oil and gas permission types module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| oilgas-permission-types | Oil and gas permission types[] | List of permission types being applied for |  | MUST | Select from the **oilgas-permission-type** enum |
| related-permissions | Related permissions[]{} | List of related permissions |  | MAY | Used in onshore extraction of oil and gas applications |
| other-details | Other details | Explanation if other ground is selected |  | MAY |  |
| will-consolidate-permissions | Will consolidate permissions | Is the applicant looking to consolidate permissions? |  | MUST |  |
| details | Details | Details about the consolidation or update of permissions |  | MAY | Rule: is a MUST if `will-consolidate-permissions` is `True` |
| related-proposals | Related proposals[]{} | Previous permissions for minerals development on the site (if any) |  | MAY |  |


**Related permission-details component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application that permission was received for | MUST | 
oilgas-permission-type | Oil and gas permission type | An oil and gas related permission type | MUST | Select from the **oilgas-permission-type** enum
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MUST | 
condition-number | Condition number | Number of any condition being breached | MAY | Rule: is a MUST if `oilgas-permission-type` is `variation-condition`


**Related proposal component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST | 
application-type | Application type | The type of planning application | MUST | Select from the **application-type** enum
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MUST | 

**Validation rules**

- rule