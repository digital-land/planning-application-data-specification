field | description | application-types |	required | notes
--- | --- | --- | --- | ---
removal-reasons | Reasons for the proposed removal of hedgerow(s) | hedgerow-removal | MUST |
plan-references[] | References to plans showing the stretches of hedgerows to be removed | hedgerow-removal | MUST | References should be document references from `application.documents`
hedgerow-length | Total length of hedgerow proposed for removal (in metres) | hedgerow-removal | MUST	|Rule: Must be a positive number
hedgerow-less-than-30-years | Is the hedgerow less than 30 years old? (`true`/`false`) | hedgerow-removal | MUST |	
planting-evidence-attached | Is evidence of the date of planting attached?	(`true`/`false`) | hedgerow-removal | MAY |	Required if `hedgerow-less-than-30-years` is `true`
interest-declaration | The applicant's interest or ownership | hedgerow-removal | MUST | See the [hedgerow interest declaration enum](https://github.com/digital-land/planning-application-data-specification/discussions/216)
