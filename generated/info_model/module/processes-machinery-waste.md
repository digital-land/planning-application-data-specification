# Processes machinery waste

How waste will be managed on the site


**Processes machinery waste module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-activity-details | Site activity details | Description of activities, processes, and end products including site operations, plant, ventilation, and machinery |  | MUST |  |
| proposal-waste-management | Proposal waste management | Whether the proposal involves any waste management facility that is relevant to the proposal |  | MUST |  |
| waste-management | Waste management[]{} | List of applicable waste management facilities involved in the proposal |  | MAY | Applicants should only include entries for facilities that are applicable to the proposal. |
| waste-streams | Waste streams throughput{} | Annual throughput for waste streams by waste type |  | MAY |  |


**Waste management component**

field | name | description | required | notes
-- | -- | -- | -- | --
waste-management-facility-type | Waste management facility type | Type of waste management facility being described in this entry | MUST | Select from the **waste-management-type** enum
total-capacity | Total capacity | Total capacity of void in cubic metres (or tonnes/litres) | MUST | 
unit-type | Unit type | Unit for capacity/throughput (e.g. cubic metres, tonnes, litres) | MUST | Select from the **waste-capacity-unit** enum
annual-throughput | Annual throughput | Maximum annual operational throughput in tonnes/litres | MUST | 
unit-type | Unit type | Unit for capacity/throughput (e.g. cubic metres, tonnes, litres) | MUST | Select from the **waste-capacity-unit** enum


**Waste streams component**

field | name | description | required | notes
-- | -- | -- | -- | --
municipal | Municipal | Maximum throughput for municipal waste (annual throughput in tonnes/litres) | MAY | 
construction-demolition | Construction demolition | Maximum throughput for construction and demolition waste (annual throughput in tonnes/litres) | MAY | 
commercial-industrial | Commercial industrial | Maximum throughput for commercial and industrial waste (annual throughput in tonnes/litres) | MAY | 
hazardous | Hazardous | Maximum throughput for hazardous waste (annual throughput in tonnes/litres) | MAY | 

**Validation rules**

- if proposal-waste-management == true then waste-management is required
- if proposal-waste-management == true then waste-streams is required
- is-total-capacity-known and is-annual-throughput-known only apply to outline applications