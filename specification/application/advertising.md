# Advertising

 An application for all types of advertisements and signs

## Contents

Modules

* [Advertisement period](#advertisement-period-advert-period)
* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee / member](#authority-employee-member-conflict-of-interest)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Details of proposed advertisement(s)](#details-of-proposed-advertisements-proposed-advert-details)
* [Interest details](#interest-details-interest-details)
* [Interest in the land](#interest-in-the-land-interest-in-land)
* [Location of advertisement(s)](#location-of-advertisements-advert-location)
* [Materials](#materials-materials)
* [Neighbour and community consultation](#neighbour-and-community-consultation-community-consultation)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Site address details](#site-address-details-site-details)
* [Site visit](#site-visit-site-visit)
* [Type of proposed advertisement(s)](#type-of-proposed-advertisements-advertisement-types)

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

### Advertisement period (advert-period)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advert-start-date | The start of the time period that consent to advertisement is sought | advertising | MUST | should be in `YYYY-MM-DD` format |
| advert-end-date | The end of the time period that consent to advertisement is sought | advertising | MUST | should be in `YYYY-MM-DD` format |

---

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

### Details of proposed advertisement(s) (proposed-advert-details)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisement[] | Structured data about each proposed advertisement |  | MUST | Rule: must be one or more entries |

**Advertisement**

| field | description | notes |
| --- | --- | --- |
| height-from-ground | Height from ground to the base of the advertisement | in metres |
| height | Height of dimensions of advertisement | in metric |
| width | Width of dimensions of advertisement | in metric |
| depth | Depth of dimensions of advertisement | in metric |
| symbol-height-max | Maximum height of any individual letters or symbols | in metric |
| colour | Colour of proposed sign | |
| materials | Materials of proposed sign | | 
| max-projection | Maximum projection of the advertisement from the face of the building | |
| illuminated | True or False. Will the sign(s) be illuminated? | |
| illumination-method | | Required if `illuminated` is true |
| illuminance-level | | Required if `illuminated` is true. cd/m2 |
| illumination-type | Static or intermittent | Required if `illuminated` is true. Is an illumination-type codelist required? |

---

### Interest details (interest-details)

This section collects information on who owns the land or building and the applicants interest

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
applicant-interest | Applicant's interest in the land/listed building |  | MUST | One of: see [applicant's interest type enum](https://github.com/digital-land/planning-application-data-specification/discussions/202) or `None`.
owner-details[]{} | Details of the owner if the applicant is a lessee or occupier |   | MAY | Rule: Required if `applicant-interest` is Lessee or Occupier.
interested-persons[]{} | Details of other interested persons in the listed building |   | MAY | Rule: Required if `applicant-interest` is None.

**Owner(s) model**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.

**Interested persons model**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
nature-of-interest | Nature of the interest in the building | String | MUST | E.g., ownership, tenancy, heritage group.
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.
reason-not-informed | Reason why they were not informed | String | CONDITIONAL | Rule: Required if informed-of-application is False.

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

---

### Interest in the land (interest-in-land)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicant-owns-land | True of False |  | MUST | |
| permission-obtained | True or False. Has permission of the owner for the display of an advertisement been obtained? | | MAY | Rule is a MUST if `applicant-owns-land` is True |
| permission-not-obtained-details | Details if permission not obtained | | MAY | Rule is a MUST if `applicant-owns-land` is True and `permission-obtained` is FALSE |

---

### Location of advertisement(s) (advert-location)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-advert-in-place | True of False |  | MUST | |
| advert-placed-date | YYYY-MM-DD | | MAY | Rule is a MUST if `is-advert-in-place` is True |
| is-replacement-advert | True or False | | MUST |  |
| document-reference[] | References to drawings and photos showing existing signs | | MAY | Rule is a MUST if `is-advert-in-place` OR  `is-replacement-advert` are True |
| is-advert-overhanging | True or False if advertisement will project over a footpath or other public highway | | MUST | |

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

### Type of proposed advertisement(s) (advertisement-types)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisement-proposal-description |  |  | MUST | |
| advertisement-proposal-type[]{} | Expected to provide counts for each advertisement type | | MUST |  |

**advertisement-proposal-type**

| field | description | notes |
| --- | --- | --- |
| advertisement-type | one of the advertisement-types or other | see [advertisement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/190) |
| advertisement-count | number of this type of advertisement | |
| advertisement-other-description | If other is selected then details are required | |

---


## Required codelists

The following codelists are required by modules in this application type:

### Advertisement type (advertisement-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| fascia | Fascia | |
| projecting-hanging | Projecting or hanging sign | |
| hoarding | Hoarding | |
| other | Other | |

---

### Applicant interest type (applicant-interest-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
owner | Owner |
lessee | Lessee | 
occupier | Occupier | 

---

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

### Site visit contact type (site-visit-contact-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
applicant | Applicant | The applicant of the application
agent | Agent | The agent who completed the form

---

