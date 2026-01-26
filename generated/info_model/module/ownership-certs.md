# Ownership certificates and agricultural land declaration

Who will be affected by the proposal and whether they have been notified, such as agricultural tenants

**Ownership certificates and agricultural land declaration module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| sole-owner | Sole owner | Is the applicant the sole owner of the land? | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MUST |  |
| agricultural-tenants | Agricultural tenants | Are there any agricultural tenants on the land? | hh, full, outline, demolition-con-area, s73, extraction-oil-gas | MUST |  |
| owners-and-tenants | Owners and tenants[]{} | List of known owners and agricultural tenants | hh, full, outline, demolition-con-area, s73, extraction-oil-gas | MAY |  |
| lbc-owners | Owners of listed building[]{} | List of known owners | lbc | MAY |  |
| steps-taken | Steps taken | Description of steps taken to identify unknown owners or tenants | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY |  |
| newspaper-notices | Newspaper notices[]{} | Details of notices published in papers | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY |  |
| ownership-cert-option | Ownership certificate type | The type of ownership certificate based on ownership and tenancy status | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY | Select from the **ownership-cert-type** enum |
| applicant-signature | Applicant signature | Digital signature of the applicant | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY |  |
| agent-signature | Agent signature | Digital signature of the agent (if applicable) | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY |  |
| declaration-date | Declaration date | The date the declaration was made | hh, full, outline, demolition-con-area, lbc, s73, extraction-oil-gas | MAY |  |


**Notified person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | details of the owner (or tenant when not a listed building consent application) | MAY | 
notice-date | Notice date | Date when notice was served | MAY | 


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
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 

