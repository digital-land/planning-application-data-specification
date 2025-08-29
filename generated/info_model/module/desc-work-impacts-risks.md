# Description of work impacts and risks

Description of proposed development and assessment of impacts on
amenity, air traffic, defence assets, and protected views


**Description of work impacts and risks module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| description | Description | Description of proposed development including details of proposed work and external appearance |  | MUST |  |
| dwellinghouse-height | Dwellinghouse height | Height from ground to highest point of roof in metres |  | MUST |  |
| proposed-height | Proposed height | Height once the additional storeys have been added in metres |  | MUST |  |
| impact-on-amenity | Impact on amenity | Details of the impacts on the amenity of any adjoining premises including overlooking, privacy and the loss of light including how these will be mitigated |  | MUST |  |
| air-traffic-defence-impacts | Air traffic defence impacts | Details of any air traffic and defence asset impacts, including how these will be mitigated |  | MUST |  |
| protected-view-impact | Protected view impact | Details of the impact on any protected view where relevant |  | MUST |  |

**Validation rules**

- dwellinghouse-height > 0 AND proposed-height > 0
- proposed-height >= dwellinghouse-height (advisory)
- impact-on-amenity must include mitigation details where impacts identified
- air-traffic-defence-impacts must include mitigation details where impacts identified