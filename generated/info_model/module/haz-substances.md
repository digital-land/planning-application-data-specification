# Hazardous substances

Details of hazardous substances requiring consent used as part of the development

**Hazardous substances module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| involves-hazardous-substances | Involves hazardous substances | Indicates if hazardous substances are involved in the proposal | full, outline | MUST | Select from the **yes-no-not-applicable** enum |
| substance-types | Substance types[]{} | List of hazardous substances and their quantities | full, outline | MAY | Rule: is a MUST if `involves-hazardous-substances` is `yes` |
| hazardous-sub-consent-req | Hazardous substance consent required | Does the proposal involve the use or storage of any substances requiring hazardous substances consent | extraction-oil-gas | MUST |  |
| hazardous-sub-consent-details | Hazardous substance consent details | Details of hazardous substance consent requirements | extraction-oil-gas | MAY | Rule: is a MUST if `hazardous-sub-consent-req` is `True` |


**Hazardous substance component**

field | name | description | required | notes
-- | -- | -- | -- | --
hazardous-substance-type | Hazardous substance type | Reference of hazardous substance type from predefined list | MUST | Select from the **hazardous-sub-type** enum
hazardous-substance-other | Hazardous substance other | The specific name of the hazardous substance if other is selected | MAY | Rule: is a MUST if `hazardous-substance-type` is `other`
amount | Amount | The total amount due for the application fee | MUST | 

**Validation rules**

- if application-type in ['full', 'outline'] and involves-hazardous-substances == 'yes' then substance-types is required
- if application-type == 'extraction-oil-gas' and hazardous-sub-consent-req == true then hazardous-sub-consent-details is required
- if hazardous-substance-type == 'other' then name is required
- amount > 0