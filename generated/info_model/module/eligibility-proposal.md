# Eligibility proposal

Eligibility criteria related to proposal design and construction including storey construction,
height restrictions, roof specifications, and material requirements


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| principal-part-only | Principal part only | Will the additional storeys be constructed only on the principal part of the building |  | MUST |  |
| ceiling-height-exceeds-3m | Ceiling height exceeds 3m | Will the internal floor-to-ceiling height of any additional storey exceed 3 metres |  | MUST |  |
| existing-ceiling-height-exceeds-3m | Existing ceiling height exceeds 3m | Will the internal floor-to-ceiling height of any existing storey exceed 3 metres |  | MUST |  |
| building-height-exceeds-18m | Building height exceeds 18m | Will the height of the extended building exceed 18 metres |  | MUST |  |
| roof-height-exceeds-3-5m | Roof height exceeds 3.5m | Will the roof exceed 3.5 metres above the highest part of the existing roof |  | MUST |  |
| roof-height-exceeds-7m | Roof height exceeds 7m | Will the roof exceed 7 metres above the highest part of the existing roof |  | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached |  | MUST |  |
| extension-on-attached-dwelling | Extension on attached dwelling | Will the extension result in the highest part exceeding 3.5 metres above the attached roof |  | MAY | Rule: is a MUST if `is-dwelling-detached` is `False` |
| extension-below-terrace-roof | Extension below terrace roof | Will the extension result in the highest part exceeding 3.5 metres above any roof in the terrace |  | MAY | Rule: is a MUST if `is-dwelling-detached` is `False` |
| roof-pitch-matching | Roof pitch matching | Will the roof pitch of the extended dwelling match the existing roof pitch |  | MUST |  |
| window-on-side-elevation | Window on side elevation | Will the development include a side elevation window or roof slope window |  | MUST |  |
| materials-similar-exterior | Materials similar exterior | Will exterior materials be similar to those of the existing dwelling |  | MUST |  |
| dwellinghouse-use | Dwellinghouse use | Will the extended dwelling remain as a Class C3 dwellinghouse or ancillary use |  | MUST |  |

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