# Interest details

Details of the applicant's interest in land or listed buildings and information about
other interested parties including owners and persons with interests in the property


| applicant-interest | Applicant interest | Description of the applicant's interest in the land |  | MUST |  |
| owner-details | Owner details[]{} | Details of property owners including their personal information and notification status |  | MAY |  |
| interested-persons | Interested persons[]{} | Details of persons with an interest in the property including their personal information, nature of interest, and notification status |  | MAY | Rule: is a MUST if `applicant-interest` is `none` |
| applicant-owns-land | Applicant owns land | True or False indicating whether the applicant owns the land where the advertisement will be displayed |  | MUST |  |
| permission-obtained | Permission obtained | True or False indicating whether permission of the owner for the display of an advertisement has been obtained |  | MAY | Rule: is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Permission not obtained details | Details explaining why permission from the land owner has not been obtained for the advertisement display |  | MAY |  |


**LDC Owner Details model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the property owner | MUST | 
informed-of-application | Informed of application | Whether the owner has been informed of the application | MUST | 


**LDC Interested Person model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the interested person | MUST | 
nature-of-interest | Nature of interest | Description of the nature of a person's interest in the property | MUST | 
informed-of-application | Informed of application | Whether the person has been informed of the application | MUST | 
reason-not-informed | Reason not informed | Reason why a person was not informed of the application | MAY | 


**Person obj model**

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
- No advertisement to be displayed without permission of owner or person with interest entitled to grant permission