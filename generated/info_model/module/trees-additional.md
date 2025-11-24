# Trees additional information

Further details of any issues relating to trees on the site

**Trees additional information module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| advice-from-authority | Advice from authority | Any advice provided on-site by a Local Planning Authority (LPA) officer |  | MAY |  |
| condition-concerns | Condition concerns | Whether there are concerns the tree(s) are diseased or might break or fall | consent-under-tpo | MUST |  |
| causing-subsidence | Causing subsidence | Whether subsidence damage is being caused by the tree(s) | consent-under-tpo | MUST |  |
| causing-structural-damage | Causing structural damage | Whether structural damage is being caused by the tree(s) | consent-under-tpo | MUST |  |
| supporting-documents | Supporting documents[]{} | Documents supporting the work required to trees |  | MUST |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- If condition-concerns is true then Arboricultural impact assessment document is required
- If causing-subsidence is true then Subsidence Report is required
- If causing-structural-damage is true then a Structural damage report is required
- supporting-documents must include sketch plan, supporting documents, reports, or photographs
- supporting-documents must include any documents required based on condition concerns, subsidence, or structural damage
- each document in supporting-documents must have a `reference` that matches a document in application.documents