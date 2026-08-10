# Trees location

Where trees affected by the proposed development are located.

**Trees location module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-site-different | Is site different | Whether the site where trees are located is different from the applicant's address |  | MUST |  |
| site-locations | Site locations[]{} | Details of the sites on which the tree(s) are located |  | MAY | Rule: is a MUST if `is-site-different` is `True` |


**Site location component**

field | name | description | required | notes
-- | -- | -- | -- | --
geometry | Site boundary | A polygon or multipolygon boundary | MUST | 
site-address | Site address{} | A structured object containing an address used to describe a development site. | MUST | UPRNs are not needed in case of notification for work to trees in conservation area
easting | Easting | Easting coordinate in British National Grid (EPSG:27700) | MAY | 
northing | Northing | Northing coordinate in British National Grid (EPSG:27700) | MAY | 
latitude | Latitude | Latitude coordinate in WGS84 (EPSG:4326) | MAY | 
longitude | Longitude | Longitude coordinate in WGS84 (EPSG:4326) | MAY | 


**Site address component**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Text representation of an address or site | MUST | 
postcode | Postcode | Postcode for a contact address or site | MAY | 
uprns | UPRNs[] | Unique Property Reference Numbers (UPRNs) for existing premises within a site boundary | MAY | 
usrns | USRNs[] | Unique Street Reference Numbers (USRNs) associated with the site | MAY | 

**Validation rules**

- site-locations only required if the site is different from the applicant's address
- Each site-location must include a site boundary and site address
- If easting is provided, northing must also be provided and vice versa
- Online services can send the boundary supplied by the applicant/agent
- The planning authority must translate site information received on a paper form into the required structured site-location data, including the site boundary