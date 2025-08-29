# Existing use

Information about the current and previous use of the site, including contamination status and supporting documents.


**Existing use module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| existing-use-details | Existing use details[]{} | List of existing site uses and related land areas |  | MUST |  |
| site-vacant | Site vacant | Is the site currently vacant |  | MUST |  |
| last-use-details | Last use details | Description of the last use of the site |  | MAY | Rule: is a MUST if `site-vacant` is `True` |
| last-use-end-date | Last use end date | Date the last use ended (YYYY-MM-DD format) |  | MAY | Rule: is a MUST if `site-vacant` is `True` |
| is-contaminated-land | Is contaminated land | Is the site known to be contaminated? |  | MUST |  |
| is-suspected-contaminated-land | Is suspected contaminated land | Is the site suspected of contamination? |  | MUST |  |
| proposed-use-contamination-risk | Proposed use contamination risk | Is the proposed use vulnerable to the presence of contamination? |  | MUST |  |
| contamination-assessment | Contamination assessment | Reference to contamination assessment document |  | MAY |  |


**Existing use detail component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-details | Use details | Further detail of the use | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`
land-part | Land part | Which part of the land the use relates to | MUST | 

**Validation rules**

- last-use-details and last-use-end-date are required if site-vacant is true
- contamination-assessment is required if any of is-contaminated-land, is-suspected-contaminated-land, or proposed-use-contamination-risk is true