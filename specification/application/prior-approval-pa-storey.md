# Prior approval

This applies to  developments with permitted development rights (where developments are granted planning permission by national legislation without the need to submit a planning application)

## Sub-type: Additional storeys

## Contents

Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of proposed works, impacts and risks](#description-of-proposed-works-impacts-and-risks-desc-work-impacts-risks)
* [Eligibility - Related operations and works](#eligibility---related-operations-and-works-eligibility-related-works)
* [Eligibility - The current building and site](#eligibility---the-current-building-and-site-eligibility-current-building)
* [Eligibility - The proposed development](#eligibility---the-proposed-development-eligibility-proposal)
* [Site address details](#site-address-details-site-details)

Sub-type modules

* [Description of proposed works, impacts and risks](#description-of-proposed-works-impacts-and-risks-desc-work-impacts-risks)
* [Eligibility - Related operations and works](#eligibility---related-operations-and-works-eligibility-related-works)
* [Eligibility - The current building and site](#eligibility---the-current-building-and-site-eligibility-current-building)
* [Eligibility - The proposed development](#eligibility---the-proposed-development-eligibility-proposal)

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

### Description of proposed works, impacts and risks (desc-work-impacts-risks)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
description | Description of proposed development including details of proposed work and external appearance |  | MUST | 
dwellinghouse-height | Height from ground to highest point of roof | | MUST | Should be in metres
proposed-height | Height once the additional storeys have been added | | MUST | Should be in metres
impact-on-amenity | Details of the impacts on the amenity of any adjoining premises including overlooking, privacy and the loss of light including how these will be mitigated | | MUST | Should include mitigations
air-traffic-defence-impacts | Details of any air traffic and defence asset impacts, include how these will be mitigated | | MUST | Should include mitigations
protected-view-impact | Provide details of the impact on any protected view | | MUST | Form says where relevant

---

### Eligibility - Related operations and works (eligibility-related-works)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| external-support-required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening? | | MUST | Impacts whether prior approval is applicable. True or False |

---

### Eligibility - The current building and site (eligibility-current-building)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
in-building-construction-period | Was the current building constructed between 1 July 1948 and 28 October 2018? (`True`/`False`) |   | MUST | One of True, False. If False, application cannot proceed.
additional-storeys-added | Have additional storeys already been added to the original building? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
dwelling-permitted-use | Was the current use of the building granted by permitted development rights? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
site-location-constraint | Is any part of the land or site located in a restricted area? (`True`/`False`)  |   | MUST | One of True, False. If True, application cannot proceed

---

### Eligibility - The proposed development (eligibility-proposal)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
principal-part-only | Will the additional storeys be constructed only on the principal part of the building? |   | MUST | If No, the application cannot proceed.
ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any additional storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
existing-ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any existing storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
building-height-exceeds-18m | Will the height of the extended building exceed 18 metres? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-3-5m | Will the roof exceed 3.5 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-7m | Will the roof exceed 7 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
extension-on-attached-dwelling | Will the extension result in the highest part exceeding 3.5 metres above the attached roof? |   | MAY | Only applicable if the dwelling is not detached.
extension-below-terrace-roof | Will th extension result in the highest part exceeding 3.5 metres above any roof in the terrace? |   | MAY | Only applicable if the dwelling is not detached.
roof-pitch-matching | Will the roof pitch of the extended dwelling match the existing roof pitch? |   | MUST | If No, the application cannot proceed.
window-on-side-elevation | Will the development include a side elevation window or roof slope window? |   | MUST | If Yes, further assessment may be required.
materials-similar-exterior | Will exterior materials be similar to those of the existing dwelling? |   | MUST | If No, the application cannot proceed.
dwellinghouse-use | Will the extended dwelling remain as a Class C3 dwellinghouse or ancillary use? |   | MUST | If No, the application cannot proceed.

---

## Sub-type modules
The following modules are required for this sub-type.

### Description of proposed works, impacts and risks (desc-work-impacts-risks)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
description | Description of proposed development including details of proposed work and external appearance |  | MUST | 
dwellinghouse-height | Height from ground to highest point of roof | | MUST | Should be in metres
proposed-height | Height once the additional storeys have been added | | MUST | Should be in metres
impact-on-amenity | Details of the impacts on the amenity of any adjoining premises including overlooking, privacy and the loss of light including how these will be mitigated | | MUST | Should include mitigations
air-traffic-defence-impacts | Details of any air traffic and defence asset impacts, include how these will be mitigated | | MUST | Should include mitigations
protected-view-impact | Provide details of the impact on any protected view | | MUST | Form says where relevant

---

### Eligibility - Related operations and works (eligibility-related-works)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| external-support-required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening? | | MUST | Impacts whether prior approval is applicable. True or False |

---

### Eligibility - The current building and site (eligibility-current-building)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
in-building-construction-period | Was the current building constructed between 1 July 1948 and 28 October 2018? (`True`/`False`) |   | MUST | One of True, False. If False, application cannot proceed.
additional-storeys-added | Have additional storeys already been added to the original building? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
dwelling-permitted-use | Was the current use of the building granted by permitted development rights? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
site-location-constraint | Is any part of the land or site located in a restricted area? (`True`/`False`)  |   | MUST | One of True, False. If True, application cannot proceed

---

### Eligibility - The proposed development (eligibility-proposal)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
principal-part-only | Will the additional storeys be constructed only on the principal part of the building? |   | MUST | If No, the application cannot proceed.
ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any additional storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
existing-ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any existing storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
building-height-exceeds-18m | Will the height of the extended building exceed 18 metres? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-3-5m | Will the roof exceed 3.5 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-7m | Will the roof exceed 7 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
extension-on-attached-dwelling | Will the extension result in the highest part exceeding 3.5 metres above the attached roof? |   | MAY | Only applicable if the dwelling is not detached.
extension-below-terrace-roof | Will th extension result in the highest part exceeding 3.5 metres above any roof in the terrace? |   | MAY | Only applicable if the dwelling is not detached.
roof-pitch-matching | Will the roof pitch of the extended dwelling match the existing roof pitch? |   | MUST | If No, the application cannot proceed.
window-on-side-elevation | Will the development include a side elevation window or roof slope window? |   | MUST | If Yes, further assessment may be required.
materials-similar-exterior | Will exterior materials be similar to those of the existing dwelling? |   | MUST | If No, the application cannot proceed.
dwellinghouse-use | Will the extended dwelling remain as a Class C3 dwellinghouse or ancillary use? |   | MUST | If No, the application cannot proceed.

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

