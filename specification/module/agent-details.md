| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| title | Title of individual | | MAY |  |
| first-name | First name of the individual | | MUST |  |
| last-name | last name of the individual | | MUST |  |
| address | | | | exact structure of address TBC |
| post-code | | | MAY | |
| email | Email used to contact agent | pip | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | pip | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | pip | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`
