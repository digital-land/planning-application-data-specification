# Development type

Information about oil and gas development applications including phases, 
quantities, licensing, and environmental considerations


**Development type module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| development-phase | Development phase | Phases of oil and gas development the application covers |  | MUST | Select from the **development-phase** enum |
| development-description | Development description | Brief description of the development, including main oils, gases, and machinery |  | MUST |  |
| quantity-cubic-metres | Quantity cubic metres | Quantity of oil or gas involved in cubic metres |  | MUST |  |
| permission-period-years | Permission period years | Period of permission sought in years |  | MAY |  |
| hydrocarbon-licence-block | Hydrocarbon licence block | Hydrocarbon licence block where the development is located |  | MUST | Typically an identifier like "PEDL123" |
| surface-site-area-hectares | Surface site area hectares | Surface site area in hectares |  | MAY | could this be calculated from the site boundary? |
| site-hectares-provided-by | Site hectares provided by | Who provided the site hectares value (applicant or system) |  | MAY | Select from the **provided-by** enum |
| environmental-statement | Environmental statement | Is an Environmental Statement attached to the application |  | MUST |  |
| environmental-statement-reference | Environmental statement reference | Reference to the environmental statement document |  | MAY | Rule: is a MUST if `environmental-statement` is `True` |

**Validation rules**

- development-phase must contain at least one value from development-phases codelist
- quantity-cubic-metres must be a positive number
- surface-site-area-hectares must be a positive number
- environmental-statement-reference is required when environmental-statement is true
- environmental-statement-reference must reference a valid document in the application
- hydrocarbon-licence-block typically follows format PEDL123