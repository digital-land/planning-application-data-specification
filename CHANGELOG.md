
<a name="v0.1.67"></a>
## [v0.1.67](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.66...v0.1.67) (2026-03-24)

Align mhclg and gla housing types

### ⚒️ Tooling

* add housing type hierarchy (commit [256c1edb](https://github.com/digital-land/planning-application-data-specification/commit/256c1edbbc06b442381191bafc2f8f4241c428fa))

### 𝌭 Model changes

* add the housing-type usage table (commit [0a796506](https://github.com/digital-land/planning-application-data-specification/commit/0a7965069e7f667fa44ce6788c19ea00339d538a))
* define housing type usage table (commit [2d9d5ed3](https://github.com/digital-land/planning-application-data-specification/commit/2d9d5ed3efc54204cb460b54b2fe91bf42ab9179))

### 📚 Documentation

* document the usage pattern when value used across multiple profiles (commit [4beb0bdc](https://github.com/digital-land/planning-application-data-specification/commit/4beb0bdc15d82c4aef6647a18c16c2829ed56ea9))


<a name="v0.1.66"></a>
## [v0.1.66](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.65...v0.1.66) (2026-03-24)

Improve the operational days model

### 𝌭 Model changes

* retire day-type field and codelist (commit [ca923f31](https://github.com/digital-land/planning-application-data-specification/commit/ca923f31069159202796eea08144f3e5e11ceb47))
* update operational-days to use schedule-days (commit [86397501](https://github.com/digital-land/planning-application-data-specification/commit/86397501c63382b50bbf758fe949a6da35dc4252))
* define schedule-days field (commit [7455d42d](https://github.com/digital-land/planning-application-data-specification/commit/7455d42d5aec33775b1e1713ca07240f0e35b958))
* add schedule-day codelist (commit [3ef399e6](https://github.com/digital-land/planning-application-data-specification/commit/3ef399e6eb727611d1b7001d216b395361fd8425))

### 🐛 Bug Fixes

* examples using operational-days (commit [ed59ab20](https://github.com/digital-land/planning-application-data-specification/commit/ed59ab2071cb3ce57dfd586bcda0bef088b6a08c))

### 📚 Documentation

* add decision record for operational days component change (commit [a8529ebb](https://github.com/digital-land/planning-application-data-specification/commit/a8529ebb509523c75b0eb641f56503d0c60183f9))


<a name="v0.1.65"></a>
## [v0.1.65](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.64...v0.1.65) (2026-03-24)

refactor and refine

### ⚒️ Tooling

* commandline interface to find existing forms (commit [e9b613fd](https://github.com/digital-land/planning-application-data-specification/commit/e9b613fd9be7615c03d3191e622e2b453088748e))
* Moved the two 2025 analysis CSVs (commit [b42cb31a](https://github.com/digital-land/planning-application-data-specification/commit/b42cb31a586a62dad266b6fa57c14cf1aa2ff64e))
* return fresh loader data on each call (commit [07a73e81](https://github.com/digital-land/planning-application-data-specification/commit/07a73e810c75ce4125bd48487310871705c0c63a))
* add integrity checks for usage tables (commit [af4e8b3c](https://github.com/digital-land/planning-application-data-specification/commit/af4e8b3c2be14753c50121ac4ed84dd4f9571fff))

### 𝌭 Model changes

* remove application-types from tenure type codelist (commit [86cda80c](https://github.com/digital-land/planning-application-data-specification/commit/86cda80c5f4e60a1e549b80746da96b3eb84518d))
* add tenure type usage details to usage table (commit [c1a6d1c0](https://github.com/digital-land/planning-application-data-specification/commit/c1a6d1c0c33f9193e2e36861e85cf95bf374ec4d))
* define the tenure type codelist usage table (commit [6f8b9fb6](https://github.com/digital-land/planning-application-data-specification/commit/6f8b9fb64a2506076edd54969cf8af785dc25ec6))
* add profile codelist (commit [c6aed60f](https://github.com/digital-land/planning-application-data-specification/commit/c6aed60fc873e3bfb5f15adac9f1137f9d68771d))

### 🐛 Bug Fixes

* inconsistencies after file model change (commit [8b626a44](https://github.com/digital-land/planning-application-data-specification/commit/8b626a441b2c96c53a4a4139b1b2399836f1798b))
* incorrect need status (commit [ee556073](https://github.com/digital-land/planning-application-data-specification/commit/ee556073ab0c61b07fb061cb528996993f860299))

### 📚 Documentation

* document the commandline interface (commit [c342d427](https://github.com/digital-land/planning-application-data-specification/commit/c342d4274ed30e9ac61fc8ac22746a9ddef75045))
* add note about codelist usage to main specification README (commit [b1db6d41](https://github.com/digital-land/planning-application-data-specification/commit/b1db6d41f2b85e6e974c5cc6e40b6d708b8c60c3))
* document the codelist usage pattern, as seen in tenure-types (commit [3322cc8c](https://github.com/digital-land/planning-application-data-specification/commit/3322cc8c9286fa1a63a7c7c6e2558a07b7b478db))


<a name="v0.1.64"></a>
## [v0.1.64](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.63...v0.1.64) (2026-03-23)

align tenure types with GLA

### ⚒️ Tooling

* add integrity checks for usage tables (commit [c7f17e1d](https://github.com/digital-land/planning-application-data-specification/commit/c7f17e1de1e08a061aad5f7ae87aafa079c523ad))

### 𝌭 Model changes

* remove application-types from tenure type codelist (commit [26f26a01](https://github.com/digital-land/planning-application-data-specification/commit/26f26a01ebeae8c9825e9e2da5a9eac9dd7d357b))
* add tenure type usage details to usage table (commit [ca98373e](https://github.com/digital-land/planning-application-data-specification/commit/ca98373ee8f6eb6e170d0e015d92578c019d7b6d))
* define the tenure type codelist usage table (commit [d79fb5ee](https://github.com/digital-land/planning-application-data-specification/commit/d79fb5ee3dbe1bb3b664aeb84ed78095ef154d2b))
* add profile codelist (commit [b384d2cf](https://github.com/digital-land/planning-application-data-specification/commit/b384d2cf0db383129befbd2d6004fb8e059d9139))
* add child GLA tenure types to tenure type codelist (commit [afa2c00f](https://github.com/digital-land/planning-application-data-specification/commit/afa2c00f03bdd46315dfac76adac73df651c7662))
* add parent field to tenure-type codelist (commit [44e148eb](https://github.com/digital-land/planning-application-data-specification/commit/44e148eb4cfee765883ec3cd484f625465b3a55c))

### 📚 Documentation

* add note about codelist usage to main specification README (commit [630a3336](https://github.com/digital-land/planning-application-data-specification/commit/630a33363b4b0829c43ccc1d02cc9da5dd03a4d9))
* document the codelist usage pattern, as seen in tenure-types (commit [2d72e881](https://github.com/digital-land/planning-application-data-specification/commit/2d72e88194b05db5c1043edf28c1acc82369d102))


<a name="v0.1.63"></a>
## [v0.1.63](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.62...v0.1.63) (2026-03-17)

rework tool to extract open issues

### ⚒️ Tooling

* change daily issue export schedule (commit [8e16ae50](https://github.com/digital-land/planning-application-data-specification/commit/8e16ae50d736435d62ac612fb009d5d3d3ce0c6e))
* add exported open issue datasets (commit [02c7c79f](https://github.com/digital-land/planning-application-data-specification/commit/02c7c79fea63e7e3b3eba83e4d829e24cc8eb753))
* fail on GitHub issue fetch errors (commit [5afb0254](https://github.com/digital-land/planning-application-data-specification/commit/5afb02542e10ac266e4f9d1c6a0581f425c99b9e))
* remove retired issue tracking pipeline (commit [3816829b](https://github.com/digital-land/planning-application-data-specification/commit/3816829b88ce192d26e2cb86e11cc22da2dbd72e))
* wire issue export into automation (commit [b39e8b80](https://github.com/digital-land/planning-application-data-specification/commit/b39e8b80e5a230c704bff740c09997f9472960c2))
* refactor GitHub issue exporter (commit [29943b06](https://github.com/digital-land/planning-application-data-specification/commit/29943b06484a574e91005bb22c7d8a748374c40a))

### 🐛 Bug Fixes

* tenure type csv (commit [fdf4b977](https://github.com/digital-land/planning-application-data-specification/commit/fdf4b9774a9da3f72e2c5e05d58fcb1c22b188b1))

### 📚 Documentation

* adding another need (commit [e3c7c3ba](https://github.com/digital-land/planning-application-data-specification/commit/e3c7c3ba216b111425d123e555184a9e35f9b2ba))
* add a series of needs extracted from community sessions (commit [d964b340](https://github.com/digital-land/planning-application-data-specification/commit/d964b3407c4b304c5d825e6459802326f35facd7))


<a name="v0.1.62"></a>
## [v0.1.62](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.61...v0.1.62) (2026-03-13)

Track level of completeness of submission spec relative to application volumes

### ⚒️ Tooling

* update spec.py to reuse structure in completeness.py (commit [96e42c20](https://github.com/digital-land/planning-application-data-specification/commit/96e42c20d5f45ebebf1e736e9db9ea3acd896e65))
* add notes to progress page (commit [c1a05b98](https://github.com/digital-land/planning-application-data-specification/commit/c1a05b98bb6fe1fc1d460c201ccbecb1b466311b))
* add a section explaining how scope was decided (commit [f19d69ad](https://github.com/digital-land/planning-application-data-specification/commit/f19d69ad1f084bb44784e164f6549bd74461076a))
* add breakdown by app type to progress page (commit [8026d624](https://github.com/digital-land/planning-application-data-specification/commit/8026d624a38430cb58f7553f6777d20a18f30600))
* render progress page to display coverage (commit [742bd8e5](https://github.com/digital-land/planning-application-data-specification/commit/742bd8e5620645f63f1995013d7dcc56b3531436))
* provide verbose breakdown of what is and is not currently covered by spec (commit [90e95da1](https://github.com/digital-land/planning-application-data-specification/commit/90e95da1719a2784d3e820923aac2f2788650351))
* handle split of tree works app in completeness calc (commit [3faa807c](https://github.com/digital-land/planning-application-data-specification/commit/3faa807c242208dd0001a4b98a3400b090a2c976))
* add command to calc submission coverage of scope (commit [3ebb2bda](https://github.com/digital-land/planning-application-data-specification/commit/3ebb2bda086e44ddfcfb621d271a0f2183b2450f))
* add script to workout which volume records are in scope based on scoping criteria (commit [f553c54d](https://github.com/digital-land/planning-application-data-specification/commit/f553c54d82d61e76392c46f9bff336f196889ff6))

### 🐛 Bug Fixes

* logic of in or out scope evaluation (commit [8e5b6a18](https://github.com/digital-land/planning-application-data-specification/commit/8e5b6a1816e1e1c5221d9cf544961072f5c4d445))
* remove duplicate form record (commit [a5335ad2](https://github.com/digital-land/planning-application-data-specification/commit/a5335ad225961a197f778cbf84cb243055022caa))

### 📚 Documentation

* add volume data from 2024 (commit [e2728dae](https://github.com/digital-land/planning-application-data-specification/commit/e2728daef5b12ba7c7b43793083867f6914157a0))
* add decision record for hierarchical codelists (commit [0413d98a](https://github.com/digital-land/planning-application-data-specification/commit/0413d98af9f6b1dd244d8ca7a5a874bffd7d1433))


<a name="v0.1.61"></a>
## [v0.1.61](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.60...v0.1.61) (2026-03-10)

Combine application types and subtypes into one codelist

### ⚒️ Tooling

* make check runner easier to scan (commit [11696023](https://github.com/digital-land/planning-application-data-specification/commit/11696023e7e6a3720a3f6d810ea1c19fbfb4a096))
* small refactor of specifciation check code (commit [9f2999da](https://github.com/digital-land/planning-application-data-specification/commit/9f2999dab37fc7f11c831a7d9d8446a90f60e4a4))
* link to form to propose need if search yields not results (commit [7ad1cbe9](https://github.com/digital-land/planning-application-data-specification/commit/7ad1cbe9b19242d01a08906bdc3af11dc46773c8))
* remove subtype from json schema (commit [16e822eb](https://github.com/digital-land/planning-application-data-specification/commit/16e822eb91e41d253b2813483a8a9503f2096c22))
* expand codelist checker tests (commit [5175f979](https://github.com/digital-land/planning-application-data-specification/commit/5175f979ad9a2a7998525b1f4e446410b2cb0cf5))
* Split codelist integrity checks (commit [3a4a3d31](https://github.com/digital-land/planning-application-data-specification/commit/3a4a3d31acdd051f4a4f1e2e9749a8b0d3bb102d))
* add test to make sure parent field in codelist refers to existing entry in file (commit [48f8b660](https://github.com/digital-land/planning-application-data-specification/commit/48f8b6607679b9264c8ff38655e6dc6439f687c9))

### 𝌭 Model changes

* remove application-sub-type field (commit [ae581707](https://github.com/digital-land/planning-application-data-specification/commit/ae5817078b8b2de9cf7f1cd48fca3c45863c3451))
* remove subtye condition (commit [07846f68](https://github.com/digital-land/planning-application-data-specification/commit/07846f68a88ef197365bffd26cad07c585887e17))
* merge application type and subtype codelists (commit [750e6686](https://github.com/digital-land/planning-application-data-specification/commit/750e6686f651c4156e7d554448b5063f01bd64ce))

### 🐛 Bug Fixes

* erroneous example (commit [f4c1deeb](https://github.com/digital-land/planning-application-data-specification/commit/f4c1deeb1ebe4edfc6c7e9a3d5e6fc536d4b3ad3))

### 👷‍♀️ Application changes

* add remaining prior approval and change of use applications to codelist (commit [7a3883fc](https://github.com/digital-land/planning-application-data-specification/commit/7a3883fcab2c3d6555a547d7c279cfe40096f5d1))

### 📚 Documentation

* remove reference to subtypes (commit [4bf0a678](https://github.com/digital-land/planning-application-data-specification/commit/4bf0a678228f3542392113adc518b97b12738f9f))
* add hierarchical codelist pattern with parent field (commit [be73dde6](https://github.com/digital-land/planning-application-data-specification/commit/be73dde602d8fa10884d729096b2d288bbd4ca01))


<a name="v0.1.60"></a>
## [v0.1.60](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.59...v0.1.60) (2026-03-09)

Minor refactoring

### ⚒️ Tooling

* make check runner easier to scan (commit [dcf669d3](https://github.com/digital-land/planning-application-data-specification/commit/dcf669d33e28a8ee3a0f449fd1aca7ff6bfe68d7))
* small refactor of specifciation check code (commit [ba78ce41](https://github.com/digital-land/planning-application-data-specification/commit/ba78ce41fa55fb51f0f503f80fe02ec8616a65c4))
* link to form to propose need if search yields not results (commit [3ec184c3](https://github.com/digital-land/planning-application-data-specification/commit/3ec184c310deae5f05a425589915cd655a0c1709))
* add satisfied-by section to justification section on need pages (commit [ce93c758](https://github.com/digital-land/planning-application-data-specification/commit/ce93c758572e09cbfcadb14ebc855ab070af42a1))
* make satisfied-by chips links (commit [bcca2fac](https://github.com/digital-land/planning-application-data-specification/commit/bcca2facb826c80baab424553b8537ad7bf69a18))
* tweak layout of static site homepage for easier reading (commit [bd63035a](https://github.com/digital-land/planning-application-data-specification/commit/bd63035a49a72923f85ff7226613d1bb81f890ee))
* include listing codelists in outputs (commit [ef4c3166](https://github.com/digital-land/planning-application-data-specification/commit/ef4c3166ee760bdb04c196605549edfb9603b8b1))
* add make target to output lists of elements of spec (commit [98ef79c8](https://github.com/digital-land/planning-application-data-specification/commit/98ef79c8ea6d2fbee8cfd447bbedc522933fab28))
* output list of elements of the spec (commit [1e9fc334](https://github.com/digital-land/planning-application-data-specification/commit/1e9fc3342381d7d5cb11a4cb1ed112c4359f26f8))

### 🐛 Bug Fixes

* rename file to match field identifier (commit [125d9a5c](https://github.com/digital-land/planning-application-data-specification/commit/125d9a5c0f8bd6009c7bd7b5ba566e5e79f7a6e6))
* rename codelist field to match identifier (commit [8a303cc6](https://github.com/digital-land/planning-application-data-specification/commit/8a303cc60086db3a725c684ba5323a054782d6cc))
* required-if blocks refer to correct fields (commit [0b22798f](https://github.com/digital-land/planning-application-data-specification/commit/0b22798f4c3222aecd5f9ff1f9b9eb244f1b3c2c))
* integrity checks should match require-if field references to local fields list (commit [a7c06ca5](https://github.com/digital-land/planning-application-data-specification/commit/a7c06ca5efc7a2166fd3db0fd5dfadcc8de852aa))

### 📚 Documentation

* add short description of dataset schema origin (commit [6618b4a6](https://github.com/digital-land/planning-application-data-specification/commit/6618b4a68913a4466adf9a1bace6c63086c3547a))
* save outputted element lists (commit [0685e4d3](https://github.com/digital-land/planning-application-data-specification/commit/0685e4d35f228303b723b4f81555abf5f9dff399))


<a name="v0.1.59"></a>
## [v0.1.59](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.58...v0.1.59) (2026-02-26)

Refinement of static site in preparation for sharing at Feb community session

### ⚒️ Tooling

* add satisfied-by section to justification section on need pages (commit [7ad72a89](https://github.com/digital-land/planning-application-data-specification/commit/7ad72a89df69efe542400a3901ec57a9dbf155ff))
* make satisfied-by chips links (commit [b1448c1c](https://github.com/digital-land/planning-application-data-specification/commit/b1448c1c89f754cc1d70a5db922b41928953c531))
* tweak layout of static site homepage for easier reading (commit [a8fde170](https://github.com/digital-land/planning-application-data-specification/commit/a8fde170f93248f12f0d90067884550464bb3584))
* include listing codelists in outputs (commit [5d181a23](https://github.com/digital-land/planning-application-data-specification/commit/5d181a2393e20f0ce3e9c2388983a394cde39d5e))
* add make target to output lists of elements of spec (commit [cb865b98](https://github.com/digital-land/planning-application-data-specification/commit/cb865b98e45a52009adb1dc7021b241577559cb0))
* output list of elements of the spec (commit [60844b5a](https://github.com/digital-land/planning-application-data-specification/commit/60844b5a4dc03f3f47c36443e2a8d7a6df3b2f50))
* link from field details pages to raw schema in repo (commit [446f0ebf](https://github.com/digital-land/planning-application-data-specification/commit/446f0ebf6a22ac2b762ace2a013428324714c992))
* render field pages in static site (commit [699882b7](https://github.com/digital-land/planning-application-data-specification/commit/699882b7a48e824e4f132cb261df2885c8e8a4bc))
* add a shared-elements section to static site (for fields and codelists) (commit [d3a9ee01](https://github.com/digital-land/planning-application-data-specification/commit/d3a9ee01a754f1355f0e562873d2eb7833d6220c))
* add codelists section (commit [3ab88665](https://github.com/digital-land/planning-application-data-specification/commit/3ab88665cd02a31c153e5561d495ea0a3b9ab059))
* stub component pages (commit [0e9a254c](https://github.com/digital-land/planning-application-data-specification/commit/0e9a254cd468eb23c433363076102283a35c23b9))
* use ModuleDef for module lists (commit [2e6361ed](https://github.com/digital-land/planning-application-data-specification/commit/2e6361ed870292f7b0704b6cc83e3b8feb736656))
* restructure the module details page (commit [048e626d](https://github.com/digital-land/planning-application-data-specification/commit/048e626dfb20df661b8b0a8e2e6349748a284916))
* add copy-assets target to makefile (commit [b668aa25](https://github.com/digital-land/planning-application-data-specification/commit/b668aa257710e7a9cf3e1d5dda247e6b23e87b2d))
* Refactor static site rendering to use resolved field views and support nested components (commit [1a43c7d4](https://github.com/digital-land/planning-application-data-specification/commit/1a43c7d4e5f1cabdbb824bdf19ffc1628e3c3ffa))
* tweak layout of the application schema pages (commit [899d1d95](https://github.com/digital-land/planning-application-data-specification/commit/899d1d95f2b596e6920167d7d4b2d966aed8cc84))
* add js filtering to user needs list (commit [2ec49a74](https://github.com/digital-land/planning-application-data-specification/commit/2ec49a74c9672399e41c9eb82e2a2a87039ce6a2))
* tweak layout of the list of user needs (commit [725a243d](https://github.com/digital-land/planning-application-data-specification/commit/725a243d33381bdc347383d3b681570b5820401d))

### 🐛 Bug Fixes

* url to the need-filters js (commit [58451cc7](https://github.com/digital-land/planning-application-data-specification/commit/58451cc7a080922b01cbc29502548b84a0082ac4))
* extra comma in csv (commit [20676e7c](https://github.com/digital-land/planning-application-data-specification/commit/20676e7cf5bface2ec3c786a11f1485026781436))
* links from application page to module (commit [cf00608d](https://github.com/digital-land/planning-application-data-specification/commit/cf00608de60182e875b5818039bd69cb9e729962))
* remove unused outputs (commit [a28161e0](https://github.com/digital-land/planning-application-data-specification/commit/a28161e079d6e4364392110e28423224caafaefd))
* typology attr on dataset schemas (commit [205d77bc](https://github.com/digital-land/planning-application-data-specification/commit/205d77bc539b98e517e19cab96ba4ccc0939b04c))

### 📚 Documentation

* add short description of dataset schema origin (commit [834de623](https://github.com/digital-land/planning-application-data-specification/commit/834de623a74064fb4fe99bfd3e569da4cfcc20df))
* save outputted element lists (commit [285d9715](https://github.com/digital-land/planning-application-data-specification/commit/285d9715defa001f4a92b00bb2dbd8244b13eb69))
* Fix formatting in README.md for clarity (commit [a377748e](https://github.com/digital-land/planning-application-data-specification/commit/a377748ee7b28b245c52159212d0be79473578bc))


<a name="v0.1.58"></a>
## [v0.1.58](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.57...v0.1.58) (2026-02-17)

Flesh out more of static site

### ⚒️ Tooling

* link from field details pages to raw schema in repo (commit [29cefb09](https://github.com/digital-land/planning-application-data-specification/commit/29cefb098559741768d872bf05acde991cc04fc5))
* render field pages in static site (commit [d40b00a1](https://github.com/digital-land/planning-application-data-specification/commit/d40b00a1bbbf10f679725c33e2535fc73c87cdb1))
* add a shared-elements section to static site (for fields and codelists) (commit [1040a235](https://github.com/digital-land/planning-application-data-specification/commit/1040a235de1905ded9d7fe02a79b6d7302097106))
* add codelists section (commit [8e26375c](https://github.com/digital-land/planning-application-data-specification/commit/8e26375c5f99ea90f677badd6ce73337cdb20a30))
* stub component pages (commit [7d9e43c8](https://github.com/digital-land/planning-application-data-specification/commit/7d9e43c868b922d9a77116fd648e3e49820168d2))
* use ModuleDef for module lists (commit [00da068e](https://github.com/digital-land/planning-application-data-specification/commit/00da068ec15c8f7abfd70842d170f864f3db7d80))
* restructure the module details page (commit [eba120fc](https://github.com/digital-land/planning-application-data-specification/commit/eba120fc1cfef161a957f05ab141b39251bd5230))
* add copy-assets target to makefile (commit [33d68f4d](https://github.com/digital-land/planning-application-data-specification/commit/33d68f4ddc0c983bfdf1fb30a3b48d786ac1d55a))
* Refactor static site rendering to use resolved field views and support nested components (commit [b12e725a](https://github.com/digital-land/planning-application-data-specification/commit/b12e725abee2358b70a62c0de0e69b9522df47f6))
* tweak layout of the application schema pages (commit [8c0fb87a](https://github.com/digital-land/planning-application-data-specification/commit/8c0fb87acc4dea7514161aae2cf6848fda10d969))
* add js filtering to user needs list (commit [158f8762](https://github.com/digital-land/planning-application-data-specification/commit/158f87621b28598dabe15d6edcbf299d36850285))
* tweak layout of the list of user needs (commit [bee8c52a](https://github.com/digital-land/planning-application-data-specification/commit/bee8c52a4ea1ce320891b8e3327427c0630775b1))
* add breadcrumbs to needs and justification pages (commit [b8e6949a](https://github.com/digital-land/planning-application-data-specification/commit/b8e6949a3787d646aa40a8e97adf7edd4afd5cdb))
* display breakdown of what combination of fields and datasets satisfy a need in justification record pages (commit [aa9b1170](https://github.com/digital-land/planning-application-data-specification/commit/aa9b11708466f263f244f043910d918c21756a72))
* add search/filter functionality to user needs page (commit [1dde7aae](https://github.com/digital-land/planning-application-data-specification/commit/1dde7aae23e852d34d3401ea68e66a232f5fa1f7))

### 🐛 Bug Fixes

* typology attr on dataset schemas (commit [43753fd5](https://github.com/digital-land/planning-application-data-specification/commit/43753fd5eb6237cb219574882fef264e25622f69))
* url to justification index page (commit [14b4f3d9](https://github.com/digital-land/planning-application-data-specification/commit/14b4f3d92ce972b1e9cd6236c0b78c719eb4d90a))
* output generator (commit [d06aebda](https://github.com/digital-land/planning-application-data-specification/commit/d06aebdaa6bcad309ece715e313fbf82dd316d1b))


<a name="v0.1.57"></a>
## [v0.1.57](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.56...v0.1.57) (2026-01-29)

Docs and timeline for decisions

### ⚒️ Tooling

* extend cli find command to included finding where component is used (commit [18dc4dbe](https://github.com/digital-land/planning-application-data-specification/commit/18dc4dbea0f2d4fc947ee5a2633c2c6f5af40340))
* cli to output url to existing form for each application type (commit [fd03e093](https://github.com/digital-land/planning-application-data-specification/commit/fd03e0936c7b1533124c34f1f5b4166813e74fbd))

### 𝌭 Model changes

* add semantic annotations to decision-condition dataset (commit [fec3721f](https://github.com/digital-land/planning-application-data-specification/commit/fec3721f5a32efaa704f3abb1aeedf12e22e7e83))
* add semantic annotations to planning-condition dataset (commit [8f722d22](https://github.com/digital-land/planning-application-data-specification/commit/8f722d2201296e1be56f74d9f410c7873cebd63c))
* add semantic annotation to reference field (commit [630a2fa5](https://github.com/digital-land/planning-application-data-specification/commit/630a2fa5fe4cb239e6992c3eb43e65c8203cb987))
* add semantic annotations to section 106 dataset (commit [cbaa9a52](https://github.com/digital-land/planning-application-data-specification/commit/cbaa9a52153c7ffca502497d163ceb9c16f5d5b4))
* add semantic annotations to planning permisison timeline dataset (commit [2726a283](https://github.com/digital-land/planning-application-data-specification/commit/2726a283967a032ae9b31ab3534d387a566c42ba))
* add semantic annotations to planning application document dataset (commit [49a37e08](https://github.com/digital-land/planning-application-data-specification/commit/49a37e08be28e217c596306cba6a691b37e9c51b))
* add planning-permission-timeline dataset to decision stage specification (commit [a587f633](https://github.com/digital-land/planning-application-data-specification/commit/a587f6339236ebb0f65ab7289c6045e34e03fe4f))
* add planning-application-document dataset (commit [65f9a45e](https://github.com/digital-land/planning-application-data-specification/commit/65f9a45e59e926b5944e2cecc88261c283cfb168))
* add codelist for permission process events (commit [c923913f](https://github.com/digital-land/planning-application-data-specification/commit/c923913fcceee0fb9719ce7b6291d5aaf03d294c))

### 🐛 Bug Fixes

* add missing notes attrs to datasets (commit [15786c96](https://github.com/digital-land/planning-application-data-specification/commit/15786c96a3b6691facfa84ac5b7b16e78bf14d87))
* correct sources on a few needs (commit [0505ecda](https://github.com/digital-land/planning-application-data-specification/commit/0505ecda98903e98342147e2978f968a75f2c592))
* correct example payload after spec changes (commit [10b5892e](https://github.com/digital-land/planning-application-data-specification/commit/10b5892e6183068dcf65ec4ead52f56ccec4c09e))
* some required-of statements in modules should be lists of conditions not dicts (commit [49adf34e](https://github.com/digital-land/planning-application-data-specification/commit/49adf34ed34780aa3a3072525080e786eef6844f))

### 📚 Documentation

* add need dd-need-077 about access to all documents (commit [88d3a826](https://github.com/digital-land/planning-application-data-specification/commit/88d3a8266d8f84ec944b84baf0574f099f8d4bcb))
* add a data need for timeline datasets requiring what and when data points (commit [751b89e2](https://github.com/digital-land/planning-application-data-specification/commit/751b89e2fad35e6bd79d1a795951de428b13187f))
* ad a series of needs about aspects of process that need tracking (commit [dc768446](https://github.com/digital-land/planning-application-data-specification/commit/dc76844646950042de9cab9ed3072143bd7c7cde))
* add another condition type that can be used in justification records (commit [ae3771cf](https://github.com/digital-land/planning-application-data-specification/commit/ae3771cf0e8ebeed4f7081c1369149c2c4be770e))
* add need about tracking what happens in the planning permission process (commit [befa60cd](https://github.com/digital-land/planning-application-data-specification/commit/befa60cdefb3f241cf7ca7569fab32a4866e914d))
* add the relevant github discussion number to codelist definitions (commit [f017a232](https://github.com/digital-land/planning-application-data-specification/commit/f017a23241aa5a6374db9bdd3f75c33f21bc1e1f))


<a name="v0.1.56"></a>
## [v0.1.56](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.55...v0.1.56) (2026-01-27)

dates (and more) in submission spec

### ⚒️ Tooling

* cli to output url to existing form for each application type (commit [866b2fff](https://github.com/digital-land/planning-application-data-specification/commit/866b2fffd8fcf09e813ea2dd22782dc1d840f6a2))
* check that all date fields have date_precision attr set (commit [ecefb205](https://github.com/digital-land/planning-application-data-specification/commit/ecefb205b113f5362d4091c5c2a2267b4c7698b1))
* add some tests for the render static site code (commit [6ed09e1a](https://github.com/digital-land/planning-application-data-specification/commit/6ed09e1a833dedf5283688b0a4cfdcb90c9f443b))
* include justification record on dataset page when available (commit [68d26df8](https://github.com/digital-land/planning-application-data-specification/commit/68d26df8fa06db8e60a32072d02a4c7f257f8b85))
* link to justification records on the /decision-stage page (commit [7221d921](https://github.com/digital-land/planning-application-data-specification/commit/7221d921bc960bc381f9832cadd055e8a688db3e))
* tweak layout of 'help to improve this application schema' section (commit [5fd2456a](https://github.com/digital-land/planning-application-data-specification/commit/5fd2456a95ad08b1d03df2fb9e93fd2954342a42))
* add a page per module to static site generator (commit [6dc14299](https://github.com/digital-land/planning-application-data-specification/commit/6dc14299c1794bed9714989aeb775840afedb703))
* add cli command to list which needs have been satisfied (commit [be9d6170](https://github.com/digital-land/planning-application-data-specification/commit/be9d61705631c863be790a6534dbad51a7fd4587))
* add content menu to application details page (commit [d5fff0cb](https://github.com/digital-land/planning-application-data-specification/commit/d5fff0cb6b28d729c52a2781d08f90865863b24b))

### 𝌭 Model changes

* reuse declaration-date field instead of signature-date field in ownership cert module (commit [8c77e064](https://github.com/digital-land/planning-application-data-specification/commit/8c77e0645168ba562450ecba39081a3611df28fb))
* add date_precision attr to all datetime fields (commit [d7c15bc4](https://github.com/digital-land/planning-application-data-specification/commit/d7c15bc481f3da745a1c6e335f43b19bd7196120))
* all date fields should be of type datetime (commit [ac888279](https://github.com/digital-land/planning-application-data-specification/commit/ac88827956cfaf7f0fb7c161eccf8a540cca8705))
* update decision schema to include fields recently added to site dataset (commit [64b20d3d](https://github.com/digital-land/planning-application-data-specification/commit/64b20d3dd85a82ce8d34a2012152b914ce08399d))
* add name field to site dataset so planners can more easily refer to it consistently (commit [a9b3d873](https://github.com/digital-land/planning-application-data-specification/commit/a9b3d87308ebdfbdcad6e630797d87b7b1ac2ebc))
* state the Site dataset is semantically a closeMatch to ifcSite (commit [cb47de48](https://github.com/digital-land/planning-application-data-specification/commit/cb47de481ae2a1d7562804be0b21d605132fc44e))
* add the decision-maker codelist (commit [cfebd335](https://github.com/digital-land/planning-application-data-specification/commit/cfebd33529cdf714a844cc5bfd876164018fe973))
* add missing codelist attribute to request-by field (commit [6dd9dfc2](https://github.com/digital-land/planning-application-data-specification/commit/6dd9dfc2cdf6b5c9197941ddcaadf214ae428121))
* add the organisation codelist (commit [ffddddde](https://github.com/digital-land/planning-application-data-specification/commit/ffdddddeaa967dbb89ca2051270e2657a1ee2847))

### 🐛 Bug Fixes

* correct example payload after spec changes (commit [87a1d170](https://github.com/digital-land/planning-application-data-specification/commit/87a1d1702b38e7e0cd00d6b99e15c0b3fc1b7879))
* some required-of statements in modules should be lists of conditions not dicts (commit [aa7f717d](https://github.com/digital-land/planning-application-data-specification/commit/aa7f717d94b016aaa21470defce9ecc5655a6948))
* status of decision record 0007 (commit [d6bc1249](https://github.com/digital-land/planning-application-data-specification/commit/d6bc124951002dee9ed2bae2908871bc21eb79fc))

### 📚 Documentation

* add the relevant github discussion number to codelist definitions (commit [750541a4](https://github.com/digital-land/planning-application-data-specification/commit/750541a424a84a8a7afb4f51178c218c286e997b))
* add not of potentially flexible date fields (commit [7024d4a4](https://github.com/digital-land/planning-application-data-specification/commit/7024d4a4bb58221fa589ddc765c247594719a9cf))
* document decision and approach to using dates and setting precision (commit [537d99f7](https://github.com/digital-land/planning-application-data-specification/commit/537d99f701b9b048018ace7a9fd7f67eaff50645))
* add notes to section 106 dataset that summarise our understanding of section 106s (commit [f7beddcc](https://github.com/digital-land/planning-application-data-specification/commit/f7beddcc4fa7389a5b6fc4f3c72a106db45c831e))
* update just-0017 so that its more of a rule that datasets should have a name field (commit [5aafd957](https://github.com/digital-land/planning-application-data-specification/commit/5aafd957ff68a8a8cfa09fff1343b9c1dbd56a80))


<a name="v0.1.55"></a>
## [v0.1.55](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.54...v0.1.55) (2026-01-23)

add codelists and a name field to decision spec

### 𝌭 Model changes

* update decision schema to include fields recently added to site dataset (commit [0e6815bc](https://github.com/digital-land/planning-application-data-specification/commit/0e6815bc59c74688d8f51f980c3cd66cd8f1aa9b))
* add name field to site dataset so planners can more easily refer to it consistently (commit [8da8a40c](https://github.com/digital-land/planning-application-data-specification/commit/8da8a40c897c2482880c6114d331ef67a7b21401))
* state the Site dataset is semantically a closeMatch to ifcSite (commit [71239704](https://github.com/digital-land/planning-application-data-specification/commit/71239704e2eeac6701ea75dc62b3244a4690f0fe))
* add the decision-maker codelist (commit [b53bba91](https://github.com/digital-land/planning-application-data-specification/commit/b53bba91232ecb9d090a8b72965de59a0ef540f4))
* add missing codelist attribute to request-by field (commit [23d7ca63](https://github.com/digital-land/planning-application-data-specification/commit/23d7ca63f1111d1dc59bfd3169d7f5a416b8d691))
* add the organisation codelist (commit [1d1cdbc5](https://github.com/digital-land/planning-application-data-specification/commit/1d1cdbc5df8ace933e8912592baedcd29fa82676))

### 📚 Documentation

* add notes to section 106 dataset that summarise our understanding of section 106s (commit [4f6004e8](https://github.com/digital-land/planning-application-data-specification/commit/4f6004e889b28bd64e6645aaab34693e454b227f))
* update just-0017 so that its more of a rule that datasets should have a name field (commit [2a8873b7](https://github.com/digital-land/planning-application-data-specification/commit/2a8873b7389936b0649b7aec0bc85b073a731a58))


<a name="v0.1.54"></a>
## [v0.1.54](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.53...v0.1.54) (2026-01-23)

Add justification records to static site

### ⚒️ Tooling

* add some tests for the render static site code (commit [5319bd85](https://github.com/digital-land/planning-application-data-specification/commit/5319bd85497d48c0ce44a081b0b4420d8110c856))
* include justification record on dataset page when available (commit [e39baeed](https://github.com/digital-land/planning-application-data-specification/commit/e39baeed416aa237beabd823c379003549f0a81f))
* link to justification records on the /decision-stage page (commit [75776a05](https://github.com/digital-land/planning-application-data-specification/commit/75776a05018d7e0ecb24db5699b443749066ab76))
* tweak layout of 'help to improve this application schema' section (commit [c800cac8](https://github.com/digital-land/planning-application-data-specification/commit/c800cac8522cfe1b33ac04bfe9dc56a3c841dee6))
* add a page per module to static site generator (commit [94711a8c](https://github.com/digital-land/planning-application-data-specification/commit/94711a8c3220622d4c7baed394473b32e6828472))
* add cli command to list which needs have been satisfied (commit [e15367c0](https://github.com/digital-land/planning-application-data-specification/commit/e15367c039e243ce5b997f06ede123a374c37226))
* add content menu to application details page (commit [29d3d4c4](https://github.com/digital-land/planning-application-data-specification/commit/29d3d4c448ffab025a709726755e605a9f8475ba))

### 𝌭 Model changes

* add document and documentation-url field pair to section 106 dataset (commit [624356e5](https://github.com/digital-land/planning-application-data-specification/commit/624356e58ccc73d01624c7cbafb7ebe0680efef3))


<a name="v0.1.53"></a>
## [v0.1.53](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.52...v0.1.53) (2026-01-21)

Add additional datasets to decision-stage specification

### 𝌭 Model changes

* add document and documentation-url field pair to section 106 dataset (commit [430114af](https://github.com/digital-land/planning-application-data-specification/commit/430114af602bb56cb4362501ac1360d1bc946203))
* add section 106 dataset to decision-stage specification (commit [d6a7e4dd](https://github.com/digital-land/planning-application-data-specification/commit/d6a7e4ddda423bf8f02d2725e8cf5a1f0989d9f1))
* add decision notice field to section 106 dataset (commit [d05cdb86](https://github.com/digital-land/planning-application-data-specification/commit/d05cdb86d76a205b140b751e244a7f9899972613))
* add a section 106 dataset (commit [0be82502](https://github.com/digital-land/planning-application-data-specification/commit/0be82502bfeeedbefc501dfe25daa050efceafb8))
* add site-boundary field to site dataset (commit [5e6ef36d](https://github.com/digital-land/planning-application-data-specification/commit/5e6ef36d991004f8e9541498ea5d46d6dceac0c5))
* add a site dataset for site linked to planning applications (commit [bf225a57](https://github.com/digital-land/planning-application-data-specification/commit/bf225a57d93aab85da5b1b8cbcf7af8b379934d2))

### 📚 Documentation

* flesh out rationale for decision-notice field on section 106 dataset (commit [e0d20e13](https://github.com/digital-land/planning-application-data-specification/commit/e0d20e13373e079eee85bbc8e90a08993d7b0b18))
* add user need about section 106s (commit [c594937d](https://github.com/digital-land/planning-application-data-specification/commit/c594937d72dab58b2cae1c2939686c2a71625c5b))
* add a data need about spatial representations (commit [e6279179](https://github.com/digital-land/planning-application-data-specification/commit/e6279179da339b470230ac36e1cde895ef90bc5e))


<a name="v0.1.52"></a>
## [v0.1.52](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.51...v0.1.52) (2026-01-19)

Adding and indexing user needs

### ⚒️ Tooling

* sort out layout of justification index and detail pages (commit [c8960c05](https://github.com/digital-land/planning-application-data-specification/commit/c8960c059f24febfcc8ade245626e0b298705325))
* add content of justification record on needs page (commit [18cadaf1](https://github.com/digital-land/planning-application-data-specification/commit/18cadaf169cba58bb627e852007bdcc66ae1bc68))
* add links to take user to issue template for adding new needs/requirements (commit [85ab4bd6](https://github.com/digital-land/planning-application-data-specification/commit/85ab4bd671c2180c87398a7d800fec63e1a73054))
* tweak layout of needs index (commit [d10900f3](https://github.com/digital-land/planning-application-data-specification/commit/d10900f31c48d30439a65e0d4684976482c0dfd5))
* stub pages for the justification records (commit [8e28456b](https://github.com/digital-land/planning-application-data-specification/commit/8e28456b6d10927b9e70b3af0ee043e8e7565907))
* user needs checker should check source.types are consistent (commit [4be8f6a0](https://github.com/digital-land/planning-application-data-specification/commit/4be8f6a09fd1c7379512e89ff547b03e0c98960d))
* components in standalone only modules should include 'only for application' column if applicable (commit [bd488cef](https://github.com/digital-land/planning-application-data-specification/commit/bd488cef8f114c4731daca114638bdb006a49312))

### 𝌭 Model changes

* add example of operational times to component definition (commit [a37f3f0e](https://github.com/digital-land/planning-application-data-specification/commit/a37f3f0eb3d9ac1697f853ea76f765f304c3f357))

### 📚 Documentation

* add couple of user needs about committee output (commit [0f4e1e9e](https://github.com/digital-land/planning-application-data-specification/commit/0f4e1e9e4cb49fd528154dfda83bd1bdd24db9ed))
* add batch of user needs taken from ps1 and ps2 return analysis (commit [08b3a0ce](https://github.com/digital-land/planning-application-data-specification/commit/08b3a0ce53e633c7cbb447de259986bb801b8873))
* document another batch of user needs (commit [dcc8a329](https://github.com/digital-land/planning-application-data-specification/commit/dcc8a3296235d40ec0bb35a6d34991e7755bc5e8))
* add and refine user-needs for decision stage (commit [c0a28365](https://github.com/digital-land/planning-application-data-specification/commit/c0a2836536bb750af2394044954ea91e912dddb3))


<a name="v0.1.51"></a>
## [v0.1.51](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.5...v0.1.51) (2026-01-16)

Resolving issue from DMSF analysis

### ⚒️ Tooling

* components in standalone only modules should include 'only for application' column if applicable (commit [9b2ffc04](https://github.com/digital-land/planning-application-data-specification/commit/9b2ffc049e2358514e58b779e7af92c46ec2f500))
* update integrity checks to handle when field has end-date (commit [31a6578a](https://github.com/digital-land/planning-application-data-specification/commit/31a6578af1d649b6e592fe351ea3b297346e405a))
* stub a page for each application (commit [aa76cf86](https://github.com/digital-land/planning-application-data-specification/commit/aa76cf862d87b32d91797d5bb3f32d9d478e468e))

### 𝌭 Model changes

* add example of operational times to component definition (commit [64f4a1f9](https://github.com/digital-land/planning-application-data-specification/commit/64f4a1f967093a1fed4635a59d7a6eec6976e82e))
* added new connect-to-drainage-system-oil-gas field to handle variation in extraction-oil-gas applications (commit [c9b5b11b](https://github.com/digital-land/planning-application-data-specification/commit/c9b5b11b1460f621b43e0ba5e1791c6224b4e465))
* remove employment-impact field, not par tof existing forms (commit [577c124f](https://github.com/digital-land/planning-application-data-specification/commit/577c124f51c83a4ff261539cb55580bc9a0299cc))
* clarify the not-applicable field in room-details-outline is for disambiguating a blank row (commit [a617705b](https://github.com/digital-land/planning-application-data-specification/commit/a617705b729e7dbdcbeede5c145a1a602655ce27))
* add codelists for handling measurement unit types (commit [35af6751](https://github.com/digital-land/planning-application-data-specification/commit/35af67514b5c196f048ae1697cdd16482f2e2bb8))
* clarify WGS84 is government chosen standard for exchange of location data (commit [02ea8082](https://github.com/digital-land/planning-application-data-specification/commit/02ea80829048e708d3d86829f290cd81b9736ba3))
* replaces details field with supporting-documents field in foul sewage module (commit [53a12cec](https://github.com/digital-land/planning-application-data-specification/commit/53a12cecb426ba4ac0ac5737ee5a0eb8442ef38c))
* rationalise and document approach to including and referencing documents (commit [eacec70f](https://github.com/digital-land/planning-application-data-specification/commit/eacec70f5ce1c97d0defaefffb9be870abce8bbb))
* add uploaded-date to document component (commit [755ed9b0](https://github.com/digital-land/planning-application-data-specification/commit/755ed9b0602f9d327528457e0feba6e6cda7bd9a))
* update illumination-method field to use an illumination-method codelist (commit [1d3188cf](https://github.com/digital-land/planning-application-data-specification/commit/1d3188cff8c301b1a2ffec91bf0b03212e8f87b4))

### 🐛 Bug Fixes

* produce-foul-sewage was not showing it is only applicable to extraction-oil-gas apps in info_model output (commit [de66ed1a](https://github.com/digital-land/planning-application-data-specification/commit/de66ed1a0569bee62381f5bfbe27f3cdfa37febc))
* issue with condition structure in unit-quantities component (commit [b0b19621](https://github.com/digital-land/planning-application-data-specification/commit/b0b1962141c6dac15123a7012a741e79e8785eea))
* ldc-existing-use shouldn't be able to say unknown on unit-qunanties (commit [cd19f907](https://github.com/digital-land/planning-application-data-specification/commit/cd19f9075be7557206e2222c1d645d7325c527b3))
* hedgerow-removal module should use supporting-documents field (commit [881c605b](https://github.com/digital-land/planning-application-data-specification/commit/881c605b482e7b4234788acb9aa9ec31b77e6dc0))
* the path to the documentation folder (commit [c4085d20](https://github.com/digital-land/planning-application-data-specification/commit/c4085d2063de7b7c3028b3942838944143f07115))
* add missing applies-if attributes to hazardous substances module so variants are covered (commit [24cf08b3](https://github.com/digital-land/planning-application-data-specification/commit/24cf08b388707f2c46c7274bc68a807b038830bf))
* remove incorrect reference to highways module (commit [e3ae2700](https://github.com/digital-land/planning-application-data-specification/commit/e3ae27003e9077855d3d50dffd3709dfb3fb56a7))

### 📚 Documentation

* add clearer decision record for requiring WGS84 for location data (commit [29e83b4e](https://github.com/digital-land/planning-application-data-specification/commit/29e83b4ef3c19011624a6a2b16fe9ded5f5497cb))
* clarify that document references are expected to come from the submission service whether created by system or applicant (commit [f3af71bb](https://github.com/digital-land/planning-application-data-specification/commit/f3af71bb8d8c1194da99545c18a171c11ec246ea))
* add design decision record about consolidating approach to referring to documents in modules (commit [3acccfcf](https://github.com/digital-land/planning-application-data-specification/commit/3acccfcf926f5e8bdcedd7f00201cc27a858dbad))


<a name="v0.1.5"></a>
## [v0.1.5](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.45...v0.1.5) (2026-01-13)

Add a proof of concept static site for viewing the specifications

### ⚒️ Tooling

* stub a page for each application (commit [f33b3dd6](https://github.com/digital-land/planning-application-data-specification/commit/f33b3dd61d2f0e1af0a15efb3cf99600df28e498))
* workflow to output to docs folder (commit [966be522](https://github.com/digital-land/planning-application-data-specification/commit/966be522d7ede762d7b198ed317929f5a40558de))
* fix urls and links so can test local and serve on github pages (commit [5e65a586](https://github.com/digital-land/planning-application-data-specification/commit/5e65a58640a4fa3bee932c91ca1d2dece8beb1e4))
* move static site from generated/github-pages to docs so it can be served (commit [01428659](https://github.com/digital-land/planning-application-data-specification/commit/014286595a29040aff565794941c0826afc3a843))
* move documentation from docs to documentation folder (commit [701adfea](https://github.com/digital-land/planning-application-data-specification/commit/701adfeafc5f52f1fe56c7696af4218b94986aae))
* github workflow to automate building static site (commit [8179c80a](https://github.com/digital-land/planning-application-data-specification/commit/8179c80a70c417a8ee2af3c3b27b2f1be59f287c))
* improve the layout of the fields on the detailed dataset pages (commit [80bc3a6a](https://github.com/digital-land/planning-application-data-specification/commit/80bc3a6a2d3a78c84b50e4a7836cb12aa20cf833))
* list what needs a field satisfies on dataset detail pages (commit [5ea06e31](https://github.com/digital-land/planning-application-data-specification/commit/5ea06e3124a18be316452c508f91a151350ecf23))
* add link to fields that are references to other datasets (commit [0c6ac94a](https://github.com/digital-land/planning-application-data-specification/commit/0c6ac94aec94b3f9e48eab2fac6998ad39d1cad3))
* work on layout of specification parts (commit [38141626](https://github.com/digital-land/planning-application-data-specification/commit/38141626374046b71a0d58e77dbc2bcdffcf9ec5))
* layout the details of a need (commit [3912aacd](https://github.com/digital-land/planning-application-data-specification/commit/3912aacd49c9c2a2ae4b9f5793c3ea39d74dfae4))
* list needs satisfied by dataset on dataset page (commit [a4d4554a](https://github.com/digital-land/planning-application-data-specification/commit/a4d4554acee9a2556f1d8a3fc20e7470cdee717b))
* add some local css to generated github pages (commit [aa943a6e](https://github.com/digital-land/planning-application-data-specification/commit/aa943a6e88b68316c10dee7d2c0d8d86abe87e81))
* add introductions to different spec index pages (commit [94270f84](https://github.com/digital-land/planning-application-data-specification/commit/94270f84f9ab914209035927e90ef992bcbf7bf6))
* setup initial rendering of static pages to view specifications (commit [5a0d73a5](https://github.com/digital-land/planning-application-data-specification/commit/5a0d73a58eb59a59e6fde9cc3a967ccfdb0d453f))
* add integrity checks for specifications (platform-like) (commit [4eb06af7](https://github.com/digital-land/planning-application-data-specification/commit/4eb06af79b497d4966e314479bf62acbbc10b58c))

### 𝌭 Model changes

* add schema file for decision stage specification (commit [c8c830c7](https://github.com/digital-land/planning-application-data-specification/commit/c8c830c7b2bda8390ad708049a6f41e29ca8abc6))

### 🐛 Bug Fixes

* links in nav bar (commit [94bb01e2](https://github.com/digital-land/planning-application-data-specification/commit/94bb01e2698e0a45a6d262ee39cf1ba274f43e06))
* incorrect attribute used on justification record (commit [37378231](https://github.com/digital-land/planning-application-data-specification/commit/373782314018a3e5d6679a5fe3efb3fd0e3763fd))
* justification integrity checks should only check for needs attr (commit [acd7a122](https://github.com/digital-land/planning-application-data-specification/commit/acd7a12259ca81b7dc4070e11400c092a13a49fd))


<a name="v0.1.45"></a>
## [v0.1.45](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.44...v0.1.45) (2026-01-09)

Add schema for initial decision stage specification

### ⚒️ Tooling

* add integrity checks for specifications (platform-like) (commit [0ce09764](https://github.com/digital-land/planning-application-data-specification/commit/0ce0976434aa66df9448b72a890ed06af437a0a7))
* justification checks should check field belongs to dataset (commit [b96dafe6](https://github.com/digital-land/planning-application-data-specification/commit/b96dafe6356f3f251dcedd6f1c633fa583696dad))

### 𝌭 Model changes

* add schema file for decision stage specification (commit [66801297](https://github.com/digital-land/planning-application-data-specification/commit/668012978c7f337a1af87a548766e230bfce4cee))
* rename dataset from decision to decision-notice (commit [e4b32240](https://github.com/digital-land/planning-application-data-specification/commit/e4b322406946dc441c9bb0753a9e5503e4cdbd1d))
* add planning-condition field (commit [b057c7af](https://github.com/digital-land/planning-application-data-specification/commit/b057c7afca3fef66d86ad058573261ea19512a41))
* add discharged-by field to decision-condition dataset (commit [be561894](https://github.com/digital-land/planning-application-data-specification/commit/be561894ce2f47d36d32e6b30fbac8968e81a15b))
* add requested-by field to decision-condition dataset (commit [6c1d343a](https://github.com/digital-land/planning-application-data-specification/commit/6c1d343ad5ff94af38cfc9f43254f38de8301e0e))
* add organisation field to planning-condition and decision-condition datasets (commit [cdd6bef1](https://github.com/digital-land/planning-application-data-specification/commit/cdd6bef126a4e40825fe96c7e4a0a495319319be))
* add links to decision and planning-condition datasets to decision-condition dataset (commit [d17bc50f](https://github.com/digital-land/planning-application-data-specification/commit/d17bc50fe99ad11ba211ce8736235fd0223164af))
* add reference field to decision-condition dataset (commit [4d5024fb](https://github.com/digital-land/planning-application-data-specification/commit/4d5024fb80efe2d9f18f014a17d130ad49538d5a))
* add skeleton decision-condition dataset (commit [3f80407d](https://github.com/digital-land/planning-application-data-specification/commit/3f80407d6f594209c76ddaf7c2d3e1bf768b161d))
* add reason field to planning-condition dataset (commit [0d45e638](https://github.com/digital-land/planning-application-data-specification/commit/0d45e63898847d4ea9dbd81e0adb3675e49e72d0))
* add name field to planning-condition dataset (commit [5ecfde4d](https://github.com/digital-land/planning-application-data-specification/commit/5ecfde4d11fa78327662f382ff8246737fe85fe6))
* add description field to planning-condition dataset (commit [da53b35e](https://github.com/digital-land/planning-application-data-specification/commit/da53b35e33c4b8b71fa0de74ba7f553d33439455))
* add a planning-condition dataset (commit [e82b2f35](https://github.com/digital-land/planning-application-data-specification/commit/e82b2f35ca9eba55ed2d8857b6f5b7910aac23e6))

### 📚 Documentation

* document decision to rename dataset to decision-notice (commit [0cd69267](https://github.com/digital-land/planning-application-data-specification/commit/0cd692679d9882bf386033f0249752712045000b))
* add need dd-need-054 (commit [f9dd17db](https://github.com/digital-land/planning-application-data-specification/commit/f9dd17dbb90313c66c7f5433d6d601228c4ab5b2))
* justification record for counting number of conditions associated with a decision (commit [a5911ead](https://github.com/digital-land/planning-application-data-specification/commit/a5911ead8e7cfcee458ec914f213ea6bc62e71ba))
* dd-need-052 is satisfied (commit [1487d8af](https://github.com/digital-land/planning-application-data-specification/commit/1487d8af7b7c08e1017ebfb5e19337e835466943))
* add a data need for making things identifiable for humans (commit [6ea8115c](https://github.com/digital-land/planning-application-data-specification/commit/6ea8115c9a4472842a7a8e4bc33a47d04881f21d))
* add batch of needs related to conditions (commit [5c8da9a0](https://github.com/digital-land/planning-application-data-specification/commit/5c8da9a0fc46cad593ed855e0d1fbc6ebecbcaa2))
* add needs about understanding conditions and seeing where they apply (commit [aaebf034](https://github.com/digital-land/planning-application-data-specification/commit/aaebf0342684ddd885b41e3d8a235a3954b5a1d3))
* add couple of needs about recording conditions as data (commit [ad67c390](https://github.com/digital-land/planning-application-data-specification/commit/ad67c3904bc2c1a5da58b3c03e28d6a2da2ef250))


<a name="v0.1.44"></a>
## [v0.1.44](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.43...v0.1.44) (2026-01-09)

Work on an initial model for conditions

### ⚒️ Tooling

* justification checks should check field belongs to dataset (commit [a66530e1](https://github.com/digital-land/planning-application-data-specification/commit/a66530e12c41f84aa0aac98ccaf5e5624417bc03))
* correct error message printing from fields integrity checks (commit [73b58121](https://github.com/digital-land/planning-application-data-specification/commit/73b58121c3ecd2e56802dd106576fba83692081d))
* add integrity checks for justification records (commit [a5fac6de](https://github.com/digital-land/planning-application-data-specification/commit/a5fac6deac4823bc1336e9d74a61cbf170614511))
* add integrity checks for needs (commit [ec3fab13](https://github.com/digital-land/planning-application-data-specification/commit/ec3fab13a925757f1d5a27136f735738516b2caf))
* give error and warning msgs colours for easier interpretation (commit [de785786](https://github.com/digital-land/planning-application-data-specification/commit/de78578685e6551afaf28ab28be35fa462713759))
* add integrity checks for dataset definitions (commit [7bb50a66](https://github.com/digital-land/planning-application-data-specification/commit/7bb50a6603506bc4da39fbf08a3e950701cb1472))

### 𝌭 Model changes

* rename dataset from decision to decision-notice (commit [d2b3bcd4](https://github.com/digital-land/planning-application-data-specification/commit/d2b3bcd47ff94dc616c479d0dc1f95e4aba3b696))
* add planning-condition field (commit [e6784a90](https://github.com/digital-land/planning-application-data-specification/commit/e6784a90ee173d05c45cca54c4524dab3b0161ba))
* add discharged-by field to decision-condition dataset (commit [4fa77e85](https://github.com/digital-land/planning-application-data-specification/commit/4fa77e85d871bce815727018d810e7a9cdd74037))
* add requested-by field to decision-condition dataset (commit [642781ad](https://github.com/digital-land/planning-application-data-specification/commit/642781ad8ff83e975a2782b45d1bbca0ffcd1fb8))
* add organisation field to planning-condition and decision-condition datasets (commit [8670d3d0](https://github.com/digital-land/planning-application-data-specification/commit/8670d3d037317fd9cbff9fc2b44a66d259aa2dd1))
* add links to decision and planning-condition datasets to decision-condition dataset (commit [7240e4e9](https://github.com/digital-land/planning-application-data-specification/commit/7240e4e9b8fb71fda9cb19564389689479840fc2))
* add reference field to decision-condition dataset (commit [70ccfe5f](https://github.com/digital-land/planning-application-data-specification/commit/70ccfe5fdc4e60d0dbb04b44c061e980c5f65e9c))
* add skeleton decision-condition dataset (commit [cdff8bc6](https://github.com/digital-land/planning-application-data-specification/commit/cdff8bc64df7da9b24203aa2ab30997b58005e20))
* add reason field to planning-condition dataset (commit [8eba1564](https://github.com/digital-land/planning-application-data-specification/commit/8eba1564e2775bd53b87c745a44b340877c67813))
* add name field to planning-condition dataset (commit [049378b2](https://github.com/digital-land/planning-application-data-specification/commit/049378b27803682a72c90ee368011ae67226f384))
* add description field to planning-condition dataset (commit [879a6704](https://github.com/digital-land/planning-application-data-specification/commit/879a6704d3b1457beef2775705348a1418b62085))
* add a planning-condition dataset (commit [492a05ee](https://github.com/digital-land/planning-application-data-specification/commit/492a05eec8989cab28b1e6dcbe2097338dc3a7d8))

### 🐛 Bug Fixes

* add notes attr to dataset schemas (commit [63c01fca](https://github.com/digital-land/planning-application-data-specification/commit/63c01fca908ac9aca05933782b0921233f453a5f))
* rename needs files to correct format (commit [895e8f94](https://github.com/digital-land/planning-application-data-specification/commit/895e8f94213f19ffce6f8e03263bb4c01c09afe4))
* pointer to existing need (commit [edd06b0d](https://github.com/digital-land/planning-application-data-specification/commit/edd06b0da3614b5b1a7582948a0f7c37c92584fe))
* attr should be name not title (commit [59a3fa72](https://github.com/digital-land/planning-application-data-specification/commit/59a3fa72ed0736c8798284454bd44bde90351905))
* in need records variations should be a list of need ids (commit [d956db30](https://github.com/digital-land/planning-application-data-specification/commit/d956db306b2d4cb2a7fa2681f8ca7bd658457b94))
* add missing github disucssion numbers to codelist schemas (commit [eb41359d](https://github.com/digital-land/planning-application-data-specification/commit/eb41359db778f11a95d7f9fd7994ebfb9597fb18))

### 📚 Documentation

* document decision to rename dataset to decision-notice (commit [5dc00630](https://github.com/digital-land/planning-application-data-specification/commit/5dc006304e957f78d0fc14cb585e8f275b18a479))
* add need dd-need-054 (commit [dd47d12a](https://github.com/digital-land/planning-application-data-specification/commit/dd47d12a1235e70e01ca1c41dfdf67789153bfb4))
* justification record for counting number of conditions associated with a decision (commit [d39d0180](https://github.com/digital-land/planning-application-data-specification/commit/d39d01800ef7695ecd852be8de040a95752f15d3))
* dd-need-052 is satisfied (commit [3d0f927a](https://github.com/digital-land/planning-application-data-specification/commit/3d0f927aaa016d20501a56fc3fd1eca9411d4d84))
* add a data need for making things identifiable for humans (commit [5b853c49](https://github.com/digital-land/planning-application-data-specification/commit/5b853c497de6b259994dbeafa1933c062e825f6e))
* add batch of needs related to conditions (commit [c0ee020a](https://github.com/digital-land/planning-application-data-specification/commit/c0ee020a4c7c7339abe64d259502045243fb5050))
* add needs about understanding conditions and seeing where they apply (commit [16b59e94](https://github.com/digital-land/planning-application-data-specification/commit/16b59e9475ad20d20ee38f0138235fe5d83925c0))
* add couple of needs about recording conditions as data (commit [d97b0fde](https://github.com/digital-land/planning-application-data-specification/commit/d97b0fde39da2355246a6541b0a55b801a0cf4cf))


<a name="v0.1.43"></a>
## [v0.1.43](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.42.1...v0.1.43) (2026-01-07)

Add integrity checks for datasets, needs and justification records

### ⚒️ Tooling

* correct error message printing from fields integrity checks (commit [1cbdc14c](https://github.com/digital-land/planning-application-data-specification/commit/1cbdc14cca244eb92c7edf42464dc971c61e339e))
* add integrity checks for justification records (commit [945f7139](https://github.com/digital-land/planning-application-data-specification/commit/945f7139b4d766a686d31c8e081f1629807d50a9))
* add integrity checks for needs (commit [40878201](https://github.com/digital-land/planning-application-data-specification/commit/40878201356e05da3e000757cea5bda8a18a607d))
* give error and warning msgs colours for easier interpretation (commit [23a05e71](https://github.com/digital-land/planning-application-data-specification/commit/23a05e71b1b34157eeb3c7ed1462c6c720a25373))
* add integrity checks for dataset definitions (commit [adc96e5a](https://github.com/digital-land/planning-application-data-specification/commit/adc96e5a51132c96b688aaac50bcf7cffc8038c6))

### 𝌭 Model changes

* add application-types field to planning-application dataset (commit [3f635308](https://github.com/digital-land/planning-application-data-specification/commit/3f635308ffecd0641f47b577192701306e884140))
* add routes to access decision notice to decision dataset (commit [b084d1bb](https://github.com/digital-land/planning-application-data-specification/commit/b084d1bbf2779f7f04d8fd529d69132f4a944739))
* add description field to planning application records (commit [d817496c](https://github.com/digital-land/planning-application-data-specification/commit/d817496ce5c3bdedf0ba4f134d4d165c8df86f45))
* add planning-officer-recommendation field to decision dataset (commit [cd22d8b4](https://github.com/digital-land/planning-application-data-specification/commit/cd22d8b4932651550b22ad57752b28d8c07ec871))
* add decision-maker field to decision dataset (commit [f598ca5e](https://github.com/digital-land/planning-application-data-specification/commit/f598ca5e11a200a302ff857c1b2a8a83d2b750a6))
* add organisation field to decision dataset (commit [d00f3be0](https://github.com/digital-land/planning-application-data-specification/commit/d00f3be0ba400a704a45844a1a4f6f200d78e470))
* add received-date field to planning application records (commit [59345f20](https://github.com/digital-land/planning-application-data-specification/commit/59345f2021a37c9688336ef6ae576c678d5a8ae7))
* add decision-date field to decision dataset (commit [9aebe12d](https://github.com/digital-land/planning-application-data-specification/commit/9aebe12d95bc22070b0910c88f5cf9343820b6af))

### 🐛 Bug Fixes

* add notes attr to dataset schemas (commit [148b55c7](https://github.com/digital-land/planning-application-data-specification/commit/148b55c7c244758a189acbf82b66478368f93df4))
* rename needs files to correct format (commit [030b051b](https://github.com/digital-land/planning-application-data-specification/commit/030b051b69becea706a1724d2e2ad1f2c7f3995c))
* pointer to existing need (commit [1de1d3b4](https://github.com/digital-land/planning-application-data-specification/commit/1de1d3b43878e5a426fe3ab4fba87dd5849b86ec))
* attr should be name not title (commit [c8109f14](https://github.com/digital-land/planning-application-data-specification/commit/c8109f141d1937c865f6e56d7db54c4bcd1a0751))
* in need records variations should be a list of need ids (commit [58b7b314](https://github.com/digital-land/planning-application-data-specification/commit/58b7b314cce67e95e2e637e1e252fd3cf306154d))
* add missing github disucssion numbers to codelist schemas (commit [16350c87](https://github.com/digital-land/planning-application-data-specification/commit/16350c870f06b61683cdc73d08c383afb445ecbe))

### 📚 Documentation

* add just-0008 record for decisions in a period (commit [7f98527d](https://github.com/digital-land/planning-application-data-specification/commit/7f98527d42f729b708c792115472783716e9e274))
* add just-0005 for satisfying volume need (dd-need-031) (commit [e059fefb](https://github.com/digital-land/planning-application-data-specification/commit/e059fefb847c84412ba09653d3939a47bf5ac4ee))
* tweak description for just-0004 (commit [389a9b0b](https://github.com/digital-land/planning-application-data-specification/commit/389a9b0b94b97ed3a8d7fa9b64d83e18d1f99c03))


<a name="v0.1.42.1"></a>
## [v0.1.42.1](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.42...v0.1.42.1) (2026-01-06)

Add missing field to decision dataset draft

### 𝌭 Model changes

* add application-types field to planning-application dataset (commit [f33a79d5](https://github.com/digital-land/planning-application-data-specification/commit/f33a79d59c921d54ddf601ea6878adcc246747ee))


<a name="v0.1.42"></a>
## [v0.1.42](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.41...v0.1.42) (2026-01-06)

Initial draft of decision dataset

### 𝌭 Model changes

* add routes to access decision notice to decision dataset (commit [621a9d98](https://github.com/digital-land/planning-application-data-specification/commit/621a9d982b084d4cb41661dcc0b09a5a72a60058))
* add description field to planning application records (commit [bdb900ec](https://github.com/digital-land/planning-application-data-specification/commit/bdb900ec6b92cdc491dab65a3582ee2da027a296))
* add planning-officer-recommendation field to decision dataset (commit [32efccd9](https://github.com/digital-land/planning-application-data-specification/commit/32efccd99b170f05e44f1ec98c59be0bcbfe1a52))
* add decision-maker field to decision dataset (commit [4b76484b](https://github.com/digital-land/planning-application-data-specification/commit/4b76484b9beff0639a197b4e927a8d38b5819c49))
* add organisation field to decision dataset (commit [1c85f916](https://github.com/digital-land/planning-application-data-specification/commit/1c85f916b0a0c6cc7fec6cb813fb85b680c6ffcd))
* add received-date field to planning application records (commit [16225998](https://github.com/digital-land/planning-application-data-specification/commit/16225998062e133c34a67da77126815467aaf763))
* add decision-date field to decision dataset (commit [a80a1204](https://github.com/digital-land/planning-application-data-specification/commit/a80a12049e089a58d3ea94a3086e5175adf7dc92))
* add documentation and document urls to planning application dataset (commit [eb2c149d](https://github.com/digital-land/planning-application-data-specification/commit/eb2c149dcd2b216c47d0a45b283c262b8647213f))

### 📚 Documentation

* add just-0008 record for decisions in a period (commit [828edf9a](https://github.com/digital-land/planning-application-data-specification/commit/828edf9abf957782f158a0b228d44e27cc5a2a5b))
* add just-0005 for satisfying volume need (dd-need-031) (commit [8111a753](https://github.com/digital-land/planning-application-data-specification/commit/8111a753804e32a63802ff42fe80518553e2d022))
* tweak description for just-0004 (commit [5e9077a0](https://github.com/digital-land/planning-application-data-specification/commit/5e9077a079be8b8b66c229fb37cc78269656ced5))
* add descriptions to document and documentation fields in planning application dataset (commit [27131eeb](https://github.com/digital-land/planning-application-data-specification/commit/27131eebb7f21d6a98e3bc0e7954567204ec8d8c))
* add need dd-need-032 (commit [ff4ff24e](https://github.com/digital-land/planning-application-data-specification/commit/ff4ff24e770a740c393fddada0f4282afcf2387b))
* add series of identified needs around decision stage data (commit [fd6edd60](https://github.com/digital-land/planning-application-data-specification/commit/fd6edd6011881471cb2105a3df2f2bcdc98bd61c))


<a name="v0.1.41"></a>
## [v0.1.41](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.40...v0.1.41) (2025-12-19)

Align spec with decision on submitting documents

### 𝌭 Model changes

* remove checksum field from file component, no longer needed (commit [93596f70](https://github.com/digital-land/planning-application-data-specification/commit/93596f70b883d4b5abe3b775b5ff4ad0ba3a09c7))
* remove option to link to a file instead of including it, see decision 0003-how-to-provide-documents-with-submission (commit [563b0bf3](https://github.com/digital-land/planning-application-data-specification/commit/563b0bf3483b51287a73b97e6b6a38eb6ecc9f92))

### 📚 Documentation

* add need dd-need-010 (commit [c2519d9c](https://github.com/digital-land/planning-application-data-specification/commit/c2519d9ce573bfa5c23c11e3be8e1de93850f29b))
* add need-ps-004 (commit [83ad2ec9](https://github.com/digital-land/planning-application-data-specification/commit/83ad2ec906e81536098f7b47168f1bc90ba4ec49))
* add dd-need-017 (commit [d223ddda](https://github.com/digital-land/planning-application-data-specification/commit/d223dddaf6203a456dd019631b157b4a671f5c15))
* update dd-need-014 (commit [cef91d76](https://github.com/digital-land/planning-application-data-specification/commit/cef91d7623ff0eaea24721a1c05a8dd68e4b242b))
* add dd-need031 (commit [b06f85ea](https://github.com/digital-land/planning-application-data-specification/commit/b06f85eaf5bd4b37c7fa631c2a1fff2dc4a499dc))


<a name="v0.1.40"></a>
## [v0.1.40](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.38...v0.1.40) (2025-12-19)

Begin adding the working draft decision stage specification to repository

### ⚒️ Tooling

* handle not allowing additional properties, should output false: (commit [bddbc22a](https://github.com/digital-land/planning-application-data-specification/commit/bddbc22a43dc2fbf7b7ea1d726a66465f0857482))

### 𝌭 Model changes

* Clarify dataset intent and relationships with semantic metadata (commit [e9c5a03a](https://github.com/digital-land/planning-application-data-specification/commit/e9c5a03a5ae05f111539ede278a6d0f57426fe7f))
* add skeleton definition of planning application dataset (commit [397c0ded](https://github.com/digital-land/planning-application-data-specification/commit/397c0ded4fbcc3096816a83fa135f1e1ae3282a6))
* add planning-application and decision fields to decision dataset (commit [c7601a81](https://github.com/digital-land/planning-application-data-specification/commit/c7601a81061312e03dc33238c7987067bbf3076e))
* add a skeleton dataset definition for the decision dataset (commit [2439d7bc](https://github.com/digital-land/planning-application-data-specification/commit/2439d7bc2fabfac4d52ca9115d65aec8dc90a290))
* add allow-additional-properties to all other application types (commit [07863d41](https://github.com/digital-land/planning-application-data-specification/commit/07863d4104c3e538752a8bcda5332e3d2793dd82))
* add allow-additional-properties to outline apps (commit [5ad93cc7](https://github.com/digital-land/planning-application-data-specification/commit/5ad93cc70bda2b7bd776aca6a82a6bab7326330e))

### 🐛 Bug Fixes

* date on design decision record (commit [35eeb23c](https://github.com/digital-land/planning-application-data-specification/commit/35eeb23ce59c4e34a82a3e05eeeb16b7904621a1))
* mistakes in first dataset and justification files (commit [9c5ffdb9](https://github.com/digital-land/planning-application-data-specification/commit/9c5ffdb9cfa247a0f32329227f55df65821107b3))
* remove redundant info models for oil and gas app (commit [7247fc36](https://github.com/digital-land/planning-application-data-specification/commit/7247fc3638474527616144d0a23e32bed2304d72))
* remove redundant info models for outline apps (commit [48a7e2b5](https://github.com/digital-land/planning-application-data-specification/commit/48a7e2b5d2167d46993678d1329b825078731fa9))

### 📚 Documentation

* add need dd-need-010 (commit [c4d36b6f](https://github.com/digital-land/planning-application-data-specification/commit/c4d36b6f6d4170c6b70f88bb9891debd6b4685b6))
* add need-ps-004 (commit [480175e7](https://github.com/digital-land/planning-application-data-specification/commit/480175e7396364778c5a10cdc038a2c1eda442e0))
* add dd-need-017 (commit [8ee24112](https://github.com/digital-land/planning-application-data-specification/commit/8ee24112dc8221d1dd6dc36bc9ee77aebac9c2bf))
* update dd-need-014 (commit [5c8e4ec0](https://github.com/digital-land/planning-application-data-specification/commit/5c8e4ec051221f5a397c5e9f02623d4f651caf29))
* add dd-need031 (commit [0bf88abe](https://github.com/digital-land/planning-application-data-specification/commit/0bf88abecf5403f1c3ce3c5e5a839df544b1b218))
* update just-0001 to make it more of a universal rule to be applied across datasets (commit [b62c213f](https://github.com/digital-land/planning-application-data-specification/commit/b62c213f5cf8e820fd6eeca1884708f13be21ca5))
* add design decision record for calling dataset planning-application (commit [2a044bc4](https://github.com/digital-land/planning-application-data-specification/commit/2a044bc48b0c8f766aff3cc968c0b957f279c1d2))
* add justication record for dd-need-033 and dd-need-034 (commit [58e0cd69](https://github.com/digital-land/planning-application-data-specification/commit/58e0cd69583ac530da4f2a14e4150f461180f5f7))
* add a couple of needs (commit [3907d8df](https://github.com/digital-land/planning-application-data-specification/commit/3907d8df11f85e5c6eb8a3bcbe432699e276c3a0))
* add design decision record about submitting documents with applications (commit [3875017f](https://github.com/digital-land/planning-application-data-specification/commit/3875017f36d62290ddeacc7cba54cae8f0e3e67d))
* update specification folder readme based on feedback (commit [1a4c5dc6](https://github.com/digital-land/planning-application-data-specification/commit/1a4c5dc6118db50aba92996183c8e93e1125d239))
* document what need and justification records are (commit [9c68d9ba](https://github.com/digital-land/planning-application-data-specification/commit/9c68d9bab17b3dc0d424699a3a9c2ce9c9483749))
* log how dd-need-048 is satisfied (commit [6987161d](https://github.com/digital-land/planning-application-data-specification/commit/6987161d39d4cb59ef2c2a5492358b4be1f746fb))
* capture how data-need-001 is satisfied (commit [bec330a0](https://github.com/digital-land/planning-application-data-specification/commit/bec330a0574642e6c599502eb0b3415e828730b9))
* document how the data model is structured (commit [77017a2e](https://github.com/digital-land/planning-application-data-specification/commit/77017a2e5a1fb1b8d1c9811c4e16ee4998f6ea1b))


<a name="v0.1.38"></a>
## [v0.1.38](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.37...v0.1.38) (2025-12-16)

Be explicit about allowing additional properties or not

### ⚒️ Tooling

* handle not allowing additional properties, should output false: (commit [11421cd0](https://github.com/digital-land/planning-application-data-specification/commit/11421cd0c3bab7976450d5d19fa2ad9cfc81a5d7))
* update JSON schema generator to handle allow-additional-properties attr (commit [b1b5d0ff](https://github.com/digital-land/planning-application-data-specification/commit/b1b5d0ffc53c0ecd6b80680ee06aee7465f9e2ca))
* count number of fields of a module for comparison (commit [da2ed088](https://github.com/digital-land/planning-application-data-specification/commit/da2ed0881115420b4b732b89815479605b369207))
* fix generating application fields section (commit [7e9f2d66](https://github.com/digital-land/planning-application-data-specification/commit/7e9f2d66b397c73d34e950be1338684f13f61bb2))

### 𝌭 Model changes

* add allow-additional-properties to all other application types (commit [407a8095](https://github.com/digital-land/planning-application-data-specification/commit/407a8095819948ea3dd0eb4b038ee474185d6e7b))
* add allow-additional-properties to outline apps (commit [e0960d75](https://github.com/digital-land/planning-application-data-specification/commit/e0960d75501a357aac2b2fe779bf85fbb39b9616))
* add allow-additional-properties: true to full application definition (commit [7b4f58d5](https://github.com/digital-land/planning-application-data-specification/commit/7b4f58d5b2755d2e510de9edac5a9cf9566d2c03))
* list permission types that make related-permission related required (commit [c35150f7](https://github.com/digital-land/planning-application-data-specification/commit/c35150f7c5f803a9eb927b573a7ab9566ab66de4))
* add missing permission type module and use in extract oil gas application (commit [77758962](https://github.com/digital-land/planning-application-data-specification/commit/77758962fc6766ae1225f01fed539ebcad5ca046))

### 🐛 Bug Fixes

* remove redundant info models for oil and gas app (commit [c874330e](https://github.com/digital-land/planning-application-data-specification/commit/c874330e3e86ee28f5293b2cab2ce40309f3904b))
* remove redundant info models for outline apps (commit [e3107295](https://github.com/digital-land/planning-application-data-specification/commit/e310729597b35e787b07ad2c6d432574e9a943f7))
* typo in documentation (commit [2932ccd1](https://github.com/digital-land/planning-application-data-specification/commit/2932ccd18d28919cdab7b71009f3ec2a48b934c9))

### 📚 Documentation

* add decision record for allowing additional properties (commit [eea1c30d](https://github.com/digital-land/planning-application-data-specification/commit/eea1c30d10c0c9c7ae2582c6dab0e1f990f73e72))
* document the differences between submission and decision specifications (commit [1aadbbc6](https://github.com/digital-land/planning-application-data-specification/commit/1aadbbc684f6f6379c966c37fffa9752eb514bfd))


<a name="v0.1.37"></a>
## [v0.1.37](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.36...v0.1.37) (2025-12-05)

Add missing nmodule

### 𝌭 Model changes

* list permission types that make related-permission related required (commit [cc7718e1](https://github.com/digital-land/planning-application-data-specification/commit/cc7718e196a83db1c79a719cdeb5c66e980db035))
* add missing permission type module and use in extract oil gas application (commit [6ca7cbcc](https://github.com/digital-land/planning-application-data-specification/commit/6ca7cbcc2202b13e09897df6477634715949582d))


<a name="v0.1.36"></a>
## [v0.1.36](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.35...v0.1.36) (2025-11-24)

Responding to feedback

### ⚒️ Tooling

* build a codelist that combines local-authorities, national-park-authorities and development corporations (commit [8459b7cc](https://github.com/digital-land/planning-application-data-specification/commit/8459b7cce4b57e83700d14be38760bcd6dbdf7ef))
* expand cli to find instances of fields (commit [cea826d2](https://github.com/digital-land/planning-application-data-specification/commit/cea826d24b246ecabd42f6c6278f8f879a517a7c))
* commandline interface to find which app types use a module (commit [f8071acb](https://github.com/digital-land/planning-application-data-specification/commit/f8071acb136df84849d03c1aa895f06da0f43311))

### 𝌭 Model changes

* remove unused application module (commit [5ebf1d12](https://github.com/digital-land/planning-application-data-specification/commit/5ebf1d124ead71a3e5ac37de5f12e7c9617a0117))
* add end-date to unused application module (commit [89802de0](https://github.com/digital-land/planning-application-data-specification/commit/89802de04b198b1ec5d5935c928dda6b48d060ec))
* add built planning-authority codelist (commit [e171ba8d](https://github.com/digital-land/planning-application-data-specification/commit/e171ba8db2146d52da394464592fbda2da707c11))
* define planning-authority codelist needed for planning-authority field (commit [56ff295a](https://github.com/digital-land/planning-application-data-specification/commit/56ff295a0aa22634c8eadd08491363058a2797cb))
* add missing description of proposal for work to lb for lawful dev cert module (commit [11fa70a5](https://github.com/digital-land/planning-application-data-specification/commit/11fa70a59721ce5e0212827b272994efb89ed62a))
* add notes to technical details consent application (commit [3e88183b](https://github.com/digital-land/planning-application-data-specification/commit/3e88183b40d0548355ae3a12cfad6ac5ba78a769))
* add planning-requirement codelist (commit [879e056b](https://github.com/digital-land/planning-application-data-specification/commit/879e056b5616d0df6052469db07dbaacfaefd3c0))

### 🐛 Bug Fixes

* add rules stating modules referencing documents must refer to documents in application.documents (commit [c60bf1d0](https://github.com/digital-land/planning-application-data-specification/commit/c60bf1d0c2fb0b616751866206b9555dfc59efff))
* update ldc-proposed-work-lb app to use desc-proposed-works-lb-ldc module (commit [30972d27](https://github.com/digital-land/planning-application-data-specification/commit/30972d27e844ac0aaa82513d017510865d67aed9))
* use the right interest in details or land modules for advertising and ldc applications (commit [f03307f9](https://github.com/digital-land/planning-application-data-specification/commit/f03307f9a34b27ea7b67ce4b1d53f112c9f7793e))
* correct datatype to date on -date fields (commit [2ddcd4c0](https://github.com/digital-land/planning-application-data-specification/commit/2ddcd4c00a6169707d2ea42701deaafd63db40be))

### 👷‍♀️ Application changes

* add schema for technical details consent application (commit [aa59179a](https://github.com/digital-land/planning-application-data-specification/commit/aa59179a78d7c8e79a30a03dfaa06b1dff4bcc88))

### 📚 Documentation

* split application types by priority -> those that affect housing delivery (commit [59a74062](https://github.com/digital-land/planning-application-data-specification/commit/59a74062c24e9a34bc55dab41a0a8edee3dfb827))
* add technical details consent to list of applications in scope (commit [45e61c2d](https://github.com/digital-land/planning-application-data-specification/commit/45e61c2dcaebfa6d420a9c1125f8209a88ca9609))
* add some documentation about the work into decision data (commit [fe5b4fe2](https://github.com/digital-land/planning-application-data-specification/commit/fe5b4fe2ce2ca1894bc9bd67d1cda5e932471364))


<a name="v0.1.35"></a>
## [v0.1.35](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.34...v0.1.35) (2025-10-30)

Fixes and enhancements

### ⚒️ Tooling

* increase flexibility of where codelist sources can reside (commit [35816cc5](https://github.com/digital-land/planning-application-data-specification/commit/35816cc586ecd78fc36551c6e422b2e211ffa9e4))
* generate version of spreadsheet output with references (commit [df7b194e](https://github.com/digital-land/planning-application-data-specification/commit/df7b194ea4a5b7fc7efa7804d2bf04f77a38f43b))

### 𝌭 Model changes

* add use-class-accommodation codelist, used in room details component (commit [c0b2775b](https://github.com/digital-land/planning-application-data-specification/commit/c0b2775b2e1aa2ddec9a01a6ae6963d9102c6b52))
* add use-class codelist (commit [73e82898](https://github.com/digital-land/planning-application-data-specification/commit/73e82898b81289d232c551f7138aa0cb0fdf4536))

### 🐛 Bug Fixes

* add missing application-subtype codelist (commit [dd72ae9a](https://github.com/digital-land/planning-application-data-specification/commit/dd72ae9af8de960bae28c5cfb367c18c15bdae11))
* add missing source url for application-type codelist (commit [059b30fb](https://github.com/digital-land/planning-application-data-specification/commit/059b30fbba944f2887a2935d15be6f5ed0331b01))
* rename use-class field to use-class-accommodation to more accurately reflect purpose' (commit [a15399aa](https://github.com/digital-land/planning-application-data-specification/commit/a15399aa546294e4f0cecb6106945f86e0041dc8))
* required-of condition should have value attr (commit [aceb32e0](https://github.com/digital-land/planning-application-data-specification/commit/aceb32e058d279dc32ee01df01449e5a37036f41))
* github workflow ci issues (commit [88ec0aa7](https://github.com/digital-land/planning-application-data-specification/commit/88ec0aa7201115764c4d4893ce22d208deb417c1))


<a name="v0.1.34"></a>
## [v0.1.34](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.33...v0.1.34) (2025-10-27)

Tool tweaks and documentation

### ⚒️ Tooling

* add make target to move documentation to generated folder (commit [a948479c](https://github.com/digital-land/planning-application-data-specification/commit/a948479cb665b7928764917195a377e4b2295fe3))
* add documentation for outputs generated from the model (commit [8e138893](https://github.com/digital-land/planning-application-data-specification/commit/8e1388934a40be5d3e199d19d1f16cbc112a362a))

### 𝌭 Model changes

* add specific description to name field in document component (commit [b090b11b](https://github.com/digital-land/planning-application-data-specification/commit/b090b11bc5b05db0aac8bf2336a607312faace1c))
* update legislation field to legislation-urls (commit [57a64e98](https://github.com/digital-land/planning-application-data-specification/commit/57a64e98828e19116bdea29a8fc0b1d54b96df56))

### 🐛 Bug Fixes

* issues with bullet lists in documentation (commit [57621827](https://github.com/digital-land/planning-application-data-specification/commit/57621827326a2b08ccbc5e9161be60e3e830134a))
* extra column in one row of planning application types dataset (commit [ea82e2cc](https://github.com/digital-land/planning-application-data-specification/commit/ea82e2ccf533618d5b68640b983fab5c14ddfbca))

### 👷‍♀️ Application changes

* add missing description for extraction of oil and gas applications (commit [dc4cbf7b](https://github.com/digital-land/planning-application-data-specification/commit/dc4cbf7bcf0080432c7848da023b18aa4ea63e1c))

### 📚 Documentation

* add links to the corresponding output code and folderS (commit [1969c6f6](https://github.com/digital-land/planning-application-data-specification/commit/1969c6f69aa314071021628ebbe83e407e0d8dc1))


<a name="v0.1.33"></a>
## [v0.1.33](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.32...v0.1.33) (2025-09-24)

Generate JSON schemas

### ⚒️ Tooling

* add func to return applications where a module is used (commit [0c4de6d6](https://github.com/digital-land/planning-application-data-specification/commit/0c4de6d6c167e0542b4d971cacdcb01c71f53e20))
* ran black formatting (commit [04be585b](https://github.com/digital-land/planning-application-data-specification/commit/04be585b75e8867807bfd8a3c5f4ea812eca4c9a))
* Parameterize json schema validation unit test test_valid_application (commit [022e7018](https://github.com/digital-land/planning-application-data-specification/commit/022e7018e9d29b574854b9ca2e86b01e0ba183db))
* Refactored to move mapping helpers to own module. Fixed bug in mapping incorrectly or'ing multiple required lists, when in should have been and'ing (commit [ddf32f62](https://github.com/digital-land/planning-application-data-specification/commit/ddf32f62cfeff72fffc61071b835d4bb18736b42))
* update example HH payload to use correct organisation reference (commit [ef565897](https://github.com/digital-land/planning-application-data-specification/commit/ef5658976b7657325beb4e85ff07ae6e18522169))
* check fields referenced in required-if statements exist (commit [e60e87a1](https://github.com/digital-land/planning-application-data-specification/commit/e60e87a1bac51d89f5e5926dd304dccc7e44f0a9))

### 𝌭 Model changes

* tweak 2 modules descriptions (commit [ffaeade3](https://github.com/digital-land/planning-application-data-specification/commit/ffaeade3c3b80e6f1718cf086c73937110b9cc69))
* rename field from additional-material-information to providing-additional-material-information (commit [5de1b49e](https://github.com/digital-land/planning-application-data-specification/commit/5de1b49e99f3c6e773ae3b617de9226144890332))
* add minimal sample hh payload (commit [a44e2eea](https://github.com/digital-land/planning-application-data-specification/commit/a44e2eea3b9608a090d2f8e77c0e9bd627f547bc))

### 🐛 Bug Fixes

* Fixed incorrect property type in example and added required supported-documents property (commit [488d43b4](https://github.com/digital-land/planning-application-data-specification/commit/488d43b42564d3097a8a7c3717098b0b976834e4))
* supporting documents only needed in access rights of way module if one of the other fields is true. Corrected in sample payload (commit [05b4940e](https://github.com/digital-land/planning-application-data-specification/commit/05b4940e8022d5c542048013934a908618be541e))
* Removed redundant allOf in cases where only one condition to evaluate. Updated example payload to use correct datatypes. Updated conftest to load new example - note still fails test (commit [db333dcf](https://github.com/digital-land/planning-application-data-specification/commit/db333dcfbc533f26a14b29d26b8fef3601070c5b))
* issue with circular imports (commit [da4994ff](https://github.com/digital-land/planning-application-data-specification/commit/da4994ffaaca8104e441969fce45fe14df9f7667))
* JSON schema generation now works for appliction sub-types. Extented load_spefication_model to resolve inheritance hierachies (commit [c7edc6d9](https://github.com/digital-land/planning-application-data-specification/commit/c7edc6d9cce8d850087b47c2f3ec5650da1ec5ad))
* List of required properties for application was not listing all modules (commit [1563367f](https://github.com/digital-land/planning-application-data-specification/commit/1563367fbaa1199b1dd5c6ec06e8215ceb6de771))

### 👷‍♀️ Application changes

* add missing spec for extraction of oil and gas application (commit [78262cff](https://github.com/digital-land/planning-application-data-specification/commit/78262cff5f12902987965076be3ae9adaece20a5))

### 📚 Documentation

* Added example script is done (commit [0b7e2b98](https://github.com/digital-land/planning-application-data-specification/commit/0b7e2b98c496bab96b5b9c0950491fa85a82f64a))
* Added notion of using tags to denote schema version in url. (commit [92f9282c](https://github.com/digital-land/planning-application-data-specification/commit/92f9282cd8886e29d83d6ef6fa820dd629213169))
* Clarify validation steps (commit [9808d666](https://github.com/digital-land/planning-application-data-specification/commit/9808d666f9d79d984eb9ef3b6c9b6e6533bb17bb))
* Update json-schema-generation.md (commit [bbb3d431](https://github.com/digital-land/planning-application-data-specification/commit/bbb3d4318f973aab003df11c2806bc4e4c0a56ab))
* Added note about need for sample applications (commit [5f217738](https://github.com/digital-land/planning-application-data-specification/commit/5f217738dec236f8181c00b6a5497cf21b251d3a))
* Reworked the conditional logic mapping section of json schema generation to be clearer (commit [145ee2fc](https://github.com/digital-land/planning-application-data-specification/commit/145ee2fc3914c26c371cb515f390acdcbd992ac5))
* Update future considerations (commit [009d3342](https://github.com/digital-land/planning-application-data-specification/commit/009d33424a7775210d0599ecb3c9423c77f4f335))
* Clarify code comments Add future considerations to readme. Correct example hh application json (commit [ce688fd8](https://github.com/digital-land/planning-application-data-specification/commit/ce688fd82c7a9a5e99c7c833bb36c550cfa09c94))


<a name="v0.1.32"></a>
## [v0.1.32](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.31...v0.1.32) (2025-09-12)

batch updates and descriptions

### ⚒️ Tooling

* to batch update application or module definitions (commit [e9690a38](https://github.com/digital-land/planning-application-data-specification/commit/e9690a387c9d89c561e90c71aeef39ff1ccd1f00))

### 𝌭 Model changes

* rework module descriptions (commit [a9392792](https://github.com/digital-land/planning-application-data-specification/commit/a939279276875e3fc65ceb08999be8bebee819fe))

### 👷‍♀️ Application changes

* add synonyms for Approval of details reserved by condition applications (commit [19ab81f0](https://github.com/digital-land/planning-application-data-specification/commit/19ab81f0315584fee279bf82241c4436aea1466c))
* tweak so application names based on feedback (commit [4b9ffaeb](https://github.com/digital-land/planning-application-data-specification/commit/4b9ffaeb8814ad0ac7b605942849da4e976ddc0d))
* update description for lbc and demolition in conservation area applications (commit [0ee8358a](https://github.com/digital-land/planning-application-data-specification/commit/0ee8358a68820a84ed9c815d05053b7cd0fe66a9))


<a name="v0.1.31"></a>
## [v0.1.31](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.30...v0.1.31) (2025-09-10)

update the list of application types

### ⚒️ Tooling

* compare complete list of application types with those defined in the specification(s) (commit [7ecd124d](https://github.com/digital-land/planning-application-data-specification/commit/7ecd124d4ceee65da197fe34a528178da5d81ec2))

### 𝌭 Model changes

* tweaks to application type data based on feedback (commit [368b471a](https://github.com/digital-land/planning-application-data-specification/commit/368b471a7b962135c95f4b9a700d935a5a867be5))
* add declarative version of permission-type module (commit [2b622f7e](https://github.com/digital-land/planning-application-data-specification/commit/2b622f7e7cdd2da1805ba3001eb283bc8fd313d2))

### 🐛 Bug Fixes

* mv schemas for planning requirement datasets to docs (commit [6aaf78ed](https://github.com/digital-land/planning-application-data-specification/commit/6aaf78edbfbd973d515e414e89d2d14e60206585))
* remove compiled application specifications from specification/application folder: (commit [3ebd6e02](https://github.com/digital-land/planning-application-data-specification/commit/3ebd6e0266de7e88bbdfc4a308803328c3829f10))
* remove rest of replaced module info models (commit [4fe142fa](https://github.com/digital-land/planning-application-data-specification/commit/4fe142fa3244da613272fbe2caafd4f9712682ba))
* remove replaced information models (commit [ee362acd](https://github.com/digital-land/planning-application-data-specification/commit/ee362acd33045ee0db7b228c6db86b136ff024be))
* module should use required-if structure not applies-if (commit [c6c89b54](https://github.com/digital-land/planning-application-data-specification/commit/c6c89b54b268b3fcd93e343180dbc2915ffe20de))

### 👷‍♀️ Application changes

* add public sector infrastucture to list of application types (commit [dcf54c74](https://github.com/digital-land/planning-application-data-specification/commit/dcf54c740b50d0da35f57b5708e97d99a5efc9de))
* add hazardous substance consent to list of application types (commit [23052e3d](https://github.com/digital-land/planning-application-data-specification/commit/23052e3ddb021af9de8d96205379f0c00dacfb87))
* add review of mineral permission to list of application types (commit [356ce94f](https://github.com/digital-land/planning-application-data-specification/commit/356ce94ffa8532a58d53c2f55b327552c59103e0))
* add technical details consent to list of application types (commit [de282222](https://github.com/digital-land/planning-application-data-specification/commit/de282222725ca6fbcb3ec1983428f39b04f90646))
* add minerals application to list of application types (commit [95c2de5a](https://github.com/digital-land/planning-application-data-specification/commit/95c2de5a011b9ff9e972d832872861f83e38044c))
* add regulation 4 to list of application types (commit [5cf94ae1](https://github.com/digital-land/planning-application-data-specification/commit/5cf94ae10412e9e6c749a531c9d34efb5f49dc88))
* add regulation 3 to list of application types (commit [8e8b69a6](https://github.com/digital-land/planning-application-data-specification/commit/8e8b69a636748ebe4e8612fe1bd0a97ad3b44e63))
* add change of use to list of application types (commit [7304eb35](https://github.com/digital-land/planning-application-data-specification/commit/7304eb353b0abaed859c3a0a60983b92916464a6))
* add transport and works act order to list of application types (commit [c73f1561](https://github.com/digital-land/planning-application-data-specification/commit/c73f156140867a09c920ededd3fdef4638ececbd))
* add modification or discharge of section 106 obligation to list of application types (commit [c5d1987e](https://github.com/digital-land/planning-application-data-specification/commit/c5d1987ea3d5f14eb4986fb205c0ea58cd116c96))
* add mineral extraction to list of application types (commit [fbe3c605](https://github.com/digital-land/planning-application-data-specification/commit/fbe3c605d0854edba5099daa75db34fbd5668777))
* add additional environmental approval to extend permission period to list of application types (commit [29504f1a](https://github.com/digital-land/planning-application-data-specification/commit/29504f1a7092a08c6c51524f2f4c251097d142aa))
* add modification of conditions relating to construction of working hours to list of application types (commit [d1b6137f](https://github.com/digital-land/planning-application-data-specification/commit/d1b6137fdcbcbe636f5442b5cb8f815ce5de457e))
* add nsips to list of application types (commit [5a9f1b26](https://github.com/digital-land/planning-application-data-specification/commit/5a9f1b262232da602287caf5662a98d3a14147b0))
* add overhead line consent to list of application types (commit [ee30bfd0](https://github.com/digital-land/planning-application-data-specification/commit/ee30bfd0d6c79ba7375492033a15301389bfc07c))
* add certificate of alternative appropriate dev to list of application types (commit [7ac52197](https://github.com/digital-land/planning-application-data-specification/commit/7ac521979749033c2cefbc9914f8453282503e28))
* add footpath diversion to list of application types (commit [10778fd6](https://github.com/digital-land/planning-application-data-specification/commit/10778fd6a912d68c23111d68c2deb122be3ec829))
* add land drainage consent to list of application types (commit [5b2ca0ac](https://github.com/digital-land/planning-application-data-specification/commit/5b2ca0ac45a6ef7514b8f6a62e79bd34c8bc4e15))
* add waste development to list of application types (commit [f5e70d5c](https://github.com/digital-land/planning-application-data-specification/commit/f5e70d5c22fb45084bccb9070f5d8f4ebf0b3b0c))


<a name="v0.1.30"></a>
## [v0.1.30](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.27...v0.1.30) (2025-09-08)

Spreadsheet generator

### ⚒️ Tooling

* code to extract all modules into a csv (commit [fd657b95](https://github.com/digital-land/planning-application-data-specification/commit/fd657b95d494c9691c2627f3691b19a6a3f6abf8))
* add spreadsheet builder to make targets (commit [98623db5](https://github.com/digital-land/planning-application-data-specification/commit/98623db5fa9e9b1868d2d7c84ee57aefaec891de))
* generate spreadsheets for all top level app types (commit [6768fa03](https://github.com/digital-land/planning-application-data-specification/commit/6768fa03455209896190f7323cd4bce63660602e))
* make the application details in rows optional (commit [e3dc5195](https://github.com/digital-land/planning-application-data-specification/commit/e3dc5195c1b5e36a5e9d681fe766ad3fb17f16f8))
* create spreadsheet for compiled spec that only includes relevant fields (commit [ad86115b](https://github.com/digital-land/planning-application-data-specification/commit/ad86115b2e0968ae0f548533540b75ab8de5e4cc))
* add check of applies-if structure in modules (commit [57feb11b](https://github.com/digital-land/planning-application-data-specification/commit/57feb11bf74c1ec737cf1e9d55c2aa9df8e1f688))
* add a FieldInstance class to handle overrides in modules (commit [5d9a657a](https://github.com/digital-land/planning-application-data-specification/commit/5d9a657ad32d3998fbbf33c11c09e6b2751ae668))
* minor refactoring of spreadsheet generator (commit [8593d26c](https://github.com/digital-land/planning-application-data-specification/commit/8593d26cf8a6bfad5a9b660dde7e8c5fa71fb6e8))
* output example hh specification as spreadsheet (commit [91cd5f4c](https://github.com/digital-land/planning-application-data-specification/commit/91cd5f4c09791275720141aa8a29f62d67c42826))
* func to load the specification as objects (commit [d2b8ec46](https://github.com/digital-land/planning-application-data-specification/commit/d2b8ec46203923ecac211f980706a45042f02750))
* output spreadsheet style spec using example specification (commit [08604096](https://github.com/digital-land/planning-application-data-specification/commit/08604096231494f87169ba355dd9ba41167feac2))
* code to extract all modules into a csv (commit [3e77f5bf](https://github.com/digital-land/planning-application-data-specification/commit/3e77f5bf051f67370263a8fac0dd289be6a16731))
* func to return original forms for an app type (commit [30c47be8](https://github.com/digital-land/planning-application-data-specification/commit/30c47be8b8954a70e1109caf2871dcc90bb075b7))

### 🐛 Bug Fixes

* conditions should be required-if not applies-if (commit [418753a9](https://github.com/digital-land/planning-application-data-specification/commit/418753a917464a1e02f849b9b591426a95da6a80))
* name field needs specific description when used in supporting document component (commit [897b4ddd](https://github.com/digital-land/planning-application-data-specification/commit/897b4dddd1f29c05e6eb48fa41171ddf829d22ac))
* incorrect structure used for applies-if application-type conditions (commit [8e9c0d6e](https://github.com/digital-land/planning-application-data-specification/commit/8e9c0d6e56227bd551148d743bfe19c9c1a7aad3))


<a name="v0.1.27"></a>
## [v0.1.27](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.26...v0.1.27) (2025-08-29)

Resolve remaining phase 1 issues and improve tooling

### ⚒️ Tooling

* include list of codelists in contents of compiled specifications (commit [d3e9082a](https://github.com/digital-land/planning-application-data-specification/commit/d3e9082aa6499ba1b96317dd0e563f5d58a105a4))
* include contents of codelists in compiled specifications (commit [22182445](https://github.com/digital-land/planning-application-data-specification/commit/221824450ee638cca0e98f596cae7afdc3188fdf))
* compiling specifications follows the extend attr for sub application types (commit [f652d0fc](https://github.com/digital-land/planning-application-data-specification/commit/f652d0fc8fd776896f1354cc166ef5fd29d46e70))
* add check to confirm codelist referenced exists (commit [7a604f2b](https://github.com/digital-land/planning-application-data-specification/commit/7a604f2b7f692094e808cb7a31e577954b8eeee1))
* set up tests for tooling code (commit [341b5fae](https://github.com/digital-land/planning-application-data-specification/commit/341b5faea76cb00e1499a2b379eb1bfdd7fb3f51))
* refactor section that outputs markdown tables for info model (commit [89f6156d](https://github.com/digital-land/planning-application-data-specification/commit/89f6156ddbd6f345c60aa9b01238b8ffdf81d72e))

### 𝌭 Model changes

* make it clear net-additional-floorspace should be calculated automatically (commit [c96afb9e](https://github.com/digital-land/planning-application-data-specification/commit/c96afb9eea1ba7ec72580d7f7a4d7cd7749b3758))
* handle variance in room-details component for outline applications (commit [f0b63044](https://github.com/digital-land/planning-application-data-specification/commit/f0b63044b8f950a59a608c91d5c44524bbd555e8))
* handle variance in floorspace-details module for outline apps (commit [30e56c2f](https://github.com/digital-land/planning-application-data-specification/commit/30e56c2f3a50d94eae1d791c3774d1102b93f6b3))
* add non-residential-change-outline to handle unknown answer for outline applications (commit [ea4bff64](https://github.com/digital-land/planning-application-data-specification/commit/ea4bff647439dda47df2a405057bd3acdf6e93d3))
* experiment with codifying a count-constraint (commit [a86a4c0f](https://github.com/digital-land/planning-application-data-specification/commit/a86a4c0fc8acf661530f098bd64162ce01832aae))
* add illumination-type codelist (commit [58af557e](https://github.com/digital-land/planning-application-data-specification/commit/58af557e0846a039594e1d17c77c79b366c4ee84))

### 🐛 Bug Fixes

* typos in illumination-type codelist (commit [a619a046](https://github.com/digital-land/planning-application-data-specification/commit/a619a046456ab4022c685d26b5d4466e93ab3c37))
* use correct field for outline applications, should be separate-recycling-arrangements-outline (commit [0eb59fc2](https://github.com/digital-land/planning-application-data-specification/commit/0eb59fc24aceb0cac23a86d70be213eace313e39))
* information model output for modules (commit [defdad5d](https://github.com/digital-land/planning-application-data-specification/commit/defdad5d5837be43b247d38db83e28027f2a6434))
* pass codelists to field checks (commit [88887b64](https://github.com/digital-land/planning-application-data-specification/commit/88887b64e68b3da45b32a6063f69152846e0e565))
* references to codelists (commit [0e915d1a](https://github.com/digital-land/planning-application-data-specification/commit/0e915d1ac8aed7c58ad5b1b1af566ba7e6ea0253))


<a name="v0.1.26"></a>
## [v0.1.26](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.25...v0.1.26) (2025-08-27)

Tooling: integrity checks and generating information models

### ⚒️ Tooling

* automate generation of information model when declarative model changes (commit [3560fbec](https://github.com/digital-land/planning-application-data-specification/commit/3560fbecf1ec5342d00136a3fbfcc8b506881f04))
* output whole application module and substructures when generating compiled spec (commit [90217e12](https://github.com/digital-land/planning-application-data-specification/commit/90217e1281833e950949433403080e68d5a4a866))
* generate all application info models (commit [e8e02e95](https://github.com/digital-land/planning-application-data-specification/commit/e8e02e9520a9feb828d2ebe0bc1c3a04bd418859))
* script to regenerate all module info models (commit [18e6f1df](https://github.com/digital-land/planning-application-data-specification/commit/18e6f1df768884bfc3f5576f52889094888dd10c))
* update checking required-if conditions in components (commit [c631583c](https://github.com/digital-land/planning-application-data-specification/commit/c631583c4134a556bbcfaa27fa053de7a7416abb))
* handle applications that extend base application (commit [f8b8fca3](https://github.com/digital-land/planning-application-data-specification/commit/f8b8fca3fac71fe83cfc5420e2d03f9079ae24f7))
* func to generate whole info model for given app type (commit [c4ac54f5](https://github.com/digital-land/planning-application-data-specification/commit/c4ac54f590b60ec9a732cd29d89d5956f9ca5b33))
* add util func to save string to file (commit [4c735bb0](https://github.com/digital-land/planning-application-data-specification/commit/4c735bb02dfb4403dcdbb06207b167abdfcc782c))
* make sure reference to enum is bold (commit [d0afd98b](https://github.com/digital-land/planning-application-data-specification/commit/d0afd98b440abd5f3280df1f20e8ba58711272de))
* add integrity checks for codelists (commit [782c5130](https://github.com/digital-land/planning-application-data-specification/commit/782c513088b9903c7f368b388753a7333b2fae11))

### 𝌭 Model changes

* tweak name of application module (commit [e981b7ee](https://github.com/digital-land/planning-application-data-specification/commit/e981b7eefc06932558748caf2e249bf47cb04f1c))
* all application info models now in generated/info_model/application (commit [18e472aa](https://github.com/digital-land/planning-application-data-specification/commit/18e472aa47105c01a618160df5e210240c46417e))
* generated info models now in generated/info_model directory (commit [bb17e05b](https://github.com/digital-land/planning-application-data-specification/commit/bb17e05b9c9c2dcd69478c00f412ebec0fbad3b2))
* define application-type codelist (commit [42ee3cfd](https://github.com/digital-land/planning-application-data-specification/commit/42ee3cfd4d0c212629a0c11141db67ab6251f7c3))
* add declarative version of existing-use module (commit [c4bf273f](https://github.com/digital-land/planning-application-data-specification/commit/c4bf273f4627ce41a43353f3d7872e1a7781a83c))

### 🐛 Bug Fixes

* typo in output path (commit [e573abce](https://github.com/digital-land/planning-application-data-specification/commit/e573abce2d2892aa746d4211a1af2e45227603fe))
* errors with conditions in components (commit [5d1bfce5](https://github.com/digital-land/planning-application-data-specification/commit/5d1bfce5fedff418277854a2371172e85fc862d6))
* cardinality must be 1 or n (commit [64784b5d](https://github.com/digital-land/planning-application-data-specification/commit/64784b5d01a103f142940873646a714944e67e25))
* codelist checks, only read *.schema.md files (commit [956adb30](https://github.com/digital-land/planning-application-data-specification/commit/956adb30a6f222d651a6000e4ae4d16d52cfd099))
* validation attr should be rules (commit [025cdaf2](https://github.com/digital-land/planning-application-data-specification/commit/025cdaf26fb08f81886c89240715e770d5833334))


<a name="v0.1.25"></a>
## [v0.1.25](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.24...v0.1.25) (2025-08-15)

Add codelist and codelist definitions

### 𝌭 Model changes

* add source attr for codelists (commit [bac5be96](https://github.com/digital-land/planning-application-data-specification/commit/bac5be9641a5a80cc28c8a22587d8ab64a0f7a49))
* define rights-of-way-answer codelist (commit [86b02c06](https://github.com/digital-land/planning-application-data-specification/commit/86b02c0643c57365bfe099a4c83aab04deea983d))
* define parking-space-type codelist (commit [2fa6d770](https://github.com/digital-land/planning-application-data-specification/commit/2fa6d770768c4ea98d79f888feb6989f86bdb7e9))
* define listed-building-grade codelist (commit [795bb584](https://github.com/digital-land/planning-application-data-specification/commit/795bb584f17c77f1b655ecccefbf5a90613cc668))
* define grounds-ldc-pre-apr-2024 codelist (commit [80a21254](https://github.com/digital-land/planning-application-data-specification/commit/80a212544a9a01fe96f3c97924665bdde48488a4))
* define ground-ldc-post-apr-2024 codelist (commit [c4b3aa70](https://github.com/digital-land/planning-application-data-specification/commit/c4b3aa70194f3a220f44f785a5210dd13920a92e))
* define building-element-type codelist (commit [bd99241b](https://github.com/digital-land/planning-application-data-specification/commit/bd99241b75e72a156ef3a914099aeec117c49539))
* define bng-exemptions codelist (commit [521f7653](https://github.com/digital-land/planning-application-data-specification/commit/521f7653cdfa3ac904403a4e9ddf609cf7c1da8d))
* define designations codelist (commit [30e33d82](https://github.com/digital-land/planning-application-data-specification/commit/30e33d82636d861a009c389c128b07a5d261558d))
* define yes-no-unknown codelist (commit [6f795169](https://github.com/digital-land/planning-application-data-specification/commit/6f795169ff196bee0a7c69160be51d372afec2cb))
* define yes-no-not-applicable codelist (commit [c802ee00](https://github.com/digital-land/planning-application-data-specification/commit/c802ee00880d87fad73ab794ae20c13bac3f332e))
* define waste-management-type codelist (commit [49b282ec](https://github.com/digital-land/planning-application-data-specification/commit/49b282ec129b10076054208b133c097087b0ca4c))
* define user-role-type codelist (commit [372fe561](https://github.com/digital-land/planning-application-data-specification/commit/372fe561bec8c0c6b1dc997d8c368ff7cfe2703d))
* define tenure-type codelist (commit [7823425f](https://github.com/digital-land/planning-application-data-specification/commit/7823425fdbbd9c30922b8d65da200f1fc81a4dff))
* define surface-water-disposal-type codelist (commit [2cb37974](https://github.com/digital-land/planning-application-data-specification/commit/2cb37974a842aa7c2132a7d0e76ab287fc16a126))
* define site-visit-contact-type codelist (commit [16f43272](https://github.com/digital-land/planning-application-data-specification/commit/16f43272c84615e0c683f0abfcb59c0ca872ece6))
* define site-constraints codelist (commit [6a02e2e3](https://github.com/digital-land/planning-application-data-specification/commit/6a02e2e33411dc2316e541da22b6c815768a0b19))
* define reserved-matter-type codelist (commit [bd4d1a42](https://github.com/digital-land/planning-application-data-specification/commit/bd4d1a420c4b8628bce422de573f37eebe4e8dc1))
* define provided-by codelist (commit [4411ec23](https://github.com/digital-land/planning-application-data-specification/commit/4411ec2318787c057de405dd297ab2fdb44b4f98))
* define permission-type codelist (commit [45176b26](https://github.com/digital-land/planning-application-data-specification/commit/45176b26277ccdb433366d717d9dd1e5ccfe7547))
* define ownership-cert-type codelist (commit [a0a58e39](https://github.com/digital-land/planning-application-data-specification/commit/a0a58e394b6536e6201edd11ad8eed555d140933))
* define operation-type codelist (commit [9d63aa76](https://github.com/digital-land/planning-application-data-specification/commit/9d63aa76297aa0ed065d7f0b9f1d60c074f0cc3e))
* define non-res-measurement-type codelist (commit [690da25e](https://github.com/digital-land/planning-application-data-specification/commit/690da25e264e689de3d2ef05dd4f449664b30f14))
* define lb-alertation-type codelist (commit [3118cea7](https://github.com/digital-land/planning-application-data-specification/commit/3118cea7a28b45dbc14826878273943f68f1f872))
* define lawful-dev-cert-need codelist (commit [57cd087f](https://github.com/digital-land/planning-application-data-specification/commit/57cd087f88296fac4917aa074807994d494b1629))
* define housing-type codelist (commit [85f0cf35](https://github.com/digital-land/planning-application-data-specification/commit/85f0cf35ad115d53c41f73a9a413063e8f769cdc))
* rename codelist to hedgerow-interest-type (commit [38a15dd5](https://github.com/digital-land/planning-application-data-specification/commit/38a15dd5a643fd110275b94ebf3e107f5eb63a6c))
* define hedgerow-interest-dec codelist (commit [4f989361](https://github.com/digital-land/planning-application-data-specification/commit/4f9893614c1d5e1469914554edf0e8979b76dbe6))
* define hazardous-sub-type codelist (commit [439ced8d](https://github.com/digital-land/planning-application-data-specification/commit/439ced8dbc707811fdf837910db6c0f0acc385c3))
* define foul-sewage-disposal-type codelist (commit [f4177c14](https://github.com/digital-land/planning-application-data-specification/commit/f4177c147fce694f4458a1ca3c6131d0c240fb79))
* define day-type codelist (commit [a1f6bbbe](https://github.com/digital-land/planning-application-data-specification/commit/a1f6bbbe6d337d42329d3b7c074308c67025e697))
* define contact-priority codelist (commit [70cebdd1](https://github.com/digital-land/planning-application-data-specification/commit/70cebdd13355d96c22d2d233d06e6683888a8bc8))
* define applicant-interest-type codelist (commit [2899d07c](https://github.com/digital-land/planning-application-data-specification/commit/2899d07c3db576cf39b924c6c5d446da49b14cf2))
* define affected-area-type codelist (commit [ee65d4aa](https://github.com/digital-land/planning-application-data-specification/commit/ee65d4aaa4f141437f9387c88ae100028f7cccac))
* define advertisement-type codelist (commit [39ebe980](https://github.com/digital-land/planning-application-data-specification/commit/39ebe980a8cc5e332723c3557e3a6f270cf82624))
* move source of development phase codelist (commit [2f0ec899](https://github.com/digital-land/planning-application-data-specification/commit/2f0ec899140fb6bac2f4ccf57fb3fd53b520ed23))
* define development-phase codelist (commit [892cdf2c](https://github.com/digital-land/planning-application-data-specification/commit/892cdf2c7b016c13c01d5a57d7468f1d35ebdc94))

### 🐛 Bug Fixes

* remove replaced codelists (commit [24f008a7](https://github.com/digital-land/planning-application-data-specification/commit/24f008a727683e86493e8d2ee601badaf08e1668))
* remove duplicate codelist (commit [d6888020](https://github.com/digital-land/planning-application-data-specification/commit/d6888020edb2b564e185844489fee1018c6fbce9))

### 📚 Documentation

* write up current structure for defining codelists for the specification (commit [c4e4e8fd](https://github.com/digital-land/planning-application-data-specification/commit/c4e4e8fdf9ee70b09a47a9486eabaf396d951956))


<a name="v0.1.24"></a>
## [v0.1.24](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.23...v0.1.24) (2025-08-12)

Add all remaining application type definitions

### 🐛 Bug Fixes

* fix datatype for advert-placed-date field (commit [b5ae0ce6](https://github.com/digital-land/planning-application-data-specification/commit/b5ae0ce6488748364a749543d2462106b285beda))

### 👷‍♀️ Application changes

* define app structures for ldc applications (commit [57fb5cec](https://github.com/digital-land/planning-application-data-specification/commit/57fb5cec5b0e0b5b86c3a4d6aeb657f015e4883d))
* define app structures for prior-approval applications (commit [003c94b5](https://github.com/digital-land/planning-application-data-specification/commit/003c94b5d47174ccc8f0d4f5ba32d2166fe65ba1))
* define app structures for outline applications (commit [ed59288b](https://github.com/digital-land/planning-application-data-specification/commit/ed59288b5d959ed7be2b147b3ffaf3e770e3221e))
* define the structure for full application (commit [2331b6f9](https://github.com/digital-land/planning-application-data-specification/commit/2331b6f9e4d613e979146b2c234bfeef8a6e5532))
* define the structure for lbc application (commit [fa4e9d13](https://github.com/digital-land/planning-application-data-specification/commit/fa4e9d13abe7473b61ac1d0ef6df10ed0fa94424))
* define the structure for notice-trees-in-con-area application (commit [2112a44b](https://github.com/digital-land/planning-application-data-specification/commit/2112a44b07e63d6301b23ea9d104b93ada99739b))
* define the structure for reserved-matters application (commit [86194678](https://github.com/digital-land/planning-application-data-specification/commit/86194678e163417f7e31e46fd7a04eb9d5a7cbe8))
* define the structure for s73 application (commit [ddb57c3e](https://github.com/digital-land/planning-application-data-specification/commit/ddb57c3e1ce20f749851573ecfb9b896c7914eb6))
* define the structure for non-material-amendment application (commit [099c70bf](https://github.com/digital-land/planning-application-data-specification/commit/099c70bf3faf74824a72eb53d2c1086d7947ba34))
* define the structure for hedgerow-removal application (commit [df0aab3e](https://github.com/digital-land/planning-application-data-specification/commit/df0aab3e456e0180c892b2e5adfee7bad5c69cf7))
* define the structure for demolition-con-area application (commit [72f9bd23](https://github.com/digital-land/planning-application-data-specification/commit/72f9bd2322c46d377890d000d939dafebde5f8ac))
* add declarative version of approval-condition application (commit [3be761ab](https://github.com/digital-land/planning-application-data-specification/commit/3be761ab287065a3c79af783157e77d3c30082a4))
* add declarative version of advertising application (commit [b4733304](https://github.com/digital-land/planning-application-data-specification/commit/b473330411531cd3bb966b084deb10994e267fca))


<a name="v0.1.23"></a>
## [v0.1.23](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.22...v0.1.23) (2025-07-22)

Bit of tidying things up

### ⚒️ Tooling

* alter table format if generating for specific app type (commit [94efdfa3](https://github.com/digital-land/planning-application-data-specification/commit/94efdfa3924d03568031ccecc7fa9327c1a9f0ee))
* refactor generate info model script (commit [84842d25](https://github.com/digital-land/planning-application-data-specification/commit/84842d251a0e1fcfc967fb55864bb6f5d2490ab5))
* generate module markdown filtering fields that are not applicable (commit [cf72d84e](https://github.com/digital-land/planning-application-data-specification/commit/cf72d84e07354b6f8d56b5da43525b474241747a))
* generate the markdown for a module (commit [63a62a7e](https://github.com/digital-land/planning-application-data-specification/commit/63a62a7e79bbc3809f85f6eb6ad753d638f2ec00))
* check only expected attrs are included in module definitions (commit [e94920a0](https://github.com/digital-land/planning-application-data-specification/commit/e94920a05317dd9b8993b4828bd3e350f1894348))

### 🐛 Bug Fixes

* pip-reference should have an applies-if condition not required-if condition (commit [daab0a7b](https://github.com/digital-land/planning-application-data-specification/commit/daab0a7bfed8f29e5aded16449b4fef4a032e072))
* remove unneccessay attrs from module definitions (commit [102afc31](https://github.com/digital-land/planning-application-data-specification/commit/102afc31563ddd03a15b2bfef93e15144ee2694f))
* implementation is an allowable attr for module definitions (commit [c9b075ef](https://github.com/digital-land/planning-application-data-specification/commit/c9b075ef67882248b65855217ca8fbb5f60adafa))
* module attribute should be notes not note (commit [8a50b22e](https://github.com/digital-land/planning-application-data-specification/commit/8a50b22e39ad8fb2ef8c9815da54981b1296d5a6))
* module attribute should be rules not validation (commit [75c02d8b](https://github.com/digital-land/planning-application-data-specification/commit/75c02d8b82a4974fccd25243af691ca5a0977980))


<a name="v0.1.22"></a>
## [v0.1.22](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.21...v0.1.22) (2025-07-18)

Final set of declarative versions of modules

### 𝌭 Model changes

* add declarative version of interest-details module (commit [3893fc3f](https://github.com/digital-land/planning-application-data-specification/commit/3893fc3f2031a2dca13679ba650e4db6f8d11650))
* add declarative version of eligibility-related-works module (commit [6a456dd9](https://github.com/digital-land/planning-application-data-specification/commit/6a456dd9d55d706b464665044953778d50a4d1bd))
* add declarative version of eligibility module (commit [4b1639a0](https://github.com/digital-land/planning-application-data-specification/commit/4b1639a027dd1bb13de203ede28faa44c749c4d2))
* add declarative version of eligibility-proposal module (commit [71db37b9](https://github.com/digital-land/planning-application-data-specification/commit/71db37b9f936d7b7cce0f7be57f3bda5bed9af8b))


<a name="v0.1.21"></a>
## [v0.1.21](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.20...v0.1.21) (2025-07-18)

Reworking the residential units module

### ⚒️ Tooling

* generate field dataset (commit [99f1cba7](https://github.com/digital-land/planning-application-data-specification/commit/99f1cba72adb27a81735b8e98e8c32d273d0986d))

### 𝌭 Model changes

* rename field from residential-unit-change to will-residential-units-change (commit [72cdf872](https://github.com/digital-land/planning-application-data-specification/commit/72cdf872f8a371b8cff75baba72e16f200751e4f))
* add declarative version of the res-units module (commit [78a602e6](https://github.com/digital-land/planning-application-data-specification/commit/78a602e67908ca31b5acb0c666962aad0a643687))
* update the res-unit module to handle houses of any bedroom number (commit [5ab7aa41](https://github.com/digital-land/planning-application-data-specification/commit/5ab7aa41b23c5edcc21ab42d229564fb26e25798))

### 🐛 Bug Fixes

* field description needed to be in quotes (commit [31128dd6](https://github.com/digital-land/planning-application-data-specification/commit/31128dd67501f25da797f968d45f635c58507c8e))

### 📚 Documentation

* added implementation note about how res-units module should be interpreted for paper forms (commit [03c7e367](https://github.com/digital-land/planning-application-data-specification/commit/03c7e36760f25386023ae10f4e11b2ca94be2e20))


<a name="v0.1.20"></a>
## [v0.1.20](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.19...v0.1.20) (2025-07-17)

Declarative versions of modules

### 𝌭 Model changes

* handle variance with Outline app by allowing unknown (commit [75a0b5b8](https://github.com/digital-land/planning-application-data-specification/commit/75a0b5b8c44ee14006a454a4fa7c1ee9a0f16f99))
* add declarative version of flood-risk-assessment module (commit [71fde7a9](https://github.com/digital-land/planning-application-data-specification/commit/71fde7a9ca6ad9a166624950822e20129bdd29ca))
* add declarative version of grounds-proposed-use module (commit [eb469e62](https://github.com/digital-land/planning-application-data-specification/commit/eb469e6235cdd386045f5c9d9c5f3190ec644d2f))
* add declarative version of the hedgerow-removal module (commit [10cb0be6](https://github.com/digital-land/planning-application-data-specification/commit/10cb0be641c5eda31a447598004d1fedf5e0d79a))
* add declarative version of ldc-interest module (commit [4687322e](https://github.com/digital-land/planning-application-data-specification/commit/4687322e60046843b69bc008a5cc10691abe1d2e))
* add declarative version of the non-res-floorspace module (commit [b17a03d4](https://github.com/digital-land/planning-application-data-specification/commit/b17a03d41ef448e4a456b771b4b34d91116b7a72))
* add declarative version of proposal-details-ldc module (commit [a74feecc](https://github.com/digital-land/planning-application-data-specification/commit/a74feecc4ad0f6b3125476b16b8c5569ae4b10ea))
* add declarative version of proposed-advert-details module (commit [9961d1af](https://github.com/digital-land/planning-application-data-specification/commit/9961d1afa7e6df240fd30d03da26411681f73a62))
* add declarative version of use-works-activity module (commit [73827192](https://github.com/digital-land/planning-application-data-specification/commit/738271922c2635609e68977846fe8c7a806a837c))
* add new has-new-disposal-arrangements field to foul-sewage module (commit [870d08e3](https://github.com/digital-land/planning-application-data-specification/commit/870d08e38a7f26c79ba05011b91b0ac0993df43e))
* consolidate related-proposals and related-applications into single related-applications approach (commit [1662e277](https://github.com/digital-land/planning-application-data-specification/commit/1662e277b05fa1f424122d95e99c639941939e62))
* add declarative version of hrs-operation module (commit [9d378af1](https://github.com/digital-land/planning-application-data-specification/commit/9d378af12ad7ea4bd26c998662c2e48a54b3a7f9))

### 🐛 Bug Fixes

* add the missing applies-if conditions to the original fields in waste-storage-collection module (commit [44fbcc12](https://github.com/digital-land/planning-application-data-specification/commit/44fbcc12b87465884b72e8fdf75a0bec8af3898f))


<a name="v0.1.19"></a>
## [v0.1.19](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.18...v0.1.19) (2025-07-16)

BNG and declarative modules

### 𝌭 Model changes

* add declarative version of grounds-for-application module (commit [d096caac](https://github.com/digital-land/planning-application-data-specification/commit/d096caac505c1abab8eb9fa9221ccaf4b13b18ad))
* add declarative version of grounds-existing-use module (commit [c0bf0d52](https://github.com/digital-land/planning-application-data-specification/commit/c0bf0d52b12137a1330f5d45006b74ee617b470c))
* rename in-building-construction-period field to was-constructed-btw-1948-2018 (commit [30394f20](https://github.com/digital-land/planning-application-data-specification/commit/30394f20cb3dc7a512c9c2cfbc61206bb048c65d))
* rename site-location-constraint field to is-site-in-restricted-area (commit [35b82026](https://github.com/digital-land/planning-application-data-specification/commit/35b82026bff4bb659d14d1d6a4ddfe9475ea1c57))
* rename dwelling-permitted-use field to was-use-granted-by-pdr (commit [92e28133](https://github.com/digital-land/planning-application-data-specification/commit/92e2813366e92c893eca478a1497d680b4e0e105))
* rename additional-storeys-added field to has-additional-storeys (commit [a51e97f4](https://github.com/digital-land/planning-application-data-specification/commit/a51e97f4cbd15229f8e42479b3a4212de94e2ac1))
* add declarative version of eligibility-current-building module (commit [ff5a68bd](https://github.com/digital-land/planning-application-data-specification/commit/ff5a68bd44c2b419b44e1a506fc48337f52a50a6))
* update declarative version of bng module with bng-condition-exemption-reasons substructure (commit [3fb24921](https://github.com/digital-land/planning-application-data-specification/commit/3fb2492175e7eee28fcfaee8184854132272966b))
* add sub-structure to BNG module to capture specific exemptions cited (commit [30136eba](https://github.com/digital-land/planning-application-data-specification/commit/30136ebac717452d3b6a1621739f6f705b0b5b8d))
* add bng-exemption-reason codelist (commit [90e727cf](https://github.com/digital-land/planning-application-data-specification/commit/90e727cf1aef37dde21957f944714438a843f3d8))
* rename existing-use-change field to has-existing-use-changed (commit [c57b63a4](https://github.com/digital-land/planning-application-data-specification/commit/c57b63a43e45380fb880887be84b6f93b84bf879))
* rename existing-use-interrupted field to has-existing-use-interrupted (commit [8c28e6db](https://github.com/digital-land/planning-application-data-specification/commit/8c28e6dbe3008dcd32d4c6a1dc66c6e9b02b0423))
* add declarative version of info-support-ldc module (commit [7a59d3a1](https://github.com/digital-land/planning-application-data-specification/commit/7a59d3a1a0eff9f7ea6a7747609bee2cf4cc688c))
* rename substituting-document field to is-substituting-document (commit [4e6cecd5](https://github.com/digital-land/planning-application-data-specification/commit/4e6cecd559e0ad0ffd6b1f2b3d6ef05b91d1b14c))
* add declarative version of nm-amendment-details module (commit [b0109e39](https://github.com/digital-land/planning-application-data-specification/commit/b0109e392f9ca332014e79dd0cc5e4b139f8d992))
* handle variance in ownership certificates module between lbc and other applications (commit [4552d7d4](https://github.com/digital-land/planning-application-data-specification/commit/4552d7d4715e1731d01420ea106e9b170f9e72c4))
* rename owners-and-tenants component to notified-person (commit [71c631f1](https://github.com/digital-land/planning-application-data-specification/commit/71c631f142d8bb6e15856acc27f3e16ec50bfd8d))
* add a combined parking-space-type enum (commit [07ea2508](https://github.com/digital-land/planning-application-data-specification/commit/07ea2508ec7d63af8d60e277c68080db11bdacda))
* add declarative version of desc-proposed-works module (commit [514ca9bc](https://github.com/digital-land/planning-application-data-specification/commit/514ca9bc496323fce3d25113f189781d3064b099))
* add declarative version of plans-drawings-supporting-materials module (commit [e3b20ff8](https://github.com/digital-land/planning-application-data-specification/commit/e3b20ff82bb9398138b4b44629f55a0c271cd9c2))


<a name="v0.1.18"></a>
## [v0.1.18](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.17...v0.1.18) (2025-07-15)

More declarative versions added and issues resolved

### 𝌭 Model changes

* add declarative version of desc-proposed-works module (commit [a925d326](https://github.com/digital-land/planning-application-data-specification/commit/a925d326e03b64bb05e03b8699b13fd2bdbf4035))
* add declarative version of plans-drawings-supporting-materials module (commit [3002aa57](https://github.com/digital-land/planning-application-data-specification/commit/3002aa5733482bca54aee1eae7037e33230d4b27))
* rename type field to waste-management-facility-type (commit [eae95604](https://github.com/digital-land/planning-application-data-specification/commit/eae956046ccbfd425c7e376367b928bbaeda6089))
* add specification processes-machinery-waste module for outline applications (commit [9b05a03f](https://github.com/digital-land/planning-application-data-specification/commit/9b05a03f9a701348424b55732a96444a5f4ba832))
* add declarative version of desc-work-impacts-risks module (commit [d8dac9a2](https://github.com/digital-land/planning-application-data-specification/commit/d8dac9a27a386ccd62d46e48959af8fbf26ae721))
* reanme within-site-constraints field to is-within-site-constraints (commit [51d27af4](https://github.com/digital-land/planning-application-data-specification/commit/51d27af4a4e571347ce29454b24c5343ab30332b))
* rename rear-extension-length field to is-extension-beyond-rear-wall (commit [d85023c7](https://github.com/digital-land/planning-application-data-specification/commit/d85023c7070dcbc6d9b723b916ef5dadf925ac2d))
* field in eligibility-proposal should be is-dwelling-detached (commit [02fd137b](https://github.com/digital-land/planning-application-data-specification/commit/02fd137b7fb5bb1ed8d48599e6b1f5729307f2d2))
* rename dwelling-detached field to is-dwelling-detached (commit [1ca6280e](https://github.com/digital-land/planning-application-data-specification/commit/1ca6280ef48eea63888fc9720565eef2ce6e0807))
* rename extension-height-over-4m field to is-extension-height-over-4m (commit [d6092ba3](https://github.com/digital-land/planning-application-data-specification/commit/d6092ba3e02b0aac9855dbc44053d525f04ef5b1))
* rename single-storey-extension to is-single-storey-extension (commit [d0ae1bda](https://github.com/digital-land/planning-application-data-specification/commit/d0ae1bda3ed7555f17c731db2ba5bbdcff4f7807))
* add declarative version of eligibility-extension module (commit [78fab5b3](https://github.com/digital-land/planning-application-data-specification/commit/78fab5b3d897c199eb29d57f0636378c32d570ea))
* designations and site-constraints fields should both use designations enum (commit [045697a3](https://github.com/digital-land/planning-application-data-specification/commit/045697a3c7973c9ecc57d2c863d90ded46470073))
* combine designation and sigte-constraint codelists (commit [23a42e57](https://github.com/digital-land/planning-application-data-specification/commit/23a42e57510bafec1cb485c6292fd9424e466eef))
* add declarative version of grounds-ldc module (commit [5f72b7ff](https://github.com/digital-land/planning-application-data-specification/commit/5f72b7ffa13e5f221f76dbd92dac5f5f93f4043e))
* grounds for ldc is now in 2 parts, pre and post 2025-04-25 (commit [41bcb706](https://github.com/digital-land/planning-application-data-specification/commit/41bcb70683ed986d0a67a2e02d0683051c159f45))
* add codelists needed for grounds for ldc module (commit [b79067d1](https://github.com/digital-land/planning-application-data-specification/commit/b79067d19801f691bdd6d98c0b8a2257f47cc7b3))

### 🐛 Bug Fixes

* update csv field to application-types (commit [d836c962](https://github.com/digital-land/planning-application-data-specification/commit/d836c962cafbb9908b49901beda4288613fccdde))


<a name="v0.1.17"></a>
## [v0.1.17](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.16...v0.1.17) (2025-07-09)

More declarative versions added

### 𝌭 Model changes

* add proposal-waste-management-outline field to handle variance between application types (commit [83718a95](https://github.com/digital-land/planning-application-data-specification/commit/83718a950843ee9d91a165aed925d1c2061f0879))
* is-annual-throughput-known and is-total-capacity-known fields only applicable in outline applications (commit [a08dfbdc](https://github.com/digital-land/planning-application-data-specification/commit/a08dfbdc0fb915ef8e750fbfb803ce2382ff0224))
* add declarative version of processes-machinery-waste module (commit [3fd5e222](https://github.com/digital-land/planning-application-data-specification/commit/3fd5e22251f66fb0c9f123f6f2e022e800247e12))
* add declarative version of site-ownership module (commit [72e48530](https://github.com/digital-land/planning-application-data-specification/commit/72e485307746da3f9951e79d26095e86054b1b8d))
* add declarative version of foul-sewage module (commit [69d1e6c0](https://github.com/digital-land/planning-application-data-specification/commit/69d1e6c0b7e16f188e8b6de8a51582f03e61aaef))
* add declarative version of hazardous-substance module (commit [e6ebf79f](https://github.com/digital-land/planning-application-data-specification/commit/e6ebf79f95b693712394b0ccf82d0c3499935eae))
* add yes-no-not-applicable codelist (commit [ee40ffde](https://github.com/digital-land/planning-application-data-specification/commit/ee40ffdeabfc5cb84204434d773343e550b2e149))
* add declarative version of desc-existing-use module (commit [b3f6e370](https://github.com/digital-land/planning-application-data-specification/commit/b3f6e370c8c70477ef9edf59168400c8bdd6c4e1))
* add declarative version of advert-location module (commit [da168073](https://github.com/digital-land/planning-application-data-specification/commit/da16807397cbda89a090059ec0a871ca8af7bca0))


<a name="v0.1.16"></a>
## [v0.1.16](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.15...v0.1.16) (2025-07-08)

More issues resolved and declarative versions added

### ⚒️ Tooling

* summarise progress towards declarative model (commit [79d5d45e](https://github.com/digital-land/planning-application-data-specification/commit/79d5d45ebb8991a2a586670f25f3d94da1afab5d))
* func to output list of modules with no current issues (commit [4925e9b6](https://github.com/digital-land/planning-application-data-specification/commit/4925e9b6aba2d79d5105af1710fffd0276ba8df9))

### 𝌭 Model changes

* unknown-proposed only applicable in outline-some applications (commit [eb59fea2](https://github.com/digital-land/planning-application-data-specification/commit/eb59fea2d826abe5d8f8520d6f62848bce7161b2))
* add declarative version of vehicle-parking module (commit [30694ecc](https://github.com/digital-land/planning-application-data-specification/commit/30694ecc1d632904f95bb734466d4297a7c98eb5))
* add declarative version of interest-in-land module (commit [5b56930b](https://github.com/digital-land/planning-application-data-specification/commit/5b56930b057d199d2cde3e708d1b0e98031a1f43))
* add declarative version of waste-storage-collection module (commit [0d471c41](https://github.com/digital-land/planning-application-data-specification/commit/0d471c416bda5b5008324628e68f5cd23d4eb4ba))
* add declarative version of storage-facilities module (commit [8af25866](https://github.com/digital-land/planning-application-data-specification/commit/8af258667fb3ecb59188f45c50c9643504e7b665))
* add declarative version of related-proposals module (commit [ea581a71](https://github.com/digital-land/planning-application-data-specification/commit/ea581a713e3dff9a7a8277d59ddfdd406c7f596f))
* add declarative version of lb-alter module (commit [3d22d9cb](https://github.com/digital-land/planning-application-data-specification/commit/3d22d9cb32a4350cbdd2c5db9e3cbffac48c2eb4))
* add declarative version of equip-mentod module (commit [064663a5](https://github.com/digital-land/planning-application-data-specification/commit/064663a5854782b28ecae33821cb91ff7f4b2e74))
* rename fte to total-fte for clarity (commit [f2ee6d19](https://github.com/digital-land/planning-application-data-specification/commit/f2ee6d193ee3f80ecda00ff6b6c063beab531859))
* add declarative version of employment module (commit [350d5644](https://github.com/digital-land/planning-application-data-specification/commit/350d5644228bc91e9eeaf975bf514dc7b11460fe))
* proposed-employees of employment module is sub-structure (commit [6a34ec05](https://github.com/digital-land/planning-application-data-specification/commit/6a34ec0507ca3b814472b98386867bb278342873))
* add declarative version of discharge-con module (commit [107826f9](https://github.com/digital-land/planning-application-data-specification/commit/107826f9bd0fec8c7db0e5e28a79db9abef1c699))
* add declarative version of advertisement-types module (commit [7cefbe3d](https://github.com/digital-land/planning-application-data-specification/commit/7cefbe3d84ca3ffb887fa1d387b27d08bb9174e5))
* add declarative version of designated-areas module (commit [a3a963f6](https://github.com/digital-land/planning-application-data-specification/commit/a3a963f6a8ab95444d80a8bbc78ae546a7841fac))
* add declarative version of con-remove-vary module (commit [75866084](https://github.com/digital-land/planning-application-data-specification/commit/758660841ed924b4fe11f229a8ea8ac51347b171))
* add declarative version of community-consultation module (commit [c1cec61c](https://github.com/digital-land/planning-application-data-specification/commit/c1cec61c3fca2add45b77c8d519ef1a3ac868e92))
* add declarative version of bio-geo-arch-con module (commit [6f5bdbcf](https://github.com/digital-land/planning-application-data-specification/commit/6f5bdbcf3a121ff0ef5487b014f8efa66e5be914))
* add declarative version of advert-period module (commit [46480473](https://github.com/digital-land/planning-application-data-specification/commit/46480473fbb5d5c757625e09f9eb46da6caad2f0))
* add declarative version of adj-premises module (commit [ea22e94b](https://github.com/digital-land/planning-application-data-specification/commit/ea22e94b7fa39fdd24a7d1fe76c73ac59892c139))
* rename field from discharging-part to is-discharging-part (commit [869f1e0e](https://github.com/digital-land/planning-application-data-specification/commit/869f1e0e09c1bf503591bdf7aa6b051ba7ed9b4d))
* add declarative version of part-discharge module (commit [fa0a6a54](https://github.com/digital-land/planning-application-data-specification/commit/fa0a6a5497f7ce075176d2f5b4ac7a13f6f0cf6a))
* add is-annual-throughput-known field to processed-machinery-waste module (commit [3e527ca5](https://github.com/digital-land/planning-application-data-specification/commit/3e527ca5d6dfc50c736bf9faa1631590aecf531a))
* add is-total-capacity-known field to processed-machinery-waste module (commit [b12d93a6](https://github.com/digital-land/planning-application-data-specification/commit/b12d93a6c5215acea5b06e189ec2604f4c0e785f))

### 🐛 Bug Fixes

* correct declarative model errors (commit [5f84de4b](https://github.com/digital-land/planning-application-data-specification/commit/5f84de4b3be9d74d86052ed01b42567046e22813))
* also include all modules with no issues (commit [63835f8e](https://github.com/digital-land/planning-application-data-specification/commit/63835f8e6eae5714510b7cd4f9e9f4d7c862b030))
* add missing address component (commit [f25fa2d8](https://github.com/digital-land/planning-application-data-specification/commit/f25fa2d8158e2f628bcc4a6fc8d52f4f46a615f1))
* fieldname typo" (commit [53152bdc](https://github.com/digital-land/planning-application-data-specification/commit/53152bdc1d200fd3d7c87ff02b1f57907072d1c2))

### 📚 Documentation

* add row counts to module tracking pages (commit [6b4608a2](https://github.com/digital-land/planning-application-data-specification/commit/6b4608a2672b1539998f7ab100cc323d8a4522f0))


<a name="v0.1.15"></a>
## [v0.1.15](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.14...v0.1.15) (2025-07-02)

More issues resolved and declarative versions added

### ⚒️ Tooling

* add integrity check for enum fields (commit [ad300760](https://github.com/digital-land/planning-application-data-specification/commit/ad30076085f1ca59191e0be0e8c899f06f14d024))

### 𝌭 Model changes

* add declarative version of site-area module (commit [725aec79](https://github.com/digital-land/planning-application-data-specification/commit/725aec792f48ce6073759d6678aacdb151c73b4e))
* rename field site-area in site-area module to site-area-in-hectares (commit [abd3c464](https://github.com/digital-land/planning-application-data-specification/commit/abd3c464f465fdd880716de7df8da21ddcde89e8))
* update development-phase, only looking for a single phase of development (commit [00e3de66](https://github.com/digital-land/planning-application-data-specification/commit/00e3de662de278e44198637b4e1243f4603e66b8))
* add declarative version of dev-type module (commit [39ef287c](https://github.com/digital-land/planning-application-data-specification/commit/39ef287c9592fc49145509e28112eae1de8aabe8))
* add declarative version of lb-grade module (commit [dd305af8](https://github.com/digital-land/planning-application-data-specification/commit/dd305af89962b96f2a03c8823cd356bbc088fafb))
* add declarative version of immunity-from-listing (commit [2b54832f](https://github.com/digital-land/planning-application-data-specification/commit/2b54832f0201760d318d6a58be93041d8ff7fe5d))
* add yes-no-unknown codelist (commit [9f3a3827](https://github.com/digital-land/planning-application-data-specification/commit/9f3a3827347b97f401b2dc3dcd4f9c70786e923f))

### 🐛 Bug Fixes

* add missing declarative version of lb-grade module (commit [53afd5b1](https://github.com/digital-land/planning-application-data-specification/commit/53afd5b167661d8c8b0409f74c34f7768ce1910c))
* all failing field checks (commit [bf9bc111](https://github.com/digital-land/planning-application-data-specification/commit/bf9bc11146d9184cd11be0640402932e9b76ecf9))

### 📚 Documentation

* decided to use enum instead of nullable boolean field (commit [ea12e963](https://github.com/digital-land/planning-application-data-specification/commit/ea12e9630a2738f5534a1fa7b32f3f1f5712ab67))


<a name="v0.1.14"></a>
## [v0.1.14](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.13...v0.1.14) (2025-07-01)

Define the consent-under-tpo application

### 𝌭 Model changes

* add declarative version of trees-additional module (commit [239d38be](https://github.com/digital-land/planning-application-data-specification/commit/239d38be4ba9897183316a1bc28786a1abb66ae7))
* add is-site-different field for clarity (commit [e20cc097](https://github.com/digital-land/planning-application-data-specification/commit/e20cc097c53e1191fbcc6b785408d0eeb2268ed3))
* add declarative version of trees-location module (commit [3857490e](https://github.com/digital-land/planning-application-data-specification/commit/3857490e07d0ac88e85a665672103b8fca28d901))
* add declarative version of trees-ownership module (commit [ce193541](https://github.com/digital-land/planning-application-data-specification/commit/ce193541c801347a3a8cac7f6992212eba1763a3))
* add declarative version of tree-work-details module (commit [92fefcb9](https://github.com/digital-land/planning-application-data-specification/commit/92fefcb96c08764ec4d7085b98754b59de2018a6))
* add declarative version of tpo module (commit [01334f6a](https://github.com/digital-land/planning-application-data-specification/commit/01334f6ab71ca43ff370d65538768221a4d798d2))
* rename field from demolition-part to is-partial-demolition (commit [6a120767](https://github.com/digital-land/planning-application-data-specification/commit/6a12076705915edf74a3322e374e9b2dd47623ed))
* rename field from demolition-building-in-curtilage to is-demolishing-building-in-curtilage (commit [ddad61a2](https://github.com/digital-land/planning-application-data-specification/commit/ddad61a27f48d2768f0479c44498cfc5f5af812e))
* rename field from demolition-total to is-total-demolition (commit [50578c0b](https://github.com/digital-land/planning-application-data-specification/commit/50578c0b6c94cec2a2570eb46f0f39911870e7ee))
* rename field from demolition to is-proposing-demolition (commit [2bfd30a6](https://github.com/digital-land/planning-application-data-specification/commit/2bfd30a6cb1b2c06760d0d3f4d8bbd01033aaab2))
* add declarative version of demolition module (commit [3508417d](https://github.com/digital-land/planning-application-data-specification/commit/3508417df02f124a234a6e6f0583708f38018b66))
* add declarative version of demolition-reason module (commit [de83ef8c](https://github.com/digital-land/planning-application-data-specification/commit/de83ef8c922c6fcd666deb95e24b58d21f0b04dc))
* field in demolition-reason should be called reason (commit [12368ec5](https://github.com/digital-land/planning-application-data-specification/commit/12368ec532023ab823fc1f407ad30a11888bc776))
* rename field, post-code to postcode (commit [9d7d7091](https://github.com/digital-land/planning-application-data-specification/commit/9d7d7091ebb42f4a7405d472c9d897034688b391))

### 👷‍♀️ Application changes

* remove trees-location module from consent-under-tpo applications (commit [3559c129](https://github.com/digital-land/planning-application-data-specification/commit/3559c129a5c1756c716ef020dde23b32460c94be))
* define the consent-under-tpo application (commit [06b37216](https://github.com/digital-land/planning-application-data-specification/commit/06b37216f5811431c2f463bf728381ab7f2c440b))


<a name="v0.1.13"></a>
## [v0.1.13](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.12...v0.1.13) (2025-06-26)

Resolving consistency of contact-details for PIP applications

### 𝌭 Model changes

* regenerate compiled spec for PIP applications (commit [ff7f01e3](https://github.com/digital-land/planning-application-data-specification/commit/ff7f01e3a425ee7b830278fe7a31ed7c7c6a1aa6))
* keep contact details separate from details modules in PiP applications, see issue [#294](https://github.com/digital-land/planning-application-data-specification/issues/294) (commit [e4166ecd](https://github.com/digital-land/planning-application-data-specification/commit/e4166ecd844b354a73ab6740915cc2f68eb3be98))
* add declarative version of proposal-details-inc-non-residential module (commit [663cb20c](https://github.com/digital-land/planning-application-data-specification/commit/663cb20c3f9cf8b9b273b363ebab648c132fbc90))
* add declarative version of site-info module (commit [779e29c5](https://github.com/digital-land/planning-application-data-specification/commit/779e29c5a64d0a64d48b915001e3241ca3a7f3c7))
* update supporting document part of site-info to be consistent with other instances (commit [d411aed4](https://github.com/digital-land/planning-application-data-specification/commit/d411aed4187bd5f64980099dc129ecd4079e6704))

### 👷‍♀️ Application changes

* add agent and applicant contact modules to pip application (commit [fd40df33](https://github.com/digital-land/planning-application-data-specification/commit/fd40df33f4073e2ea016c625dadc18c1b9dbc6aa))
* add declarative version of pip application (commit [d963d5c0](https://github.com/digital-land/planning-application-data-specification/commit/d963d5c0c2292db981140e0adec780258cd33d98))

### 📚 Documentation

* regenerate a single file with all modules (commit [ed29c128](https://github.com/digital-land/planning-application-data-specification/commit/ed29c12875ded51634fa3896b99ea38007715333))


<a name="v0.1.12"></a>
## [v0.1.12](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.11...v0.1.12) (2025-06-26)

resolving issues and improving field names

### 𝌭 Model changes

* rename field from householder-development to is-householder-development (commit [2dd5944f](https://github.com/digital-land/planning-application-data-specification/commit/2dd5944f2b7bae4332abd35877ddc388dd6e0a1e))
* rename field from development-started to has-development-started (commit [80a75ab8](https://github.com/digital-land/planning-application-data-specification/commit/80a75ab81977895dd1e327fbe4edaf437a9c4767))
* rename field from development-completed to has-development-completed (commit [3483c905](https://github.com/digital-land/planning-application-data-specification/commit/3483c9058de74816f396609413fb43e1ae68c551))
* rename field completion-date to development-completed-date (commit [f62cbccd](https://github.com/digital-land/planning-application-data-specification/commit/f62cbccdd75bc8aa549723a75325700248c88ee0))
* rename field start-date to development-start-date (commit [d994510b](https://github.com/digital-land/planning-application-data-specification/commit/d994510b2dbfc95baadb23ca4d431d15fdf3864f))
* create declarative version of desc-your-proposal module (commit [851ad0d9](https://github.com/digital-land/planning-application-data-specification/commit/851ad0d9b8f577212f64a025dcd59a55fac47060))
* use same fields as existing related-proposal component (commit [2587d0b7](https://github.com/digital-land/planning-application-data-specification/commit/2587d0b73ca65e6a9e7fe86321e10c041a17d671))
* rename field, disposal-required to is-disposal-required (commit [ec3bf484](https://github.com/digital-land/planning-application-data-specification/commit/ec3bf4846a173443414b3079948acadf1688947b))
* add declarative version of trade-effluent module (commit [4d6a320c](https://github.com/digital-land/planning-application-data-specification/commit/4d6a320cdad9c0213f32d0ed3d43172c943d3682))
* add declarative version of vol-agreement module (commit [78a29adc](https://github.com/digital-land/planning-application-data-specification/commit/78a29adc2f2a88697ac3b5709e885355525ced86))
* declarative version of supporting-info module (commit [147a0246](https://github.com/digital-land/planning-application-data-specification/commit/147a0246947b53370810315b333185ff4a636610))
* rename contact to contact-reference (commit [48959fca](https://github.com/digital-land/planning-application-data-specification/commit/48959fca0f2f498a8ea293a8e20c378081c44194))

### 🐛 Bug Fixes

* typo (commit [b1f5a1d1](https://github.com/digital-land/planning-application-data-specification/commit/b1f5a1d1bc31435d03cdd4c63a5bfa622f6c55c5))
* integrity checks picks up ill formed required-if conditions (commit [23445b54](https://github.com/digital-land/planning-application-data-specification/commit/23445b5479d2733a96ebeff17ca453377d9b3e5c))

### 📚 Documentation

* add note about trade-effluent from policy (commit [66b15df0](https://github.com/digital-land/planning-application-data-specification/commit/66b15df054cd9a90b38e27e8d667e95b66339afe))
* tweaks to the documentation for declarative model (commit [ca988b5d](https://github.com/digital-land/planning-application-data-specification/commit/ca988b5d8cf997a11d52e3ebc6837872df568e80))
* add documentation for the application interface (commit [94c2fef5](https://github.com/digital-land/planning-application-data-specification/commit/94c2fef57033071df7cbca3a0b544aa0c464fc84))


<a name="v0.1.11"></a>
## [v0.1.11](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.1...v0.1.11) (2025-06-20)

Responding to answers we got from DM policy

### 𝌭 Model changes

* add a user-role field to agent-details module (commit [8a37e1bf](https://github.com/digital-land/planning-application-data-specification/commit/8a37e1bf70d8a866b80134300a7ff16167f4f9a0))

### 👷‍♀️ Application changes

* add the conflict of interest module to prior approval applications [non-declarative] (commit [0c1964c6](https://github.com/digital-land/planning-application-data-specification/commit/0c1964c61b8b4d592b60885145fe6adb2fa00d1f))
* add the conflict of interest module to approval of conditions applications [non-declarative] (commit [ad51e235](https://github.com/digital-land/planning-application-data-specification/commit/ad51e23567dd6ea17140f30be076c9a7d8ba144e))
* add the conflict of interest module to s73 applications [non-declarative] (commit [91056cb5](https://github.com/digital-land/planning-application-data-specification/commit/91056cb5f41438ba943d71d6cb3c405b1acb56e6))


<a name="v0.1.1"></a>
## [v0.1.1](https://github.com/digital-land/planning-application-data-specification/compare/v0.1.0...v0.1.1) (2025-06-20)

First declarative model implementation for hh applications

### ⚒️ Tooling

* add integrity checks for application configuration (commit [d34f7fbb](https://github.com/digital-land/planning-application-data-specification/commit/d34f7fbbbaa50465ac00a6a8bc7d7d268438810a))
* add some basic checks for declarative model (commit [43dea70f](https://github.com/digital-land/planning-application-data-specification/commit/43dea70f786333796bb284852fc7b014aa1ca139))

### 𝌭 Model changes

* create declarative pieces for top level application fields (commit [053837d1](https://github.com/digital-land/planning-application-data-specification/commit/053837d1b5fc0f0e0f0a3d010b94ac60dbfbe9fa))
* add missing field definition for newspaper-notices (commit [a618bbe6](https://github.com/digital-land/planning-application-data-specification/commit/a618bbe6fb2716c81a730812844b7d21baa3ba8f))
* rename falling-trees-risk field to has-falling-trees-risk (commit [fd74efbd](https://github.com/digital-land/planning-application-data-specification/commit/fd74efbda6a340e4881ac4ebc0a6b670097ce065))

### 🐛 Bug Fixes

* add missing end-date attr to module definitions (commit [145f6b42](https://github.com/digital-land/planning-application-data-specification/commit/145f6b42a2ca01361ba04b24a5c5417f77cd4b78))
* correct typo to building-elements (commit [ba337f0e](https://github.com/digital-land/planning-application-data-specification/commit/ba337f0e814dd91516d5e8c892ad61c2b95a9685))

### 👷‍♀️ Application changes

* define the hh application (commit [b2cf2c76](https://github.com/digital-land/planning-application-data-specification/commit/b2cf2c76937f90eb6fe76f20cf0ae710cbccebae))


<a name="v0.1.0"></a>
## v0.1.0 (2025-06-18)

MHCLG worked with the planning community to develop a set of specifications for the submission of planning applications. A first draft of these specifications was completed by the end of March 2025. We they asked for feedback on them. This feedback window finished on 16 May 2025. Since then we have been turning the feedback into issues to be worked through.

