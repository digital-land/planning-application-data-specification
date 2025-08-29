# Advertisement location

Information about advertisement placement including whether it's already in place,
replacement status, and potential overhang over public areas


**Advertisement location module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-advert-in-place | Is advert in place | Whether the advertisement is already in place |  | MUST |  |
| advert-placed-date | Advert placed date | Date when the advertisement was placed (YYYY-MM-DD format) |  | MAY | Rule: is a MUST if `is-advert-in-place` is `True` |
| is-replacement-advert | Is replacement advert | Whether this is a replacement advertisement |  | MUST |  |
| document-reference | Document reference[]{} | References to documents detailing the proposed alterations |  | MAY | Rule: is a MUST if `is-advert-in-place` is `True`. Rule: is a MUST if `is-replacement-advert` is `True` |
| is-advert-overhanging | Is advert overhanging | Whether the advertisement will project over a footpath or other public highway |  | MUST |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- if is-advert-in-place == true then advert-placed-date is required
- if (is-advert-in-place == true OR is-replacement-advert == true) then document-reference is required