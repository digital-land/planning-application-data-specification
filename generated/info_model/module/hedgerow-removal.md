# Hedgerow removal notice

Information required for hedgerow removal notices including removal reasons, plans, length details, age considerations, and interest declarations


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| removal-reasons | Removal reasons | Reasons for the proposed removal of hedgerow(s) |  | MUST |  |
| plan-references | Plan references[] | References to plans showing the stretches of hedgerows to be removed |  | MUST |  |
| hedgerow-length | Hedgerow length | Total length, in metres, of hedgerow proposed for removal |  | MUST |  |
| hedgerow-less-than-30-years | Hedgerow less than 30 years | Is the hedgerow less than 30 years old? |  | MUST |  |
| planting-evidence-attached | Planting evidence attached | Is evidence of the date of planting attached? |  | MAY |  |
| interest-declaration | Interest declaration | The applicant's interest or ownership in the hedgerow |  | MUST | Select from the **hedgerow-interest-dec** enum |

**Validation rules**

- hedgerow-length must be a positive number
- planting-evidence-attached is required if hedgerow-less-than-30-years is true
- plan-references should reference documents in application.documents