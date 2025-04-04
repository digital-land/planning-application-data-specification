field | description | application-types | required | notes
-- | -- | -- | -- | --
non-residential-change | Does the proposal involve the loss, gain, or change of non-residential floorspace? | full;outline | MUST | Boolean (true / false).
floorspace-details[]{} | List of non-residential floorspace changes by use class | full;outline | MAY | Required if non-residential-change is Yes.
room-details[] | List of room changes for hotels, residential institutions and hostels | full;outline | MAY | Required if change to hotels, residential institutions and hostel floorspace |

**Floorspace details**


field | description | data type | required | notes
-- | -- | -- | -- | --
use | Type of non-residential use class | Enum+other | MUST | See [Use Class Enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
specified-use | Specify the use that sits outside the lettered use classes | String | MAY | Rule: is a MUST if `use` is `other` or `sui generis`
existing-gross-floorspace | Existing gross internal floorspace (sqm) | Number | MUST | Must be 0 or positive.
floorspace-lost | Gross floorspace to be lost by change of use (sqm) | Number | MUST | Must be 0 or positive.
total-gross-proposed | Total gross internal floorspace proposed (sqm) | Number | MUST | Must be 0 or positive.
net-additional-floorspace | Net additional gross internal floorspace (sqm) | Number | MUST | Calculated as total-gross-proposed - existing-gross-floorspace.


**Room details**

For certain use classes (C1, C2, C2A), applicants must provide room details:

field | description | data type | required | notes
-- | -- | -- | -- | --
use-class | Type of non-residential use class | Enum | MUST | Only required for C1, C2, C2A, or Other.
existing-rooms-lost | Existing rooms to be lost by change of use | Number | MUST | Must be 0 or positive.
total-rooms-proposed | Total rooms proposed (including change of use) | Number | MUST | Must be 0 or positive.
net-additional-rooms | Net additional rooms following development | Number | MUST | Calculated as total-rooms-proposed - existing-rooms-lost.
