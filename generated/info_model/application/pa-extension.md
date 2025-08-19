# Larger Home Extension

Planning application for extension

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Adjacent premises](#adjacent-premises)
* [Description of proposed works](#description-of-proposed-works)
* [Eligibility extension](#eligibility-extension)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |

## Adjacent premises

Information about addresses of properties adjacent to the development site


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for the adjoining properties | MUST |  |


**Address model**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 
uprn | UPRN | Unique Property Reference Number | MAY | 

**Validation rules**

- At least one address must be provided
- Each address must have address-text as minimum requirement
- UPRN should be provided where known for accurate property identification

## Description of proposed works

Description of proposed development works including extension measurements
and detailed work specifications for planning applications


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposed-works-details | Proposed works details | Description of the proposed works including detailed explanation of the work | MUST |  |
| extension-depth | Extension depth | How far the extension extends beyond the rear wall, measured externally in metres | MUST |  |
| max-extension-height | Maximum extension height | Maximum height of the extension, measured externally from natural ground level in metres | MUST |  |
| eaves-height | Eaves height | Height at the eaves of the extension, measured externally from natural ground level in metres | MUST |  |

**Validation rules**

- extension-depth > 0 AND max-extension-height > 0 AND eaves-height > 0
- eaves-height <= max-extension-height
- extension-depth measurement taken from external face of existing rear wall
- max-extension-height and eaves-height measured from natural ground level
- proposed-works-details.length > 10

## Eligibility extension

Eligibility criteria for extension applications to determine if the proposal
meets the requirements for the application type


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-single-storey-extension | Single storey extension | Will the extension be a single storey | MUST |  |
| is-extension-height-over-4m | Extension height over 4m | Will the extension exceed 4 metres in height | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached | MUST |  |
| is-extension-beyond-rear-wall | Extension beyond rear wall | Will the extension extend beyond the rear wall of the original dwelling | MUST |  |
| extension-length | Extension length | Length of rear extension in metres | MUST |  |
| is-within-site-constraints | Within site constraints | Is the dwellinghouse within any restricted area | MUST |  |
| site-constraints | Site constraints[] | List of specific site constraints that restrict development | MAY | Select from the **designation** enum |

**Validation rules**

- if is-single-storey-extension == false then application is ineligible
- if is-extension-height-over-4m == true then application is ineligible
- if is-within-site-constraints == true then application is ineligible
- if is-within-site-constraints == true then site-constraints is required
- extension-length must comply with permitted development limits based on is-dwelling-detached value
