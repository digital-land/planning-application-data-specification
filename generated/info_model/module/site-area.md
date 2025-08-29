# Site area

Information about the size of the development site, including 
the area measurement and source of the measurement


**Site area module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-area-in-hectares | Site area in hectares | The size of the site in hectares |  | MUST |  |
| site-area-provided-by | Site area provided by | Who provided the site area value |  | MAY | Select from the **provided-by** enum |

**Validation rules**

- site-area-in-hectares must be a positive number
- Authority can use site-area-provided-by to determine if calculation verification is needed
- site-area-in-hectares is measured in hectares