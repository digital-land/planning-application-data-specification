Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
involves-hazardous-substances | Indicates if hazardous substances are involved | full;outline  | MUST | One of Yes, No, Not Applicable.
substance-types[] | List of hazardous substances and their quantities |  full;outline  | MAY | Required if hazardous-substances-involved is Yes.
hazardous-sub-consent-req | Does the proposal involve the use or storage of any substances requiring hazardous substances consent? (`true`/`false`) | extraction-oil-gas | MUST | 
hazardous-sub-consent-details | Details of hazardous substance consent | extraction-oil-gas | MAY | Is a MUST if `hazardous-sub-consent-req` is true

**Hazardous substance types**

Field | Description | Notes
-- | -- | --
hazardous-substance-type | Reference of hazardous substance type | Predefined list (see [hazardous-substances enum](https://github.com/digital-land/planning-application-data-specification/discussions/196)) + option for Other.
name | Name of the hazardous substance | Only required if Other is selected
amount | Amount of the substance in tonnes | Numeric. Must be greater than 0.
