# Hours of operation

Proposed operating hours if the proposed development is intended for non-residential use.

**Hours of operation module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| hours-of-operation | Hours of operation[]{} | List the hours of operation by non-residential use | full, outline, extraction-oil-gas | MUST |  |
| additional-information | Additional information | Any additional information (such as hours of use of other machinery within the site-generators, pumps, etc) | extraction-oil-gas | MAY |  |


**Hours of operation component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-other | Use other | Specify use if use is "other" | MAY | Rule: is a MUST if `use` is `other`. Required if use is "other"
operational-times | Operational times[]{} | Structured data for operational hours by day | MAY | Rule: is a MUST if `hours-not-known` is `True`. Must be completed if hours-not-known is not provided
hours-not-known | Hours not known | Applicant states they do not know the hours of operation | MAY | 


**Operational times component**

field | name | description | required | notes
-- | -- | -- | -- | --
day-type | Day type | Day or type of day | MUST | Select from the **day-type** enum
closed | Closed | True or False - explicitly state when closed | MAY | If True, open-time and close-time must be empty
time-ranges | Time ranges[]{} | Opening and closing times for the day | MAY | Rule: is a MUST if `closed` is `False`. Can have multiple ranges (e.g., morning and evening opening)


**Time range component**

field | name | description | required | notes
-- | -- | -- | -- | --
open-time | Open time | Opening time | MUST | Format: HH:MM
close-time | Close time | Closing time | MUST | Format: HH:MM

**Validation rules**

- At least one hours-of-operation entry must be provided
- Either operational-times or hours-not-known must be provided within each hours-of-operation entry
- use-other is required when use is 'other'
- time-ranges is required when not closed
- open-time and close-time must be in HH:MM format
- close-time must be after open-time within same time range