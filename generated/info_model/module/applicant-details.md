# Applicant details

Name and contact information for the parties making the application.

**Applicant details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicants | Applicants[]{} |  |  | MUST |  |


**Applicant component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
person | Person{} | Detail to help identify a person | MUST | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
contact-address | Contact address{} | A structured object containing an address used for correspondence. | MUST | 


**Contact address component**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Text representation of an address or site | MUST | 
postcode | Postcode | Postcode for a contact address or site | MAY | 
uprn | UPRN | Unique Property Reference Number for a property | MAY | 

**Validation rules**

- At least one applicant must be provided
- Each applicant reference must be unique within the application