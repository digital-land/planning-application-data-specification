field | description | data type | application-types | required | notes
-- | -- | -- | -- | -- | --
permission-types[] | List of permission types being applied for | Array | extraction-oil-gas | MUST | One or more from the [permission types enum](https://github.com/digital-land/planning-application-data-specification/discussions/198).
related-applications[]{} | List of related proposals with reference and decision dates | Array | extraction-oil-gas | MAY | Required if any application type involves prior permissions.
other-details | | String | extraction-oil-gas | MAY |  If there are other details not covered by the application types 
consolidate-permissions | Is the applicant willing to consolidate or update existing permissions? | Boolean | extraction-oil-gas | MUST | Yes / No. If Yes, further details are required.
consolidate-details | Details about the consolidation or update of permissions | String | extraction-oil-gas | CONDITIONAL | Required if consolidate-permissions is Yes.

**Related proposals** 

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
proposal-type | Type of related proposal | Enum | MUST | Enum value from Application Type
reference-number | Reference number of the related proposal | String | MUST | Unique identifier for the proposal
decision-date | Decision date of the related proposal | Date | MUST | Format: YYYY-MM-DD.
