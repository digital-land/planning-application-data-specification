# Description of proposed works

Details of development plans such as extensions measurements or work specifications

**Description of proposed works module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposed-works-details | Proposed works details | Description of the proposed works including detailed explanation of the work |  | MUST |  |
| extension-depth | Extension depth | How far the extension extends beyond the rear wall, measured externally in metres |  | MUST |  |
| max-extension-height | Maximum extension height | Maximum height of the extension, measured externally from natural ground level in metres |  | MUST |  |
| eaves-height | Eaves height | Height at the eaves of the extension, measured externally from natural ground level in metres |  | MUST |  |

**Validation rules**

- extension-depth > 0 AND max-extension-height > 0 AND eaves-height > 0
- eaves-height <= max-extension-height
- extension-depth measurement taken from external face of existing rear wall
- max-extension-height and eaves-height measured from natural ground level
- proposed-works-details.length > 10