Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
residential-unit-change | Proposal includes the gain, loss or change of use of residential units (True/False) | full;outline;ldc | MUST | Could be calculated from answers to next parts?
unit-counts[] | List of unit counts by tenure and housing type | full;outline;ldc | MAY | Is MUST if `residential-unit-change` is True
total-existing-units | The total number of existing units | full;outline;ldc | MUST |
total-proposed-units | The total number of proposed units | full;outline;ldc | MUST |
net-change | Calculated net change in units | full;outline;ldc | MUST | Calculated as proposed-units - existing-units. Format: Integer

**Unit counts**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | See [tenure type enum](https://github.com/digital-land/planning-application-data-specification/discussions/162)
housing-type | Type of housing | Enum | MUST | See [housing type enum](https://github.com/digital-land/planning-application-data-specification/discussions/163)
unknown-units | Whether the number of units is unknown (`true`/`false`) | Boolean | MAY | True if the applicant does not know the unit count.
existing-units[] | Number of existing units by bedroom count | Object | MAY | See "Bedroom Count Structure" below.
proposed-units[] | Number of proposed units by bedroom count | Object | MAY | See "Bedroom Count Structure" below.

**Bedroom count** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
bedroom-1 | Number of 1-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-2 | Number of 2-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-3 | Number of 3-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-4+ | Number of 4 or more bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-count-unknown | Number units where the bedroom number is unknown | Integer | MAY | Not required if unknown is True.
total-units | Total number of units | Integer | MAY | Not required if unknown is True. Calculated as the sum of all bedroom counts.
