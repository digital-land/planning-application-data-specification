**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element[]{} | List of building elements where materials are being described (e.g., walls, roof). | hh;full;demolition-con-area;lbc;advertising;outline | MUST | See Building element structure. One entry per building element.
additional-material-information | Indicates whether additional documents are provided to supplement the materials description | hh;full;demolition-con-area;lbc;advertising;outline | MUST | (`true` or `false`).
supporting-documents[] | Details for documents providing additional material information. | hh;full;demolition-con-area;lbc;advertising;outline | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
