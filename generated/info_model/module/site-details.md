# Site details

Where the proposed development will be built.

**Site details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-locations | Site locations[]{} | Details of the sites where development or works are proposed |  | MUST |  |


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

- {'description': 'At least one site-location must be provided for tree works applications', 'field': 'site-locations', 'require': {'min': 1}, 'type': 'count-constraint', 'when': {'application-type': {'in': ['tree-works']}}}
- {'description': 'Exactly one site-location for all other applications types', 'field': 'site-locations', 'require': {'exact': 1}, 'type': 'count-constraint', 'when': {'application-type': {'not': ['tree-works']}}}
- If easting is provided, northing must also be provided and vice versa
- If latitude is provided, longitude must also be provided and vice versa
- Each site-location must include a site boundary and site address
- The planning authority must translate site information received on a paper form into the required structured site-location data, including the site boundary
- Site boundary must be valid WKT
- UPRNs must be valid format
- USRNs must be 8-digit strings
- Post code must be valid UK format