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

## Use the package in your code

In the consuming project, import `Specification` and load the local repository directory containing `specification/`, `data/` and `user-needs/`. For example, this retrieves the definition of the `description` field:

```python
from planning_application_specification import Specification

specification = Specification.load("/absolute/path/to/specification-checkout")
description = specification.field("description")
```

The package reads data from that directory when loaded. After editing specification data, load it again to use the updated values; reinstalling the package is not necessary.
