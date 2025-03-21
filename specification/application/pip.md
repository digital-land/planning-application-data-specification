# Permission in principle

An alternative way of getting planning permission for housing-led development which separates the consideration of matters of principle from the technical detail of the development

## Contents

Modules

* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee / member](#authority-employee-member-conflict-of-interest)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of the proposed development including any non-residential development](#description-of-the-proposed-development-including-any-non-residential-development-proposal-details-inc-non-residential)
* [Site address details](#site-address-details-site-details)
* [Site information](#site-information-site-info)

---

## Application data specification

field	| description	| data-type | required | notes
--- | --- | --- | --- | ---
reference | UUID for the application record | UUID | MUST | 
application-types[] | A list of planning application types | Enum | MUST | See [list of application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)
application-sub-type | Sub-category of the application | Enum | See [list of application sub-types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv)
planning-authority | The reference of the planning authority the application has been submitted to | Organisation reference | MUST | 
submission-date | Date the application is submitted. In `YYYY-MM-DD` format |	Date | MUST |	
modules[] | List of required sections/modules for this application | List |	MUST | List of predefined module references that can be used to validate the application
documents[]{} | List of submitted documents | List | MUST |	Uses a document model to capture references and details.

**Document structure**

field | description | required | notes
--- | --- | --- | ---
reference | A reference for the document | MUST | This should be unique
name | The name or title of the document | MUST | 
description | Brief description of what the document contains	| MAY | Optional but useful for context
document-types[] | List of codelist references that the document covers | MUST | Use the planning requirements enum
file | The digital file or a reference to where the file is stored | MUST | Object / URL / Blob
mime-type | The document's MIME type | MAY | e.g., application/pdf, image/jpeg

---

## Modules

These modules are all required for this application type

### Agent name and address (agent-details)

Details about the agent

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent{} | Details of the agent | | MUST | |

**Agent object**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| company | The company the agent works for | | MAY | |
| Contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact agent | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | MAY | is this still necessary? |

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
| applicants[]{} | Details for one or more applicants | | MUST | Rules: must be one or more named applicants |

**Applicant object**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| Contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact agent | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Authority employee / member (conflict-of-interest)

This section ensures transparency by declaring any connection between the applicant or agent and the local authority’s staff or elected members that could present a conflict of interest.

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member  | | MUST | answer may be different depending on the parties involved |
| name | Name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how individual is related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST |

---

### Checklist (checklist)

This section provides details of the national planning requirements the applicant is required to submit along with the application

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type |  | MUST |  |

---

### Declaration (declaration)

Applicants and agents are required to declare information provided is correct

| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | The applicant(s) and agent need to confirm the information provided is correct to the best of their knowledge | | MUST | Boolean - `true` / `false`
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |

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

Details to help locate the site proposed for development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-boundary | Geometry of the site of the development | | MUST | online services can send the boundary supplied by the applicant/agent. Paper forms would need one of the other fields translated into this |
| address-text | Text address if available for the site | | MAY | does the address need to be structured data or a blob of text like in some app forms? |
| easting | Grid reference | | MAY | |
| northing | Grid reference | | MAY | |
| latitude | Latitude coordinate in EPSG:4326 (WGS84) | | MAY | |
| longitude | Longitude coordinate in EPSG:4326 (WGS84) | | MAY | |
| description | Description of the location if `address-text` does not exist for development/site | | MAY | | 

### Rules

Applicant/agent must provide one of:
* site-boundary
* address
* easting + northing

---

### Site information (site-info)

_To do: add description for module_

## Site information 

Field | Description | Application-Types | Required? | Notes
-- | -- | -- | -- | --
site-area{} | The total area of the site |   | MUST | See "Site Area Structure" below
existing-use[]{} | Structured information on the current use of the site |   | MUST | An array, as there may be multiple uses (see "Existing Use Structure")
known-constraints[] | A list of the known constraints affecting the site |   | MUST | See the [Site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)
supporting-documents[]{} | A list of documents with the supporting information for the idenitifed site constraints | MAY | Rule: a MUST if `known-constraints` is not empty

### Site Area Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
value | Numeric value representing site area | Number | MUST | Should ideally be calculated from site boundary
unit | Unit of measurement for site area | Enum | MUST | One of: m2, hectares
provided-by | Whether the site area was provided by the applicant or system |   | MAY | Enum: Applicant, System/Service

### Existing Use Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
use-classes[] | List of applicable use classes | Enum | MUST | Mixed-use sites can list multiple classes. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
floorspace | Total floorspace for the use | Number | MUST | Numeric value. Expected in m2

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
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

