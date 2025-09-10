# Immunity from listing

Whether the applicant has obtained a Certificate of Immunity (COI) meaning the building in question cannot be listed

**Immunity from listing module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| cert-of-immunity-sought | Certificate of immunity sought | Has a certificate of immunity been sought |  | MUST | Select from the **yes-no-unknown** enum |
| application-result | Application result | Provide the result of the application for a certificate of immunity |  | MAY |  |

**Validation rules**

- application-result is required when cert-of-immunity-sought is 'yes'