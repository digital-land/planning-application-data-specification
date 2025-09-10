# Non residential floorspace

Details of changes to non-residential floorspace in the proposed development.

**Non residential floorspace module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| non-residential-change | Non residential change | Does the proposal involve the loss, gain, or change of non-residential floorspace? | full | MUST |  |
| non-residential-change-outline | Non residential change | Does the proposal involve the loss, gain, or change of non-residential floorspace? | outline | MUST | Select from the **yes-no-unknown** enum. this is only used in outline applications where unknown is an option |
| floorspace-details | Floorspace details[]{} | List of non-residential floorspace changes by use class | full | MAY | Rule: is a MUST if `non-residential-change` is `True` |
| floorspace-details-outline | Floorspace details[]{} | List of non-residential floorspace changes by use class. | outline | MAY | Rule: is a MUST if `non-residential-change-outline` is `True`. This field is used solely for outline applications |
| room-details | Room details[]{} | List of room changes for hotels, residential institutions and hostels | full | MAY | Required if change to hotels, residential institutions and hostel floorspace (C1, C2, C2A use classes) |
| room-details-outline | Room details[]{} | List of room changes for hotels, residential institutions and hostels | outline | MAY | Required if change to hotels, residential institutions and hostel floorspace (C1, C2, C2A use classes). Only for outline applications. |


**Floorspace details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | 
existing-gross-floorspace | Existing gross floorspace | Existing gross internal floorspace, in sqm | MUST | 
floorspace-lost | Floorspace lost | Gross floorspace to be lost by change of use, in sqm | MUST | 
total-gross-proposed | Total gross proposed | Total gross internal floorspace proposed, in sqm | MUST | 
net-additional-floorspace | Net additional floorspace | Net additional gross internal floorspace, in sqm | MUST | Calculated as total-gross-proposed - existing-gross-floorspace. This should be calculated automatically


**Floorspace details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | 
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
existing-gross-floorspace | Existing gross floorspace | Existing gross internal floorspace, in sqm | MUST | 
is-floorspace-lost-known | Is floorspace lost known | Whether the amount of floorspace to be lost is known | MAY | 
floorspace-lost | Floorspace lost | Gross floorspace to be lost by change of use, in sqm | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-floorspace-lost-known` is `True`
is-total-gross-proposed-known | Is total gross proposed known | Whether the total gross proposed floorspace is known | MAY | 
total-gross-proposed | Total gross proposed | Total gross internal floorspace proposed, in sqm | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-total-gross-proposed-known` is `True`
net-additional-floorspace | Net additional floorspace | Net additional gross internal floorspace, in sqm | MUST | Calculated as total-gross-proposed - existing-gross-floorspace. This should be calculated automatically


**Room details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use-class | Use class | Type of non-residential use class | MUST | Select from the **use-class** enum. Only required for C1, C2, C2A, or Other use classes
existing-rooms-lost | Existing rooms lost | Existing rooms to be lost by change of use | MUST | Must be 0 or positive
total-rooms-proposed | Total rooms proposed | Total rooms proposed (including change of use) | MUST | Must be 0 or positive
net-additional-rooms | Net additional rooms | Net additional rooms following development | MUST | Calculated as total-rooms-proposed - existing-rooms-lost


**Room details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use-class | Use class | Type of non-residential use class | MUST | Select from the **use-class** enum. Only required for C1, C2, C2A, or Other use classes
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
is-existing-rooms-lost-known | Is existing rooms lost known | Whether the total existing rooms that will be lost is known | MAY | 
existing-rooms-lost | Existing rooms lost | Existing rooms to be lost by change of use | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-existing-rooms-lost-known` is `True`. Must be 0 or positive
is-total-rooms-proposed-known | Is total rooms proposed known | Whether the total rooms proposed is known | MAY | 
total-rooms-proposed | Total rooms proposed | Total rooms proposed (including change of use) | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-total-rooms-proposed-known` is `True`. Must be 0 or positive
net-additional-rooms | Net additional rooms | Net additional rooms following development | MUST | Calculated as total-rooms-proposed - existing-rooms-lost

**Validation rules**

- floorspace-details is required when non-residential-change is true
- room-details is required when floorspace involves C1, C2, C2A, or other use classes
- specified-use is required when use is other or sui generis
- All floorspace values must be 0 or positive
- All room values must be 0 or positive
- net-additional-floorspace must equal total-gross-proposed minus existing-gross-floorspace
- net-additional-rooms must equal total-rooms-proposed minus existing-rooms-lost