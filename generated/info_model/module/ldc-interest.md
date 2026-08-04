# LDC Interest

Who had a say in whether the proposal should go ahead

**LDC Interest module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-interest-type | Applicant interest type | The applicant’s relationship to the land, property or building |  | MUST | Select from the **applicant-interest-type** enum |
| owner-details | Owner details[]{} | Details of the owner if the applicant is a lessee or occupier |  | MAY |  |
| interested-persons | Interested persons[]{} | Details of other interested persons in the listed building |  | MAY | Rule: is a MUST if `applicant-interest-type` is `none` |


**LDC Owner Details component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the property owner | MUST | 
informed-of-application | Informed of application | Whether the owner has been informed of the application | MUST | 


**LDC Interested Person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the interested person | MUST | 
nature-of-interest | Nature of interest | Description of the nature of a person's interest in the property | MUST | 
informed-of-application | Informed of application | Whether the person has been informed of the application | MUST | 
reason-not-informed | Reason not informed | Reason why a person was not informed of the application | MAY | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 

**Validation rules**

- owner-details is required if applicant-interest-type is 'lessee' or 'occupier'
- interested-persons is required if applicant-interest-type is 'none'
- at least one of owner-details or interested-persons must be provided