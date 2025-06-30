| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of work applicant wishes to carry out. It should include identifying the trees, species and setting out the work | notice-trees-in-con-area;consent-under-tpo | MUST | |
| tree-details[]{} | Details of each tree that is part of the proposal | notice-trees-in-con-area;consent-under-tpo | MAY | |

**tree details structure**

field | description | application-type
-- | -- | --
reference | Identifier for the tree, use the TPO identifier if applicable |  
species | The species of the tree  |  
description-of-works | Describe the nature of the work to this tree  |  
reason | Explain the reason for the work | tpo
replanting-description | Details of replanting | tpo
