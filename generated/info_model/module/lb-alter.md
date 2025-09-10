# Listed building alterations

Details of any changes being made to a listed building as part of development works

**Listed building alterations module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposal-alter-lb | Proposal alter listed building | True or False if proposal includes alterations to a listed building |  | MUST |  |
| proposal-alter-lb-types | Proposal alteration types[] | Select from a list of listed building alteration types, select all that apply |  | MAY | Select from the **lb-alteration-type** enum |
| document-reference | Document reference[]{} | References to documents detailing the proposed alterations |  | MAY |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 

