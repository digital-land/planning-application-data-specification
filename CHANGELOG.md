
<a name="v0.1.43"></a>
## [v0.1.43](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.42.1...v0.1.43) (2026-01-07)

Add integrity checks for datasets, needs and justification records

### ⚒️ Tooling

* correct error message printing from fields integrity checks (commit [1cbdc14](https://github.com/digital-land/planning-application-data-specification/commit/1cbdc14cca244eb92c7edf42464dc971c61e339e))
* add integrity checks for justification records (commit [945f713](https://github.com/digital-land/planning-application-data-specification/commit/945f7139b4d766a686d31c8e081f1629807d50a9))
* add integrity checks for needs (commit [4087820](https://github.com/digital-land/planning-application-data-specification/commit/40878201356e05da3e000757cea5bda8a18a607d))
* give error and warning msgs colours for easier interpretation (commit [23a05e7](https://github.com/digital-land/planning-application-data-specification/commit/23a05e71b1b34157eeb3c7ed1462c6c720a25373))
* add integrity checks for dataset definitions (commit [adc96e5](https://github.com/digital-land/planning-application-data-specification/commit/adc96e5a51132c96b688aaac50bcf7cffc8038c6))

### 𝌭 Model changes

* add application-types field to planning-application dataset (commit [3f63530](https://github.com/digital-land/planning-application-data-specification/commit/3f635308ffecd0641f47b577192701306e884140))
* add routes to access decision notice to decision dataset (commit [b084d1b](https://github.com/digital-land/planning-application-data-specification/commit/b084d1bbf2779f7f04d8fd529d69132f4a944739))
* add description field to planning application records (commit [d817496](https://github.com/digital-land/planning-application-data-specification/commit/d817496ce5c3bdedf0ba4f134d4d165c8df86f45))
* add planning-officer-recommendation field to decision dataset (commit [cd22d8b](https://github.com/digital-land/planning-application-data-specification/commit/cd22d8b4932651550b22ad57752b28d8c07ec871))
* add decision-maker field to decision dataset (commit [f598ca5](https://github.com/digital-land/planning-application-data-specification/commit/f598ca5e11a200a302ff857c1b2a8a83d2b750a6))
* add organisation field to decision dataset (commit [d00f3be](https://github.com/digital-land/planning-application-data-specification/commit/d00f3be0ba400a704a45844a1a4f6f200d78e470))
* add received-date field to planning application records (commit [59345f2](https://github.com/digital-land/planning-application-data-specification/commit/59345f2021a37c9688336ef6ae576c678d5a8ae7))
* add decision-date field to decision dataset (commit [9aebe12](https://github.com/digital-land/planning-application-data-specification/commit/9aebe12d95bc22070b0910c88f5cf9343820b6af))

### 🐛 Bug Fixes

* add notes attr to dataset schemas (commit [148b55c](https://github.com/digital-land/planning-application-data-specification/commit/148b55c7c244758a189acbf82b66478368f93df4))
* rename needs files to correct format (commit [030b051](https://github.com/digital-land/planning-application-data-specification/commit/030b051b69becea706a1724d2e2ad1f2c7f3995c))
* pointer to existing need (commit [1de1d3b](https://github.com/digital-land/planning-application-data-specification/commit/1de1d3b43878e5a426fe3ab4fba87dd5849b86ec))
* attr should be name not title (commit [c8109f1](https://github.com/digital-land/planning-application-data-specification/commit/c8109f141d1937c865f6e56d7db54c4bcd1a0751))
* in need records variations should be a list of need ids (commit [58b7b31](https://github.com/digital-land/planning-application-data-specification/commit/58b7b314cce67e95e2e637e1e252fd3cf306154d))
* add missing github disucssion numbers to codelist schemas (commit [16350c8](https://github.com/digital-land/planning-application-data-specification/commit/16350c870f06b61683cdc73d08c383afb445ecbe))

### 📚 Documentation

* add just-0008 record for decisions in a period (commit [7f98527](https://github.com/digital-land/planning-application-data-specification/commit/7f98527d42f729b708c792115472783716e9e274))
* add just-0005 for satisfying volume need (dd-need-031) (commit [e059fef](https://github.com/digital-land/planning-application-data-specification/commit/e059fefb847c84412ba09653d3939a47bf5ac4ee))
* tweak description for just-0004 (commit [389a9b0](https://github.com/digital-land/planning-application-data-specification/commit/389a9b0b94b97ed3a8d7fa9b64d83e18d1f99c03))


<a name="v0.1.42.1"></a>
## [v0.1.42.1](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.42...v0.1.42.1) (2026-01-06)

Add missing field to decision dataset draft

### 𝌭 Model changes

* add application-types field to planning-application dataset (commit [f33a79d](https://github.com/digital-land/planning-application-data-specification/commit/f33a79d59c921d54ddf601ea6878adcc246747ee))


<a name="v0.1.42"></a>
## [v0.1.42](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.41...v0.1.42) (2026-01-06)

Initial draft of decision dataset

### 𝌭 Model changes

* add routes to access decision notice to decision dataset (commit [621a9d9](https://github.com/digital-land/planning-application-data-specification/commit/621a9d982b084d4cb41661dcc0b09a5a72a60058))
* add description field to planning application records (commit [bdb900e](https://github.com/digital-land/planning-application-data-specification/commit/bdb900ec6b92cdc491dab65a3582ee2da027a296))
* add planning-officer-recommendation field to decision dataset (commit [32efccd](https://github.com/digital-land/planning-application-data-specification/commit/32efccd99b170f05e44f1ec98c59be0bcbfe1a52))
* add decision-maker field to decision dataset (commit [4b76484](https://github.com/digital-land/planning-application-data-specification/commit/4b76484b9beff0639a197b4e927a8d38b5819c49))
* add organisation field to decision dataset (commit [1c85f91](https://github.com/digital-land/planning-application-data-specification/commit/1c85f916b0a0c6cc7fec6cb813fb85b680c6ffcd))
* add received-date field to planning application records (commit [1622599](https://github.com/digital-land/planning-application-data-specification/commit/16225998062e133c34a67da77126815467aaf763))
* add decision-date field to decision dataset (commit [a80a120](https://github.com/digital-land/planning-application-data-specification/commit/a80a12049e089a58d3ea94a3086e5175adf7dc92))
* add documentation and document urls to planning application dataset (commit [eb2c149](https://github.com/digital-land/planning-application-data-specification/commit/eb2c149dcd2b216c47d0a45b283c262b8647213f))

### 📚 Documentation

* add just-0008 record for decisions in a period (commit [828edf9](https://github.com/digital-land/planning-application-data-specification/commit/828edf9abf957782f158a0b228d44e27cc5a2a5b))
* add just-0005 for satisfying volume need (dd-need-031) (commit [8111a75](https://github.com/digital-land/planning-application-data-specification/commit/8111a753804e32a63802ff42fe80518553e2d022))
* tweak description for just-0004 (commit [5e9077a](https://github.com/digital-land/planning-application-data-specification/commit/5e9077a079be8b8b66c229fb37cc78269656ced5))
* add descriptions to document and documentation fields in planning application dataset (commit [27131ee](https://github.com/digital-land/planning-application-data-specification/commit/27131eebb7f21d6a98e3bc0e7954567204ec8d8c))
* add need dd-need-032 (commit [ff4ff24](https://github.com/digital-land/planning-application-data-specification/commit/ff4ff24e770a740c393fddada0f4282afcf2387b))
* add series of identified needs around decision stage data (commit [fd6edd6](https://github.com/digital-land/planning-application-data-specification/commit/fd6edd6011881471cb2105a3df2f2bcdc98bd61c))


<a name="v0.1.41"></a>
## [v0.1.41](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.40...v0.1.41) (2025-12-19)

Align spec with decision on submitting documents

### 𝌭 Model changes

* remove checksum field from file component, no longer needed (commit [93596f7](https://github.com/digital-land/planning-application-data-specification/commit/93596f70b883d4b5abe3b775b5ff4ad0ba3a09c7))
* remove option to link to a file instead of including it, see decision 0003-how-to-provide-documents-with-submission (commit [563b0bf](https://github.com/digital-land/planning-application-data-specification/commit/563b0bf3483b51287a73b97e6b6a38eb6ecc9f92))

### 📚 Documentation

* add need dd-need-010 (commit [c2519d9](https://github.com/digital-land/planning-application-data-specification/commit/c2519d9ce573bfa5c23c11e3be8e1de93850f29b))
* add need-ps-004 (commit [83ad2ec](https://github.com/digital-land/planning-application-data-specification/commit/83ad2ec906e81536098f7b47168f1bc90ba4ec49))
* add dd-need-017 (commit [d223ddd](https://github.com/digital-land/planning-application-data-specification/commit/d223dddaf6203a456dd019631b157b4a671f5c15))
* update dd-need-014 (commit [cef91d7](https://github.com/digital-land/planning-application-data-specification/commit/cef91d7623ff0eaea24721a1c05a8dd68e4b242b))
* add dd-need031 (commit [b06f85e](https://github.com/digital-land/planning-application-data-specification/commit/b06f85eaf5bd4b37c7fa631c2a1fff2dc4a499dc))


<a name="v0.1.40"></a>
## [v0.1.40](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.38...v0.1.40) (2025-12-19)

Begin adding the working draft decision stage specification to repository

### ⚒️ Tooling

* handle not allowing additional properties, should output false: (commit [bddbc22](https://github.com/digital-land/planning-application-data-specification/commit/bddbc22a43dc2fbf7b7ea1d726a66465f0857482))

### 𝌭 Model changes

* Clarify dataset intent and relationships with semantic metadata (commit [e9c5a03](https://github.com/digital-land/planning-application-data-specification/commit/e9c5a03a5ae05f111539ede278a6d0f57426fe7f))
* add skeleton definition of planning application dataset (commit [397c0de](https://github.com/digital-land/planning-application-data-specification/commit/397c0ded4fbcc3096816a83fa135f1e1ae3282a6))
* add planning-application and decision fields to decision dataset (commit [c7601a8](https://github.com/digital-land/planning-application-data-specification/commit/c7601a81061312e03dc33238c7987067bbf3076e))
* add a skeleton dataset definition for the decision dataset (commit [2439d7b](https://github.com/digital-land/planning-application-data-specification/commit/2439d7bc2fabfac4d52ca9115d65aec8dc90a290))
* add allow-additional-properties to all other application types (commit [07863d4](https://github.com/digital-land/planning-application-data-specification/commit/07863d4104c3e538752a8bcda5332e3d2793dd82))
* add allow-additional-properties to outline apps (commit [5ad93cc](https://github.com/digital-land/planning-application-data-specification/commit/5ad93cc70bda2b7bd776aca6a82a6bab7326330e))

### 🐛 Bug Fixes

* date on design decision record (commit [35eeb23](https://github.com/digital-land/planning-application-data-specification/commit/35eeb23ce59c4e34a82a3e05eeeb16b7904621a1))
* mistakes in first dataset and justification files (commit [9c5ffdb](https://github.com/digital-land/planning-application-data-specification/commit/9c5ffdb9cfa247a0f32329227f55df65821107b3))
* remove redundant info models for oil and gas app (commit [7247fc3](https://github.com/digital-land/planning-application-data-specification/commit/7247fc3638474527616144d0a23e32bed2304d72))
* remove redundant info models for outline apps (commit [48a7e2b](https://github.com/digital-land/planning-application-data-specification/commit/48a7e2b5d2167d46993678d1329b825078731fa9))

### 📚 Documentation

* add need dd-need-010 (commit [c4d36b6](https://github.com/digital-land/planning-application-data-specification/commit/c4d36b6f6d4170c6b70f88bb9891debd6b4685b6))
* add need-ps-004 (commit [480175e](https://github.com/digital-land/planning-application-data-specification/commit/480175e7396364778c5a10cdc038a2c1eda442e0))
* add dd-need-017 (commit [8ee2411](https://github.com/digital-land/planning-application-data-specification/commit/8ee24112dc8221d1dd6dc36bc9ee77aebac9c2bf))
* update dd-need-014 (commit [5c8e4ec](https://github.com/digital-land/planning-application-data-specification/commit/5c8e4ec051221f5a397c5e9f02623d4f651caf29))
* add dd-need031 (commit [0bf88ab](https://github.com/digital-land/planning-application-data-specification/commit/0bf88abecf5403f1c3ce3c5e5a839df544b1b218))
* update just-0001 to make it more of a universal rule to be applied across datasets (commit [b62c213](https://github.com/digital-land/planning-application-data-specification/commit/b62c213f5cf8e820fd6eeca1884708f13be21ca5))
* add design decision record for calling dataset planning-application (commit [2a044bc](https://github.com/digital-land/planning-application-data-specification/commit/2a044bc48b0c8f766aff3cc968c0b957f279c1d2))
* add justication record for dd-need-033 and dd-need-034 (commit [58e0cd6](https://github.com/digital-land/planning-application-data-specification/commit/58e0cd69583ac530da4f2a14e4150f461180f5f7))
* add a couple of needs (commit [3907d8d](https://github.com/digital-land/planning-application-data-specification/commit/3907d8df11f85e5c6eb8a3bcbe432699e276c3a0))
* add design decision record about submitting documents with applications (commit [3875017](https://github.com/digital-land/planning-application-data-specification/commit/3875017f36d62290ddeacc7cba54cae8f0e3e67d))
* update specification folder readme based on feedback (commit [1a4c5dc](https://github.com/digital-land/planning-application-data-specification/commit/1a4c5dc6118db50aba92996183c8e93e1125d239))
* document what need and justification records are (commit [9c68d9b](https://github.com/digital-land/planning-application-data-specification/commit/9c68d9bab17b3dc0d424699a3a9c2ce9c9483749))
* log how dd-need-048 is satisfied (commit [6987161](https://github.com/digital-land/planning-application-data-specification/commit/6987161d39d4cb59ef2c2a5492358b4be1f746fb))
* capture how data-need-001 is satisfied (commit [bec330a](https://github.com/digital-land/planning-application-data-specification/commit/bec330a0574642e6c599502eb0b3415e828730b9))
* document how the data model is structured (commit [77017a2](https://github.com/digital-land/planning-application-data-specification/commit/77017a2e5a1fb1b8d1c9811c4e16ee4998f6ea1b))


<a name="v0.1.38"></a>
## [v0.1.38](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.37...v0.1.38) (2025-12-16)

Be explicit about allowing additional properties or not

### ⚒️ Tooling

* handle not allowing additional properties, should output false: (commit [11421cd](https://github.com/digital-land/planning-application-data-specification/commit/11421cd0c3bab7976450d5d19fa2ad9cfc81a5d7))
* update JSON schema generator to handle allow-additional-properties attr (commit [b1b5d0f](https://github.com/digital-land/planning-application-data-specification/commit/b1b5d0ffc53c0ecd6b80680ee06aee7465f9e2ca))
* count number of fields of a module for comparison (commit [da2ed08](https://github.com/digital-land/planning-application-data-specification/commit/da2ed0881115420b4b732b89815479605b369207))
* fix generating application fields section (commit [7e9f2d6](https://github.com/digital-land/planning-application-data-specification/commit/7e9f2d66b397c73d34e950be1338684f13f61bb2))

### 𝌭 Model changes

* add allow-additional-properties to all other application types (commit [407a809](https://github.com/digital-land/planning-application-data-specification/commit/407a8095819948ea3dd0eb4b038ee474185d6e7b))
* add allow-additional-properties to outline apps (commit [e0960d7](https://github.com/digital-land/planning-application-data-specification/commit/e0960d75501a357aac2b2fe779bf85fbb39b9616))
* add allow-additional-properties: true to full application definition (commit [7b4f58d](https://github.com/digital-land/planning-application-data-specification/commit/7b4f58d5b2755d2e510de9edac5a9cf9566d2c03))
* list permission types that make related-permission related required (commit [c35150f](https://github.com/digital-land/planning-application-data-specification/commit/c35150f7c5f803a9eb927b573a7ab9566ab66de4))
* add missing permission type module and use in extract oil gas application (commit [7775896](https://github.com/digital-land/planning-application-data-specification/commit/77758962fc6766ae1225f01fed539ebcad5ca046))

### 🐛 Bug Fixes

* remove redundant info models for oil and gas app (commit [c874330](https://github.com/digital-land/planning-application-data-specification/commit/c874330e3e86ee28f5293b2cab2ce40309f3904b))
* remove redundant info models for outline apps (commit [e310729](https://github.com/digital-land/planning-application-data-specification/commit/e310729597b35e787b07ad2c6d432574e9a943f7))
* typo in documentation (commit [2932ccd](https://github.com/digital-land/planning-application-data-specification/commit/2932ccd18d28919cdab7b71009f3ec2a48b934c9))

### 📚 Documentation

* add decision record for allowing additional properties (commit [eea1c30](https://github.com/digital-land/planning-application-data-specification/commit/eea1c30d10c0c9c7ae2582c6dab0e1f990f73e72))
* document the differences between submission and decision specifications (commit [1aadbbc](https://github.com/digital-land/planning-application-data-specification/commit/1aadbbc684f6f6379c966c37fffa9752eb514bfd))


<a name="v0.1.37"></a>
## [v0.1.37](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.36...v0.1.37) (2025-12-05)

Add missing nmodule

### 𝌭 Model changes

* list permission types that make related-permission related required (commit [cc7718e](https://github.com/digital-land/planning-application-data-specification/commit/cc7718e196a83db1c79a719cdeb5c66e980db035))
* add missing permission type module and use in extract oil gas application (commit [6ca7cbc](https://github.com/digital-land/planning-application-data-specification/commit/6ca7cbcc2202b13e09897df6477634715949582d))


<a name="v0.1.36"></a>
## [v0.1.36](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.35...v0.1.36) (2025-11-24)

Responding to feedback

### ⚒️ Tooling

* build a codelist that combines local-authorities, national-park-authorities and development corporations (commit [8459b7c](https://github.com/digital-land/planning-application-data-specification/commit/8459b7cce4b57e83700d14be38760bcd6dbdf7ef))
* expand cli to find instances of fields (commit [cea826d](https://github.com/digital-land/planning-application-data-specification/commit/cea826d24b246ecabd42f6c6278f8f879a517a7c))
* commandline interface to find which app types use a module (commit [f8071ac](https://github.com/digital-land/planning-application-data-specification/commit/f8071acb136df84849d03c1aa895f06da0f43311))

### 𝌭 Model changes

* remove unused application module (commit [5ebf1d1](https://github.com/digital-land/planning-application-data-specification/commit/5ebf1d124ead71a3e5ac37de5f12e7c9617a0117))
* add end-date to unused application module (commit [89802de](https://github.com/digital-land/planning-application-data-specification/commit/89802de04b198b1ec5d5935c928dda6b48d060ec))
* add built planning-authority codelist (commit [e171ba8](https://github.com/digital-land/planning-application-data-specification/commit/e171ba8db2146d52da394464592fbda2da707c11))
* define planning-authority codelist needed for planning-authority field (commit [56ff295](https://github.com/digital-land/planning-application-data-specification/commit/56ff295a0aa22634c8eadd08491363058a2797cb))
* add missing description of proposal for work to lb for lawful dev cert module (commit [11fa70a](https://github.com/digital-land/planning-application-data-specification/commit/11fa70a59721ce5e0212827b272994efb89ed62a))
* add notes to technical details consent application (commit [3e88183](https://github.com/digital-land/planning-application-data-specification/commit/3e88183b40d0548355ae3a12cfad6ac5ba78a769))
* add planning-requirement codelist (commit [879e056](https://github.com/digital-land/planning-application-data-specification/commit/879e056b5616d0df6052469db07dbaacfaefd3c0))

### 🐛 Bug Fixes

* add rules stating modules referencing documents must refer to documents in application.documents (commit [c60bf1d](https://github.com/digital-land/planning-application-data-specification/commit/c60bf1d0c2fb0b616751866206b9555dfc59efff))
* update ldc-proposed-work-lb app to use desc-proposed-works-lb-ldc module (commit [30972d2](https://github.com/digital-land/planning-application-data-specification/commit/30972d27e844ac0aaa82513d017510865d67aed9))
* use the right interest in details or land modules for advertising and ldc applications (commit [f03307f](https://github.com/digital-land/planning-application-data-specification/commit/f03307f9a34b27ea7b67ce4b1d53f112c9f7793e))
* correct datatype to date on -date fields (commit [2ddcd4c](https://github.com/digital-land/planning-application-data-specification/commit/2ddcd4c00a6169707d2ea42701deaafd63db40be))

### 👷‍♀️ Application changes

* add schema for technical details consent application (commit [aa59179](https://github.com/digital-land/planning-application-data-specification/commit/aa59179a78d7c8e79a30a03dfaa06b1dff4bcc88))

### 📚 Documentation

* split application types by priority -> those that affect housing delivery (commit [59a7406](https://github.com/digital-land/planning-application-data-specification/commit/59a74062c24e9a34bc55dab41a0a8edee3dfb827))
* add technical details consent to list of applications in scope (commit [45e61c2](https://github.com/digital-land/planning-application-data-specification/commit/45e61c2dcaebfa6d420a9c1125f8209a88ca9609))
* add some documentation about the work into decision data (commit [fe5b4fe](https://github.com/digital-land/planning-application-data-specification/commit/fe5b4fe2ce2ca1894bc9bd67d1cda5e932471364))


<a name="v0.1.35"></a>
## [v0.1.35](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.34...v0.1.35) (2025-10-30)

Fixes and enhancements

### ⚒️ Tooling

* increase flexibility of where codelist sources can reside (commit [35816cc](https://github.com/digital-land/planning-application-data-specification/commit/35816cc586ecd78fc36551c6e422b2e211ffa9e4))
* generate version of spreadsheet output with references (commit [df7b194](https://github.com/digital-land/planning-application-data-specification/commit/df7b194ea4a5b7fc7efa7804d2bf04f77a38f43b))

### 𝌭 Model changes

* add use-class-accommodation codelist, used in room details component (commit [c0b2775](https://github.com/digital-land/planning-application-data-specification/commit/c0b2775b2e1aa2ddec9a01a6ae6963d9102c6b52))
* add use-class codelist (commit [73e8289](https://github.com/digital-land/planning-application-data-specification/commit/73e82898b81289d232c551f7138aa0cb0fdf4536))

### 🐛 Bug Fixes

* add missing application-subtype codelist (commit [dd72ae9](https://github.com/digital-land/planning-application-data-specification/commit/dd72ae9af8de960bae28c5cfb367c18c15bdae11))
* add missing source url for application-type codelist (commit [059b30f](https://github.com/digital-land/planning-application-data-specification/commit/059b30fbba944f2887a2935d15be6f5ed0331b01))
* rename use-class field to use-class-accommodation to more accurately reflect purpose' (commit [a15399a](https://github.com/digital-land/planning-application-data-specification/commit/a15399aa546294e4f0cecb6106945f86e0041dc8))
* required-of condition should have value attr (commit [aceb32e](https://github.com/digital-land/planning-application-data-specification/commit/aceb32e058d279dc32ee01df01449e5a37036f41))
* github workflow ci issues (commit [88ec0aa](https://github.com/digital-land/planning-application-data-specification/commit/88ec0aa7201115764c4d4893ce22d208deb417c1))


<a name="v0.1.34"></a>
## [v0.1.34](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.33...v0.1.34) (2025-10-27)

Tool tweaks and documentation

### ⚒️ Tooling

* add make target to move documentation to generated folder (commit [a948479](https://github.com/digital-land/planning-application-data-specification/commit/a948479cb665b7928764917195a377e4b2295fe3))
* add documentation for outputs generated from the model (commit [8e13889](https://github.com/digital-land/planning-application-data-specification/commit/8e1388934a40be5d3e199d19d1f16cbc112a362a))

### 𝌭 Model changes

* add specific description to name field in document component (commit [b090b11](https://github.com/digital-land/planning-application-data-specification/commit/b090b11bc5b05db0aac8bf2336a607312faace1c))
* update legislation field to legislation-urls (commit [57a64e9](https://github.com/digital-land/planning-application-data-specification/commit/57a64e98828e19116bdea29a8fc0b1d54b96df56))

### 🐛 Bug Fixes

* issues with bullet lists in documentation (commit [5762182](https://github.com/digital-land/planning-application-data-specification/commit/57621827326a2b08ccbc5e9161be60e3e830134a))
* extra column in one row of planning application types dataset (commit [ea82e2c](https://github.com/digital-land/planning-application-data-specification/commit/ea82e2ccf533618d5b68640b983fab5c14ddfbca))

### 👷‍♀️ Application changes

* add missing description for extraction of oil and gas applications (commit [dc4cbf7](https://github.com/digital-land/planning-application-data-specification/commit/dc4cbf7bcf0080432c7848da023b18aa4ea63e1c))

### 📚 Documentation

* add links to the corresponding output code and folderS (commit [1969c6f](https://github.com/digital-land/planning-application-data-specification/commit/1969c6f69aa314071021628ebbe83e407e0d8dc1))


<a name="v0.1.33"></a>
## [v0.1.33](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.32...v0.1.33) (2025-09-24)

Generate JSON schemas

### ⚒️ Tooling

* add func to return applications where a module is used (commit [0c4de6d](https://github.com/digital-land/planning-application-data-specification/commit/0c4de6d6c167e0542b4d971cacdcb01c71f53e20))
* ran black formatting (commit [04be585](https://github.com/digital-land/planning-application-data-specification/commit/04be585b75e8867807bfd8a3c5f4ea812eca4c9a))
* Parameterize json schema validation unit test test_valid_application (commit [022e701](https://github.com/digital-land/planning-application-data-specification/commit/022e7018e9d29b574854b9ca2e86b01e0ba183db))
* Refactored to move mapping helpers to own module. Fixed bug in mapping incorrectly or'ing multiple required lists, when in should have been and'ing (commit [ddf32f6](https://github.com/digital-land/planning-application-data-specification/commit/ddf32f62cfeff72fffc61071b835d4bb18736b42))
* update example HH payload to use correct organisation reference (commit [ef56589](https://github.com/digital-land/planning-application-data-specification/commit/ef5658976b7657325beb4e85ff07ae6e18522169))
* check fields referenced in required-if statements exist (commit [e60e87a](https://github.com/digital-land/planning-application-data-specification/commit/e60e87a1bac51d89f5e5926dd304dccc7e44f0a9))

### 𝌭 Model changes

* tweak 2 modules descriptions (commit [ffaeade](https://github.com/digital-land/planning-application-data-specification/commit/ffaeade3c3b80e6f1718cf086c73937110b9cc69))
* rename field from additional-material-information to providing-additional-material-information (commit [5de1b49](https://github.com/digital-land/planning-application-data-specification/commit/5de1b49e99f3c6e773ae3b617de9226144890332))
* add minimal sample hh payload (commit [a44e2ee](https://github.com/digital-land/planning-application-data-specification/commit/a44e2eea3b9608a090d2f8e77c0e9bd627f547bc))

### 🐛 Bug Fixes

* Fixed incorrect property type in example and added required supported-documents property (commit [488d43b](https://github.com/digital-land/planning-application-data-specification/commit/488d43b42564d3097a8a7c3717098b0b976834e4))
* supporting documents only needed in access rights of way module if one of the other fields is true. Corrected in sample payload (commit [05b4940](https://github.com/digital-land/planning-application-data-specification/commit/05b4940e8022d5c542048013934a908618be541e))
* Removed redundant allOf in cases where only one condition to evaluate. Updated example payload to use correct datatypes. Updated conftest to load new example - note still fails test (commit [db333dc](https://github.com/digital-land/planning-application-data-specification/commit/db333dcfbc533f26a14b29d26b8fef3601070c5b))
* issue with circular imports (commit [da4994f](https://github.com/digital-land/planning-application-data-specification/commit/da4994ffaaca8104e441969fce45fe14df9f7667))
* JSON schema generation now works for appliction sub-types. Extented load_spefication_model to resolve inheritance hierachies (commit [c7edc6d](https://github.com/digital-land/planning-application-data-specification/commit/c7edc6d9cce8d850087b47c2f3ec5650da1ec5ad))
* List of required properties for application was not listing all modules (commit [1563367](https://github.com/digital-land/planning-application-data-specification/commit/1563367fbaa1199b1dd5c6ec06e8215ceb6de771))

### 👷‍♀️ Application changes

* add missing spec for extraction of oil and gas application (commit [78262cf](https://github.com/digital-land/planning-application-data-specification/commit/78262cff5f12902987965076be3ae9adaece20a5))

### 📚 Documentation

* Added example script is done (commit [0b7e2b9](https://github.com/digital-land/planning-application-data-specification/commit/0b7e2b98c496bab96b5b9c0950491fa85a82f64a))
* Added notion of using tags to denote schema version in url. (commit [92f9282](https://github.com/digital-land/planning-application-data-specification/commit/92f9282cd8886e29d83d6ef6fa820dd629213169))
* Clarify validation steps (commit [9808d66](https://github.com/digital-land/planning-application-data-specification/commit/9808d666f9d79d984eb9ef3b6c9b6e6533bb17bb))
* Update json-schema-generation.md (commit [bbb3d43](https://github.com/digital-land/planning-application-data-specification/commit/bbb3d4318f973aab003df11c2806bc4e4c0a56ab))
* Added note about need for sample applications (commit [5f21773](https://github.com/digital-land/planning-application-data-specification/commit/5f217738dec236f8181c00b6a5497cf21b251d3a))
* Reworked the conditional logic mapping section of json schema generation to be clearer (commit [145ee2f](https://github.com/digital-land/planning-application-data-specification/commit/145ee2fc3914c26c371cb515f390acdcbd992ac5))
* Update future considerations (commit [009d334](https://github.com/digital-land/planning-application-data-specification/commit/009d33424a7775210d0599ecb3c9423c77f4f335))
* Clarify code comments Add future considerations to readme. Correct example hh application json (commit [ce688fd](https://github.com/digital-land/planning-application-data-specification/commit/ce688fd82c7a9a5e99c7c833bb36c550cfa09c94))


<a name="v0.1.32"></a>
## [v0.1.32](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.31...v0.1.32) (2025-09-12)

batch updates and descriptions

### ⚒️ Tooling

* to batch update application or module definitions (commit [e9690a3](https://github.com/digital-land/planning-application-data-specification/commit/e9690a387c9d89c561e90c71aeef39ff1ccd1f00))

### 𝌭 Model changes

* rework module descriptions (commit [a939279](https://github.com/digital-land/planning-application-data-specification/commit/a939279276875e3fc65ceb08999be8bebee819fe))

### 👷‍♀️ Application changes

* add synonyms for Approval of details reserved by condition applications (commit [19ab81f](https://github.com/digital-land/planning-application-data-specification/commit/19ab81f0315584fee279bf82241c4436aea1466c))
* tweak so application names based on feedback (commit [4b9ffae](https://github.com/digital-land/planning-application-data-specification/commit/4b9ffaeb8814ad0ac7b605942849da4e976ddc0d))
* update description for lbc and demolition in conservation area applications (commit [0ee8358](https://github.com/digital-land/planning-application-data-specification/commit/0ee8358a68820a84ed9c815d05053b7cd0fe66a9))


<a name="v0.1.31"></a>
## [v0.1.31](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.30...v0.1.31) (2025-09-10)

update the list of application types

### ⚒️ Tooling

* compare complete list of application types with those defined in the specification(s) (commit [7ecd124](https://github.com/digital-land/planning-application-data-specification/commit/7ecd124d4ceee65da197fe34a528178da5d81ec2))

### 𝌭 Model changes

* tweaks to application type data based on feedback (commit [368b471](https://github.com/digital-land/planning-application-data-specification/commit/368b471a7b962135c95f4b9a700d935a5a867be5))
* add declarative version of permission-type module (commit [2b622f7](https://github.com/digital-land/planning-application-data-specification/commit/2b622f7e7cdd2da1805ba3001eb283bc8fd313d2))

### 🐛 Bug Fixes

* mv schemas for planning requirement datasets to docs (commit [6aaf78e](https://github.com/digital-land/planning-application-data-specification/commit/6aaf78edbfbd973d515e414e89d2d14e60206585))
* remove compiled application specifications from specification/application folder: (commit [3ebd6e0](https://github.com/digital-land/planning-application-data-specification/commit/3ebd6e0266de7e88bbdfc4a308803328c3829f10))
* remove rest of replaced module info models (commit [4fe142f](https://github.com/digital-land/planning-application-data-specification/commit/4fe142fa3244da613272fbe2caafd4f9712682ba))
* remove replaced information models (commit [ee362ac](https://github.com/digital-land/planning-application-data-specification/commit/ee362acd33045ee0db7b228c6db86b136ff024be))
* module should use required-if structure not applies-if (commit [c6c89b5](https://github.com/digital-land/planning-application-data-specification/commit/c6c89b54b268b3fcd93e343180dbc2915ffe20de))

### 👷‍♀️ Application changes

* add public sector infrastucture to list of application types (commit [dcf54c7](https://github.com/digital-land/planning-application-data-specification/commit/dcf54c740b50d0da35f57b5708e97d99a5efc9de))
* add hazardous substance consent to list of application types (commit [23052e3](https://github.com/digital-land/planning-application-data-specification/commit/23052e3ddb021af9de8d96205379f0c00dacfb87))
* add review of mineral permission to list of application types (commit [356ce94](https://github.com/digital-land/planning-application-data-specification/commit/356ce94ffa8532a58d53c2f55b327552c59103e0))
* add technical details consent to list of application types (commit [de28222](https://github.com/digital-land/planning-application-data-specification/commit/de282222725ca6fbcb3ec1983428f39b04f90646))
* add minerals application to list of application types (commit [95c2de5](https://github.com/digital-land/planning-application-data-specification/commit/95c2de5a011b9ff9e972d832872861f83e38044c))
* add regulation 4 to list of application types (commit [5cf94ae](https://github.com/digital-land/planning-application-data-specification/commit/5cf94ae10412e9e6c749a531c9d34efb5f49dc88))
* add regulation 3 to list of application types (commit [8e8b69a](https://github.com/digital-land/planning-application-data-specification/commit/8e8b69a636748ebe4e8612fe1bd0a97ad3b44e63))
* add change of use to list of application types (commit [7304eb3](https://github.com/digital-land/planning-application-data-specification/commit/7304eb353b0abaed859c3a0a60983b92916464a6))
* add transport and works act order to list of application types (commit [c73f156](https://github.com/digital-land/planning-application-data-specification/commit/c73f156140867a09c920ededd3fdef4638ececbd))
* add modification or discharge of section 106 obligation to list of application types (commit [c5d1987](https://github.com/digital-land/planning-application-data-specification/commit/c5d1987ea3d5f14eb4986fb205c0ea58cd116c96))
* add mineral extraction to list of application types (commit [fbe3c60](https://github.com/digital-land/planning-application-data-specification/commit/fbe3c605d0854edba5099daa75db34fbd5668777))
* add additional environmental approval to extend permission period to list of application types (commit [29504f1](https://github.com/digital-land/planning-application-data-specification/commit/29504f1a7092a08c6c51524f2f4c251097d142aa))
* add modification of conditions relating to construction of working hours to list of application types (commit [d1b6137](https://github.com/digital-land/planning-application-data-specification/commit/d1b6137fdcbcbe636f5442b5cb8f815ce5de457e))
* add nsips to list of application types (commit [5a9f1b2](https://github.com/digital-land/planning-application-data-specification/commit/5a9f1b262232da602287caf5662a98d3a14147b0))
* add overhead line consent to list of application types (commit [ee30bfd](https://github.com/digital-land/planning-application-data-specification/commit/ee30bfd0d6c79ba7375492033a15301389bfc07c))
* add certificate of alternative appropriate dev to list of application types (commit [7ac5219](https://github.com/digital-land/planning-application-data-specification/commit/7ac521979749033c2cefbc9914f8453282503e28))
* add footpath diversion to list of application types (commit [10778fd](https://github.com/digital-land/planning-application-data-specification/commit/10778fd6a912d68c23111d68c2deb122be3ec829))
* add land drainage consent to list of application types (commit [5b2ca0a](https://github.com/digital-land/planning-application-data-specification/commit/5b2ca0ac45a6ef7514b8f6a62e79bd34c8bc4e15))
* add waste development to list of application types (commit [f5e70d5](https://github.com/digital-land/planning-application-data-specification/commit/f5e70d5c22fb45084bccb9070f5d8f4ebf0b3b0c))


<a name="v0.1.30"></a>
## [v0.1.30](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.27...v0.1.30) (2025-09-08)

Spreadsheet generator

### ⚒️ Tooling

* code to extract all modules into a csv (commit [fd657b9](https://github.com/digital-land/planning-application-data-specification/commit/fd657b95d494c9691c2627f3691b19a6a3f6abf8))
* add spreadsheet builder to make targets (commit [98623db](https://github.com/digital-land/planning-application-data-specification/commit/98623db5fa9e9b1868d2d7c84ee57aefaec891de))
* generate spreadsheets for all top level app types (commit [6768fa0](https://github.com/digital-land/planning-application-data-specification/commit/6768fa03455209896190f7323cd4bce63660602e))
* make the application details in rows optional (commit [e3dc519](https://github.com/digital-land/planning-application-data-specification/commit/e3dc5195c1b5e36a5e9d681fe766ad3fb17f16f8))
* create spreadsheet for compiled spec that only includes relevant fields (commit [ad86115](https://github.com/digital-land/planning-application-data-specification/commit/ad86115b2e0968ae0f548533540b75ab8de5e4cc))
* add check of applies-if structure in modules (commit [57feb11](https://github.com/digital-land/planning-application-data-specification/commit/57feb11bf74c1ec737cf1e9d55c2aa9df8e1f688))
* add a FieldInstance class to handle overrides in modules (commit [5d9a657](https://github.com/digital-land/planning-application-data-specification/commit/5d9a657ad32d3998fbbf33c11c09e6b2751ae668))
* minor refactoring of spreadsheet generator (commit [8593d26](https://github.com/digital-land/planning-application-data-specification/commit/8593d26cf8a6bfad5a9b660dde7e8c5fa71fb6e8))
* output example hh specification as spreadsheet (commit [91cd5f4](https://github.com/digital-land/planning-application-data-specification/commit/91cd5f4c09791275720141aa8a29f62d67c42826))
* func to load the specification as objects (commit [d2b8ec4](https://github.com/digital-land/planning-application-data-specification/commit/d2b8ec46203923ecac211f980706a45042f02750))
* output spreadsheet style spec using example specification (commit [0860409](https://github.com/digital-land/planning-application-data-specification/commit/08604096231494f87169ba355dd9ba41167feac2))
* code to extract all modules into a csv (commit [3e77f5b](https://github.com/digital-land/planning-application-data-specification/commit/3e77f5bf051f67370263a8fac0dd289be6a16731))
* func to return original forms for an app type (commit [30c47be](https://github.com/digital-land/planning-application-data-specification/commit/30c47be8b8954a70e1109caf2871dcc90bb075b7))

### 🐛 Bug Fixes

* conditions should be required-if not applies-if (commit [418753a](https://github.com/digital-land/planning-application-data-specification/commit/418753a917464a1e02f849b9b591426a95da6a80))
* name field needs specific description when used in supporting document component (commit [897b4dd](https://github.com/digital-land/planning-application-data-specification/commit/897b4dddd1f29c05e6eb48fa41171ddf829d22ac))
* incorrect structure used for applies-if application-type conditions (commit [8e9c0d6](https://github.com/digital-land/planning-application-data-specification/commit/8e9c0d6e56227bd551148d743bfe19c9c1a7aad3))


<a name="v0.1.27"></a>
## [v0.1.27](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.26...v0.1.27) (2025-08-29)

Resolve remaining phase 1 issues and improve tooling

### ⚒️ Tooling

* include list of codelists in contents of compiled specifications (commit [d3e9082](https://github.com/digital-land/planning-application-data-specification/commit/d3e9082aa6499ba1b96317dd0e563f5d58a105a4))
* include contents of codelists in compiled specifications (commit [2218244](https://github.com/digital-land/planning-application-data-specification/commit/221824450ee638cca0e98f596cae7afdc3188fdf))
* compiling specifications follows the extend attr for sub application types (commit [f652d0f](https://github.com/digital-land/planning-application-data-specification/commit/f652d0fc8fd776896f1354cc166ef5fd29d46e70))
* add check to confirm codelist referenced exists (commit [7a604f2](https://github.com/digital-land/planning-application-data-specification/commit/7a604f2b7f692094e808cb7a31e577954b8eeee1))
* set up tests for tooling code (commit [341b5fa](https://github.com/digital-land/planning-application-data-specification/commit/341b5faea76cb00e1499a2b379eb1bfdd7fb3f51))
* refactor section that outputs markdown tables for info model (commit [89f6156](https://github.com/digital-land/planning-application-data-specification/commit/89f6156ddbd6f345c60aa9b01238b8ffdf81d72e))

### 𝌭 Model changes

* make it clear net-additional-floorspace should be calculated automatically (commit [c96afb9](https://github.com/digital-land/planning-application-data-specification/commit/c96afb9eea1ba7ec72580d7f7a4d7cd7749b3758))
* handle variance in room-details component for outline applications (commit [f0b6304](https://github.com/digital-land/planning-application-data-specification/commit/f0b63044b8f950a59a608c91d5c44524bbd555e8))
* handle variance in floorspace-details module for outline apps (commit [30e56c2](https://github.com/digital-land/planning-application-data-specification/commit/30e56c2f3a50d94eae1d791c3774d1102b93f6b3))
* add non-residential-change-outline to handle unknown answer for outline applications (commit [ea4bff6](https://github.com/digital-land/planning-application-data-specification/commit/ea4bff647439dda47df2a405057bd3acdf6e93d3))
* experiment with codifying a count-constraint (commit [a86a4c0](https://github.com/digital-land/planning-application-data-specification/commit/a86a4c0fc8acf661530f098bd64162ce01832aae))
* add illumination-type codelist (commit [58af557](https://github.com/digital-land/planning-application-data-specification/commit/58af557e0846a039594e1d17c77c79b366c4ee84))

### 🐛 Bug Fixes

* typos in illumination-type codelist (commit [a619a04](https://github.com/digital-land/planning-application-data-specification/commit/a619a046456ab4022c685d26b5d4466e93ab3c37))
* use correct field for outline applications, should be separate-recycling-arrangements-outline (commit [0eb59fc](https://github.com/digital-land/planning-application-data-specification/commit/0eb59fc24aceb0cac23a86d70be213eace313e39))
* information model output for modules (commit [defdad5](https://github.com/digital-land/planning-application-data-specification/commit/defdad5d5837be43b247d38db83e28027f2a6434))
* pass codelists to field checks (commit [88887b6](https://github.com/digital-land/planning-application-data-specification/commit/88887b64e68b3da45b32a6063f69152846e0e565))
* references to codelists (commit [0e915d1](https://github.com/digital-land/planning-application-data-specification/commit/0e915d1ac8aed7c58ad5b1b1af566ba7e6ea0253))


<a name="v0.1.26"></a>
## [v0.1.26](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.25...v0.1.26) (2025-08-27)

Tooling: integrity checks and generating information models

### ⚒️ Tooling

* automate generation of information model when declarative model changes (commit [3560fbe](https://github.com/digital-land/planning-application-data-specification/commit/3560fbecf1ec5342d00136a3fbfcc8b506881f04))
* output whole application module and substructures when generating compiled spec (commit [90217e1](https://github.com/digital-land/planning-application-data-specification/commit/90217e1281833e950949433403080e68d5a4a866))
* generate all application info models (commit [e8e02e9](https://github.com/digital-land/planning-application-data-specification/commit/e8e02e9520a9feb828d2ebe0bc1c3a04bd418859))
* script to regenerate all module info models (commit [18e6f1d](https://github.com/digital-land/planning-application-data-specification/commit/18e6f1df768884bfc3f5576f52889094888dd10c))
* update checking required-if conditions in components (commit [c631583](https://github.com/digital-land/planning-application-data-specification/commit/c631583c4134a556bbcfaa27fa053de7a7416abb))
* handle applications that extend base application (commit [f8b8fca](https://github.com/digital-land/planning-application-data-specification/commit/f8b8fca3fac71fe83cfc5420e2d03f9079ae24f7))
* func to generate whole info model for given app type (commit [c4ac54f](https://github.com/digital-land/planning-application-data-specification/commit/c4ac54f590b60ec9a732cd29d89d5956f9ca5b33))
* add util func to save string to file (commit [4c735bb](https://github.com/digital-land/planning-application-data-specification/commit/4c735bb02dfb4403dcdbb06207b167abdfcc782c))
* make sure reference to enum is bold (commit [d0afd98](https://github.com/digital-land/planning-application-data-specification/commit/d0afd98b440abd5f3280df1f20e8ba58711272de))
* add integrity checks for codelists (commit [782c513](https://github.com/digital-land/planning-application-data-specification/commit/782c513088b9903c7f368b388753a7333b2fae11))

### 𝌭 Model changes

* tweak name of application module (commit [e981b7e](https://github.com/digital-land/planning-application-data-specification/commit/e981b7eefc06932558748caf2e249bf47cb04f1c))
* all application info models now in generated/info_model/application (commit [18e472a](https://github.com/digital-land/planning-application-data-specification/commit/18e472aa47105c01a618160df5e210240c46417e))
* generated info models now in generated/info_model directory (commit [bb17e05](https://github.com/digital-land/planning-application-data-specification/commit/bb17e05b9c9c2dcd69478c00f412ebec0fbad3b2))
* define application-type codelist (commit [42ee3cf](https://github.com/digital-land/planning-application-data-specification/commit/42ee3cfd4d0c212629a0c11141db67ab6251f7c3))
* add declarative version of existing-use module (commit [c4bf273](https://github.com/digital-land/planning-application-data-specification/commit/c4bf273f4627ce41a43353f3d7872e1a7781a83c))

### 🐛 Bug Fixes

* typo in output path (commit [e573abc](https://github.com/digital-land/planning-application-data-specification/commit/e573abce2d2892aa746d4211a1af2e45227603fe))
* errors with conditions in components (commit [5d1bfce](https://github.com/digital-land/planning-application-data-specification/commit/5d1bfce5fedff418277854a2371172e85fc862d6))
* cardinality must be 1 or n (commit [64784b5](https://github.com/digital-land/planning-application-data-specification/commit/64784b5d01a103f142940873646a714944e67e25))
* codelist checks, only read *.schema.md files (commit [956adb3](https://github.com/digital-land/planning-application-data-specification/commit/956adb30a6f222d651a6000e4ae4d16d52cfd099))
* validation attr should be rules (commit [025cdaf](https://github.com/digital-land/planning-application-data-specification/commit/025cdaf26fb08f81886c89240715e770d5833334))


<a name="v0.1.25"></a>
## [v0.1.25](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.24...v0.1.25) (2025-08-15)

Add codelist and codelist definitions

### 𝌭 Model changes

* add source attr for codelists (commit [bac5be9](https://github.com/digital-land/planning-application-data-specification/commit/bac5be9641a5a80cc28c8a22587d8ab64a0f7a49))
* define rights-of-way-answer codelist (commit [86b02c0](https://github.com/digital-land/planning-application-data-specification/commit/86b02c0643c57365bfe099a4c83aab04deea983d))
* define parking-space-type codelist (commit [2fa6d77](https://github.com/digital-land/planning-application-data-specification/commit/2fa6d770768c4ea98d79f888feb6989f86bdb7e9))
* define listed-building-grade codelist (commit [795bb58](https://github.com/digital-land/planning-application-data-specification/commit/795bb584f17c77f1b655ecccefbf5a90613cc668))
* define grounds-ldc-pre-apr-2024 codelist (commit [80a2125](https://github.com/digital-land/planning-application-data-specification/commit/80a212544a9a01fe96f3c97924665bdde48488a4))
* define ground-ldc-post-apr-2024 codelist (commit [c4b3aa7](https://github.com/digital-land/planning-application-data-specification/commit/c4b3aa70194f3a220f44f785a5210dd13920a92e))
* define building-element-type codelist (commit [bd99241](https://github.com/digital-land/planning-application-data-specification/commit/bd99241b75e72a156ef3a914099aeec117c49539))
* define bng-exemptions codelist (commit [521f765](https://github.com/digital-land/planning-application-data-specification/commit/521f7653cdfa3ac904403a4e9ddf609cf7c1da8d))
* define designations codelist (commit [30e33d8](https://github.com/digital-land/planning-application-data-specification/commit/30e33d82636d861a009c389c128b07a5d261558d))
* define yes-no-unknown codelist (commit [6f79516](https://github.com/digital-land/planning-application-data-specification/commit/6f795169ff196bee0a7c69160be51d372afec2cb))
* define yes-no-not-applicable codelist (commit [c802ee0](https://github.com/digital-land/planning-application-data-specification/commit/c802ee00880d87fad73ab794ae20c13bac3f332e))
* define waste-management-type codelist (commit [49b282e](https://github.com/digital-land/planning-application-data-specification/commit/49b282ec129b10076054208b133c097087b0ca4c))
* define user-role-type codelist (commit [372fe56](https://github.com/digital-land/planning-application-data-specification/commit/372fe561bec8c0c6b1dc997d8c368ff7cfe2703d))
* define tenure-type codelist (commit [7823425](https://github.com/digital-land/planning-application-data-specification/commit/7823425fdbbd9c30922b8d65da200f1fc81a4dff))
* define surface-water-disposal-type codelist (commit [2cb3797](https://github.com/digital-land/planning-application-data-specification/commit/2cb37974a842aa7c2132a7d0e76ab287fc16a126))
* define site-visit-contact-type codelist (commit [16f4327](https://github.com/digital-land/planning-application-data-specification/commit/16f43272c84615e0c683f0abfcb59c0ca872ece6))
* define site-constraints codelist (commit [6a02e2e](https://github.com/digital-land/planning-application-data-specification/commit/6a02e2e33411dc2316e541da22b6c815768a0b19))
* define reserved-matter-type codelist (commit [bd4d1a4](https://github.com/digital-land/planning-application-data-specification/commit/bd4d1a420c4b8628bce422de573f37eebe4e8dc1))
* define provided-by codelist (commit [4411ec2](https://github.com/digital-land/planning-application-data-specification/commit/4411ec2318787c057de405dd297ab2fdb44b4f98))
* define permission-type codelist (commit [45176b2](https://github.com/digital-land/planning-application-data-specification/commit/45176b26277ccdb433366d717d9dd1e5ccfe7547))
* define ownership-cert-type codelist (commit [a0a58e3](https://github.com/digital-land/planning-application-data-specification/commit/a0a58e394b6536e6201edd11ad8eed555d140933))
* define operation-type codelist (commit [9d63aa7](https://github.com/digital-land/planning-application-data-specification/commit/9d63aa76297aa0ed065d7f0b9f1d60c074f0cc3e))
* define non-res-measurement-type codelist (commit [690da25](https://github.com/digital-land/planning-application-data-specification/commit/690da25e264e689de3d2ef05dd4f449664b30f14))
* define lb-alertation-type codelist (commit [3118cea](https://github.com/digital-land/planning-application-data-specification/commit/3118cea7a28b45dbc14826878273943f68f1f872))
* define lawful-dev-cert-need codelist (commit [57cd087](https://github.com/digital-land/planning-application-data-specification/commit/57cd087f88296fac4917aa074807994d494b1629))
* define housing-type codelist (commit [85f0cf3](https://github.com/digital-land/planning-application-data-specification/commit/85f0cf35ad115d53c41f73a9a413063e8f769cdc))
* rename codelist to hedgerow-interest-type (commit [38a15dd](https://github.com/digital-land/planning-application-data-specification/commit/38a15dd5a643fd110275b94ebf3e107f5eb63a6c))
* define hedgerow-interest-dec codelist (commit [4f98936](https://github.com/digital-land/planning-application-data-specification/commit/4f9893614c1d5e1469914554edf0e8979b76dbe6))
* define hazardous-sub-type codelist (commit [439ced8](https://github.com/digital-land/planning-application-data-specification/commit/439ced8dbc707811fdf837910db6c0f0acc385c3))
* define foul-sewage-disposal-type codelist (commit [f4177c1](https://github.com/digital-land/planning-application-data-specification/commit/f4177c147fce694f4458a1ca3c6131d0c240fb79))
* define day-type codelist (commit [a1f6bbb](https://github.com/digital-land/planning-application-data-specification/commit/a1f6bbbe6d337d42329d3b7c074308c67025e697))
* define contact-priority codelist (commit [70cebdd](https://github.com/digital-land/planning-application-data-specification/commit/70cebdd13355d96c22d2d233d06e6683888a8bc8))
* define applicant-interest-type codelist (commit [2899d07](https://github.com/digital-land/planning-application-data-specification/commit/2899d07c3db576cf39b924c6c5d446da49b14cf2))
* define affected-area-type codelist (commit [ee65d4a](https://github.com/digital-land/planning-application-data-specification/commit/ee65d4aaa4f141437f9387c88ae100028f7cccac))
* define advertisement-type codelist (commit [39ebe98](https://github.com/digital-land/planning-application-data-specification/commit/39ebe980a8cc5e332723c3557e3a6f270cf82624))
* move source of development phase codelist (commit [2f0ec89](https://github.com/digital-land/planning-application-data-specification/commit/2f0ec899140fb6bac2f4ccf57fb3fd53b520ed23))
* define development-phase codelist (commit [892cdf2](https://github.com/digital-land/planning-application-data-specification/commit/892cdf2c7b016c13c01d5a57d7468f1d35ebdc94))

### 🐛 Bug Fixes

* remove replaced codelists (commit [24f008a](https://github.com/digital-land/planning-application-data-specification/commit/24f008a727683e86493e8d2ee601badaf08e1668))
* remove duplicate codelist (commit [d688802](https://github.com/digital-land/planning-application-data-specification/commit/d6888020edb2b564e185844489fee1018c6fbce9))

### 📚 Documentation

* write up current structure for defining codelists for the specification (commit [c4e4e8f](https://github.com/digital-land/planning-application-data-specification/commit/c4e4e8fdf9ee70b09a47a9486eabaf396d951956))


<a name="v0.1.24"></a>
## [v0.1.24](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.23...v0.1.24) (2025-08-12)

Add all remaining application type definitions

### 🐛 Bug Fixes

* fix datatype for advert-placed-date field (commit [b5ae0ce](https://github.com/digital-land/planning-application-data-specification/commit/b5ae0ce6488748364a749543d2462106b285beda))

### 👷‍♀️ Application changes

* define app structures for ldc applications (commit [57fb5ce](https://github.com/digital-land/planning-application-data-specification/commit/57fb5cec5b0e0b5b86c3a4d6aeb657f015e4883d))
* define app structures for prior-approval applications (commit [003c94b](https://github.com/digital-land/planning-application-data-specification/commit/003c94b5d47174ccc8f0d4f5ba32d2166fe65ba1))
* define app structures for outline applications (commit [ed59288](https://github.com/digital-land/planning-application-data-specification/commit/ed59288b5d959ed7be2b147b3ffaf3e770e3221e))
* define the structure for full application (commit [2331b6f](https://github.com/digital-land/planning-application-data-specification/commit/2331b6f9e4d613e979146b2c234bfeef8a6e5532))
* define the structure for lbc application (commit [fa4e9d1](https://github.com/digital-land/planning-application-data-specification/commit/fa4e9d13abe7473b61ac1d0ef6df10ed0fa94424))
* define the structure for notice-trees-in-con-area application (commit [2112a44](https://github.com/digital-land/planning-application-data-specification/commit/2112a44b07e63d6301b23ea9d104b93ada99739b))
* define the structure for reserved-matters application (commit [8619467](https://github.com/digital-land/planning-application-data-specification/commit/86194678e163417f7e31e46fd7a04eb9d5a7cbe8))
* define the structure for s73 application (commit [ddb57c3](https://github.com/digital-land/planning-application-data-specification/commit/ddb57c3e1ce20f749851573ecfb9b896c7914eb6))
* define the structure for non-material-amendment application (commit [099c70b](https://github.com/digital-land/planning-application-data-specification/commit/099c70bf3faf74824a72eb53d2c1086d7947ba34))
* define the structure for hedgerow-removal application (commit [df0aab3](https://github.com/digital-land/planning-application-data-specification/commit/df0aab3e456e0180c892b2e5adfee7bad5c69cf7))
* define the structure for demolition-con-area application (commit [72f9bd2](https://github.com/digital-land/planning-application-data-specification/commit/72f9bd2322c46d377890d000d939dafebde5f8ac))
* add declarative version of approval-condition application (commit [3be761a](https://github.com/digital-land/planning-application-data-specification/commit/3be761ab287065a3c79af783157e77d3c30082a4))
* add declarative version of advertising application (commit [b473330](https://github.com/digital-land/planning-application-data-specification/commit/b473330411531cd3bb966b084deb10994e267fca))


<a name="v0.1.23"></a>
## [v0.1.23](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.22...v0.1.23) (2025-07-22)

Bit of tidying things up

### ⚒️ Tooling

* alter table format if generating for specific app type (commit [94efdfa](https://github.com/digital-land/planning-application-data-specification/commit/94efdfa3924d03568031ccecc7fa9327c1a9f0ee))
* refactor generate info model script (commit [84842d2](https://github.com/digital-land/planning-application-data-specification/commit/84842d251a0e1fcfc967fb55864bb6f5d2490ab5))
* generate module markdown filtering fields that are not applicable (commit [cf72d84](https://github.com/digital-land/planning-application-data-specification/commit/cf72d84e07354b6f8d56b5da43525b474241747a))
* generate the markdown for a module (commit [63a62a7](https://github.com/digital-land/planning-application-data-specification/commit/63a62a7e79bbc3809f85f6eb6ad753d638f2ec00))
* check only expected attrs are included in module definitions (commit [e94920a](https://github.com/digital-land/planning-application-data-specification/commit/e94920a05317dd9b8993b4828bd3e350f1894348))

### 🐛 Bug Fixes

* pip-reference should have an applies-if condition not required-if condition (commit [daab0a7](https://github.com/digital-land/planning-application-data-specification/commit/daab0a7bfed8f29e5aded16449b4fef4a032e072))
* remove unneccessay attrs from module definitions (commit [102afc3](https://github.com/digital-land/planning-application-data-specification/commit/102afc31563ddd03a15b2bfef93e15144ee2694f))
* implementation is an allowable attr for module definitions (commit [c9b075e](https://github.com/digital-land/planning-application-data-specification/commit/c9b075ef67882248b65855217ca8fbb5f60adafa))
* module attribute should be notes not note (commit [8a50b22](https://github.com/digital-land/planning-application-data-specification/commit/8a50b22e39ad8fb2ef8c9815da54981b1296d5a6))
* module attribute should be rules not validation (commit [75c02d8](https://github.com/digital-land/planning-application-data-specification/commit/75c02d8b82a4974fccd25243af691ca5a0977980))


<a name="v0.1.22"></a>
## [v0.1.22](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.21...v0.1.22) (2025-07-18)

Final set of declarative versions of modules

### 𝌭 Model changes

* add declarative version of interest-details module (commit [3893fc3](https://github.com/digital-land/planning-application-data-specification/commit/3893fc3f2031a2dca13679ba650e4db6f8d11650))
* add declarative version of eligibility-related-works module (commit [6a456dd](https://github.com/digital-land/planning-application-data-specification/commit/6a456dd9d55d706b464665044953778d50a4d1bd))
* add declarative version of eligibility module (commit [4b1639a](https://github.com/digital-land/planning-application-data-specification/commit/4b1639a027dd1bb13de203ede28faa44c749c4d2))
* add declarative version of eligibility-proposal module (commit [71db37b](https://github.com/digital-land/planning-application-data-specification/commit/71db37b9f936d7b7cce0f7be57f3bda5bed9af8b))


<a name="v0.1.21"></a>
## [v0.1.21](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.20...v0.1.21) (2025-07-18)

Reworking the residential units module

### ⚒️ Tooling

* generate field dataset (commit [99f1cba](https://github.com/digital-land/planning-application-data-specification/commit/99f1cba72adb27a81735b8e98e8c32d273d0986d))

### 𝌭 Model changes

* rename field from residential-unit-change to will-residential-units-change (commit [72cdf87](https://github.com/digital-land/planning-application-data-specification/commit/72cdf872f8a371b8cff75baba72e16f200751e4f))
* add declarative version of the res-units module (commit [78a602e](https://github.com/digital-land/planning-application-data-specification/commit/78a602e67908ca31b5acb0c666962aad0a643687))
* update the res-unit module to handle houses of any bedroom number (commit [5ab7aa4](https://github.com/digital-land/planning-application-data-specification/commit/5ab7aa41b23c5edcc21ab42d229564fb26e25798))

### 🐛 Bug Fixes

* field description needed to be in quotes (commit [31128dd](https://github.com/digital-land/planning-application-data-specification/commit/31128dd67501f25da797f968d45f635c58507c8e))

### 📚 Documentation

* added implementation note about how res-units module should be interpreted for paper forms (commit [03c7e36](https://github.com/digital-land/planning-application-data-specification/commit/03c7e36760f25386023ae10f4e11b2ca94be2e20))


<a name="v0.1.20"></a>
## [v0.1.20](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.19...v0.1.20) (2025-07-17)

Declarative versions of modules

### 𝌭 Model changes

* handle variance with Outline app by allowing unknown (commit [75a0b5b](https://github.com/digital-land/planning-application-data-specification/commit/75a0b5b8c44ee14006a454a4fa7c1ee9a0f16f99))
* add declarative version of flood-risk-assessment module (commit [71fde7a](https://github.com/digital-land/planning-application-data-specification/commit/71fde7a9ca6ad9a166624950822e20129bdd29ca))
* add declarative version of grounds-proposed-use module (commit [eb469e6](https://github.com/digital-land/planning-application-data-specification/commit/eb469e6235cdd386045f5c9d9c5f3190ec644d2f))
* add declarative version of the hedgerow-removal module (commit [10cb0be](https://github.com/digital-land/planning-application-data-specification/commit/10cb0be641c5eda31a447598004d1fedf5e0d79a))
* add declarative version of ldc-interest module (commit [4687322](https://github.com/digital-land/planning-application-data-specification/commit/4687322e60046843b69bc008a5cc10691abe1d2e))
* add declarative version of the non-res-floorspace module (commit [b17a03d](https://github.com/digital-land/planning-application-data-specification/commit/b17a03d41ef448e4a456b771b4b34d91116b7a72))
* add declarative version of proposal-details-ldc module (commit [a74feec](https://github.com/digital-land/planning-application-data-specification/commit/a74feecc4ad0f6b3125476b16b8c5569ae4b10ea))
* add declarative version of proposed-advert-details module (commit [9961d1a](https://github.com/digital-land/planning-application-data-specification/commit/9961d1afa7e6df240fd30d03da26411681f73a62))
* add declarative version of use-works-activity module (commit [7382719](https://github.com/digital-land/planning-application-data-specification/commit/738271922c2635609e68977846fe8c7a806a837c))
* add new has-new-disposal-arrangements field to foul-sewage module (commit [870d08e](https://github.com/digital-land/planning-application-data-specification/commit/870d08e38a7f26c79ba05011b91b0ac0993df43e))
* consolidate related-proposals and related-applications into single related-applications approach (commit [1662e27](https://github.com/digital-land/planning-application-data-specification/commit/1662e277b05fa1f424122d95e99c639941939e62))
* add declarative version of hrs-operation module (commit [9d378af](https://github.com/digital-land/planning-application-data-specification/commit/9d378af12ad7ea4bd26c998662c2e48a54b3a7f9))

### 🐛 Bug Fixes

* add the missing applies-if conditions to the original fields in waste-storage-collection module (commit [44fbcc1](https://github.com/digital-land/planning-application-data-specification/commit/44fbcc12b87465884b72e8fdf75a0bec8af3898f))


<a name="v0.1.19"></a>
## [v0.1.19](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.18...v0.1.19) (2025-07-16)

BNG and declarative modules

### 𝌭 Model changes

* add declarative version of grounds-for-application module (commit [d096caa](https://github.com/digital-land/planning-application-data-specification/commit/d096caac505c1abab8eb9fa9221ccaf4b13b18ad))
* add declarative version of grounds-existing-use module (commit [c0bf0d5](https://github.com/digital-land/planning-application-data-specification/commit/c0bf0d52b12137a1330f5d45006b74ee617b470c))
* rename in-building-construction-period field to was-constructed-btw-1948-2018 (commit [30394f2](https://github.com/digital-land/planning-application-data-specification/commit/30394f20cb3dc7a512c9c2cfbc61206bb048c65d))
* rename site-location-constraint field to is-site-in-restricted-area (commit [35b8202](https://github.com/digital-land/planning-application-data-specification/commit/35b82026bff4bb659d14d1d6a4ddfe9475ea1c57))
* rename dwelling-permitted-use field to was-use-granted-by-pdr (commit [92e2813](https://github.com/digital-land/planning-application-data-specification/commit/92e2813366e92c893eca478a1497d680b4e0e105))
* rename additional-storeys-added field to has-additional-storeys (commit [a51e97f](https://github.com/digital-land/planning-application-data-specification/commit/a51e97f4cbd15229f8e42479b3a4212de94e2ac1))
* add declarative version of eligibility-current-building module (commit [ff5a68b](https://github.com/digital-land/planning-application-data-specification/commit/ff5a68bd44c2b419b44e1a506fc48337f52a50a6))
* update declarative version of bng module with bng-condition-exemption-reasons substructure (commit [3fb2492](https://github.com/digital-land/planning-application-data-specification/commit/3fb2492175e7eee28fcfaee8184854132272966b))
* add sub-structure to BNG module to capture specific exemptions cited (commit [30136eb](https://github.com/digital-land/planning-application-data-specification/commit/30136ebac717452d3b6a1621739f6f705b0b5b8d))
* add bng-exemption-reason codelist (commit [90e727c](https://github.com/digital-land/planning-application-data-specification/commit/90e727cf1aef37dde21957f944714438a843f3d8))
* rename existing-use-change field to has-existing-use-changed (commit [c57b63a](https://github.com/digital-land/planning-application-data-specification/commit/c57b63a43e45380fb880887be84b6f93b84bf879))
* rename existing-use-interrupted field to has-existing-use-interrupted (commit [8c28e6d](https://github.com/digital-land/planning-application-data-specification/commit/8c28e6dbe3008dcd32d4c6a1dc66c6e9b02b0423))
* add declarative version of info-support-ldc module (commit [7a59d3a](https://github.com/digital-land/planning-application-data-specification/commit/7a59d3a1a0eff9f7ea6a7747609bee2cf4cc688c))
* rename substituting-document field to is-substituting-document (commit [4e6cecd](https://github.com/digital-land/planning-application-data-specification/commit/4e6cecd559e0ad0ffd6b1f2b3d6ef05b91d1b14c))
* add declarative version of nm-amendment-details module (commit [b0109e3](https://github.com/digital-land/planning-application-data-specification/commit/b0109e392f9ca332014e79dd0cc5e4b139f8d992))
* handle variance in ownership certificates module between lbc and other applications (commit [4552d7d](https://github.com/digital-land/planning-application-data-specification/commit/4552d7d4715e1731d01420ea106e9b170f9e72c4))
* rename owners-and-tenants component to notified-person (commit [71c631f](https://github.com/digital-land/planning-application-data-specification/commit/71c631f142d8bb6e15856acc27f3e16ec50bfd8d))
* add a combined parking-space-type enum (commit [07ea250](https://github.com/digital-land/planning-application-data-specification/commit/07ea2508ec7d63af8d60e277c68080db11bdacda))
* add declarative version of desc-proposed-works module (commit [514ca9b](https://github.com/digital-land/planning-application-data-specification/commit/514ca9bc496323fce3d25113f189781d3064b099))
* add declarative version of plans-drawings-supporting-materials module (commit [e3b20ff](https://github.com/digital-land/planning-application-data-specification/commit/e3b20ff82bb9398138b4b44629f55a0c271cd9c2))


<a name="v0.1.18"></a>
## [v0.1.18](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.17...v0.1.18) (2025-07-15)

More declarative versions added and issues resolved

### 𝌭 Model changes

* add declarative version of desc-proposed-works module (commit [a925d32](https://github.com/digital-land/planning-application-data-specification/commit/a925d326e03b64bb05e03b8699b13fd2bdbf4035))
* add declarative version of plans-drawings-supporting-materials module (commit [3002aa5](https://github.com/digital-land/planning-application-data-specification/commit/3002aa5733482bca54aee1eae7037e33230d4b27))
* rename type field to waste-management-facility-type (commit [eae9560](https://github.com/digital-land/planning-application-data-specification/commit/eae956046ccbfd425c7e376367b928bbaeda6089))
* add specification processes-machinery-waste module for outline applications (commit [9b05a03](https://github.com/digital-land/planning-application-data-specification/commit/9b05a03f9a701348424b55732a96444a5f4ba832))
* add declarative version of desc-work-impacts-risks module (commit [d8dac9a](https://github.com/digital-land/planning-application-data-specification/commit/d8dac9a27a386ccd62d46e48959af8fbf26ae721))
* reanme within-site-constraints field to is-within-site-constraints (commit [51d27af](https://github.com/digital-land/planning-application-data-specification/commit/51d27af4a4e571347ce29454b24c5343ab30332b))
* rename rear-extension-length field to is-extension-beyond-rear-wall (commit [d85023c](https://github.com/digital-land/planning-application-data-specification/commit/d85023c7070dcbc6d9b723b916ef5dadf925ac2d))
* field in eligibility-proposal should be is-dwelling-detached (commit [02fd137](https://github.com/digital-land/planning-application-data-specification/commit/02fd137b7fb5bb1ed8d48599e6b1f5729307f2d2))
* rename dwelling-detached field to is-dwelling-detached (commit [1ca6280](https://github.com/digital-land/planning-application-data-specification/commit/1ca6280ef48eea63888fc9720565eef2ce6e0807))
* rename extension-height-over-4m field to is-extension-height-over-4m (commit [d6092ba](https://github.com/digital-land/planning-application-data-specification/commit/d6092ba3e02b0aac9855dbc44053d525f04ef5b1))
* rename single-storey-extension to is-single-storey-extension (commit [d0ae1bd](https://github.com/digital-land/planning-application-data-specification/commit/d0ae1bda3ed7555f17c731db2ba5bbdcff4f7807))
* add declarative version of eligibility-extension module (commit [78fab5b](https://github.com/digital-land/planning-application-data-specification/commit/78fab5b3d897c199eb29d57f0636378c32d570ea))
* designations and site-constraints fields should both use designations enum (commit [045697a](https://github.com/digital-land/planning-application-data-specification/commit/045697a3c7973c9ecc57d2c863d90ded46470073))
* combine designation and sigte-constraint codelists (commit [23a42e5](https://github.com/digital-land/planning-application-data-specification/commit/23a42e57510bafec1cb485c6292fd9424e466eef))
* add declarative version of grounds-ldc module (commit [5f72b7f](https://github.com/digital-land/planning-application-data-specification/commit/5f72b7ffa13e5f221f76dbd92dac5f5f93f4043e))
* grounds for ldc is now in 2 parts, pre and post 2025-04-25 (commit [41bcb70](https://github.com/digital-land/planning-application-data-specification/commit/41bcb70683ed986d0a67a2e02d0683051c159f45))
* add codelists needed for grounds for ldc module (commit [b79067d](https://github.com/digital-land/planning-application-data-specification/commit/b79067d19801f691bdd6d98c0b8a2257f47cc7b3))

### 🐛 Bug Fixes

* update csv field to application-types (commit [d836c96](https://github.com/digital-land/planning-application-data-specification/commit/d836c962cafbb9908b49901beda4288613fccdde))


<a name="v0.1.17"></a>
## [v0.1.17](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.16...v0.1.17) (2025-07-09)

More declarative versions added

### 𝌭 Model changes

* add proposal-waste-management-outline field to handle variance between application types (commit [83718a9](https://github.com/digital-land/planning-application-data-specification/commit/83718a950843ee9d91a165aed925d1c2061f0879))
* is-annual-throughput-known and is-total-capacity-known fields only applicable in outline applications (commit [a08dfbd](https://github.com/digital-land/planning-application-data-specification/commit/a08dfbdc0fb915ef8e750fbfb803ce2382ff0224))
* add declarative version of processes-machinery-waste module (commit [3fd5e22](https://github.com/digital-land/planning-application-data-specification/commit/3fd5e22251f66fb0c9f123f6f2e022e800247e12))
* add declarative version of site-ownership module (commit [72e4853](https://github.com/digital-land/planning-application-data-specification/commit/72e485307746da3f9951e79d26095e86054b1b8d))
* add declarative version of foul-sewage module (commit [69d1e6c](https://github.com/digital-land/planning-application-data-specification/commit/69d1e6c0b7e16f188e8b6de8a51582f03e61aaef))
* add declarative version of hazardous-substance module (commit [e6ebf79](https://github.com/digital-land/planning-application-data-specification/commit/e6ebf79f95b693712394b0ccf82d0c3499935eae))
* add yes-no-not-applicable codelist (commit [ee40ffd](https://github.com/digital-land/planning-application-data-specification/commit/ee40ffdeabfc5cb84204434d773343e550b2e149))
* add declarative version of desc-existing-use module (commit [b3f6e37](https://github.com/digital-land/planning-application-data-specification/commit/b3f6e370c8c70477ef9edf59168400c8bdd6c4e1))
* add declarative version of advert-location module (commit [da16807](https://github.com/digital-land/planning-application-data-specification/commit/da16807397cbda89a090059ec0a871ca8af7bca0))


<a name="v0.1.16"></a>
## [v0.1.16](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.15...v0.1.16) (2025-07-08)

More issues resolved and declarative versions added

### ⚒️ Tooling

* summarise progress towards declarative model (commit [79d5d45](https://github.com/digital-land/planning-application-data-specification/commit/79d5d45ebb8991a2a586670f25f3d94da1afab5d))
* func to output list of modules with no current issues (commit [4925e9b](https://github.com/digital-land/planning-application-data-specification/commit/4925e9b6aba2d79d5105af1710fffd0276ba8df9))

### 𝌭 Model changes

* unknown-proposed only applicable in outline-some applications (commit [eb59fea](https://github.com/digital-land/planning-application-data-specification/commit/eb59fea2d826abe5d8f8520d6f62848bce7161b2))
* add declarative version of vehicle-parking module (commit [30694ec](https://github.com/digital-land/planning-application-data-specification/commit/30694ecc1d632904f95bb734466d4297a7c98eb5))
* add declarative version of interest-in-land module (commit [5b56930](https://github.com/digital-land/planning-application-data-specification/commit/5b56930b057d199d2cde3e708d1b0e98031a1f43))
* add declarative version of waste-storage-collection module (commit [0d471c4](https://github.com/digital-land/planning-application-data-specification/commit/0d471c416bda5b5008324628e68f5cd23d4eb4ba))
* add declarative version of storage-facilities module (commit [8af2586](https://github.com/digital-land/planning-application-data-specification/commit/8af258667fb3ecb59188f45c50c9643504e7b665))
* add declarative version of related-proposals module (commit [ea581a7](https://github.com/digital-land/planning-application-data-specification/commit/ea581a713e3dff9a7a8277d59ddfdd406c7f596f))
* add declarative version of lb-alter module (commit [3d22d9c](https://github.com/digital-land/planning-application-data-specification/commit/3d22d9cb32a4350cbdd2c5db9e3cbffac48c2eb4))
* add declarative version of equip-mentod module (commit [064663a](https://github.com/digital-land/planning-application-data-specification/commit/064663a5854782b28ecae33821cb91ff7f4b2e74))
* rename fte to total-fte for clarity (commit [f2ee6d1](https://github.com/digital-land/planning-application-data-specification/commit/f2ee6d193ee3f80ecda00ff6b6c063beab531859))
* add declarative version of employment module (commit [350d564](https://github.com/digital-land/planning-application-data-specification/commit/350d5644228bc91e9eeaf975bf514dc7b11460fe))
* proposed-employees of employment module is sub-structure (commit [6a34ec0](https://github.com/digital-land/planning-application-data-specification/commit/6a34ec0507ca3b814472b98386867bb278342873))
* add declarative version of discharge-con module (commit [107826f](https://github.com/digital-land/planning-application-data-specification/commit/107826f9bd0fec8c7db0e5e28a79db9abef1c699))
* add declarative version of advertisement-types module (commit [7cefbe3](https://github.com/digital-land/planning-application-data-specification/commit/7cefbe3d84ca3ffb887fa1d387b27d08bb9174e5))
* add declarative version of designated-areas module (commit [a3a963f](https://github.com/digital-land/planning-application-data-specification/commit/a3a963f6a8ab95444d80a8bbc78ae546a7841fac))
* add declarative version of con-remove-vary module (commit [7586608](https://github.com/digital-land/planning-application-data-specification/commit/758660841ed924b4fe11f229a8ea8ac51347b171))
* add declarative version of community-consultation module (commit [c1cec61](https://github.com/digital-land/planning-application-data-specification/commit/c1cec61c3fca2add45b77c8d519ef1a3ac868e92))
* add declarative version of bio-geo-arch-con module (commit [6f5bdbc](https://github.com/digital-land/planning-application-data-specification/commit/6f5bdbcf3a121ff0ef5487b014f8efa66e5be914))
* add declarative version of advert-period module (commit [4648047](https://github.com/digital-land/planning-application-data-specification/commit/46480473fbb5d5c757625e09f9eb46da6caad2f0))
* add declarative version of adj-premises module (commit [ea22e94](https://github.com/digital-land/planning-application-data-specification/commit/ea22e94b7fa39fdd24a7d1fe76c73ac59892c139))
* rename field from discharging-part to is-discharging-part (commit [869f1e0](https://github.com/digital-land/planning-application-data-specification/commit/869f1e0e09c1bf503591bdf7aa6b051ba7ed9b4d))
* add declarative version of part-discharge module (commit [fa0a6a5](https://github.com/digital-land/planning-application-data-specification/commit/fa0a6a5497f7ce075176d2f5b4ac7a13f6f0cf6a))
* add is-annual-throughput-known field to processed-machinery-waste module (commit [3e527ca](https://github.com/digital-land/planning-application-data-specification/commit/3e527ca5d6dfc50c736bf9faa1631590aecf531a))
* add is-total-capacity-known field to processed-machinery-waste module (commit [b12d93a](https://github.com/digital-land/planning-application-data-specification/commit/b12d93a6c5215acea5b06e189ec2604f4c0e785f))

### 🐛 Bug Fixes

* correct declarative model errors (commit [5f84de4](https://github.com/digital-land/planning-application-data-specification/commit/5f84de4b3be9d74d86052ed01b42567046e22813))
* also include all modules with no issues (commit [63835f8](https://github.com/digital-land/planning-application-data-specification/commit/63835f8e6eae5714510b7cd4f9e9f4d7c862b030))
* add missing address component (commit [f25fa2d](https://github.com/digital-land/planning-application-data-specification/commit/f25fa2d8158e2f628bcc4a6fc8d52f4f46a615f1))
* fieldname typo" (commit [53152bd](https://github.com/digital-land/planning-application-data-specification/commit/53152bdc1d200fd3d7c87ff02b1f57907072d1c2))

### 📚 Documentation

* add row counts to module tracking pages (commit [6b4608a](https://github.com/digital-land/planning-application-data-specification/commit/6b4608a2672b1539998f7ab100cc323d8a4522f0))


<a name="v0.1.15"></a>
## [v0.1.15](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.14...v0.1.15) (2025-07-02)

More issues resolved and declarative versions added

### ⚒️ Tooling

* add integrity check for enum fields (commit [ad30076](https://github.com/digital-land/planning-application-data-specification/commit/ad30076085f1ca59191e0be0e8c899f06f14d024))

### 𝌭 Model changes

* add declarative version of site-area module (commit [725aec7](https://github.com/digital-land/planning-application-data-specification/commit/725aec792f48ce6073759d6678aacdb151c73b4e))
* rename field site-area in site-area module to site-area-in-hectares (commit [abd3c46](https://github.com/digital-land/planning-application-data-specification/commit/abd3c464f465fdd880716de7df8da21ddcde89e8))
* update development-phase, only looking for a single phase of development (commit [00e3de6](https://github.com/digital-land/planning-application-data-specification/commit/00e3de662de278e44198637b4e1243f4603e66b8))
* add declarative version of dev-type module (commit [39ef287](https://github.com/digital-land/planning-application-data-specification/commit/39ef287c9592fc49145509e28112eae1de8aabe8))
* add declarative version of lb-grade module (commit [dd305af](https://github.com/digital-land/planning-application-data-specification/commit/dd305af89962b96f2a03c8823cd356bbc088fafb))
* add declarative version of immunity-from-listing (commit [2b54832](https://github.com/digital-land/planning-application-data-specification/commit/2b54832f0201760d318d6a58be93041d8ff7fe5d))
* add yes-no-unknown codelist (commit [9f3a382](https://github.com/digital-land/planning-application-data-specification/commit/9f3a3827347b97f401b2dc3dcd4f9c70786e923f))

### 🐛 Bug Fixes

* add missing declarative version of lb-grade module (commit [53afd5b](https://github.com/digital-land/planning-application-data-specification/commit/53afd5b167661d8c8b0409f74c34f7768ce1910c))
* all failing field checks (commit [bf9bc11](https://github.com/digital-land/planning-application-data-specification/commit/bf9bc11146d9184cd11be0640402932e9b76ecf9))

### 📚 Documentation

* decided to use enum instead of nullable boolean field (commit [ea12e96](https://github.com/digital-land/planning-application-data-specification/commit/ea12e9630a2738f5534a1fa7b32f3f1f5712ab67))


<a name="v0.1.14"></a>
## [v0.1.14](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.13...v0.1.14) (2025-07-01)

Define the consent-under-tpo application

### 𝌭 Model changes

* add declarative version of trees-additional module (commit [239d38b](https://github.com/digital-land/planning-application-data-specification/commit/239d38be4ba9897183316a1bc28786a1abb66ae7))
* add is-site-different field for clarity (commit [e20cc09](https://github.com/digital-land/planning-application-data-specification/commit/e20cc097c53e1191fbcc6b785408d0eeb2268ed3))
* add declarative version of trees-location module (commit [3857490](https://github.com/digital-land/planning-application-data-specification/commit/3857490e07d0ac88e85a665672103b8fca28d901))
* add declarative version of trees-ownership module (commit [ce19354](https://github.com/digital-land/planning-application-data-specification/commit/ce193541c801347a3a8cac7f6992212eba1763a3))
* add declarative version of tree-work-details module (commit [92fefcb](https://github.com/digital-land/planning-application-data-specification/commit/92fefcb96c08764ec4d7085b98754b59de2018a6))
* add declarative version of tpo module (commit [01334f6](https://github.com/digital-land/planning-application-data-specification/commit/01334f6ab71ca43ff370d65538768221a4d798d2))
* rename field from demolition-part to is-partial-demolition (commit [6a12076](https://github.com/digital-land/planning-application-data-specification/commit/6a12076705915edf74a3322e374e9b2dd47623ed))
* rename field from demolition-building-in-curtilage to is-demolishing-building-in-curtilage (commit [ddad61a](https://github.com/digital-land/planning-application-data-specification/commit/ddad61a27f48d2768f0479c44498cfc5f5af812e))
* rename field from demolition-total to is-total-demolition (commit [50578c0](https://github.com/digital-land/planning-application-data-specification/commit/50578c0b6c94cec2a2570eb46f0f39911870e7ee))
* rename field from demolition to is-proposing-demolition (commit [2bfd30a](https://github.com/digital-land/planning-application-data-specification/commit/2bfd30a6cb1b2c06760d0d3f4d8bbd01033aaab2))
* add declarative version of demolition module (commit [3508417](https://github.com/digital-land/planning-application-data-specification/commit/3508417df02f124a234a6e6f0583708f38018b66))
* add declarative version of demolition-reason module (commit [de83ef8](https://github.com/digital-land/planning-application-data-specification/commit/de83ef8c922c6fcd666deb95e24b58d21f0b04dc))
* field in demolition-reason should be called reason (commit [12368ec](https://github.com/digital-land/planning-application-data-specification/commit/12368ec532023ab823fc1f407ad30a11888bc776))
* rename field, post-code to postcode (commit [9d7d709](https://github.com/digital-land/planning-application-data-specification/commit/9d7d7091ebb42f4a7405d472c9d897034688b391))

### 👷‍♀️ Application changes

* remove trees-location module from consent-under-tpo applications (commit [3559c12](https://github.com/digital-land/planning-application-data-specification/commit/3559c129a5c1756c716ef020dde23b32460c94be))
* define the consent-under-tpo application (commit [06b3721](https://github.com/digital-land/planning-application-data-specification/commit/06b37216f5811431c2f463bf728381ab7f2c440b))


<a name="v0.1.13"></a>
## [v0.1.13](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.12...v0.1.13) (2025-06-26)

Resolving consistency of contact-details for PIP applications

### 𝌭 Model changes

* regenerate compiled spec for PIP applications (commit [ff7f01e](https://github.com/digital-land/planning-application-data-specification/commit/ff7f01e3a425ee7b830278fe7a31ed7c7c6a1aa6))
* keep contact details separate from details modules in PiP applications, see issue [#294](https://github.com/digital-land/planning-application-data-specification/issues/294) (commit [e4166ec](https://github.com/digital-land/planning-application-data-specification/commit/e4166ecd844b354a73ab6740915cc2f68eb3be98))
* add declarative version of proposal-details-inc-non-residential module (commit [663cb20](https://github.com/digital-land/planning-application-data-specification/commit/663cb20c3f9cf8b9b273b363ebab648c132fbc90))
* add declarative version of site-info module (commit [779e29c](https://github.com/digital-land/planning-application-data-specification/commit/779e29c5a64d0a64d48b915001e3241ca3a7f3c7))
* update supporting document part of site-info to be consistent with other instances (commit [d411aed](https://github.com/digital-land/planning-application-data-specification/commit/d411aed4187bd5f64980099dc129ecd4079e6704))

### 👷‍♀️ Application changes

* add agent and applicant contact modules to pip application (commit [fd40df3](https://github.com/digital-land/planning-application-data-specification/commit/fd40df33f4073e2ea016c625dadc18c1b9dbc6aa))
* add declarative version of pip application (commit [d963d5c](https://github.com/digital-land/planning-application-data-specification/commit/d963d5c0c2292db981140e0adec780258cd33d98))

### 📚 Documentation

* regenerate a single file with all modules (commit [ed29c12](https://github.com/digital-land/planning-application-data-specification/commit/ed29c12875ded51634fa3896b99ea38007715333))


<a name="v0.1.12"></a>
## [v0.1.12](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.11...v0.1.12) (2025-06-26)

resolving issues and improving field names

### 𝌭 Model changes

* rename field from householder-development to is-householder-development (commit [2dd5944](https://github.com/digital-land/planning-application-data-specification/commit/2dd5944f2b7bae4332abd35877ddc388dd6e0a1e))
* rename field from development-started to has-development-started (commit [80a75ab](https://github.com/digital-land/planning-application-data-specification/commit/80a75ab81977895dd1e327fbe4edaf437a9c4767))
* rename field from development-completed to has-development-completed (commit [3483c90](https://github.com/digital-land/planning-application-data-specification/commit/3483c9058de74816f396609413fb43e1ae68c551))
* rename field completion-date to development-completed-date (commit [f62cbcc](https://github.com/digital-land/planning-application-data-specification/commit/f62cbccdd75bc8aa549723a75325700248c88ee0))
* rename field start-date to development-start-date (commit [d994510](https://github.com/digital-land/planning-application-data-specification/commit/d994510b2dbfc95baadb23ca4d431d15fdf3864f))
* create declarative version of desc-your-proposal module (commit [851ad0d](https://github.com/digital-land/planning-application-data-specification/commit/851ad0d9b8f577212f64a025dcd59a55fac47060))
* use same fields as existing related-proposal component (commit [2587d0b](https://github.com/digital-land/planning-application-data-specification/commit/2587d0b73ca65e6a9e7fe86321e10c041a17d671))
* rename field, disposal-required to is-disposal-required (commit [ec3bf48](https://github.com/digital-land/planning-application-data-specification/commit/ec3bf4846a173443414b3079948acadf1688947b))
* add declarative version of trade-effluent module (commit [4d6a320](https://github.com/digital-land/planning-application-data-specification/commit/4d6a320cdad9c0213f32d0ed3d43172c943d3682))
* add declarative version of vol-agreement module (commit [78a29ad](https://github.com/digital-land/planning-application-data-specification/commit/78a29adc2f2a88697ac3b5709e885355525ced86))
* declarative version of supporting-info module (commit [147a024](https://github.com/digital-land/planning-application-data-specification/commit/147a0246947b53370810315b333185ff4a636610))
* rename contact to contact-reference (commit [48959fc](https://github.com/digital-land/planning-application-data-specification/commit/48959fca0f2f498a8ea293a8e20c378081c44194))

### 🐛 Bug Fixes

* typo (commit [b1f5a1d](https://github.com/digital-land/planning-application-data-specification/commit/b1f5a1d1bc31435d03cdd4c63a5bfa622f6c55c5))
* integrity checks picks up ill formed required-if conditions (commit [23445b5](https://github.com/digital-land/planning-application-data-specification/commit/23445b5479d2733a96ebeff17ca453377d9b3e5c))

### 📚 Documentation

* add note about trade-effluent from policy (commit [66b15df](https://github.com/digital-land/planning-application-data-specification/commit/66b15df054cd9a90b38e27e8d667e95b66339afe))
* tweaks to the documentation for declarative model (commit [ca988b5](https://github.com/digital-land/planning-application-data-specification/commit/ca988b5d8cf997a11d52e3ebc6837872df568e80))
* add documentation for the application interface (commit [94c2fef](https://github.com/digital-land/planning-application-data-specification/commit/94c2fef57033071df7cbca3a0b544aa0c464fc84))


<a name="v0.1.11"></a>
## [v0.1.11](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.1...v0.1.11) (2025-06-20)

Responding to answers we got from DM policy

### 𝌭 Model changes

* add a user-role field to agent-details module (commit [8a37e1b](https://github.com/digital-land/planning-application-data-specification/commit/8a37e1bf70d8a866b80134300a7ff16167f4f9a0))

### 👷‍♀️ Application changes

* add the conflict of interest module to prior approval applications [non-declarative] (commit [0c1964c](https://github.com/digital-land/planning-application-data-specification/commit/0c1964c61b8b4d592b60885145fe6adb2fa00d1f))
* add the conflict of interest module to approval of conditions applications [non-declarative] (commit [ad51e23](https://github.com/digital-land/planning-application-data-specification/commit/ad51e23567dd6ea17140f30be076c9a7d8ba144e))
* add the conflict of interest module to s73 applications [non-declarative] (commit [91056cb](https://github.com/digital-land/planning-application-data-specification/commit/91056cb5f41438ba943d71d6cb3c405b1acb56e6))


<a name="v0.1.1"></a>
## [v0.1.1](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.0...v0.1.1) (2025-06-20)

First declarative model implementation for hh applications

### ⚒️ Tooling

* add integrity checks for application configuration (commit [d34f7fb](https://github.com/digital-land/planning-application-data-specification/commit/d34f7fbbbaa50465ac00a6a8bc7d7d268438810a))
* add some basic checks for declarative model (commit [43dea70](https://github.com/digital-land/planning-application-data-specification/commit/43dea70f786333796bb284852fc7b014aa1ca139))

### 𝌭 Model changes

* create declarative pieces for top level application fields (commit [053837d](https://github.com/digital-land/planning-application-data-specification/commit/053837d1b5fc0f0e0f0a3d010b94ac60dbfbe9fa))
* add missing field definition for newspaper-notices (commit [a618bbe](https://github.com/digital-land/planning-application-data-specification/commit/a618bbe6fb2716c81a730812844b7d21baa3ba8f))
* rename falling-trees-risk field to has-falling-trees-risk (commit [fd74efb](https://github.com/digital-land/planning-application-data-specification/commit/fd74efbda6a340e4881ac4ebc0a6b670097ce065))

### 🐛 Bug Fixes

* add missing end-date attr to module definitions (commit [145f6b4](https://github.com/digital-land/planning-application-data-specification/commit/145f6b42a2ca01361ba04b24a5c5417f77cd4b78))
* correct typo to building-elements (commit [ba337f0](https://github.com/digital-land/planning-application-data-specification/commit/ba337f0e814dd91516d5e8c892ad61c2b95a9685))

### 👷‍♀️ Application changes

* define the hh application (commit [b2cf2c7](https://github.com/digital-land/planning-application-data-specification/commit/b2cf2c76937f90eb6fe76f20cf0ae710cbccebae))


<a name="v0.1.0"></a>
## v0.1.0 (2025-06-18)

MHCLG worked with the planning community to develop a set of specifications for the submission of planning applications. A first draft of these specifications was completed by the end of March 2025. We they asked for feedback on them. This feedback window finished on 16 May 2025. Since then we have been turning the feedback into issues to be worked through.

