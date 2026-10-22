# Listed building grade

The grade of any listed building affected by the proposed development.

**Listed building grade module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| listed-building-grade-known | Listed building grade known | Set to true if the applicant knows the listed building grade. Set to false if they do not know it. |  | MUST |  |
| listed-building-grade | Listed building grade | The grade of the listed building, selected from the listed-building-grade codelist |  | MUST | Select from the **listed-building-grade** enum |
| listed-building | Listed building | Listed building reference for cross-referencing with listed building records |  | MAY |  |
| provided-by | Provided by | Source of the listed building grade information |  | MAY | Select from the **provided-by** enum |

**Validation rules**

- If listed-building-grade-known is true, supply a grade from the listed-building-grade codelist
- If listed-building-grade-known is false, the applicant is declaring that they do not know the grade and must not supply listed-building-grade
- If listed-building is provided, it must reference a valid listed building