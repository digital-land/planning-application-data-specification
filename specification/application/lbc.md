# Listed building consent

An application for any alteration, extension, or demolition of a listed building

## Contents

Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee / member](#authority-employee-member-conflict-of-interest)
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

### Agent contact details (agent-contact)

Details needed for contacting the agent

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| Contact-details{} | Details of how to contact the individual | | MAY | Rule: is a MUST if `application-type` is `pip` |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the individual | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

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

### Applicant contact details (applicant-contact)

Details needed for contacting the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| Contact-details{} | Details of how to contact the individual | | MAY | Rule: is a MUST if `application-type` is `pip` |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the individual | MAY | is this still necessary? |

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

### Demolition (demolition)

_To do: add description for module_

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
| reserved-matters-for-approval[] | Identifies which reserved matters are being submitted for approval as part of this application. | outline;reserved-matters | MUST | See [reserved matter type enum](https://github.com/digital-land/planning-application-data-specification/discussions/209)  |
| related-proposal | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | A description of what is being proposed, including the development, works, or change of use. | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | Has any work on the proposal has already started. (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | The date when work on the proposal started. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | Has the development or works have already been completed (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | The date when the development or works were completed. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | (`true`/`false`)| full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided | |

---

### Immunity from listing (immunity-from-listing)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| cert-of-im-sought | Has a certificate of immunity been sought. Options: Yes, No, Don't know |  | MUST |  |
| application-result | Provide the result of the application | | MAY | Rule: is required if `cert-of-im-sought` is True |

---

### Listed building alterations (lb-alter)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-alter-lb | True or False if proposal includes alterations |  | MUST |  |
| proposal-alter-lb-types[] | Select from a list of listed building alteration types, select all that apply | | MAY | Rule: is required if `proposal-alter-lb` is True |
| document-reference[] | References to documents detailing the proposed alterations | | MAY | Rule: is required if `proposal-alter-lb` is True |

See [listed building alteration types enum](https://github.com/digital-land/planning-application-data-specification/discussions/187)

---

### Listed building grading (lb-grade)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Selected from [listed-building-grade](https://dluhc-datasets.planning-data.dev/dataset/listed-building-grade) or "don't know" |  | MUST | Note the certificate of lawfulness apps do not ask about ecclesiastical grades |
| listed-building | Provide the listed building reference | | MAY | Would make it easier to cross-reference with the official listing |
| provided-by | Details of source of the data. `Applicant` or `System/Service` | | MAY | This can be used by authority to determine if they need to check the data they have been provided |

---

### Materials (materials)

Where applicable details about the materials to be used or changed should be provided. Including type, colour and name for each material

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element[]{} | List of building elements where materials are being described (e.g., walls, roof). |  | MUST | See Building element structure. One entry per building element.
additional-material-information | States whether supporting documents are being provided with further material details. |  | MUST | Boolean: true or false.
supporting-documents[] | Details for documents providing additional material information. |  | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Neighbour and community consultation (community-consultation)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| have-consulted | True or False |  | MUST | |
| description | Provide details of consultation | | MAY | Rule: is a MUST if `neighbours-consulted` is True |

---

### Ownership certificates and agricultural land declaration (ownership-certs)

Ownership of the site and/or property for development needs to be understood

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
sole-owner | Is the applicant the sole owner of the land? (True/False) |   | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |   | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[] | List of known owners and agricultural tenants |   | MAY | Required for Certificate-B or Certificate-C.
steps-taken | Steps taken to identify unknown owners or tenants |   | MAY | Required for Certificate-C or Certificate-D.
newspaper-notice | Newspaper notice details for unknown owners/tenants |   | MAY | Required for Certificate-C or Certificate-D.
ownership-cert-option | Ownership certificate type based on ownership and tenancy |   | MUST | See [ownership certificate type enum](https://github.com/digital-land/planning-application-data-specification/discussions/224)
applicant-signature | Signature of the applicant |   | MAY |  
agent-signature | Signature of the agent (if applicable) |   | MAY |  
signature-date | Date of applicant or agent signature |   | MUST | Format: YYYY-MM-DD.

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
| post-code | The post code for the address provided | MAY | |

---

### Pre-application advice (pre-app-advice)

A section for providing details of pre application advice received from the authority


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Has pre-application advice has been sought | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Boolean (`true`/`false`) |
| officer-name | Name of officer who dealt with pre-app advice | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| reference | Reference for pre-application advice application | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-date | Date applicant received the advice, in `YYYY-MM-DD` format | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-summary | Summary of the advice received | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | is this necessary if they have provided the reference? |

---

### Related proposals (related-proposals)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-related-proposals | True of False. True if any related applications, previous proposals or demolitions for the site |  | MUST | |
| related-proposal[] | List of related applications | MAY | Rule is a MUST if `has-related-proposals` is True |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided | |

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

### Site visit (site-visit)

Details needed to support a site visit

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-seen-from | Can site be seen from a public road  public footpath  bridleway or other public land (`true`/`false`) | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Indicates whether a site visit can be done without arranging access |
| contact-type | Indicate who the authority should be contacting | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | See [site visit contact type enum](https://github.com/digital-land/planning-application-data-specification/discussions/222). Enum + other |
| contact | The name of the applicant or agent | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `applicant` or `agent`. Rule: name must match agent if `contact-type` is `agent`. Rule: name must match applicant name if `contact-type` is `applicant` |
| other-contact{} | Details of specifially named contact | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `other` |

**Other contact structure**
| name | Name of person to contact | MUST | |
| number | Phone number of person to contact | MUST | |
| email | Email of person to contact | MUST | |

---


## Required codelists

The following codelists are required by modules in this application type:

### Building element type (building-element-type)

A set of building elements that applicants are expected to provide material information for

| reference | name | application-types | 
| --- | --- | -- |
| walls | Walls | advertising;demolition-con-area;full;hh;outline |
| roof | Roof | advertising;demolition-con-area;full;hh;outline |
| windows | Windows | advertising;demolition-con-area;full;hh;outline |
| doors | Doors | advertising;demolition-con-area;full;hh;outline |
| boundary-treatments | Boundary treatments | advertising;demolition-con-area;full;hh;lbc;outline |
| vehicle-access-hard-standings | Vehicle access and hard-standings | advertising;demolition-con-area;full;hh;lbc;outline |
| lighting | Lighting | advertising;demolition-con-area;full;hh;lbc;outline |
| external-walls | External walls | lbc |
| roof-covering | Roof covering | lbc |
| chimney | Chimney | lbc |
| external-doors | External doors | lbc |
| ceilings | Ceilings | lbc |
| internal-walls | Internal walls | lbc |
| floors | Floors | lbc |
| internal-doors | Internal doors | lbc |
| rainwater-goods | Rainwater goods | lbc |
| other | Other | advertising;demolition-con-area;full;hh;lbc;outline |

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

