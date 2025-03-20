## Site information 

Field | Description | Application-Types | Required? | Notes
-- | -- | -- | -- | --
site-area{} | The total area of the site |   | MUST | See "Site Area Structure" below
existing-use[]{} | Structured information on the current use of the site |   | MUST | An array, as there may be multiple uses (see "Existing Use Structure")
known-constraints[] | A list of the known constraints affecting the site |   | MUST | See the [Site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)
supporting-documents[]{} | A list of documents with the supporting information for the idenitifed site constraints | MAY | Rule: a MUST if `known-constraints` is not empty

### Site Area Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
value | Numeric value representing site area | Number | MUST | Should ideally be calculated from site boundary
unit | Unit of measurement for site area | Enum | MUST | One of: m2, hectares
provided-by | Whether the site area was provided by the applicant or system |   | MAY | Enum: Applicant, System/Service

### Existing Use Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
use-classes[] | List of applicable use classes | Enum | MUST | Mixed-use sites can list multiple classes. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
floorspace | Total floorspace for the use | Number | MUST | Numeric value. Expected in m2

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
details | Additional details about the document, for example, details about the constraint it references | String | MAY | 
