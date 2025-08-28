# Description of the proposed development including any non-residential development

Details of proposed development with specific provision for capturing both residential 
and non-residential elements, including dwelling numbers and non-residential use amounts


| description | Description | Description of proposed development including non-residential development |  | MUST |  |
| net-dwellings-min | Net dwellings minimum | The minimum number of net additional dwellings proposed as part of the development, accounting for any existing dwellings lost and new dwellings created |  | MUST |  |
| net-dwellings-max | Net dwellings maximum | The maximum number of net additional dwellings proposed as part of the development, allowing for flexibility in the final housing numbers |  | MUST |  |
| non-residential-use | Non-residential use[]{} | The amount of non-residential use, which can be expressed as floorspace, site area, or both |  | MUST |  |


**Non-residential use model**

field | name | description | required | notes
-- | -- | -- | -- | --
non-residential-measurement-type | Non-residential measurement type | Type of measurement being provided (floorspace or site-area) | MUST | Select from the **non-residential-measurement-type** enum
exact-value | Exact value | Exact figure of non-residential use | MAY | 
min | Minimum value | Lower bound of non-residential use for ranges | MAY | 
max | Maximum value | Upper bound of non-residential use for ranges | MAY | 

**Validation rules**

- net-dwellings-max must be greater than or equal to net-dwellings-min
- Each non-residential-use entry must have either exact-value OR both min and max values
- For non-residential-use ranges, max must be greater than min
- non-residential-measurement-type must be from the non-res-measurement-type codelist