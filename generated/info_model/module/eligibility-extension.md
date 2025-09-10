# Eligibility extension

How a proposal to build an extension meets relevant criteria.

**Eligibility extension module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-single-storey-extension | Single storey extension | Will the extension be a single storey |  | MUST |  |
| is-extension-height-over-4m | Extension height over 4m | Will the extension exceed 4 metres in height |  | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached |  | MUST |  |
| is-extension-beyond-rear-wall | Extension beyond rear wall | Will the extension extend beyond the rear wall of the original dwelling |  | MUST |  |
| extension-length | Extension length | Length of rear extension in metres |  | MUST |  |
| is-within-site-constraints | Within site constraints | Is the dwellinghouse within any restricted area |  | MUST |  |
| site-constraints | Site constraints[] | List of specific site constraints that restrict development |  | MAY | Select from the **designation** enum |

**Validation rules**

- if is-single-storey-extension == false then application is ineligible
- if is-extension-height-over-4m == true then application is ineligible
- if is-within-site-constraints == true then application is ineligible
- if is-within-site-constraints == true then site-constraints is required
- extension-length must comply with permitted development limits based on is-dwelling-detached value