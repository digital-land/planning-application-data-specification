# Processes machinery waste

Information about site activities, processes, and waste management development
including facility types, capacities, and throughput details. Specifically for outline applications


| site-activity-details | Site activity details | Description of activities, processes, and end products including site operations, plant, ventilation, and machinery |  | MUST |  |
| proposal-waste-management-outline | Proposal waste management outline variant | Whether the proposal involves waste management development (yes/no/unknown) |  | MUST | Select from the **yes-no-unknown** enum |
| waste-management-outline | Waste management[]{} | List of waste management facilities involved in the proposal. Specifically for outline applications |  | MAY |  |
| waste-streams | Waste streams throughput{} | Annual throughput for waste streams by waste type |  | MAY |  |


**Waste management model**

field | name | description | required | notes
-- | -- | -- | -- | --
waste-management-facility-type | Waste management facility type | Type of waste management facility | MUST | Select from the **waste-management-type** enum
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
is-total-capacity-known | Is total capacity known | Whether the total capacity is known | MUST | 
total-capacity | Total capacity | Total capacity of void in cubic metres (or tonnes/litres) | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-total-capacity-known` is `True`
is-annual-throughput-known | Is annual throughput known | Whether the annual throughput is known | MUST | 
annual-throughput | Annual throughput | Maximum annual operational throughput in tonnes/litres | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-annual-throughput-known` is `True`


**Waste streams model**

field | name | description | required | notes
-- | -- | -- | -- | --
municipal | Municipal | Maximum throughput for municipal waste (annual throughput in tonnes/litres) | MAY | 
construction-demolition | Construction demolition | Maximum throughput for construction and demolition waste (annual throughput in tonnes/litres) | MAY | 
commercial-industrial | Commercial industrial | Maximum throughput for commercial and industrial waste (annual throughput in tonnes/litres) | MAY | 
hazardous | Hazardous | Maximum throughput for hazardous waste (annual throughput in tonnes/litres) | MAY | 

**Validation rules**

- if proposal-waste-management-outline == true then waste-management-outline is required
- if proposal-waste-management-outline == true then waste-streams is required