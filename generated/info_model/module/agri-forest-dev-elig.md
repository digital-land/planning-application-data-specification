# Agricultural and forestry development eligibility

Information needed to assess agricultural unit, land parcel, agricultural purpose and wider site constraints


**Agricultural and forestry development eligibility module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| agri-unit-area | Agricultural unit area | Total area of the entire agricultural unit |  | MUST | This seems to be semantically similar to site-area |
| area-unit | Area unit | Unit of measurement for the total area of the entire agricultural unit, either square metres or hectares. |  | MUST | Select from the **area-unit** enum |
| land-parcel-area | Land parcel area | The size category for a given land parcel |  | MUST | Select from the **land-parcel-area** enum |
| agri-use-years | Agricultural use years | The years part of the length of time the land on which the proposed development would be located has been used for agriculture for the purposes of a trade or business. |  | MUST |  |
| agri-use-months | Agricultural use months | The months part of the length of time the land on which the proposed development would be located has been used for agriculture for the purposes of a trade or business. |  | MUST |  |
| is-necessary-for-agri | Is necessary for agriculture | Is the proposed development reasonably necessary for the purposes of agriculture? |  | MUST |  |
| details | Details | Explanation of why the proposed development is reasonably necessary for the purposes of agriculture. |  | MAY | Rule: is a MUST if `is-necessary-for-agri` is `True` |
| is-designed-agri | Is designed for agricultural purposes | Is the proposed development designed for the purposes of agriculture? |  | MUST |  |
| design-details | Design details | Explanation of why the proposed development is designed for the purposes of agriculture.
 |  | MAY | Rule: is a MUST if `is-designed-agri` is `True` |
| dwelling-alteration | Dwelling alteration | Whether the proposed development involves any alteration to a dwelling. |  | MUST |  |
| away-from-road | Is over 25 metres from road | Whether the proposed development is more than 25 metres from a metalled part of a trunk or classified road |  | MUST |  |
| close-to-aerodrome | Within 3km of aerodrome | Whether the proposed development is within 3 kilometres of an aerodrome |  | MUST |  |
| height-applicable | Height applicable | Whether a height is applicable | pa-road-agri-forest, pa-excavate-agri | MUST |  |
| proposed-height | Proposed height | Height of the proposed agricultural or forestry development in metres |  | MUST |  |
| affects-heritage | Affects heritage or nature conservation | Would the proposed development affect an ancient monument, archaeological site or listed building or would it be within a Site of Special Scientific Interest or a local nature reserve? |  | MUST |  |
| heritage-nature-impact-details | Heritage and nature impact details | Details of how the proposed development would affect an ancient monument, archaeological site or listed building, or relate to a Site of Special Scientific Interest or local nature reserve. |  | MAY | Rule: is a MUST if `affects-heritage` is `True` |

