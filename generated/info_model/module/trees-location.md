# Trees location

Location information for trees affected by the proposed works, required when the site is different from the applicant's address


| is-site-different | Is site different | Whether the site where trees are located is different from the applicant's address |  | MUST |  |
| site-locations | Site locations[]{} | Details of the sites on which the tree(s) are located |  | MAY | Rule: is a MUST if `is-site-different` is `True` |


**Site location model**

field | name | description | required | notes
-- | -- | -- | -- | --
site-boundary | Site boundary | Geometry of the site of the development, typically in GeoJSON format | MAY | 
address-text | Address Text | Flexible field for capturing addresses | MAY | 
postcode | Postcode | The postal code | MAY | 
easting | Easting | Easting coordinate in British National Grid (EPSG:27700) | MAY | 
northing | Northing | Northing coordinate in British National Grid (EPSG:27700) | MAY | 
latitude | Latitude | Latitude coordinate in WGS84 (EPSG:4326) | MAY | 
longitude | Longitude | Longitude coordinate in WGS84 (EPSG:4326) | MAY | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MAY | 
uprns | UPRNs[] | Unique Property Reference Numbers (UPRNs) for properties within the site boundary | MAY | 

**Validation rules**

- site-locations only required if the site is different from the applicant's address
- At least one location method must be provided per site: site-boundary, address-text, or easting+northing
- If easting is provided, northing must also be provided and vice versa
- Online services can send the boundary supplied by the applicant/agent
- Paper forms would need other fields translated into site-boundary