# Reserved matters

This application is only required when the applicant has already been granted outline planning permission. Reserved matters can include appearance, means of access, landscaping, layout and scale

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
* [Description of the proposal](#description-of-the-proposal-proposal-details)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Site address details](#site-address-details-site-details)
* [Site visit](#site-visit-site-visit)
* [Supporting information](#supporting-information-supporting-info)

### Required codelists

* [Contact priority](#contact-priority-contact-priority)
* [Reserved matter type](#reserved-matter-type-reserved-matter-type)
* [Site visit contact type](#site-visit-contact-type-site-visit-contact-type)

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

### Description of the proposal (proposal-details)

Details about the proposal

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters[] | Identifies which reserved matters are being submitted for approval as part of this application. | outline;reserved-matters | MUST | See [reserved matter type enum](https://github.com/digital-land/planning-application-data-specification/discussions/209)  |
| related-application | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | A description of what is being proposed, including the development, works, or change of use. | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | Has any work on the proposal has already started. (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | The date when work on the proposal started. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | Has the development or works have already been completed (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | The date when the development or works were completed. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | For applications made on or after 1 August 2021, is the proposal for public service infrastructure development (`true`/`false`)| full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-date | date of the decision | If decided | |

---

### Pre-application advice (pre-app-advice)

Details of pre-application advice received from the local planning authority


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Has pre-application advice has been sought | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Boolean (`true`/`false`) |
| officer-name | Name of officer who dealt with pre-app advice | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| reference | Reference for pre-application advice application | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-date | Date applicant received the advice, in `YYYY-MM-DD` format | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-summary | Summary of the advice received | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | is this necessary if they have provided the reference? |

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

### Site visit (site-visit)

Details needed to support a site visit

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| can-be-seen-from | Can site be seen from a public road  public footpath  bridleway or other public land (`true`/`false`) | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Indicates whether a site visit can be done without arranging access |
| contact-type | Indicate who the authority should be contacting | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | See [site visit contact type enum](https://github.com/digital-land/planning-application-data-specification/discussions/222). Enum + other |
| contact-reference | A reference for the applicant or agent who is the contact point for the site visit | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `applicant` or `agent`. Rule: name must match agent if `contact-type` is `agent`. Rule: name must match applicant name if `contact-type` is `applicant` |
| other-contact{} | Details of specifically named contact | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `other` |

**Other contact structure**

| field | description | requirement-level | notes |
| --- | --- | --- | --- |
| fullname | Name of person to contact | MUST | |
| number | Phone number of person to contact | MUST | |
| email | Email of person to contact | MUST | |

---

### Supporting information (supporting-info)

Information to support the application

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| replacement-drawings[]{} | List of approved drawings being replaced by new drawings | | MUST | |

**Replacement-document**

| field | description | required | notes |
| --- | --- | --- | --- |
| old-drawing-reference | Reference of the old drawing | MUST | |
| new-drawing-reference | Reference for the new drawing | MUST | |
| reason | Reason for replacing the drawing | MAY |  |

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

### Reserved matter type (reserved-matter-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| access | Access | |
| appearance | appearance | |
| landscaping | Landscaping | |
| layout | layout | |
| scale | Scale | |

---

### Site visit contact type (site-visit-contact-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
applicant | Applicant | The applicant of the application
agent | Agent | The agent who completed the form

---

