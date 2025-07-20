Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
will-residential-units-change | Proposal includes the gain, loss or change of use of residential units (True/False) | full;outline;ldc | MUST | Could be calculated from answers to next parts?
residential-unit-summary[]{} | Breakdown of unit counts by tenure and housing type | full;outline;ldc | MAY | Is MUST if `will-residential-units-change` is True
total-existing-units | The total number of existing units | full;outline;ldc | MUST |
total-proposed-units | The total number of proposed units | full;outline;ldc | MUST |
net-change | Calculated net change in units | full;outline;ldc | MUST | Calculated as proposed-units - existing-units. Format: Integer

**residential-unit-summary**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | See [tenure type enum](https://github.com/digital-land/planning-application-data-specification/discussions/162)
housing-type | Type of housing | Enum | MUST | See [housing type enum](https://github.com/digital-land/planning-application-data-specification/discussions/163)
existing-unit-breakdown[]{} | Number of existing units by bedroom count | Object | MAY | See "Unit quantities Structure" below.
proposed-unit-breakdown[]{} | Number of proposed units by bedroom count | Object | MAY | See "Unit quantities Structure" below.

**Unit quantities** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
units-unknown | Whether the number of units is unknown (`true`/`false`) | Boolean | MUST | 
units-per-bedroom-no[]{} | For this tenure and unit type | Object | MAY | MUST if `units-unknown` is False. See bedroom count
total-units | Total number of units | Integer | MAY | Not required if `units-unknown` is True. Calculated as the sum of all bedroom counts.


**bedroom count**

field | description | data-type | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | Set to true when counting units where bedroom number is unknown | Boolean | MUST || Default is false
no-of-bedrooms | The number of bedrooms in unit | integer | MAY | MUST if no-bedrooms-unknown is true
units | the number of units of that bedroom count | integer | MUST | 0 or above



rule: if will-residential-units-change = true, at least one breakdown for existing and proposed is required (count could be unknown).

implementation: For the paper forms, for space reasons, we need to limit the bedroom counts to 1, 2, 3, 4+
