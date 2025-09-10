# Trees and hedges information

Details of trees and/or hedges that will be affected by the proposed development

**Trees and hedges information module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| trees-on-site | Trees on site | Whether trees or hedges are present on the proposed development site | full;outline-some;extraction-oil-gas | MUST |  |
| trees-on-adj-land | Trees on adjacent land | Whether trees or hedges on land adjacent to the proposed development site could influence the development or might be important as part of the local landscape character | full;outline-some;extraction-oil-gas | MUST |  |
| has-falling-trees-risk | Falling trees risk | Whether there are falling trees on-premises or adjacent premises that are a risk to the development | hh | MUST |  |
| falling-trees-document | Falling trees document{} | Details of document showing location of trees that pose a risk to the development | hh | MAY | Rule: is a MUST if `has-falling-trees-risk` is `True` |
| tree-removal | Tree removal | Whether trees or hedges need to be pruned or removed | hh | MUST |  |
| tree-removal-plan | Tree removal plan{} | Details of document showing location of trees and hedges to be removed or pruned | hh | MAY | Rule: is a MUST if `tree-removal` is `True` |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- falling-trees-document reference must match a document in application.documents
- tree-removal-plan reference must match a document in application.documents