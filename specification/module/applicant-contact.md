| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| email | Email used to contact applicant | | MUST |  |
| phone-number{} | 1 or more telephone numbers to contact applicant | | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| phone-number-type | one of `mobile` or `landline` (See [phone-number-type](https://github.com/digital-land/planning-application-data-specification/discussions/185)) | Is it important to know? |
| number-preferred | Let user set which is the primary number to use | Default to False, user can select True for one number |
