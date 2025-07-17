| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisements[]{} | Structured data about each proposed advertisement |  | MUST | Rule: must be one or more entries |

**Advertisement**

| field | description | notes |
| --- | --- | --- |
| height-from-ground | Height from ground to the base of the advertisement | in metres |
| height | Height of dimensions of advertisement | in metric |
| width | Width of dimensions of advertisement | in metric |
| depth | Depth of dimensions of advertisement | in metric |
| symbol-height-max | Maximum height of any individual letters or symbols | in metric |
| colour | Colour of proposed sign | |
| materials | Materials of proposed sign | | 
| max-projection | Maximum projection of the advertisement from the face of the building | |
| illuminated | True or False. Will the sign(s) be illuminated? | |
| illumination-method | | Required if `illuminated` is true |
| illuminance-level | | Required if `illuminated` is true. cd/m2 |
| illumination-type | Static or intermittent | Required if `illuminated` is true. Is an illumination-type codelist required? |
