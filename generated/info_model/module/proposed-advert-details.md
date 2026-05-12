# Proposed advert details

Details of the proposed advertisements such as their size and how they are made

**Proposed advert details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| advertisements | Advertisements[]{} | Structured data about each proposed advertisement |  | MUST |  |


**Advertisement component**

field | name | description | required | notes
-- | -- | -- | -- | --
height-from-ground | Height from ground | Height, in metres, from ground to the base of the advertisement | MAY | in metres
height | Height | Height, in metres, of dimensions of advertisement | MAY | in metres
width | Width | Width of dimensions of advertisement | MAY | in metres
depth | Depth | Depth, in metres, of dimensions of advertisement | MAY | in metres
symbol-height-max | Symbol height max | Maximum height, in metres, of any individual letters or symbols | MAY | 
colour | Colour | Colour of proposed sign | MAY | 
materials | Materials | Materials of proposed sign | MAY | 
max-projection | Max projection | Maximum projection, in metres, of the advertisement from the face of the building | MAY | 
illuminated | Illuminated | Will the sign(s) be illuminated? | MAY | 
illumination-method | Illumination method | Method of illumination for the advertisement | MAY | Select from the **illumination-method** enum. Rule: is a MUST if `illuminated` is `True`
illuminance-level | Illuminance level | Level of illuminance for the advertisement | MAY | Rule: is a MUST if `illuminated` is `True`. Unit: cd/m2
illumination-type | Illumination type | Type of illumination (static or intermittent) | MAY | Select from the **illumination-type** enum. Rule: is a MUST if `illuminated` is `True`

**Validation rules**

- At least one advertisement entry must be provided
- illumination-method is required when illuminated is true
- illuminance-level is required when illuminated is true
- illumination-type is required when illuminated is true
- Dimensional values must be positive numbers
- illuminance-level must be positive when provided