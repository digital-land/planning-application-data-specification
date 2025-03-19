| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| email | Email used to contact applicant | | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact applicant | | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | | MAY | |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`
