# Agricultural tenancy consent

Whether land is occupied under agricultural tenancy agreements and all parties have consented to the proposed change of use.

**Agricultural tenancy consent module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| agricultural-tenants | Agricultural tenants | Whether any part of the land covered by or within the curtilage of the building is occupied under any agricultural tenancy agreements. |  | MUST |  |
| tenancy-parties-consent | Consent of all tenancy parties | Whether all parties to the agricultural tenancy agreements have consented to the proposed change of use. |  | MAY | Rule: is a MUST if `agricultural-tenants` is `True`. Required when agricultural tenancy agreements exist. Consent must cover all parties to all relevant agreements, not only the tenants. |

