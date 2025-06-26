
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

