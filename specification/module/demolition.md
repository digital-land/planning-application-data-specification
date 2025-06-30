| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-proposing-demolition | True or False based on whether proposal includes partial or total demolition of a listed building | lbc | MUST |  |
| is-total-demolition | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| is-demolishing-building-in-curtilage | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| is-partial-demolition | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| listed-building-volume | Volume of listed building in cubic metres | lbc | MAY | Rule: if `is-partial-demolition` is true then this is a MUST |
| demolition-volume | Volume of part to be demolished in cubic metres | lbc | MAY | Rule: if `is-partial-demolition` is true then this is a MUST |
| part-built-date | The approximate date the part to be removed was built | lbc | MAY | Rule: if `is-partial-demolition` is true then this is a MUST Format should be YYYY-MM-DD. Approximate dates are allowed |
| description | Description of the the building or part you are proposing to demolish | lbc | MUST | |
| reason | Reason for demolition | lbc | MUST | |
