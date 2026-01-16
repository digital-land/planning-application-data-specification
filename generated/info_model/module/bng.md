# Biodiversity net gain

How any natural habitats on the development site will be improved by the proposed works.

**Biodiversity net gain module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| bng-exempt | Biodiversity gain exemption | Statement whether the biodiversity gain condition will apply if permission is granted. Householder applicants need to confirm the biodiversity gain condition does not apply. | hh | MUST |  |
| bng-condition-applies | Biodiversity gain condition applies | Does the applicant believe the Biodiversity Gain Condition applies to this application | full, outline, demolition-con-area | MUST |  |
| bng-condition-exemption-reasons | Biodiversity gain condition exemption reason[]{} | Reasons why BNG does not apply, referencing exemptions or transitional arrangements | full, outline, demolition-con-area | MAY | Rule: is a MUST if `bng-condition-applies` is `False` |
| bng-details | Biodiversity net gain details{} | Comprehensive details about biodiversity net gain assessment including pre-development value, habitat loss information, and supporting documentation | full, outline, demolition-con-area | MAY | Rule: is a MUST if `bng-condition-applies` is `True` |


**BNG exemption reason component**

field | name | description | required | notes
-- | -- | -- | -- | --
exemption-type | Exemption type | The type of biodiversity gain exemption from the bng-exemption-type enum | MUST | Select from the **bng-exemption-type** enum
reason | Reason | The reason the exemption applies to this proposal | MUST | 


**Biodiversity net gain details component**

field | name | description | required | notes
-- | -- | -- | -- | --
pre-development-date | Pre development date | Date of pre-development biodiversity value calculation, must align with application or justified earlier date | MUST | 
pre-development-biodiversity-value | Pre development biodiversity value | Calculated biodiversity value in Habitat Biodiversity Units | MUST | 
earlier-date-reason | Earlier date reason | Reason for using a pre-development date that is earlier than the application submission | MAY | 
habitat-loss-after-2020 | Habitat loss after 2020 | Indicates whether there has been degradation of onsite habitat(s) after 30 Jan 2020 | MAY | 
habitat-loss-details | Habitat loss details{} | Details of habitat loss or degradation events | MAY | Rule: is a MUST if `habitat-loss-after-2020` is `True`
metric-publication-date | Metric publication date | Publication date of the biodiversity metric tool used for calculations | MUST | 
irreplaceable-habitats | Irreplaceable habitats | Indicates whether the site contains any irreplaceable habitats | MUST | 
irreplaceable-habitats-details | Irreplaceable habitats details | Description and references for any irreplaceable habitats identified on the site | MAY | Rule: is a MUST if `irreplaceable-habitats` is `True`
supporting-documents | Supporting documents[]{} | References to supporting documents that have been uploaded with the application | MUST | 


**Habitat loss details component**

field | name | description | required | notes
-- | -- | -- | -- | --
loss-date | Loss date | Date the activity causing habitat loss or degradation occurred | MUST | 
pre-loss-biodiversity-value | Pre loss biodiversity value | Biodiversity value immediately before habitat loss or degradation occurred, measured in Habitat Biodiversity Units | MUST | 
supporting-evidence | Supporting evidence | Description or reference to supporting documents for habitat loss or degradation evidence | MAY | 


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- application-type == 'hh' REQUIRES only bng-exempt field
- bng-condition-applies == false REQUIRES bng-condition-exemption-reasons.length >= 1
- bng-condition-applies == true REQUIRES bng-details
- application-type == 'hh' RECOMMENDS bng-exempt == false
- bng-condition-exemption-reasons[].exemption-type must be from bng-exemption-type codelist
- bng-details.pre-development-date <= application-submission-date OR earlier-date-reason provided
- bng-details.habitat-loss-after-2020 == true REQUIRES bng-details.habitat-loss-details
- bng-details.irreplaceable-habitats == true REQUIRES bng-details.irreplaceable-habitats-details