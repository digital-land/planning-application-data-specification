# Information to support LDC

Information to support Lawful Development Certificate applications including
details of existing use, interruptions, and changes to support evidence of lawfulness


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| existing-use-start-date | Existing use start date | Date when the existing use of the land or building commenced, in YYYY-MM-DD format |  | MUST |  |
| has-existing-use-interrupted | Existing use interrupted | Indicating whether the existing use has been interrupted since it commenced |  | MUST |  |
| interruption-details | Interruption details | Details of any interruption to the existing use including dates and circumstances |  | MAY | Rule: is a MUST if `has-existing-use-interrupted` is `True` |
| has-existing-use-changed | Existing use change | Indicate whether there has been any change in the existing use since it commenced |  | MUST |  |
| existing-use-change-details | Existing use change details | Details of any changes to the existing use including nature of changes and dates |  | MAY | Rule: is a MUST if `has-existing-use-changed` is `True` |

**Validation rules**

- existing-use-start-date matches YYYY-MM-DD format
- existing-use-start-date <= current_date
- has-existing-use-interrupted == true REQUIRES interruption-details.length > 0
- has-existing-use-changed== true REQUIRES existing-use-change-details.length > 0
- interruption-details must specify dates and nature of interruption when provided
- existing-use-change-details must specify dates and nature of changes when provided