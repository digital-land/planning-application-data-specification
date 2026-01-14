# Materials

What materials are being used for the proposed development

**Materials module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| building-elements | Building elements[]{} | Details of materials for a specific building element such as walls, roof, windows or doors |  | MUST |  |
| providing-additional-material-information | Providing additional material information | Is the applicant providing additional materials information on submitted plan(s)/drawing(s)/design and access statement? |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to supporting documents that have been uploaded with the application |  | MAY | Rule: is a MUST if `providing-additional-material-information` is `True` |


**Building element component**

field | name | description | required | notes
-- | -- | -- | -- | --
building-element-type | Building element type | The part of building the materials relate to, such as walls, roofs, windows, or doors | MUST | Select from the **building-element-type** enum
existing-materials | Existing materials | Description of the materials currently used for this building element | MAY | 
proposed-materials | Proposed materials | Description of the materials proposed for this building element as part of the development | MAY | 
materials-not-applicable | Materials not applicable | Indicates this building element is not relevant to the application | MAY | 
materials-not-known | Materials not known | Indicates the materials for this building element are not yet known | MAY | 


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- Each building-element must have a unique building-element-type
- At least one of: existing-materials, proposed-materials, materials-not-applicable or materials-not-known must be provided for each building-element
- materials-not-applicable cannot be true if existing-materials or proposed-materials is provided
- materials-not-known cannot be true if existing-materials or proposed-materials is provided
- supporting-documents must reference valid documents in the application