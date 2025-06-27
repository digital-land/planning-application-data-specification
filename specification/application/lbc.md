# Listed building consent

An application for any alteration, extension, or demolition of a listed building

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
* [Demolition](#demolition-demolition)
* [Description of the proposal](#description-of-the-proposal-proposal-details)
* [Immunity from listing](#immunity-from-listing-immunity-from-listing)
* [Listed building alterations](#listed-building-alterations-lb-alter)
* [Listed building grading](#listed-building-grading-lb-grade)
* [Materials](#materials-materials)
* [Neighbour and community consultation](#neighbour-and-community-consultation-community-consultation)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration-ownership-certs)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Related proposals](#related-proposals-related-proposals)
* [Site address details](#site-address-details-site-details)
* [Site visit](#site-visit-site-visit)

### Required codelists

* [Building element type](#building-element-type-building-element-type)
* [Contact priority](#contact-priority-contact-priority)
* [Listed building alteration type](#listed-building-alteration-type-lb-alteration-type)
* [Ownership certificate type](#ownership-certificate-type-ownership-cert-type)
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

### Demolition (demolition)

Permission or prior approval that may be required to demolish a building

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| demolition | True or False based on whether proposal includes partial or total demolition of a listed building | lbc | MUST |  |
| demolition-total | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| demolition-building-in-curtilage | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| demolition-part | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| listed-building-volume | Volume of listed building in cubic metres | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST |
| demolition-volume | Volume of part to be demolished in cubic metres | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST |
| part-built-date | The approximate date the part to be removed was built | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST Format should be YYYY-MM-DD. Approximate dates are allowed |
| description | Description of the the building or part you are proposing to demolish | lbc | MUST | |
| reason | Reason for demolition | lbc | MUST | |

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

### Immunity from listing (immunity-from-listing)

Whether you have an immunity from listing

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| cert-of-im-sought | Has a certificate of immunity been sought. Options: Yes, No, Don't know |  | MUST |  |
| application-result | Provide the result of the application | | MAY | Rule: is required if `cert-of-im-sought` is True |

---

### Listed building alterations (lb-alter)

What you're proposing to do to a listed building

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-alter-lb | True or False if proposal includes alterations |  | MUST |  |
| proposal-alter-lb-types[] | Select from a list of listed building alteration types, select all that apply | | MAY | Rule: is required if `proposal-alter-lb` is True |
| document-reference[] | References to documents detailing the proposed alterations | | MAY | Rule: is required if `proposal-alter-lb` is True |

See [listed building alteration types enum](https://github.com/digital-land/planning-application-data-specification/discussions/187)

---

### Listed building grading (lb-grade)

What grade the listed building is

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Selected from [listed-building-grade](https://dataset-editor.planning.data.gov.uk/dataset/listed-building-grade) or "don't know" |  | MUST | Note the certificate of lawfulness apps do not ask about ecclesiastical grades |
| listed-building | Provide the listed building reference | | MAY | Would make it easier to cross-reference with the official listing |
| provided-by | Details of source of the data. `Applicant` or `System/Service` | | MAY | This can be used by authority to determine if they need to check the data they have been provided |

---

### Materials (materials)

Details about the materials to be used or changed should be provided, including type, colour and name for each material

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-elements[]{} | List of building elements where materials are being described (e.g., walls, roof). | hh;full;demolition-con-area;lbc;advertising;outline | MUST | See Building element structure. One entry per building element.
additional-material-information | Indicates whether additional documents are provided to supplement the materials description | hh;full;demolition-con-area;lbc;advertising;outline | MUST | (`true` or `false`).
supporting-documents[] | Details for documents providing additional material information. | hh;full;demolition-con-area;lbc;advertising;outline | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Neighbour and community consultation (community-consultation)

Neighbours should be informed about development proposals and seek feedback

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| have-consulted | True or False |  | MUST | |
| description | Provide details of consultation | | MAY | Rule: is a MUST if `neighbours-consulted` is True |

---

### Ownership certificates and agricultural land declaration (ownership-certs)

Ownership of the site and/or property for development needs to be understood

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
sole-owner | Is the applicant the sole owner of the land? (True/False) | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[]{} | List of known owners and agricultural tenants | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY | Required for Certificate-B or Certificate-C.
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

### Related proposals (related-proposals)

Other applications related to the same site

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-related-proposals | True of False. True if any related applications, previous proposals or demolitions for the site |  | MUST | |
| related-proposal[] | List of related applications | MAY | Rule is a MUST if `has-related-proposals` is True |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-date | date of the decision | If decided | |

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


## Required codelists

The following codelists are required by modules in this application type:

### Building element type (building-element-type)

A set of building elements that applicants are expected to provide material information for

| reference | name | description | application-types | notes |
| --- | --- | --- | --- | --- |
| walls | Walls | A vertical construction that bounds or subdivides spaces | advertising;demolition-con-area;full;hh;outline | Referring to same thing as [IfcWall](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD1/HTML/link/ifcbuildingelement.htm) |
| roof | Roof | A covering of the top part of a building, it protects the building against the effects of weather | advertising;demolition-con-area;full;hh;outline | Referring to same thing as IfcWall |
| windows | Windows | | advertising;demolition-con-area;full;hh;outline | |
| doors | Doors | | advertising;demolition-con-area;full;hh;outline | |
| boundary-treatments | Boundary treatments | | advertising;demolition-con-area;full;hh;lbc;outline | |
| vehicle-access-hard-standings | Vehicle access and hard-standings | | advertising;demolition-con-area;full;hh;lbc;outline | |
| lighting | Lighting | | advertising;demolition-con-area;full;hh;lbc;outline | |
| external-walls | External walls | | lbc | |
| roof-covering | Roof covering | | lbc | |
| chimney | Chimney | | lbc | |
| external-doors | External doors | | lbc | |
| ceilings | Ceilings | | lbc | |
| internal-walls | Internal walls | | lbc | |
| floors | Floors | | lbc | |
| internal-doors | Internal doors | | lbc | |
| rainwater-goods | Rainwater goods | | lbc | |
| other | Other | | advertising;demolition-con-area;full;hh;lbc;outline | |

---

### Contact priority (contact-priority)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

---

### Listed building alteration type (lb-alteration-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| interior | Interior of building | Works to the interior of the building |
| exterior | Exterior of building | Works to the exterior of the building |
| fixed | Fixed structure or object | Works to any structure or object fixed to the property (or buildings with the curtilage) internally or externally |
| stripping | Stripping out | Stripping out of any internal wall, ceiling or floor finishes |

---

### Ownership certificate type (ownership-cert-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
certificate-a | Certificate A | Applicant is the sole owner of the land and there are no agricultural tenants.
certificate-b | Certificate B | Applicant knows all other owners or agricultural tenants and has notified them.
certificate-c | Certificate C | Applicant knows some of the other owners or agricultural tenants and has notified those they know.
certificate-d | Certificate D | Applicant does not know any of the other owners or agricultural tenants.

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

