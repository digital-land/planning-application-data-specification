| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of the non-material amendments the applicant seeks to make | | MUST | |
| is-substituting-document | True or False | | MUST | |
| replacement-documents[] | address, if available for the site | | MAY | Rule, is a MUST if is True |
| reason | Reason why applicant wants to make the amendment | | MUST | |

**Replacement-document**

| field | description | required | notes |
| --- | --- | --- | --- |
| old-document | Reference of the old document | MUST | |
| new-document | Reference for the new document | MUST | |
