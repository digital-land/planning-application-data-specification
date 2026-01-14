## Decision: Require WGS84 for exchanged location coordinates

**Date:** 2025-10-08  
**Status:** Accepted  

**Context:**  
- Questions were raised about whether both easting/northing (British National Grid) and latitude/longitude are required (#305).  
- The government open standard for exchanging location points mandates WGS84 lat/long ([Open standards: exchange of location point](https://www.gov.uk/government/publications/open-standards-for-government/exchange-of-location-point)).  

**Decision:**  
- Use WGS84 latitude/longitude as the required coordinate system for exchanging location data in submissions.  
- British National Grid references (easting/northing) may be included as an additional convenience field but do not replace the WGS84 requirement.  

**Consequences:**  
- Components (e.g. `site-location`) document WGS84 as the standard and note that British National Grid references can be provided additionally/derived.  
- Validation and guidance should treat WGS84 lat/long as mandatory for exchange; British National Grid is optional/extra.  
- Downstream systems can rely on WGS84 for interoperability and still consume British National Grid when supplied.  
