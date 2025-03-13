Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
development-phases[] | Phases of oil and gas development the application covers | Array (Enum) | MUST | One or more of: exploratory, appraisal, production. See [development phase enum](https://github.com/digital-land/planning-application-data-specification/discussions/194)
development-description | Brief description of the development, including main oils, gases, and machinery | String | MUST | Free text.
quantity-cubic-metres | Quantity of oil or gas involved (in cubic metres) | Number | MUST | 
permission-period-years | Period of permission sought (in years) | Number | MAY | Optional if period is not defined.
hydrocarbon-licence-block | Hydrocarbon licence block where the development is located | String | MUST | Typically an identifier like "PEDL123".
surface-site-area-hectares | Surface site area in hectares (ha) | Number | MUST | Value must be positive. Should it be calculated from the site boundary?
site-hectares-provided-by | Who provided the site hectares value | String | MAY | Either Applicant or System. Authority can use it to know if they need to check calculation
environmental-statement | Is an Environmental Statement attached to the application? | Boolean | MUST | Yes / No.
environmental-statement-reference | Reference of the environmental statement document supplied with application | String | MAY | Required if environmental-statement is True
