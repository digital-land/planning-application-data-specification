# Oil and gas ownership and notices

Ownership, agricultural tenant and public notice details for extraction of oil and gas applications

**Oil and gas ownership and notices module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| owners-and-tenants | Owners and tenants[]{} | Owners and agricultural tenants who were served notice |  | MUST |  |
| valid-posted-notices | Valid posted notices[]{} | Notices posted in each parish or ward and displayed for the required period |  | MUST |  |
| invalid-posted-notices | Invalid posted notices[]{} | Notices that were posted but not displayed for the required period |  | MAY |  |
| steps-taken | Steps taken | Steps taken to protect or replace notices that were removed, obscured or defaced |  | MAY |  |
| newspaper-notices | Newspaper notices[]{} | Newspaper notices published in the area where the land is situated |  | MUST |  |
| person-reference | Person reference | Declaration must be made by an applicant or agent making the application |  | MUST | Used to link named individuals from the form to a particular declaration or confirmation statement, for example in the declaration module.
 |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application |  | MUST |  |
| declaration-date | Declaration date | The date the declaration was made |  | MUST |  |


**Notified person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | details of the owner (or tenant when not a listed building consent application) | MAY | 
notice-served-date | Notice served date | Date when notice was served | MAY | 


**Posted notice component**

field | name | description | required | notes
-- | -- | -- | -- | --
parish-ward | Parish or ward | Parish or ward where the notice was posted | MUST | Could become a codelist-backed field in future, but this would need canonical ward and parish datasets to be available first.
notice-location | Notice location | Location where the notice was posted | MUST | 
notice-posted-date | Notice posted date | Date when the notice was posted | MUST | 


**Newspaper notice component**

field | name | description | required | notes
-- | -- | -- | -- | --
newspaper-name | Newspaper name | Name of the newspaper where notice was published | MUST | 
publication-date | Publication date | Date when the notice was published | MUST | 


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

- valid-posted-notices and invalid-posted-notices must include at least one notice in every parish or ward where the application land is situated
- steps-taken is required when `invalid-posted-notices` is provided
- newspaper-notices.publication-date must not be earlier than 21 days before the application date
- person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- declaration-date must not be in the future
- declaration-confirmed must be `true` for a submission to be valid