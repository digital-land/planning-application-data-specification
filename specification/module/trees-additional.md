field | description | application-types | required | notes
--- | --- | --- | --- | ---
advice-from-authority | Any advice provided on-site by a Local Planning Authority (LPA) officer | consent-under-tpo;notice-trees-in-con-area | MAY | 
condition-concerns | Are there concerns the tree(s) are diseased or might break or fall? (`true`/`false`) | consent-under-tpo | MUST | Rule: if true then Arboricultural impact assessment document is required
causing-subsidence | Is subsidence damage being caused by the tree(s)? (`true`/`false`) | consent-under-tpo | MUST | Rule: if `true` then Subsidence Report is required
causing-structural-damage | Is structural damage being caused by the tree(s)? (`true`/`false`) | consent-under-tpo | MUST | Rule: if `true` then a Structural damage report is required
supporting-documents[]{} | A list of the documents supporting the work required to trees | consent-under-tpo;notice-trees-in-con-area | MUST | Rule: must include sketch plan, supporting documents, reports, or photographs and any documents required given the answers to the above questions

**Supporting document structure**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
description | Description of the document | String | MAY | Optional description of the document
