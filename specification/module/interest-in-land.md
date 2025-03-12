| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicant-owns-land | True of False |  | MUST | |
| permission-obtained | True or False. Has permission of the owner for the display of an advertisement been obtained? | | MAY | Rule is a MUST if `applicant-owns-land` is True |
| permission-not-obtained-details | Details if permission not obtained | | MAY | Rule is a MUST if `applicant-owns-land` is True and `permission-obtained` is FALSE |
