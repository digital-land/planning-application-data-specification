# Ownership certificates and agricultural land declaration

Who will be affected by the proposal and whether they have been notified, such as agricultural tenants

**Ownership certificates and agricultural land declaration module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| sole-owner | Sole owner | Is the applicant the sole owner of the land? |  | MUST |  |
| agricultural-tenants | Agricultural tenants | Are there any agricultural tenants on the land? | hh, full, technical-details-consent, outline, demolition-con-area, s73 | MUST |  |
| owners-and-tenants | Owners and tenants[]{} | List of known owners and agricultural tenants | hh, full, technical-details-consent, outline, demolition-con-area, s73 | MAY |  |
| lbc-owners | Owners of listed building[]{} | List of known owners | lbc | MAY |  |
| ownership-cert-option | Ownership certificate type | The type of ownership certificate based on ownership and tenancy status |  | MAY | Select from the **ownership-cert-type** enum. Certificate type determined by ownership and notification status |
| steps-taken | Steps taken | Description of steps taken to identify unknown owners or tenants |  | MAY |  |
| newspaper-notices | Newspaper notices[]{} | Details of notices published in papers |  | MAY |  |
| person-reference | Person reference | Declaration must be made by an applicant or agent making the application |  | MUST | Used to link named individuals from the form to a particular declaration or confirmation statement, for example in the declaration module.
 |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application |  | MUST |  |
| declaration-date | Declaration date | The date the declaration was made |  | MUST |  |


**Notified person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | details of the owner (or tenant when not a listed building consent application) | MAY | 
notice-served-date | Notice served date | Date when notice was served | MAY | 


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

- person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future
- declaration-confirmed must be `true` for a submission to be valid