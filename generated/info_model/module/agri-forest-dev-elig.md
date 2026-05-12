# agri-forest-dev-elig



**agri-forest-dev-elig module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| agri-unit-area | Agricultural unit area | Total area of the entire agricultural unit |  | MUST | This seems to be semantically similar to site-area |
| land-parcel-area | Land parcel area | The size category for a given land parcel |  | MUST | Select from the **land-parcel-area** enum |
| agri-start-date | Agricultural use start date | The month and year when the land started being used for agriculture |  | MUST |  |
| is-necessary-for-agri | Is necessary for agriculture | Is the proposed development reasonably necessary for the purposes of agriculture? |  | MUST |  |
| details | Details | Explanation of why the proposed development is reasonably necessary for the purposes of agriculture. |  | MAY | Rule: is a MUST if `is-necessary-for-agri` is `True` |
| is-designed-agri | Is designed for agricultural purposes | Is the proposed development designed for the purposes of agriculture? |  | MUST |  |
| design-details | Design details | Explanation of why the proposed development is designed for the purposes of agriculture.
 |  | MAY | Rule: is a MUST if `is-designed-agri` is `True` |
| dwelling-alteration | Dwelling alteration | Whether the proposed development involves any alteration to a dwelling. |  | MUST |  |
| away-from-road | Is over 25 metres from road | Whether the proposed development is more than 25 metres from a metalled part of a trunk or classified road |  | MUST |  |
| close-to-aerodrome | Within 3km of aerodrome | Whether the proposed development is within 3 kilometres of an aerodrome |  | MUST |  |
| proposed-height | Proposed height | Height of the proposed agricultural or forestry development in metres |  | MUST |  |
| affects-heritage | Affects heritage or nature conservation | Whether the proposed development would affect local hertiage or nature considerations |  | MUST |  |
| heritage-nature-impact-details | Heritage and nature impact details | Details of how the proposed development would affect an ancient monument, archaeological site or listed building, or relate to a Site of Special Scientific Interest or local nature reserve. |  | MAY | Rule: is a MUST if `affects-heritage` is `True` |

