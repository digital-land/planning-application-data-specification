Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
site-activity-details | Description of activities, processes, and end products | full;outline | MUST | Describe site operations, including plant, ventilation, and machinery.
proposal-waste-management | Whether the proposal involves waste management development | full;outline | MUST | True if the proposal includes waste management.
waste-management[] | List of waste management facilities involved | full;outline | MAY | MUST if proposal-waste-management is True.
waste-streams{} | Annual throughput for waste streams | full;outline | MAY | MUST if proposal-waste-management is True.

**Waste management**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
type | Type of waste management facility | Enum | MUST | See [Waste Management Type Enum](https://github.com/digital-land/planning-application-data-specification/discussions/164)
not-applicable | Whether the facility is not applicable | Boolean | MAY | If True, capacity and throughput are not required.
is-total-capacity-known | Confirming whether the total capacity is known | Boolean | MUST | Only applicable for Outline applications.
total-capacity | Total capacity of void in cubic metres (or tonnes/litres) | Integer | MAY | MUST if not-applicable is False. MUST if application-type == outline and is-total-capacity-known is TRUE
is-annual-throughput-known | Confirming whether the annual throughput is known | Boolean | MUST | Only applicable for Outline applications.
annual-throughput | Maximum annual operational throughput in tonnes/litres | Integer | MAY | MUST if not-applicable is False. MUST if application-type == outline and is-annual-throughput-known is TRUE

**Waste streams**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
municipal | Maximum throughput for municipal waste | Integer | MAY | Annual throughput in tonnes/litres.
construction-demolition | Maximum throughput for construction and demolition waste | Integer | MAY | Annual throughput in tonnes/litres.
commercial-industrial | Maximum throughput for commercial and industrial waste | Integer | MAY | Annual throughput in tonnes/litres.
hazardous | Maximum throughput for hazardous waste | Integer | MAY | Annual throughput in tonnes/litres.
