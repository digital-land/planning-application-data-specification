# Electronic communications apparatus

Details of proposed and existing electronic communications apparatus and supporting technical documents.

**Electronic communications apparatus module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| apparatus-type-details | Apparatus type details | Type of electronic communications apparatus to be installed or altered. |  | MUST |  |
| proposal-description | Proposal description | Details of the electronic communications apparatus to be installed or altered, including height, size, colour and other relevant characteristics. |  | MUST |  |
| replaces-installation | Replaces existing installation | Whether the proposal replaces an existing electronic communications installation. |  | MUST |  |
| description | Existing apparatus details | Details of the existing electronic communications apparatus being replaced, including height, size, colour and other relevant characteristics. |  | MAY | Rule: is a MUST if `replaces-installation` is `True` |
| icnirp-declaration-provided | International Commission on Non-Ionizing Radiation Protection (ICNIRP) declaration provided | Whether a declaration confirming compliance with the International Commission on Non-Ionizing Radiation Protection (ICNIRP) radio frequency public exposure guidelines is being submitted. |  | MUST |  |
| icnirp-declaration-document | International Commission on Non-Ionizing Radiation Protection (ICNIRP) declaration document{} | Reference to the document declaring compliance with the International Commission on Non-Ionizing Radiation Protection (ICNIRP) radio frequency public exposure guidelines. |  | MAY | Rule: is a MUST if `icnirp-declaration-provided` is `True` |
| ecomms-template-provided | Electronic communications supplementary template provided | Whether a completed Supplementary Information Template from Appendix D of the Code of Best Practice on Mobile Phone Network Development is being provided. |  | MUST |  |
| ecomms-template-document | Electronic communications supplementary template document{} | Reference to the completed Supplementary Information Template from Appendix D of the Code of Best Practice on Mobile Phone Network Development. |  | MAY | Rule: is a MUST if `ecomms-template-provided` is `True` |


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

