# Listed building grade

Information about the grade of listed buildings affected by the planning application


**Listed building grade module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| listed-building-grade | Listed building grade | The grade of the listed building, selected from the listed-building-grade codelist or "don't know" |  | MUST | Select from the **listed-building-grade** enum |
| listed-building | Listed building | Listed building reference for cross-referencing with listed building records |  | MAY |  |
| provided-by | Provided by | Source of the listed building grade information |  | MAY | Select from the **provided-by** enum |

**Validation rules**

- listed-building-grade must be selected from the listed-building-grade codelist or 'don't know'
- If listed-building is provided, it must reference a valid listed building