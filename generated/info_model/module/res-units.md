# Residential units

Details of the residential units that make up both the current and proposed development.

**Residential units module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| will-residential-units-change | Residential unit change | Proposal includes the gain, loss or change of use of residential units |  | MUST |  |
| residential-unit-summary | Residential unit summary[]{} | Breakdown of unit counts by tenure and housing type |  | MAY | Rule: is a MUST if `will-residential-units-change` is `True` |
| total-existing-units | Total existing units | The total number of existing units |  | MUST |  |
| total-proposed-units | Total proposed units | The total number of proposed units |  | MUST |  |
| net-change | Net change | Calculated net change in units |  | MUST |  |


**Residential unit summary component**

field | name | description | required | notes
-- | -- | -- | -- | --
tenure-type | Tenure type | Category of housing tenure | MUST | Select from the **tenure-type** enum
housing-type | Housing type | Type of housing | MUST | Select from the **housing-type** enum
existing-unit-breakdown | Existing unit breakdown[]{} | Number of existing units by bedroom count | MAY | 
proposed-unit-breakdown | Proposed unit breakdown[]{} | Number of proposed units by bedroom count | MAY | 


**Unit quantities component**

field | name | description | required | notes
-- | -- | -- | -- | --
units-unknown | Units unknown | Whether the number of units is unknown | MUST | 
units-per-bedroom-no | Units per bedroom number[]{} | Number of units broken down by bedroom count | MAY | Rule: is a MUST if `units-unknown` is `False`
total-units | Total units | Total number of units | MAY | 


**Bedroom count component**

field | name | description | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | No bedrooms unknown | Set to true when counting units where bedroom number is unknown | MUST | 
no-of-bedrooms | Number of bedrooms | The number of bedrooms in unit | MAY | Rule: is a MUST if `no-bedrooms-unknown` is `False`
units | Units | The number of units of that bedroom count | MUST | 

**Validation rules**

- residential-unit-summary is required when will-residential-units-change is true
- net-change is calculated as total-proposed-units minus total-existing-units
- if will-residential-units-change is true, at least one breakdown for existing and proposed is required (count could be unknown)