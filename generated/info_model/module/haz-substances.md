# Hazardous substances

Information about hazardous substances involved in the proposal,
including substance types, quantities, and consent requirements


| involves-hazardous-substances | Involves hazardous substances | Indicates if hazardous substances are involved in the proposal |  | MUST | Select from the **yes-no-not-applicable** enum |
| substance-types | Substance types[]{} | List of hazardous substances and their quantities |  | MAY | Rule: is a MUST if `involves-hazardous-substances` is `yes` |
| hazardous-sub-consent-req | Hazardous substance consent required | Does the proposal involve the use or storage of any substances requiring hazardous substances consent |  | MUST |  |
| hazardous-sub-consent-details | Hazardous substance consent details | Details of hazardous substance consent requirements |  | MAY | Rule: is a MUST if `hazardous-sub-consent-req` is `True` |


**Hazardous substance model**

field | name | description | required | notes
-- | -- | -- | -- | --
hazardous-substance-type | Hazardous substance type | Reference of hazardous substance type from predefined list | MUST | Select from the **hazardous-sub-type** enum
hazardous-substance-other | Hazardous substance other | The specific name of the hazardous substance if other is selected | MAY | Rule: is a MUST if `hazardous-substance-type` is `other`
amount | Amount | The total amount due for the application fee | MUST | 

**Validation rules**

- if involves-hazardous-substances == 'yes' then substance-types is required
- if hazardous-sub-consent-req == true then hazardous-sub-consent-details is required
- if hazardous-substance-type == 'other' then name is required
- amount > 0