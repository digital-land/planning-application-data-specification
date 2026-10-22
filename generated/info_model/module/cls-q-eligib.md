# Class Q general eligibility

General agricultural unit, building, extension, access and location eligibility information for a Class Q change of use to dwellinghouses.

**Class Q general eligibility module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| cls-q-current-agri-unit | Current agricultural unit | Whether the site is currently part of an established agricultural unit. |  | MUST |  |
| cls-q-agri-pd-10-years | Agricultural permitted development in preceding 10 years | Whether agricultural permitted development work has been carried out on the agricultural unit during the 10 years before development begins. |  | MUST |  |
| cls-q-dimensions-exceeded | External dimension limits exceeded | Whether the resulting building extends beyond the existing building within the scope of the Class Q external dimensions question. |  | MUST | The source wording is preserved, including the phrase “other than” and the 0.2 metre subcondition. Its interpretation needs clarification before deriving automated eligibility checks. |
| cls-q-extension-exceeded | Extension limits exceeded | Whether a proposed extension exceeds any of the listed Class Q extension limits, or no extension is proposed. |  | MUST | Select from the **yes-no-not-applicable** enum |
| has-suitable-highway-access | Has suitable public highway access | Whether the building has suitable access to a public highway. |  | MUST |  |
| cls-q-existing-space-capable | Existing building space-standard capability | Whether the existing building, including permitted building work or operations but excluding any proposed extension, is capable of complying with the nationally described space standard. |  | MUST |  |
| has-location-restriction | Has location restriction | Whether any part of the land, site or building is affected by a location restriction listed for Class Q. |  | MUST | Use the Class Q question and restriction list in the field body. The source form advises applicants answering Yes not to continue and to seek advice from the local planning authority. |

