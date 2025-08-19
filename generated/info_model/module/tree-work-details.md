# Identification of tree(s) and description of works

Details of trees and proposed work to them, including identification, 
species and work descriptions


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| description | Description | Description of work applicant wishes to carry out, including identifying the trees, species and setting out the work |  | MUST |  |
| tree-details | Tree details[]{} | Details of each tree that is part of the proposal |  | MAY |  |


**Tree details model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
species | Species | The species of the tree | MAY | 
description-of-works | Description of works | Description of the nature of the work to be carried out on this tree | MAY | 
reason | Reason | A textual reason | MAY | 
replanting-description | Replanting description | Details of replanting arrangements if applicable | MAY | 

**Validation rules**

- Tree identifiers should use TPO reference numbers where applicable
- Description must include tree identification, species and work details