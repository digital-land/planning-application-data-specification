# Permission in principle

An alternative way of getting planning permission for housing-led development which separates the consideration of matters of principle from the technical detail of the development

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee/member](#authority-employee-member-conflict-of-interest)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of the proposed development including any non-residential development](#description-of-the-proposed-development-including-any-non-residential-development-proposal-details-inc-non-residential)
* [Site address details](#site-address-details-site-details)
* [Site information](#site-information-site-info)

### Required codelists

* [Contact priority](#contact-priority-contact-priority)
* [Non-residential measurement type](#non-residential-measurement-type-non-res-measurement-type)
* [Use class](#use-class-use-class)

---

## Application data specification

field	| description	| data-type | required | notes
--- | --- | --- | --- | ---
reference | UUID for the application record | UUID | MUST | 
application-types[] | A list of planning application types | Enum | MUST | See [list of application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)
application-sub-type | Further classification of the application type for specific variations | Enum | See [list of application sub-types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv)
planning-authority | The reference of the planning authority the application has been submitted to | Organisation reference | MUST | 
submission-date | Date the application is submitted. In `YYYY-MM-DD` format |	Date | MUST |	
modules[] | List of required sections/modules for this application | List |	MUST | List of predefined module references that can be used to validate the application
documents[]{} | List of submitted documents | List | MUST |	Uses a document model to capture references and details.
fee{} | The fee payable for the application | Object | MAY | 

**Document structure**

field | description | required | notes
--- | --- | --- | ---
reference | A reference for the document | MUST | This should be unique
name | The name or title of the document | MUST | 
description | Brief description of what the document contains	| MAY | Optional but useful for context
document-types[] | List of codelist references that the document covers | MUST | Use the planning requirements enum
file{} | The digital file or a reference to where the file is stored | MUST | Must contain either `url` or `base64`, but not both.

**Fee structure**

field | description | required | notes
--- | --- | --- | ---
amount | The total amount due | MUST | 
amount-paid | The amount paid | MUST |
transactions[] | References to payments or financial transactions related to this application. | MAY | Useful for audit and reconciliation.

**File data structure**

field | description | required | notes
--- | --- | --- | ---
url | A URL pointing to the stored file | MAY | For previously uploaded or hosted files
base64 | Base64-encoded content of the file | MAY | For inline file uploads
filename | Name of the file being uploaded | MUST | Useful for identifying and preserving the file
mime-type | The file's MIME type | MAY | e.g., `application/pdf`, `image/jpeg`
checksum | Hash of the file contents (e.g., SHA-256) | MAY      | Used for file validation and checking files have not been tampered with
file-size | Size of the file in bytes | MAY | Can be used to enforce limits

---

## Modules

These modules are all required for this application type

### Agent contact details (agent-contact)

Details needed for contacting the person representing the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent-reference | Use a reference from the agent details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Agent name and address (agent-details)

Details about the person representing the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent{} | Details of the agent | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Agent object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |
| company | The company the agent works for | MAY | |
| user-role | A specific of the user, either agent or proxy | MAY | used to determine if the details should be redacted

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |

---

### Applicant contact details (applicant-contact)

Details needed for contacting the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicant-reference | Use a reference from the applicant details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Applicant name and address (applicant-details)

Details about the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicants[]{} | Details for one or more applicants | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Rules: must be one or more named applicants |

**Applicant object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |

---

### Authority employee/member (conflict-of-interest)

Any connection between the applicant or agent and the local authority’s staff or elected members that could present a conflict of interest

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared. | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MUST | Answer may be different depending on the parties involved. "With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member" |
| name | Name of the individual with the conflict | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| conflict-details | Details including name, role and how individual is related to them | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MAY | Rule: if `conflict-to-declare` is true then this is a MUST |

---

### Checklist (checklist)

Details of the national planning requirements the applicant should submit along with the application

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST |  |

---

### Declaration (declaration)

Applicants and agents must declare information provided is correct

| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | (`true` / `false`)
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |

---

### Description of the proposed development including any non-residential development (proposal-details-inc-non-residential)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of proposed development including non-residential development |  | MUST | |
| net-dwellings-min | The minimum number of net additional dwellings proposed as part of the development. This accounts for any existing dwellings lost and new dwellings created. | | MUST |  |
| net-dwellings-max | The maximum number of net additional dwellings proposed as part of the development, allowing for flexibility in the final housing numbers. | | MUST |  |
| non-residential-use[]{} | The amount of non-residential use. Can be floorspace, hectares or both. | | MUST | From form: "Can be expressed as a range, a maximum or a fixed amount". This is used to check non-residential use is less than residential use |

**Non residential use structure**

| field | description | notes |
| --- | --- | --- |
| non-residential-measurement-type | The type of value being provided. `floorspace` or `site-area` | See [non-residential-measurement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/188) |
| exact-value | Exact figure of non-residential use | m2 for floorspace, hectares for site-area |
| min | Low bound of non-residential use | m2 for floorspace, hectares for site-area |
| max | Upper bound of non-residential use | m2 for floorspace, hectares for site-area |

---

### Site address details (site-details)

Details to locate the site proposed for development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-locations[]{} | Details of the sites on which the tree(s) are located | notice-trees-in-con-area;consent-under-tpo | MAY | Rule: only required if the site is different from the applicant's address | 

**site-location/details structure**

| field | description | required | notes |
| --- | --- | --- | --- |
| site-boundary | Geometry of the site of the development | MUST | online services can send the boundary supplied by the applicant/agent. Paper forms would need one of the other fields translated into this |
| address-text | Text address if available for the site | MAY | does the address need to be structured data or a blob of text like in some app forms? |
| postcode | The post code for the address provided | MAY | |
| easting | Grid reference | MAY | |
| northing | Grid reference | MAY | |
| latitude | Latitude coordinate in EPSG:4326 (WGS84) | MAY | |
| longitude | Longitude coordinate in EPSG:4326 (WGS84) | MAY | |
| description | Description of the location if `address-text` does not exist for development/site | MAY | |
| uprns[] | Where known, list the UPRNs affected by the proposal | MAY | UPRN data can support clearer tracking, analysis, and integration across systems. We recommend that the list of uprns is derived where possible |

### Rules

Applicant/agent must provide one of:
* site-boundary
* address
* easting + northing

---

### Site information (site-info)

Additional information about the site

## Site information 

Field | Description | Application-Types | Required? | Notes
-- | -- | -- | -- | --
site-area{} | The total area of the site |   | MUST | See "Site Area Structure" below
existing-use[]{} | Structured information on the current use of the site |   | MUST | An array, as there may be multiple uses (see "Existing Use Structure")
known-constraints[] | A list of the known constraints affecting the site |   | MUST | See the [Site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)
supporting-documents[]{} | A list of documents with the supporting information for the identified site constraints | MAY | Rule: a MUST if `known-constraints` is not empty

### Site Area Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
value | Numeric value representing site area | Number | MUST | Should ideally be calculated from site boundary
unit | Unit of measurement for site area | Enum | MUST | One of: m2, hectares
provided-by | Whether the site area was provided by the applicant or system |   | MAY | Enum: Applicant, System/Service

### Existing Use Structure

field | description | data type | required? | notes
-- | -- | -- | -- | --
uses[]{} | List of applicable uses | Enum | MUST | Mixed-use sites can list multiple classes. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
floorspace | Total floorspace for the use | Number | MUST | Numeric value. Expected in m2

**Use structure**
field | description | data-type | required | notes
--- | --- | --- | --- | ---
use | A non-residential use | Enum+other | MUST | 
specified-use | A specified use if no applicable use class | String | MAY | Rule: must if `use` is `sui` or `other`

**Supporting documents structure**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
details | Additional details about the document, for example, details about the constraint it references | String | MAY | 

---


## Required codelists

The following codelists are required by modules in this application type:

### Contact priority (contact-priority)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

---

### Non-residential measurement type (non-res-measurement-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| floorspace | Floorspace | Provided in m2 |
| site-area | Site area | Provided in hectares |

---

