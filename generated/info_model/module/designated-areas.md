# Designated areas

Module for capturing information about designated areas that apply to a development site


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| designations | Designations[] | List of designated areas that apply to the site |  | MUST | Select from the **designation** enum |

**Validation rules**

- Multiple selections allowed from the designation codelist
- If none of the designated areas apply to the site, the array should be empty
- Each designation in the array must be unique (no duplicates)