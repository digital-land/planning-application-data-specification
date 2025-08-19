# Additional storeys

Enlargement of a dwellinghouse by construction of additional storeys

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Description of work impacts and risks](#description-of-work-impacts-and-risks)
* [Eligibility related works](#eligibility-related-works)
* [Eligibility current building](#eligibility-current-building)
* [Eligibility proposal](#eligibility-proposal)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |

## Description of work impacts and risks

Description of proposed development and assessment of impacts on
amenity, air traffic, defence assets, and protected views


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| description | Description | Description of proposed development including details of proposed work and external appearance | MUST |  |
| dwellinghouse-height | Dwellinghouse height | Height from ground to highest point of roof in metres | MUST |  |
| proposed-height | Proposed height | Height once the additional storeys have been added in metres | MUST |  |
| impact-on-amenity | Impact on amenity | Details of the impacts on the amenity of any adjoining premises including overlooking, privacy and the loss of light including how these will be mitigated | MUST |  |
| air-traffic-defence-impacts | Air traffic defence impacts | Details of any air traffic and defence asset impacts, including how these will be mitigated | MUST |  |
| protected-view-impact | Protected view impact | Details of the impact on any protected view where relevant | MUST |  |

**Validation rules**

- dwellinghouse-height > 0 AND proposed-height > 0
- proposed-height >= dwellinghouse-height (advisory)
- impact-on-amenity must include mitigation details where impacts identified
- air-traffic-defence-impacts must include mitigation details where impacts identified

## Eligibility related works

Eligibility criteria for engineering works related to prior approval applications,
specifically relating to external support structures and curtilage extensions


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| external-support-required | External support required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening | MUST |  |

**Validation rules**

- external-support-required == true may affect prior approval eligibility

## Eligibility current building

Eligibility criteria related to current building status including construction period,
storey additions, permitted development use, and site location constraints


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| was-constructed-btw-1948-2018 | Was constructed between 1948 and 2018 | Was the current building constructed between 1 July 1948 and 28 October 2018? If False, application cannot proceed. | MUST |  |
| has-additional-storeys | Additional storeys added | Have additional storeys already been added to the original building? If True, application cannot proceed. | MUST |  |
| was-use-granted-by-pdr | Use granted by permitted development right | Was the current use of the building granted by permitted development rights? If True, application cannot proceed. | MUST |  |
| is-site-in-restricted-area | Site in restricted area | Is any part of the land or site located in a restricted area? If True, application cannot proceed. | MUST |  |

**Validation rules**

- was-constructed-btw-1948-2018 == true (required for application to proceed)
- has-additional-storeys == false (required for application to proceed)
- was-use-granted-by-pdr == false (required for application to proceed)
- is-site-in-restricted-area == false (required for application to proceed)
- was-constructed-btw-1948-2018 == true AND has-additional-storeys == false AND was-use-granted-by-pdr == false AND is-site-in-restricted-area == false

## Eligibility proposal

Eligibility criteria related to proposal design and construction including storey construction,
height restrictions, roof specifications, and material requirements


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| principal-part-only | Principal part only | Will the additional storeys be constructed only on the principal part of the building | MUST |  |
| ceiling-height-exceeds-3m | Ceiling height exceeds 3m | Will the internal floor-to-ceiling height of any additional storey exceed 3 metres | MUST |  |
| existing-ceiling-height-exceeds-3m | Existing ceiling height exceeds 3m | Will the internal floor-to-ceiling height of any existing storey exceed 3 metres | MUST |  |
| building-height-exceeds-18m | Building height exceeds 18m | Will the height of the extended building exceed 18 metres | MUST |  |
| roof-height-exceeds-3-5m | Roof height exceeds 3.5m | Will the roof exceed 3.5 metres above the highest part of the existing roof | MUST |  |
| roof-height-exceeds-7m | Roof height exceeds 7m | Will the roof exceed 7 metres above the highest part of the existing roof | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached | MUST |  |
| extension-on-attached-dwelling | Extension on attached dwelling | Will the extension result in the highest part exceeding 3.5 metres above the attached roof | MAY | Rule: is a MUST if `is-dwelling-detached` is `False` |
| extension-below-terrace-roof | Extension below terrace roof | Will the extension result in the highest part exceeding 3.5 metres above any roof in the terrace | MAY | Rule: is a MUST if `is-dwelling-detached` is `False` |
| roof-pitch-matching | Roof pitch matching | Will the roof pitch of the extended dwelling match the existing roof pitch | MUST |  |
| window-on-side-elevation | Window on side elevation | Will the development include a side elevation window or roof slope window | MUST |  |
| materials-similar-exterior | Materials similar exterior | Will exterior materials be similar to those of the existing dwelling | MUST |  |
| dwellinghouse-use | Dwellinghouse use | Will the extended dwelling remain as a Class C3 dwellinghouse or ancillary use | MUST |  |

**Validation rules**

- principal-part-only == true (required for application to proceed)
- ceiling-height-exceeds-3m == false (required for application to proceed)
- existing-ceiling-height-exceeds-3m == false (required for application to proceed)
- building-height-exceeds-18m == false (required for application to proceed)
- roof-height-exceeds-3-5m == false (required for application to proceed)
- roof-height-exceeds-7m == false (required for application to proceed)
- roof-pitch-matching == true (required for application to proceed)
- window-on-side-elevation == false (if true, further assessment required)
- materials-similar-exterior == true (required for application to proceed)
- dwellinghouse-use == true (required for application to proceed)
- if is-dwelling-detached == false, then extension-on-attached-dwelling should be considered
- if is-dwelling-detached == false, then extension-below-terrace-roof should be considered
