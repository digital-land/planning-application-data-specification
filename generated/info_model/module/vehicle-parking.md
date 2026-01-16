# Vehicle parking

Details of current parking facilities at the site and any changes that would be made by the proposed development.

**Vehicle parking module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| parking-spaces | Parking spaces[]{} | Array of parking space information by vehicle type |  | MUST |  |


**Parking space component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
parking-space-type | Parking space type | Type of parking space or vehicle type | MUST | Select from the **parking-space-type** enum | 
vehicle-type-other | Vehicle type other | Vehicle type when parking space type is 'other' | MAY | Rule: is a MUST if `parking-space-type` is `other` | 
total-existing | Total existing | Total number of existing parking spaces | MUST |  | 
total-proposed | Total proposed | Total number of proposed parking spaces | MUST |  | 
unknown-proposed | Unknown proposed | If proposed parking spaces is unknown | MAY |  | outline-some
difference-in-spaces | Difference in spaces | Net change in parking spaces (proposed minus existing) | MUST |  | 

**Validation rules**

- if parking-space-type == 'other' then vehicle-type-other is required
- total-existing >= 0 AND total-proposed >= 0 AND (unknown-proposed is empty OR unknown-proposed >= 0)
- difference-in-spaces == (total-proposed - total-existing)