# Agricultural or forestry building details

Agricultural or forestry building details

**Agricultural or forestry building details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| development-operation-types | Development operation types[] | The types of building operation included in the agricultural or forestry proposal. |  | MUST | Select from the **development-operation-type** enum |
| proposed-building-details | Proposed building details{} |  |  | MUST |  |
| building-wall-materials | Wall materials | Details of the wall materials |  | MUST |  |
| building-wall-colour | Wall colour | Colour of the wall |  | MUST |  |
| building-roof-materials | Roof materials | Details of the roof materials |  | MUST |  |
| building-roof-colour | Roof colour | Colour of the roof |  | MUST |  |
| has-agri-building-2-yrs | Agricultural building built within 2 years | Whether an agricultural building has been constructed on the agricultural unit within the last two years |  | MUST |  |
| agri-building-area | Agricultural building ground area | Overall ground area of the agricultural building constructed within the last two years, in square metres |  | MAY | Rule: is a MUST if `has-agri-building-2-yrs` is `True` |
| agri-building-distance | Agricultural building distance | Distance from the recent agricultural building to the proposed new building (in metres) |  | MAY | Rule: is a MUST if `has-agri-building-2-yrs` is `True` |
| house-livestock | Houses livestock, slurry or sewage sludge | Whether the proposed building would be used to house livestock, slurry or sewage sludge
 |  | MUST |  |
| livestock-building-400m | Livestock building distance from homes | Whether livestock building more than 400 metres from the nearest house, excluding the farmhouse |  | MAY | Rule: is a MUST if `house-livestock` is `True` |
| exceeds-threshold | Exceeds threhold | Whether the ground area covered by the proposed building exceeds the relevant Part 6 threshold |  | MUST |  |
| related-work-distance | Related work distance | Whether specified related works have been erected within 90 metres of the proposed development within the last two years |  | MUST |  |
| engineering-operations-threshold | Engineering operations threshold | Whether engineering operations exceed 1,000 square metres where the agricultural unit is 5 hectares or more |  | MUST | Select from the **yes-no-not-applicable** enum |
| within-scheduled-monument | Within Scheduled Momument | Would the erection, extension, or alteration be carried out on land or a building that is, or is within the curtilage of, a scheduled monument |  | MUST |  |


**Building details component**

field | name | description | required | notes
-- | -- | -- | -- | --
details | Details | Additional details or information about an item | MUST | 
building-length | Building length | Length of the proposed agricultural or forestry building in metres. | MUST | 
eaves-height | Eaves height | Height at the eaves of the extension, measured externally from natural ground level in metres | MUST | 
building-breadth | Building breadth | Breadth of the proposed agricultural or forestry building in metres | MUST | 
building-ridge-height | Building ridge height | Height to the ridge of the proposed agricultural or forestry building (in metres) | MUST | 

