# Class Q former agricultural unit eligibility

Agricultural unit membership history and subsequent use for a prior approval change of use from agricultural buildings to dwellinghouses where the site was formerly part of an established agricultural unit.

**Class Q former agricultural unit eligibility module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| cls-q-unit-on-2023-07-24 | Agricultural unit on 24 July 2023 | Whether the site was part of an established agricultural unit on 24 July 2023. |  | MAY | Rule: is a MUST if `cls-q-eligib.cls-q-current-agri-unit` is `False` |
| cls-q-ceased-10-years | Ceased agricultural unit membership at least 10 years before development | Whether at least 10 years will have passed since the site ceased to be part of an established agricultural unit before development begins. |  | MUST | Select from the **yes-no-not-applicable** enum. The source form provides Yes, No and Not applicable answer options. The question follows a Yes answer to the dated agricultural unit membership question. |
| cls-q-non-agri-use | Non-agricultural use since leaving agricultural unit | Whether the site has been used for any non-agricultural purpose since ceasing to be part of the agricultural unit. |  | MAY | Rule: is a MUST if `cls-q-eligib.cls-q-current-agri-unit` is `False` |

