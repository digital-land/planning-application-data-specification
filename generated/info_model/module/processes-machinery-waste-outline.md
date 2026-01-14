# Processes machinery waste

If making an 'outline' application, how waste will be managed on the development site

**Processes machinery waste module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-activity-details | Site activity details | Description of activities, processes, and end products including site operations, plant, ventilation, and machinery |  | MUST |  |
| proposal-waste-management-outline | Proposal waste management outline variant | Whether the proposal involves waste management development (yes/no/unknown) |  | MUST | Select from the **yes-no-unknown** enum |
| waste-management-outline | Waste management[]{} | List of waste management facilities involved in the proposal. Specifically for outline applications |  | MAY |  |
| waste-streams | Waste streams throughput{} | Annual throughput for waste streams by waste type |  | MAY |  |


**Waste management component**

field | name | description | required | notes
-- | -- | -- | -- | --
waste-management-facility-type | Waste management facility type | Type of waste management facility | MUST | Select from the **waste-management-type** enum
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
is-total-capacity-known | Is total capacity known | Whether the total capacity is known | MUST | 
total-capacity | Total capacity | Total capacity of void in cubic metres (or tonnes/litres) | MAY | 
unit-type | Unit type | Unit for capacity/throughput (e.g. cubic metres, tonnes, litres) | MAY | Select from the **waste-capacity-unit** enum
is-annual-throughput-known | Is annual throughput known | Whether the annual throughput is known | MUST | 
annual-throughput | Annual throughput | Maximum annual operational throughput in tonnes/litres | MAY | 
unit-type | Unit type | Unit for capacity/throughput (e.g. cubic metres, tonnes, litres) | MAY | Select from the **waste-capacity-unit** enum


**Waste streams component**

field | name | description | required | notes
-- | -- | -- | -- | --
municipal | Municipal | Maximum throughput for municipal waste (annual throughput in tonnes/litres) | MAY | 
construction-demolition | Construction demolition | Maximum throughput for construction and demolition waste (annual throughput in tonnes/litres) | MAY | 
commercial-industrial | Commercial industrial | Maximum throughput for commercial and industrial waste (annual throughput in tonnes/litres) | MAY | 
hazardous | Hazardous | Maximum throughput for hazardous waste (annual throughput in tonnes/litres) | MAY | 

**Validation rules**

- if proposal-waste-management-outline == true then waste-management-outline is required
- if proposal-waste-management-outline == true then waste-streams is required