# Hedgerow removal notice

Details of any hedgerows being removed as part of the development

**Hedgerow removal notice module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| removal-reasons | Removal reasons | Reasons for the proposed removal of hedgerow(s) |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to plans or drawings showing the stretches of hedgerow to be removed |  | MUST |  |
| hedgerow-length | Hedgerow length | Total length, in metres, of hedgerow proposed for removal |  | MUST |  |
| hedgerow-less-than-30-years | Hedgerow less than 30 years | Is the hedgerow less than 30 years old? |  | MUST |  |
| planting-evidence-attached | Planting evidence attached | Is evidence of the date of planting attached? |  | MAY |  |
| interest-declaration | Interest declaration | The applicant's interest or ownership in the hedgerow |  | MUST | Select from the **hedgerow-interest-type** enum |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- hedgerow-length must be a positive number
- planting-evidence-attached is required if hedgerow-less-than-30-years is true
- each document in supporting-documents must have a `reference` that matches a document in application.documents