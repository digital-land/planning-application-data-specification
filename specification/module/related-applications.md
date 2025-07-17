| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-related-applications | True of False. True if any related applications, previous proposals or demolitions for the site |  | MUST | |
| related-applications[] | List of related applications | MAY | Rule is a MUST if `has-related-applications` is True |

**Related applicayion**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-date | date of the decision | If decided | |
