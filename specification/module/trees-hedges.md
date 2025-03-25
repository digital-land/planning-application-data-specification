| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| falling-trees-risk | There are falling trees on-premises or adjacent premises that are a risk to the development. (`true`/`false`) | hh | MUST | |
| falling-trees-document{} | Details of document showing location of trees | hh | MAY | Rule: is a MUST if `falling-trees-risk` is `true` |
| tree-removal | Do trees or hedges need to be pruned or removed (`true`/`false`) | hh | MUST | |
| tree-removal-plan{} | Details of document showing location of trees and hedges | hh | MAY | Rule: is a MUST of ` tree-removal` is `true` |
| trees-on-site | Trees or hedges are on the proposed development site (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |
| trees-on-adj-land | Trees or hedges on land adjacent to the proposed development site that could influence the development or might be important as part of the local landscape character (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |

**tree removal plan**

field | description | data type | required? | notes
-- | -- | -- | -- | --
document-reference | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
