# Biodiversity, geological and archaeological conservation

Assessment of potential impacts on protected species, important habitats, 
biodiversity features, geological features, and archaeological features


**Biodiversity, geological and archaeological conservation module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| protected-species-impact | Protected species impact | Where is there a likelihood of protected and priority species being affected? |  | MUST | Select from the **affected-area-type** enum |
| biodiversity-features-impact | Biodiversity features impact | Where is there a likelihood of important habitats or biodiversity features being affected? |  | MUST | Select from the **affected-area-type** enum |
| geological-features-impact | Geological features impact | Where is there a likelihood of features of geological conservation importance being affected? |  | MUST | Select from the **affected-area-type** enum |
| archaeological-features-impact | Archaeological features impact | Where is there a likelihood of features of archaeological conservation importance being affected? | extraction-oil-gas | MUST | Select from the **affected-area-type** enum |

**Validation rules**

- All impact assessments must use values from the affect-area codelist or 'no'
- Archaeological features impact is only required for extraction-oil-gas applications
- Impact assessments should be based on ecological surveys and site assessments