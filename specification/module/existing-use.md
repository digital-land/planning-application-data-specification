Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-use-details | Describe the current use of the site |   | MUST | 
site-vacant | True or False | | MUST | 
last-use-details | Describe the last use of the site | | MAY | Rule, is a MUST if `site-vacant` is True 
last-use-end-date | Date the last use ended (YYYY-MM-DD format) | | MAY | Rule, is a MUST if `site-vacant` is True 
is-contaminated-land | Is the site known to be contaminated? (True/False) | | MUST | 
is-suspected-contaminated-land | Is the site suspected of contamination? (True/False) | | MUST | 
proposed-use-contamination-risk | Is the proposed use vulnerable to the presence of contamination? (True/False) | | MUST |
contamination-assessment | Reference to contamination assessment document | | MAY | Is a MUST if `is-contaminated-land`, `is-suspected-contaminated-land` or `proposed-use-contamination-risk` is True
