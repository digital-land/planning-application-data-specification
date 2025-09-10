# Demolition

Details of any demolition that needs to take place as part of the development proposal.

**Demolition module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-proposing-demolition | Is propsing demolition | Does the proposal include partial or total demolition of a listed building? |  | MUST |  |
| is-total-demolition | Is total demolition | Indicating whether the proposal involves total demolition of a listed building |  | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| is-demolishing-building-in-curtilage | Demolition building in curtilage | True or False indicating whether the proposal involves demolition of a building in the curtilage of a listed building |  | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| is-partial-demolition | Demolition part | True or False indicating whether the proposal involves partial demolition of a listed building |  | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| listed-building-volume | Listed building volume | Volume of listed building in cubic metres |  | MAY | Rule: is a MUST if `is-partial-demolition` is `True` |
| demolition-volume | Demolition volume | Volume of part to be demolished in cubic metres |  | MAY | Rule: is a MUST if `is-partial-demolition` is `True` |
| part-built-date | Part built date | The approximate date the part to be removed was built, in YYYY-MM-DD format. |  | MAY | Rule: is a MUST if `is-partial-demolition` is `True`. Approximate dates are allowed |
| description | Description | Description of the building or part you are proposing to demolish |  | MUST |  |
| reason | Reason | Reason for demolition |  | MUST |  |

