# Install and use the specification package

Use the package to read the planning application specification from another Python project. It includes the Python code and the specification data, so you do not need a separate copy of this repository.

To create a new release, follow [Build and release the specification package](releasing-specification-package.md).

## Before you start

You need:

- Python 3.10 or later
- Git
- an active Python virtual environment for the project where you will use the package

Run the installation commands in your terminal with that environment active.

## 1. Choose a release

Open the [list of releases](https://github.com/digital-land/planning-application-data-specification/releases). Each release has a version, release notes and a Git tag that identifies its source code.

Versions ending in `.devN` are development versions. GitHub labels these as prereleases to show that they are still in development.

Choose the release you want to use and copy its tag. The commands below use [2026.10.7.dev1](https://github.com/digital-land/planning-application-data-specification/releases/tag/2026.10.7.dev1) as an example. Replace that value to install a different release.

## 2. Install the package

Run:

```sh
python -m pip install "git+https://github.com/digital-land/planning-application-data-specification.git@2026.10.7.dev1"
```

Pip downloads the source for that tag, builds an installable package and installs it with its dependencies. You do not need to download or build a wheel yourself.

Check the installed version:

```sh
python -m pip show planning-application-specification
```

Installing a release does not automatically install future releases. To update, choose a newer tag and run the installation command with that tag.

### Record the version in your project

Add this line to your project's requirements file, using your chosen tag:

```text
planning-application-specification @ git+https://github.com/digital-land/planning-application-data-specification.git@2026.10.7.dev1
```

This lets other people install the same version when they set up the project. You can use a full Git commit ID instead of a tag if you need to identify the exact commit.

## 3. Read the specification

In your Python code, load the data included with the installed package:

```python
from planning_application_specification import Specification

specification = Specification.load()
description = specification.field("description")
```

This example reads the definition of the `description` field. The package also includes guidance, local codelists, usage rules, approved application combinations, needs, justifications and examples.

## Test changes to local specification data

You can use an installed package to read specification files you are editing locally. Pass the path to the repository's main directory, not its `specification/` subdirectory:

```python
specification = Specification.load(
    "/absolute/path/to/planning-application-data-specification"
)
```

Load the specification again after editing the files. You do not need to reinstall the package to read those data changes.

Leaving out the path returns to the data included with the installed package. The package does not choose a local repository based on the directory where you run your code.

## Test changes to the package's Python code

If you are changing the package code itself, install your local copy in editable mode:

```sh
python -m pip install -e /absolute/path/to/planning-application-data-specification
```

The `-e` option makes Python use the code in that directory. Your code changes are available without reinstalling. Restart a running Python process to pick up changes to code it has already imported.

An editable installation does not include the packaged copy of the specification data. Pass the local repository path to `Specification.load()` as shown above.

Reinstall if you change the package dependencies or installation settings.

### Install a built copy of your local changes

To test a normal installation from your local repository, leave out `-e`:

```sh
python -m pip install /absolute/path/to/planning-application-data-specification
```

This builds and installs the code and data as they are at that point. Run the command again when you want to install further local changes. You can then use `Specification.load()` without a path.
