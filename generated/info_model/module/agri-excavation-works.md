# Agricultural excavation or waste deposition

Details of proposed excavations or waste deposition for agricultural use.

**Agricultural excavation or waste deposition module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposed-works-area | Proposed works area{} | Area of the proposed works, with its unit of measurement. |  | MUST |  |
| proposed-works-volume | Proposed works volume | Approximate total volume of the proposed works in cubic metres. |  | MUST |  |
| proposed-works-details | Proposed works details | Please provide a detailed description of the proposed works. |  | MUST |  |
| prev-excavation-or-deposit | Previous excavation or waste deposit | Whether previous excavations or waste deposits have been carried out. |  | MUST |  |
| previous-works-area | Previous works area{} | Total area of previous works, with its unit of measurement. |  | MAY | Rule: is a MUST if `prev-excavation-or-deposit` is `True` |
| holding-size | Holding size | Size of the holding. |  | MUST |  |
| holding-number | Holding number | Number of the holding. |  | MUST |  |
| excavation-depth-or-raising-height | Excavation depth or landraising height | Depth of excavation or landfilling, or height of landraising, in metres. |  | MUST |  |
| excavated-material-retained | Excavated material retained | Whether any excavated material would be retained within the agricultural holding. |  | MUST |  |
| imported-waste-materials | Imported waste materials | Materials composing any waste brought onto the land from elsewhere. |  | MAY |  |
| affects-water | Affects water | Whether the works would affect any watercourse, surface water or groundwater. |  | MUST |  |
| water-impact-details | Water impact details | Description of how the works would affect any watercourse, surface water or groundwater. |  | MAY | Rule: is a MUST if `affects-water` is `True` |


**Area measurement component**

field | name | description | required | notes
-- | -- | -- | -- | --
size | Size | Numeric value of the area in the specified unit. | MUST | 
area-unit | Area unit | Unit of measurement for an area value. | MUST | Select from the **area-unit** enum

