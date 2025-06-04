| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation[]{} | List the hours of operation by non-residential use | full;outline;extraction-oil-gas | MUST | |
| additional-information | Any additional information (such as hours of use of other machinery within the site-generators, pumps, etc) | extraction-oil-gas | MAY | |

**hours of operation**
| field | description | required | notes |
| --- | --- | --- | --- |
| use | The use class | MUST | One of the [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) + other |
| use-other | Specify use if use is other | MAY	Required if `use` is `other`
| operational-times[]{} | Structured data for operational hours by day | MAY | Rule: Must be completed if hours-not-known is not provided |
| hours-not-known | Applicant states they do not know the hours of operation | MAY | Rule: Must be completed if operational-times is not provided |

**Opening times**
| field | description | notes |
| --- | --- | --- |
| day-type | Day or type of day | One of [day-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/197) |
| time-ranges[]{} | Opening and closing times for the day	| MUST | Can have multiple ranges (e.g., morning and evening opening) |
| closed | True or False | If True, `open-time` and `close-time` must be empty. Explicitly state when closed |

**time range structure**
field	| description |	required | notes
--- | --- | --- | ---
open-time | Opening time | MUST | Format: `HH:MM`
close-time | Closing time | MUST | Format: `HH:MM`
