
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| title | Title of individual | | MAY |  |
| first-name | First name of the individual | | MUST |  |
| last-name | last name of the individual | | MUST |  |
| company | company agent works for | | ? | |
| address-text | The address that can be used to correspond with the agent | | MAY | |
| post-code | The post code for the address provided | | MAY | |
| email | Email used to contact agent | pip | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | pip | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | pip | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`
