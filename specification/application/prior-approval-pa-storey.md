# Prior approval

This applies to  developments with permitted development rights (where developments are granted planning permission by national legislation without the need to submit a planning application)

## Sub-type: Additional storeys

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Adjoining premises](#adjoining-premises-adj-premises)
* [Adjoining premises](#adjoining-premises-adj-premises)
* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee/member](#authority-employee-member-conflict-of-interest)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of proposed works](#description-of-proposed-works-desc-proposed-works)
* [Description of proposed works](#description-of-proposed-works-desc-proposed-works)
* [Eligibility - Larger house extension](#eligibility---larger-house-extension-eligibility-extension)
* [Eligibility - Larger house extension](#eligibility---larger-house-extension-eligibility-extension)
* [Site address details](#site-address-details-site-details)

### Sub-type modules

* [Description of proposed works, impacts and risks](#description-of-proposed-works-impacts-and-risks-desc-work-impacts-risks)
* [Eligibility - Related operations and works](#eligibility---related-operations-and-works-eligibility-related-works)
* [Eligibility - The current building and site](#eligibility---the-current-building-and-site-eligibility-current-building)
* [Eligibility - The proposed development](#eligibility---the-proposed-development-eligibility-proposal)

### Required codelists

* [Contact priority](#contact-priority-contact-priority)
* [Site constraints](#site-constraints-site-constraint)

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

### Adjoining premises (adj-premises)

The addresses of any adjoining properties

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| addresses[]{} | A list of addressed for the adjoining properties | | MUST |  |

**Address model**

field | description | data type | required | notes
-- | -- | -- | -- | --
address-test | Address details | String | MUST | 
postcode | Postcode of address if available | String | MAY | 
uprn | UPRN if known | UPRN | MAY | 

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

### Eligibility - Larger house extension (eligibility-extension)

Checking eligibility for prior approval

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
single-storey-extension | Will the extension be a single storey? (True/False) |   | MUST | If False, the application cannot proceed.
extension-height-over-4m | Will the extension exceed 4 metres in height? (True/False) |   | MUST | If True, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
rear-extension-length | Will the extension extend beyond the rear wall of the original dwelling? |   | MUST | See conditional logic for limits based on attachment type.
extension-length | Length of rear extension (in metres) |   | MUST | 
within-site-constraints | Is the dwellinghouse within any restricted area? (True/False) |   | MUST | If True, the application cannot proceed.
site-constraints[] | List of specific site constraints |   | MAY | Rule: Required if within-site-restrictions is True. See [site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)

---

### Adjoining premises (adj-premises)

The addresses of any adjoining properties

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| addresses[]{} | A list of addressed for the adjoining properties | | MUST |  |

**Address model**

field | description | data type | required | notes
-- | -- | -- | -- | --
address-test | Address details | String | MUST | 
postcode | Postcode of address if available | String | MAY | 
uprn | UPRN if known | UPRN | MAY | 

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

### Eligibility - Larger house extension (eligibility-extension)

Checking eligibility for prior approval

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
single-storey-extension | Will the extension be a single storey? (True/False) |   | MUST | If False, the application cannot proceed.
extension-height-over-4m | Will the extension exceed 4 metres in height? (True/False) |   | MUST | If True, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
rear-extension-length | Will the extension extend beyond the rear wall of the original dwelling? |   | MUST | See conditional logic for limits based on attachment type.
extension-length | Length of rear extension (in metres) |   | MUST | 
within-site-constraints | Is the dwellinghouse within any restricted area? (True/False) |   | MUST | If True, the application cannot proceed.
site-constraints[] | List of specific site constraints |   | MAY | Rule: Required if within-site-restrictions is True. See [site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)

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

Checking eligibility for prior approval

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| external-support-required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening? | | MUST | Impacts whether prior approval is applicable. True or False |

---

### Eligibility - The current building and site (eligibility-current-building)

Checking eligibility for prior approval

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
in-building-construction-period | Was the current building constructed between 1 July 1948 and 28 October 2018? (`True`/`False`) |   | MUST | One of True, False. If False, application cannot proceed.
additional-storeys-added | Have additional storeys already been added to the original building? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
dwelling-permitted-use | Was the current use of the building granted by permitted development rights? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
site-location-constraint | Is any part of the land or site located in a restricted area? (`True`/`False`)  |   | MUST | One of True, False. If True, application cannot proceed

---

### Eligibility - The proposed development (eligibility-proposal)

Checking eligibility for prior approval

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

Checking eligibility for prior approval

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| external-support-required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening? | | MUST | Impacts whether prior approval is applicable. True or False |

---

### Eligibility - The current building and site (eligibility-current-building)

Checking eligibility for prior approval

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
in-building-construction-period | Was the current building constructed between 1 July 1948 and 28 October 2018? (`True`/`False`) |   | MUST | One of True, False. If False, application cannot proceed.
additional-storeys-added | Have additional storeys already been added to the original building? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
dwelling-permitted-use | Was the current use of the building granted by permitted development rights? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
site-location-constraint | Is any part of the land or site located in a restricted area? (`True`/`False`)  |   | MUST | One of True, False. If True, application cannot proceed

---

### Eligibility - The proposed development (eligibility-proposal)

Checking eligibility for prior approval

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

