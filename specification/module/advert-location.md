| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-advert-in-place | True of False |  | MUST | |
| advert-placed-date | YYYY-MM-DD | | MAY | Rule is a MUST if `is-advert-in-place` is True |
| is-replacement-advert | True or False | | MUST |  |
| document-reference[] | References to drawings and photos showing existing signs | | MAY | Rule is a MUST if `is-advert-in-place` OR  `is-replacement-advert` are True |
| is-advert-overhanging | True or False if advertisement will project over a footpath or other public highway | | MUST | |
