# Installing the specification package in another project

Use these instructions to install the Python API into another project and read specification data from a local copy of this repository. You need Python 3.10 or later and a virtual environment for the consuming project.

## Install for development

In the consuming project's virtual environment, install an editable copy from the local specification repository:

```sh
python -m pip install -e /absolute/path/to/planning-application-data-specification
```

Changes to the package's Python source are available without reinstalling. Reinstall if packaging metadata or dependencies change.

For an installed copy that does not follow Python source edits automatically, omit `-e`:

```sh
python -m pip install /absolute/path/to/planning-application-data-specification
```

Repeat that command after package code changes when you want to update the installed copy. Pip installs the required dependencies automatically.

You can also install directly from the Git repository at a chosen commit:

```sh
python -m pip install "git+https://github.com/digital-land/planning-application-data-specification.git@COMMIT"
```

## Build release archives

Run `make package` in the pa-explorer environment. This creates a wheel and source archive in `dist/` without regenerating specification outputs. The version is `2026.10.7.dev1` for this development release. For an offline build with the tools already installed in pa-explorer, run `make package PACKAGE_BUILD_FLAGS=--no-isolation`.

Both archives contain the Python package and a snapshot of canonical specification definitions, guidance, examples, local codelist and usage CSVs, application types, planning requirements and user needs. These files sit under `planning_application_specification/resources/` in the archives. They are copied during packaging and are not generated source files. Research material, analysis data and generated site output are excluded. An unpacked source archive can build the same wheel without the original checkout.

`Specification.load()` still takes a local repository path as shown below. The packaged snapshot is present for a later resource loading change and does not change that API in this release.

## Use the package in your code

In the consuming project, import `Specification` and load the local repository directory containing `specification/`, `data/` and `user-needs/`. For example, this retrieves the definition of the `description` field:

```python
from planning_application_specification import Specification

specification = Specification.load("/absolute/path/to/specification-checkout")
description = specification.field("description")
```

The package reads data from that directory when loaded. After editing specification data, load it again to use the updated values; reinstalling the package is not necessary.
