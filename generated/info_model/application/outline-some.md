# Outline Planning Permission with Some Matters Reserved

Outline planning permission with some matters reserved

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Access and rights of way](#access-and-rights-of-way)
* [Biodiversity, geological and archaeological conservation](#biodiversity,-geological-and-archaeological-conservation)
* [Foul sewage disposal](#foul-sewage-disposal)
* [Hazardous substances](#hazardous-substances)
* [Materials](#materials)
* [Trade effluent](#trade-effluent)
* [Trees and hedges information](#trees-and-hedges-information)
* [Vehicle parking](#vehicle-parking)
* [Waste storage and collection](#waste-storage-and-collection)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |

## Access and rights of way

Information about changes to access arrangements and public rights of way


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | New or altered vehicle access | Is a new or altered vehicle access proposed to/from the public highway | MUST | Select from the **rights-of-way-answers** enum |
| new-altered-pedestrian | New or altered pedestrian access | Is a new or altered pedestrian access proposed to/from the public highway | MUST | Select from the **rights-of-way-answers** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY |  |


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- All fields must use values from rights-of-way-answers codelist
- If new-altered-vehicle is yes, details must be provided in highways module
- If change-right-of-way is yes, separate rights of way order may be needed
- If temp-right-of-way is yes, details of temporary diversions must be provided

## Biodiversity, geological and archaeological conservation

Assessment of potential impacts on protected species, important habitats, 
biodiversity features, geological features, and archaeological features


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| protected-species-impact | Protected species impact | Where is there a likelihood of protected and priority species being affected? | MUST | Select from the **affect-area** enum |
| biodiversity-features-impact | Biodiversity features impact | Where is there a likelihood of important habitats or biodiversity features being affected? | MUST | Select from the **affect-area** enum |
| geological-features-impact | Geological features impact | Where is there a likelihood of features of geological conservation importance being affected? | MUST | Select from the **affect-area** enum |

**Validation rules**

- All impact assessments must use values from the affect-area codelist or 'no'
- Archaeological features impact is only required for extraction-oil-gas applications
- Impact assessments should be based on ecological surveys and site assessments

## Foul sewage disposal

Information about foul sewage disposal methods and connection to existing 
drainage systems for development proposals


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| has-new-disposal-arrangements | Has new disposal arrangements | Does the proposal include any new foul sewage disposal arrangments | MUST |  |
| foul-sewage-disposal-types | Foul sewage disposal types[] | List of ways foul sewage will be disposed of | MAY | Select from the **foul-sewage-disposal-type** enum |
| produce-foul-sewage | Produce foul sewage | Whether the proposed development will produce any foul sewage | MUST |  |
| connect-to-drainage-system | Connect to drainage system | Whether the proposal needs to connect to the existing drainage system | MUST |  |
| drainage-system-details | Drainage system details | Details of the drawings/plans that show the existing drainage system | MAY |  |

**Validation rules**

- if connect-to-drainage-system == true then drainage-system-details is required
- if application-type includes 'extraction-oil-gas' then drainage-system-details is required

## Hazardous substances

Information about hazardous substances involved in the proposal,
including substance types, quantities, and consent requirements


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| involves-hazardous-substances | Involves hazardous substances | Indicates if hazardous substances are involved in the proposal | MUST | Select from the **yes-no-not-applicable** enum |
| substance-types | Substance types[]{} | List of hazardous substances and their quantities | MAY | Rule: is a MUST if `involves-hazardous-substances` is `yes` |
| hazardous-sub-consent-req | Hazardous substance consent required | Does the proposal involve the use or storage of any substances requiring hazardous substances consent | MUST |  |
| hazardous-sub-consent-details | Hazardous substance consent details | Details of hazardous substance consent requirements | MAY | Rule: is a MUST if `hazardous-sub-consent-req` is `True` |


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

## Materials

Information about the materials used in the development, including both existing and proposed materials


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| building-elements | Building elements[]{} | Details of materials for a specific building element such as walls, roof, windows or doors | MUST |  |
| additional-material-information | Additional material information | Additional context or details about the materials to be used in the development | MUST |  |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY | Rule: is a MUST if `additional-material-information` is `True` |


**Building element model**

field | name | description | required | notes
-- | -- | -- | -- | --
building-element-type | Building element type | The part of building the materials relate to, such as walls, roofs, windows, or doors | MUST | Select from the **building-element-type** enum
existing-materials | Existing materials | Description of the materials currently used for this building element | MAY | 
proposed-materials | Proposed materials | Description of the materials proposed for this building element as part of the development | MAY | 
materials-not-applicable | Materials not applicable | Indicates this building element is not relevant to the application | MAY | 
materials-not-known | Materials not known | Indicates the materials for this building element are not yet known | MAY | 


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- Each building-element must have a unique building-element-type
- At least one of: existing-materials, proposed-materials, materials-not-applicable or materials-not-known must be provided for each building-element
- materials-not-applicable cannot be true if existing-materials or proposed-materials is provided
- materials-not-known cannot be true if existing-materials or proposed-materials is provided
- supporting-documents must reference valid documents in the application

## Trade effluent

Information about the disposal of trade effluents or waste, including whether 
disposal is required and details about the nature, volume and means of disposal


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-disposal-required | Disposal required | Does the proposal involve the disposal of trade effluents or waste (true/false) | MUST |  |
| description | Description | describe the nature, volume and means of disposal of trade effluents or waste | MAY | Rule: is a MUST if `disposal-required` is `True` |

**Validation rules**

- description is required when disposal-required is true
- Module applies to full, extraction-oil-gas, and outline application types

## Trees and hedges information

Information about trees and hedges on or adjacent to the development site, including any that pose risks or need to be removed


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |

**Validation rules**

- falling-trees-document reference must match a document in application.documents
- tree-removal-plan reference must match a document in application.documents

## Vehicle parking

Detailed information about parking spaces by vehicle type, including existing 
and proposed counts with net change calculations


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| parking-spaces | Parking spaces[]{} | Array of parking space information by vehicle type | MUST |  |


**Parking space model**

field | name | description | required | notes
-- | -- | -- | -- | --
parking-space-type | Parking space type | Type of parking space or vehicle type | MUST | Select from the **parking-space-type** enum
vehicle-type-other | Vehicle type other | Vehicle type when parking space type is 'other' | MAY | Rule: is a MUST if `parking-space-type` is `other`
total-existing | Total existing | Total number of existing parking spaces | MUST | 
total-proposed | Total proposed | Total number of proposed parking spaces | MUST | 
unknown-proposed | Unknown proposed | If proposed parking spaces is unknown | MAY | 
difference-in-spaces | Difference in spaces | Net change in parking spaces (proposed minus existing) | MUST | 

**Validation rules**

- if parking-space-type == 'other' then vehicle-type-other is required
- total-existing >= 0 AND total-proposed >= 0 AND (unknown-proposed is empty OR unknown-proposed >= 0)
- difference-in-spaces == (total-proposed - total-existing)

## Waste storage and collection

Information about waste storage and recycling arrangements for developments, 
including whether waste storage areas are needed and details of recycling provisions


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| waste-storage-area-details | Waste storage area details | Details of the waste storage area including location, size, design and access arrangements | MAY |  |
| separate-recycling-arrangements-details | Separate recycling arrangements details | Details of the recycling arrangements including types of materials, collection methods and storage facilities | MAY |  |

**Validation rules**

- waste-storage-area-details must be provided when needs-waste-storage-area is true
- separate-recycling-arrangements-details must be provided when separate-recycling-arrangements is true

## Required codelists

This are the codelist required to support this specification:

- parking-space-type
- hazardous-sub-type
- building-element-type