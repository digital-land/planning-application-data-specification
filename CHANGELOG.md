
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

