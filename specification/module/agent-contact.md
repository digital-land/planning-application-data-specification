| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| email | Email used to contact agent | | MUST |  |
| phone-number{} | 1 or more telephone numbers to contact agent | | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |
