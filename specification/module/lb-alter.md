| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-alter-lb | True or False if proposal includes alterations |  | MUST |  |
| proposal-alter-lb-types[] | Select from a list of listed building alteration types, select all that apply | | MAY | Rule: is required if `proposal-alter-lb` is True |
| document-reference[] | References to documents detailing the proposed alterations | | MAY | Rule: is required if `proposal-alter-lb` is True |

See [listed building alteration types enum](https://github.com/digital-land/planning-application-data-specification/discussions/187)
