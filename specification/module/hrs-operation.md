| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation[]{} | State the hours of opening for each non-residential use | | MUST | |
| additional-information | | extraction-oil-gas | MAY | |

**hours of operation**
| field | description | required | notes |
| --- | --- | --- | --- |
| non-residential-use | | MUST | Should this be a use class? |
| opening-times[]{} | Structured data for opening hours by day | MAY | one of `hours-of-operation` or `hours-unknown` must be completed |
| hours-unknown | Applicant states they do not know the hours of operation | MAY | one of `hours-of-operation` or `hours-unknown` must be completed |

**Opening times**
| field | description | notes |
| --- | --- | --- |
| day-type | Day of the week | One of [day-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/197) |
| open-time | | HH:MM |
| close-time | | HH:MM |
| closed | True or False | If True, `open-time` and `close-time` must be empty. Explicitly state when closed |
