| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of proposed development including non-residential development |  | MUST | |
| net-dwellings-min | The minimum number of net additional dwellings proposed as part of the development. This accounts for any existing dwellings lost and new dwellings created. | | MUST |  |
| net-dwellings-max | The maximum number of net additional dwellings proposed as part of the development, allowing for flexibility in the final housing numbers. | | MUST |  |
| non-residential-use[]{} | The amount of non-residential use. Can be floorspace, hectares or both. | | MUST | From form: "Can be expressed as a range, a maximum or a fixed amount". This is used to check non-residential use is less than residential use |

**Non residential use structure**

| field | description | notes |
| --- | --- | --- |
| non-residential-measurement-type | The type of value being provided. `floorspace` or `site-area` | See [non-residential-measurement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/188) |
| exact-value | Exact figure of non-residential use | m2 for floorspace, hectares for site-area |
| min | Low bound of non-residential use | m2 for floorspace, hectares for site-area |
| max | Upper bound of non-residential use | m2 for floorspace, hectares for site-area |
