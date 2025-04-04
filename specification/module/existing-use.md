field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details | Describe the current use of the site | full;outline;extraction-oil-gas | MUST | 
site-vacant | True or False | | MUST | 
last-use-details | Describe the last use of the site | full;outline;extraction-oil-gas | MAY | Rule, is a MUST if `site-vacant` is True 
last-use-end-date | Date the last use ended (YYYY-MM-DD format) | full;outline;extraction-oil-gas | MAY | Rule, is a MUST if `site-vacant` is True 
is-contaminated-land | Is the site known to be contaminated? (True/False) | full;outline;extraction-oil-gas | MUST | 
is-suspected-contaminated-land | Is the site suspected of contamination? (True/False) | full;outline;extraction-oil-gas | MUST | 
proposed-use-contamination-risk | Is the proposed use vulnerable to the presence of contamination? (True/False) | full;outline;extraction-oil-gas | MUST |
contamination-assessment | Reference to contamination assessment document | full;outline;extraction-oil-gas | MAY | Is a MUST if `is-contaminated-land`, `is-suspected-contaminated-land` or `proposed-use-contamination-risk` is True
