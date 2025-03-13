Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
documents[]{} | List of plans, drawings, and supporting documents |  | MUST | See Document Structure below.
inspection-address | Address where supporting material can be inspected |  | MUST | Full postal address for document inspection.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
