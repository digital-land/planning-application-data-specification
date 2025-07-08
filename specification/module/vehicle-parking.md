Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
parking-spaces[]{} | List of parking spaces by vehicle type |   | MUST | One object per vehicle type, including “Other” if specified.

**Parking space items**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
parking-space-type | Type of vehicle from the codelist | Enum / String | MUST | Select from [parking space type enum](https://github.com/digital-land/planning-application-data-specification/discussions/199), or "other" if user specifies a custom type.
vehicle-type-other | Custom value if "Other" is selected | String | MAY | Rule: Required only if `vehicle-type` is "other".
total-existing | Existing on-site parking spaces | Number | MUST | Must be 0 or positive.
total-proposed | Total proposed spaces, including retained spaces | Number | MUST | Must be 0 or positive.
unknown-proposed | Is the total proposed number unknown? | Boolean | MUST | If True, total-proposed can be left blank. Only applicable in outline-some applications
difference-in-spaces | Calculated difference between existing and proposed spaces | Number | MUST | Calculated as total-proposed - total-existing. Could be calculated by applicant or system
