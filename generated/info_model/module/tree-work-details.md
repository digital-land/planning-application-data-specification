# Identification of tree(s) and description of works

Details of trees affected by the proposed development and what work is being done to them.

**Identification of tree(s) and description of works module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| description | Description | Description of work applicant wishes to carry out, including identifying the trees, species and setting out the work |  | MUST |  |
| tree-details | Tree details[]{} | Details of each tree that is part of the proposal |  | MAY |  |


**Tree details component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | Identifier for the tree, use the TPO identifier if applicable | MUST |  | 
species | Species | The species of the tree | MAY |  | 
description-of-works | Description of works | Description of the nature of the work to be carried out on this tree | MAY |  | 
reason | Reason | Explain the reason for the work | MAY |  | consent-under-tpo
replanting-description | Replanting description | Details of replanting arrangements if applicable | MAY |  | consent-under-tpo

**Validation rules**

- Tree identifiers should use TPO reference numbers where applicable
- Description must include tree identification, species and work details