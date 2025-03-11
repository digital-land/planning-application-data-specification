**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| building-element[] | Each of the categories listed in the Materials section | | MUST | see building element |
| additional-material-information | True or False | | MUST | |
| document-reference[] | | | MAY | Rule: complete if `additional-information` is True |

**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| building-element-type | one from building element types list | | MUST | |
| existing-materials | | | MAY | if applicable |
| proposed-materials | | | MAY | if applicable |
| materials-not-applicable | True or False | | MAY | MUST if `existing-materials` and `proposed-materials` not filled out |
| materials-not-known | True or False | | MAY | MUST if `existing-materials` and `proposed-materials` not filled out |

**building element types**
| building-element-type | application-types |
| --- | --- |
| Walls | advertising;demolition-con-area;full;hh;outline |
| Roof | advertising;demolition-con-area;full;hh;outline |
| Windows | advertising;demolition-con-area;full;hh;outline |
| Doors | advertising;demolition-con-area;full;hh;outline |
| Boundary treatments | advertising;demolition-con-area;full;hh;lbc;outline |
| Vehicle access and hard-standings | advertising;demolition-con-area;full;hh;lbc;outline |
| Lighting | advertising;demolition-con-area;full;hh;lbc;outline |
| Other | advertising;demolition-con-area;full;hh;lbc;outline |
| External walls | lbc |
| Roof covering | lbc |
| Chimney | lbc |
| External doors | lbc |
| Ceilings | lbc |
| Internal walls | lbc |
| Floors | lbc |
| Internal doors | lbc |
| Rainwater goods | lbc |
