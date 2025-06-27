# Lawful development certificate

A legal document stating the lawfulness of past, present or future building use, operation or other matters, signifying that enforcement action cannot be carried out against the development

## Sub-type: LDC Proposed Work to a Listed Building

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
* [Describing what is on the site at the time of application](#describing-what-is-on-the-site-at-the-time-of-application-desc-existing-use)
* [Describing what is on the site at the time of application](#describing-what-is-on-the-site-at-the-time-of-application-desc-existing-use)
* [Description of current use, building works or activity](#description-of-current-use-building-works-or-activity-use-works-activity)
* [Description of current use, building works or activity](#description-of-current-use-building-works-or-activity-use-works-activity)
* [Details about the proposal](#details-about-the-proposal-proposal-details-ldc)
* [Details about the proposal](#details-about-the-proposal-proposal-details-ldc)
* [Grounds for application (information about the existing use(s))](#grounds-for-application-information-about-the-existing-uses-grounds-existing-use)
* [Grounds for application (information about the existing use(s))](#grounds-for-application-information-about-the-existing-uses-grounds-existing-use)
* [Grounds for application (information about the proposed use(s))](#grounds-for-application-information-about-the-proposed-uses-grounds-proposed-use)
* [Grounds for application (information about the proposed use(s))](#grounds-for-application-information-about-the-proposed-uses-grounds-proposed-use)
* [Grounds for application for a lawful development certificate](#grounds-for-application-for-a-lawful-development-certificate-grounds-ldc)
* [Grounds for application for a lawful development certificate](#grounds-for-application-for-a-lawful-development-certificate-grounds-ldc)
* [Information in support of a lawful development certificate](#information-in-support-of-a-lawful-development-certificate-info-support-ldc)
* [Information in support of a lawful development certificate](#information-in-support-of-a-lawful-development-certificate-info-support-ldc)
* [Interest details](#interest-details-interest-details)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Residential units (including conversion)](#residential-units-including-conversion-res-units)
* [Residential units (including conversion)](#residential-units-including-conversion-res-units)
* [Site address details](#site-address-details-site-details)
* [Site visit](#site-visit-site-visit)

### Sub-type modules

* [Description of proposed works](#description-of-proposed-works-desc-proposed-works)
* [Grounds for application](#grounds-for-application-grounds-for-application)
* [Listed building grading](#listed-building-grading-lb-grade)

### Required codelists

* [Applicant interest type](#applicant-interest-type-applicant-interest-type)
* [Contact priority](#contact-priority-contact-priority)
* [Housing type](#housing-type-housing-type)
* [Lawful development certificate need](#lawful-development-certificate-need-lawful-dev-cert-need)
* [Operation type](#operation-type-operation-type)
* [Site visit contact type](#site-visit-contact-type-site-visit-contact-type)
* [Tenure type](#tenure-type-tenure-type)
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

### Interest details (interest-details)

Who owns the land or building and the applicant's interest

field | description | application-Types | required | notes
-- | -- | -- | -- | --
applicant-interest | Applicant's interest in the land/listed building | ldc | MUST | One of: see [applicant's interest type enum](https://github.com/digital-land/planning-application-data-specification/discussions/202) or `None`.
owner-details[]{} | Details of the owner if the applicant is a lessee or occupier | ldc | MAY | Rule: Required if `applicant-interest` is Lessee or Occupier.
interested-persons[]{} | Details of other interested persons in the listed building | ldc | MAY | Rule: Required if `applicant-interest` is None.
applicant-owns-land | Does the applicant own the land? (`True`/`False`) | advertising | MUST |
permission-obtained | Has permission of the owner for the display of an advertisement been obtained? | advertising | MAY | Rule is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Details if permission from the owner has not been obtained | advertising | MAY | Rule is a MUST if `applicant-owns-land` is `False` and `permission-obtained` is `False` |

The [legislation](https://www.legislation.gov.uk/uksi/2007/783/schedule/2) states "No advertisement is to be displayed without the permission of the owner of the site or any other person with an interest in the site entitled to grant permission."

**Owner(s) model**

field | description | data type | required | notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.

**Interested persons model**

field | description | data type | required | notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
nature-of-interest | Nature of the interest in the building | String | MUST | 
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.
reason-not-informed | Reason why they were not informed | String | MAY | Rule: Required if `informed-of-application` is `False`.

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

### Describing what is on the site at the time of application (desc-existing-use)

_To do: add description for module_

field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details[]{} | List of existing site uses and related land areas |   | MUST | Rule: At least one use must be provided.

**existing use structure**

field | description | required | notes
-- | -- | -- | --
use | The Use class of the use | MUST | See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or other
use-details | Further detail of the use | MAY | Rule: required if `use` is `sui` or `other`
land-part | State which part of the land the `use` relates to | MUST | 

---

### Description of current use, building works or activity (use-works-activity)

Please state for which of these you need a lawful development certificate/building works (you must tick at least one option):

field | description | application-types | required | notes
-- | -- | -- | -- | --
ldc-need[] | What is the lawful development certificate needed for? |   | MUST | At least one of [lawful development need enum](https://github.com/digital-land/planning-application-data-specification/discussions/205).
use | If existing-use or use-breach-of-condition is True, state the relevant Use Class |   | MAY | If `existing-use` or `breach-con-existing-use ` in `ldc-need` then applicant needs to provide `use`. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or `other`
specified-use | The specific use if no use class suitable | | MAY | Rule: must be provided if `use` is `sui` or `other`

---

### Grounds for application for a lawful development certificate (grounds-ldc)

Description of development

Field | Description | Application-type | Required? | Notes
-- | -- | -- | -- | --
grounds[] | List of grounds under which the certificate is sought | | MUST | At least one ground must be selected. See [Grounds Enum](https://github.com/digital-land/planning-application-data-specification/discussions/204) .
other-details | Explanation if "Other" ground is selected | | MAY | Required if grounds[] includes other.
supporting-applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site. Include its date and the number of any condition being breached | | MAY | Optional, but strengthens the application.
reason | Reason why the development is considered lawful | | MUST | Applicant’s explanation for granting the certificate.

**Supporting applications / decisions**

_This is similar to other models where supporting or related applications are required. the difference being that this one also needs the condition number._

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Reference number of planning permission, certificate, or notice | String | MAY | Optional, strengthens application.
condition-number | Number of any condition being breached | String | MAY | Relevant if certificate relates to condition breach.
decision-date | Date of the decision (DD/MM/YYYY) | Date | MAY | Must be before the application submission date.

---

### Information in support of a lawful development certificate (info-support-ldc)

Information in support of a lawful development certificate

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| existing-use-start-date | YYYY-MM-DD | | MUST | |
| existing-use-interrupted | True or False | | MUST | |
| interruption-details | | | MAY | Rule, is a MUST if `existing-use-interrupted` is True |
| existing-use-change | True or False | | MUST | |
| existing-use-change-details | | | MAY | Rule, is a MUST if `existing-use-change` is True |

---

### Residential units (including conversion) (res-units)

The amount of residential units included as part of your proposal

Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
residential-unit-change | Proposal includes the gain, loss or change of use of residential units (True/False) | full;outline;ldc | MUST | Could be calculated from answers to next parts?
residential-unit-summary[]{} | Breakdown of unit counts by tenure and housing type | full;outline;ldc | MAY | Is MUST if `residential-unit-change` is True
total-existing-units | The total number of existing units | full;outline;ldc | MUST |
total-proposed-units | The total number of proposed units | full;outline;ldc | MUST |
net-change | Calculated net change in units | full;outline;ldc | MUST | Calculated as proposed-units - existing-units. Format: Integer

**residential-unit-summary**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | See [tenure type enum](https://github.com/digital-land/planning-application-data-specification/discussions/162)
housing-type | Type of housing | Enum | MUST | See [housing type enum](https://github.com/digital-land/planning-application-data-specification/discussions/163)
existing-unit-breakdown[]{} | Number of existing units by bedroom count | Object | MAY | See "Unit quantities Structure" below.
proposed-unit-breakdown[]{} | Number of proposed units by bedroom count | Object | MAY | See "Unit quantities Structure" below.

**Unit quantities** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
units-unknown | Whether the number of units is unknown (`true`/`false`) | Boolean | MUST | 
units-per-bedroom-no[]{} | For this tenure and unit type | Object | MAY | MUST if `units-unknown` is False. See bedroom count
total-units | Total number of units | Integer | MAY | Not required if `units-unknown` is True. Calculated as the sum of all bedroom counts.


**bedroom count**

field | description | data-type | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | Set to true when counting units where bedroom number is unknown | Boolean | MUST || Default is false
no-of-bedrooms | The number of bedrooms in unit | integer | MAY | MUST if no-bedrooms-unknown is true
units | the number of units of that bedroom count | integer | MUST | 0 or above



rule: if residential-unit-change = true, at least one breakdown for existing and proposed is required (count could be unknown).

---

### Describing what is on the site at the time of application (desc-existing-use)

_To do: add description for module_

field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details[]{} | List of existing site uses and related land areas |   | MUST | Rule: At least one use must be provided.

**existing use structure**

field | description | required | notes
-- | -- | -- | --
use | The Use class of the use | MUST | See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or other
use-details | Further detail of the use | MAY | Rule: required if `use` is `sui` or `other`
land-part | State which part of the land the `use` relates to | MUST | 

---

### Description of current use, building works or activity (use-works-activity)

Please state for which of these you need a lawful development certificate/building works (you must tick at least one option):

field | description | application-types | required | notes
-- | -- | -- | -- | --
ldc-need[] | What is the lawful development certificate needed for? |   | MUST | At least one of [lawful development need enum](https://github.com/digital-land/planning-application-data-specification/discussions/205).
use | If existing-use or use-breach-of-condition is True, state the relevant Use Class |   | MAY | If `existing-use` or `breach-con-existing-use ` in `ldc-need` then applicant needs to provide `use`. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or `other`
specified-use | The specific use if no use class suitable | | MAY | Rule: must be provided if `use` is `sui` or `other`

---

### Grounds for application for a lawful development certificate (grounds-ldc)

Description of development

Field | Description | Application-type | Required? | Notes
-- | -- | -- | -- | --
grounds[] | List of grounds under which the certificate is sought | | MUST | At least one ground must be selected. See [Grounds Enum](https://github.com/digital-land/planning-application-data-specification/discussions/204) .
other-details | Explanation if "Other" ground is selected | | MAY | Required if grounds[] includes other.
supporting-applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site. Include its date and the number of any condition being breached | | MAY | Optional, but strengthens the application.
reason | Reason why the development is considered lawful | | MUST | Applicant’s explanation for granting the certificate.

**Supporting applications / decisions**

_This is similar to other models where supporting or related applications are required. the difference being that this one also needs the condition number._

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Reference number of planning permission, certificate, or notice | String | MAY | Optional, strengthens application.
condition-number | Number of any condition being breached | String | MAY | Relevant if certificate relates to condition breach.
decision-date | Date of the decision (DD/MM/YYYY) | Date | MAY | Must be before the application submission date.

---

### Information in support of a lawful development certificate (info-support-ldc)

Information in support of a lawful development certificate

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| existing-use-start-date | YYYY-MM-DD | | MUST | |
| existing-use-interrupted | True or False | | MUST | |
| interruption-details | | | MAY | Rule, is a MUST if `existing-use-interrupted` is True |
| existing-use-change | True or False | | MUST | |
| existing-use-change-details | | | MAY | Rule, is a MUST if `existing-use-change` is True |

---

### Residential units (including conversion) (res-units)

The amount of residential units included as part of your proposal

Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
residential-unit-change | Proposal includes the gain, loss or change of use of residential units (True/False) | full;outline;ldc | MUST | Could be calculated from answers to next parts?
residential-unit-summary[]{} | Breakdown of unit counts by tenure and housing type | full;outline;ldc | MAY | Is MUST if `residential-unit-change` is True
total-existing-units | The total number of existing units | full;outline;ldc | MUST |
total-proposed-units | The total number of proposed units | full;outline;ldc | MUST |
net-change | Calculated net change in units | full;outline;ldc | MUST | Calculated as proposed-units - existing-units. Format: Integer

**residential-unit-summary**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | See [tenure type enum](https://github.com/digital-land/planning-application-data-specification/discussions/162)
housing-type | Type of housing | Enum | MUST | See [housing type enum](https://github.com/digital-land/planning-application-data-specification/discussions/163)
existing-unit-breakdown[]{} | Number of existing units by bedroom count | Object | MAY | See "Unit quantities Structure" below.
proposed-unit-breakdown[]{} | Number of proposed units by bedroom count | Object | MAY | See "Unit quantities Structure" below.

**Unit quantities** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
units-unknown | Whether the number of units is unknown (`true`/`false`) | Boolean | MUST | 
units-per-bedroom-no[]{} | For this tenure and unit type | Object | MAY | MUST if `units-unknown` is False. See bedroom count
total-units | Total number of units | Integer | MAY | Not required if `units-unknown` is True. Calculated as the sum of all bedroom counts.


**bedroom count**

field | description | data-type | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | Set to true when counting units where bedroom number is unknown | Boolean | MUST || Default is false
no-of-bedrooms | The number of bedrooms in unit | integer | MAY | MUST if no-bedrooms-unknown is true
units | the number of units of that bedroom count | integer | MUST | 0 or above



rule: if residential-unit-change = true, at least one breakdown for existing and proposed is required (count could be unknown).

---

### Details about the proposal (proposal-details-ldc)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-incl-building-operations | True or False | ldc | MUST | Is this only for lawful development certificate for proposed work |
| proposal-building-operations-description | | ldc | MAY | If `proposal-incl-building-operations` is True then this must be filled in |
| proposal-incl-change-of-use | True or False | ldc | MUST | |
| proposal-change-of-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-stop-date | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-started | True or False | ldc | MUST | |

---

### Grounds for application (information about the existing use(s)) (grounds-existing-use)

Current use of the site

field | description | application-types | required | notes
-- | -- | -- | -- | --
use-lawful-reason | Explanation of why the existing or last use is lawful |   | MUST | 
documents[] | List of supporting documentary evidence |   | MAY | Optional unless evidence is needed to support the justification.
use | Stated use class of the existing or last use (if applicable) |   | MAY | Use [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) (e.g., C3, B1, E).
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`

---

### Grounds for application (information about the proposed use(s)) (grounds-proposed-use)

Proposed use of development

field | description | application-type | required? | notes
-- | -- | -- | -- | --
use | State proposed use class | | MAY | Applicant's view of the relevant Use Class, if applicable. (see [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189))
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`
operation-type | Whether the proposed use is temporary or permanent | | MUST | Uses [operation type enum](https://github.com/digital-land/planning-application-data-specification/discussions/203).
temporary-details | Details of temporary use | | MAY | Required if operation-type is temporary.
reason | Reason why the development is considered lawful | | MUST | Explanation supporting the certificate application.

---

### Details about the proposal (proposal-details-ldc)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-incl-building-operations | True or False | ldc | MUST | Is this only for lawful development certificate for proposed work |
| proposal-building-operations-description | | ldc | MAY | If `proposal-incl-building-operations` is True then this must be filled in |
| proposal-incl-change-of-use | True or False | ldc | MUST | |
| proposal-change-of-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-stop-date | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-started | True or False | ldc | MUST | |

---

### Grounds for application (information about the existing use(s)) (grounds-existing-use)

Current use of the site

field | description | application-types | required | notes
-- | -- | -- | -- | --
use-lawful-reason | Explanation of why the existing or last use is lawful |   | MUST | 
documents[] | List of supporting documentary evidence |   | MAY | Optional unless evidence is needed to support the justification.
use | Stated use class of the existing or last use (if applicable) |   | MAY | Use [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) (e.g., C3, B1, E).
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`

---

### Grounds for application (information about the proposed use(s)) (grounds-proposed-use)

Proposed use of development

field | description | application-type | required? | notes
-- | -- | -- | -- | --
use | State proposed use class | | MAY | Applicant's view of the relevant Use Class, if applicable. (see [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189))
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`
operation-type | Whether the proposed use is temporary or permanent | | MUST | Uses [operation type enum](https://github.com/digital-land/planning-application-data-specification/discussions/203).
temporary-details | Details of temporary use | | MAY | Required if operation-type is temporary.
reason | Reason why the development is considered lawful | | MUST | Explanation supporting the certificate application.

---

### Description of proposed works (desc-proposed-works)

_To do: add description for module_

Field | Description | Data Type | Application Type | Required? | Notes
-- | -- | -- | -- | -- | --
proposed-works-details | Description of the proposed works | String |  | MUST | Detailed explanation of the work
extension-depth | How far the extension extends beyond the rear wall | Float | prior-approval | MUST | Measured externally in meters
max-extension-height | Maximum height of the extension | Float | prior-approval | MUST | Measured externally from natural ground level
eaves-height | Height at the eaves of the extension | Float | prior-approval | MUST | Measured externally from natural ground level

---

### Grounds for application (grounds-for-application)

Description of development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| grounds-for-application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted including why listed building consent is not required |  | MUST | |
| documents[] | Reference(s) to any supporting documentary evidence| | MUST |  |

---

### Listed building grading (lb-grade)

What grade the listed building is

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Selected from [listed-building-grade](https://dataset-editor.planning.data.gov.uk/dataset/listed-building-grade) or "don't know" |  | MUST | Note the certificate of lawfulness apps do not ask about ecclesiastical grades |
| listed-building | Provide the listed building reference | | MAY | Would make it easier to cross-reference with the official listing |
| provided-by | Details of source of the data. `Applicant` or `System/Service` | | MAY | This can be used by authority to determine if they need to check the data they have been provided |

---

## Sub-type modules
The following modules are required for this sub-type.

### Description of proposed works (desc-proposed-works)

_To do: add description for module_

Field | Description | Data Type | Application Type | Required? | Notes
-- | -- | -- | -- | -- | --
proposed-works-details | Description of the proposed works | String |  | MUST | Detailed explanation of the work
extension-depth | How far the extension extends beyond the rear wall | Float | prior-approval | MUST | Measured externally in meters
max-extension-height | Maximum height of the extension | Float | prior-approval | MUST | Measured externally from natural ground level
eaves-height | Height at the eaves of the extension | Float | prior-approval | MUST | Measured externally from natural ground level

---

### Grounds for application (grounds-for-application)

Description of development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| grounds-for-application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted including why listed building consent is not required |  | MUST | |
| documents[] | Reference(s) to any supporting documentary evidence| | MUST |  |

---

### Listed building grading (lb-grade)

What grade the listed building is

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Selected from [listed-building-grade](https://dataset-editor.planning.data.gov.uk/dataset/listed-building-grade) or "don't know" |  | MUST | Note the certificate of lawfulness apps do not ask about ecclesiastical grades |
| listed-building | Provide the listed building reference | | MAY | Would make it easier to cross-reference with the official listing |
| provided-by | Details of source of the data. `Applicant` or `System/Service` | | MAY | This can be used by authority to determine if they need to check the data they have been provided |

---


## Required codelists

The following codelists are required by modules in this application type:

### Applicant interest type (applicant-interest-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
owner | Owner |
lessee | Lessee | 
occupier | Occupier | 

---

### Contact priority (contact-priority)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

---

### Housing type (housing-type)

_To do: add description for codelist_

reference | name | description | application-types
-- | -- | -- | --
houses | Houses | Detached, semi-detached, or terraced houses. |  
flats-maisonettes | Flats/Maisonettes | Self-contained apartments or maisonettes. |  
sheltered-housing | Sheltered Housing | Housing with support for older or disabled people. |  
bedsit-studio | Bedsit/Studio | Single-room living spaces. |  
cluster-flats | Cluster Flats | Flats with shared communal areas. |  
other | Other | Any other housing type not listed. |  
live-work-units | Live-Work Units | Properties combining residential and workspace. | ldc
unknown | Unknown | When the type of housing is uncertain. | ldc

---

### Lawful development certificate need (lawful-dev-cert-need)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
existing-use | Existing use | 
existing-building-work | Existing building work |
breach-con-existing-use | Existing use in breach of condition | 
breach-con-building-work | Building work in breach of condition | 
breach-con-activity | Activity in breach of condition | 

---

### Operation type (operation-type)

_To do: add description for codelist_

reference | name | description 
--- | --- | ---
permanent | Permanent | 
temporary | Temporary | 

---

### Site visit contact type (site-visit-contact-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
applicant | Applicant | The applicant of the application
agent | Agent | The agent who completed the form

---

### Tenure type (tenure-type)

_To do: add description for codelist_

reference | name | description | application-types
-- | -- | -- | --
market-housing | Market Housing | Private housing for sale or rent. |  ldc;full;outline
social-rented | Social Rented Housing | Public/social housing at below-market rents. | ldc
intermediate-housing | Intermediate Housing | Housing with rents or ownership costs between social housing and market housing. | ldc
key-worker-housing | Key Worker Housing | Housing for essential workers (e.g. teachers, NHS staff). | ldc
affordable-rent | Social, Affordable, or Intermediate Rent | Housing for below-market rent. | full;outline
home-ownership | Affordable Home Ownership | Shared ownership or similar schemes. | full;outline
starter-homes | Starter Homes | Discounted homes for first-time buyers. | full;outline
custom-build | Self-Build and Custom Build | Homes built or commissioned by individuals. | full;outline

---

