# LDC Interest

Information about the applicant's interest in the listed building and details of other interested parties including owners and interested persons


| applicant-interest | Applicant interest | Applicant's interest in the listed building |  | MUST |  |
| owner-details | Owner details[]{} | Details of the owner if the applicant is a lessee or occupier |  | MAY |  |
| interested-persons | Interested persons[]{} | Details of other interested persons in the listed building |  | MAY |  |


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

- owner-details is required if applicant-interest is 'lessee' or 'occupier'
- interested-persons is required if applicant-interest is 'none'
- at least one of owner-details or interested-persons must be provided