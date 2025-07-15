Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
sole-owner | Is the applicant the sole owner of the land? (True/False) | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |  hh;full;outline;demolition-con-area;s73;extraction-oil-gas | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[]{} | List of known owners and agricultural tenants | hh;full;outline;demolition-con-area;s73;extraction-oil-gas  | MAY | Required for Certificate-B or Certificate-C.
lbc-owners[]{} | List of owners of the listed building | MAY | 
steps-taken | Steps taken to identify unknown owners or tenants | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY | Required for Certificate-C or Certificate-D.
newspaper-notice[]{} | Newspaper notice details for unknown owners/tenants |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MAY | Required for Certificate-C or Certificate-D.
ownership-cert-option | Ownership certificate type based on ownership and tenancy | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MUST | See [ownership certificate type enum](https://github.com/digital-land/planning-application-data-specification/discussions/224)
applicant-signature | Signature of the applicant | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY |  
agent-signature | Signature of the agent (if applicable) |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MAY |  
signature-date | Date of applicant or agent signature | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MUST | Format: YYYY-MM-DD.

**Owners and tenants**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Owner or tenant details | Person model | MUST | Reuse existing Person model.
notice-date | Date notice was served | Date | MUST | Format: YYYY-MM-DD.

**Newspaper notice**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
newspaper-name | Name of the newspaper | String | MUST |  
publication-date | Date of publication | Date | MUST | Format: YYYY-MM-DD.

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |
