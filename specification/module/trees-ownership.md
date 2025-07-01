| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-applicant-owner | Does the applicant own the trees? (`true`/`false`) | notice-trees-in-con-area;consent-under-tpo | MUST | |
| owner[]{} | Details of the owner | | MAY | Rule: required if `is-applicant-owner` is `false` |

**Owner structure**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| contact-details{} | Details of how to contact the individual | MAY | |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact agent | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | MUST | see Phone number below. Only one number can be set as the primary number |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

