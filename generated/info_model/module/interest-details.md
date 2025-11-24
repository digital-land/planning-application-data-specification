# Interest details

Names and contact details for all parties with an interest in the proposed develpoment.

**Interest details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-interest | Applicant interest | Description of the applicant's interest in the land |  | MUST |  |
| owner-details | Owner details[]{} | Details of property owners including their personal information and notification status |  | MAY |  |
| interested-persons | Interested persons[]{} | Details of persons with an interest in the property including their personal information, nature of interest, and notification status |  | MAY | Rule: is a MUST if `applicant-interest` is `none` |


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

- if applicant-interest is 'lessee' or 'occupier', then owner-details is required
- if applicant-interest is 'none', then interested-persons is required
- if applicant-owns-land is false, then permission-obtained is required
- if applicant-owns-land is false and permission-obtained is false, then permission-not-obtained-details is required