# Waste storage and collection

Any waste storage or recycling arrangements are in place, such as waste storage areas

**Waste storage and collection module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| needs-waste-storage-area | Needs waste storage area | Does the proposal require a waste storage area | full | MUST |  |
| needs-waste-storage-area-outline | Needs waste storage area | Does the proposal require a waste storage area? | outline | MUST | Select from the **yes-no-unknown** enum. Unknown is allowed in Outline applications |
| waste-storage-area-details | Waste storage area details | Details of the waste storage area including location, size, design and access arrangements |  | MAY |  |
| separate-recycling-arrangements | Separate recycling arrangements | Does the proposal include separate recycling arrangements | full | MUST |  |
| separate-recycling-arrangements-outline | Separate recycling arrangements (outline) | Does the proposal include separate recycling arrangements? | outline | MUST | Select from the **yes-no-unknown** enum. Unknown is allowable in Outline applications |
| separate-recycling-arrangements-details | Separate recycling arrangements details | Details of the recycling arrangements including types of materials, collection methods and storage facilities |  | MAY |  |

**Validation rules**

- waste-storage-area-details must be provided when needs-waste-storage-area is true
- separate-recycling-arrangements-details must be provided when separate-recycling-arrangements is true