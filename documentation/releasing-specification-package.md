# Build and release the specification package

Use this guide to check a new version of the package and publish it on GitHub so other projects can install it.

If you want to use an existing version, read [Install the specification package](installing-specification-package.md).

## Before you start

You need:

- a local copy of this repository
- the project's development dependencies installed in an active Python virtual environment
- Git and the GitHub command-line tool (`gh`), signed in to an account that can publish releases

Run the commands from the repository's main directory.
Use the same terminal session throughout so the release commands can use the values you set earlier.

Make sure the specification and package changes you want to release have been reviewed and committed on `main`.

## 1. Choose a version number

Until the specification becomes mandatory, publish development versions. Mark each one as a prerelease on GitHub to show that it is still in development.

Use the date followed by a development number:

```text
YYYY.M.D.devN
```

For example:

- `2026.10.7.dev1` is the first development release on 7 October 2026
- `2026.10.7.dev2` is the second release on that date
- `2026.10.8.dev1` starts a new sequence on 8 October 2026

Do not add a `v` at the start or leading zeros to the month or day. 
Check the [existing releases](https://github.com/digital-land/planning-application-data-specification/releases) before choosing a number. 
Do not reuse or move a published release tag: other projects may depend on that version.

The release command uses your chosen value for both `pyproject.toml` and the Git tag. You do not need to edit the version by hand.

## 2. Prepare the release

First fetch existing tags so the command can check whether your version has already been used:

```sh
git fetch origin --tags
```

Then run the release command with your chosen version. This is an example; use a new version for each release:

```sh
make release VERSION=2026.10.8.dev1
```

The command:

1. Checks that you are on `main`, with no uncommitted or untracked files, and that the tag does not already exist.
2. Updates the package version in `pyproject.toml`.
3. Runs the specification checks, package tests and package build.
4. Commits the version change with a `tool:` message, unless that version was already committed.
5. Creates an annotated local tag and checks that it matches the version in the tagged commit.

It does not push or publish anything. Review the commit and tag before continuing.

Commit work that belongs in the release before running this command. Move unrelated untracked files out of the working directory or ignore them where appropriate. Files already ignored by Git, such as `dist/`, do not block the command.

If checks fail, the command restores its version edit and stops before committing or tagging. Resolve the failure and run it again. If a later Git command fails, inspect `git status` and `git tag` before retrying; a version commit may already exist.

## 3. Check and push the tag

Run the following in your terminal from the repository's main directory. The first command reads the version from `pyproject.toml` and saves it as a shell variable called `release_version` for the commands that follow:

```sh
release_version=$(python -c 'import tomli; print(tomli.load(open("pyproject.toml", "rb"))["project"]["version"])')
echo "$release_version"
make check-release VERSION="$release_version"
```

`check-release` checks the version stored in the tagged commit. It stops if the tag is missing or does not match. It also works for tags created manually.

Check that the displayed version is the one you intend to publish. Push `main` and that tag together:

```sh
git push --atomic origin main "refs/tags/$release_version"
```

The push must succeed before you publish. If you need to rebase, remember that the local tag still points to its original commit. Review that before continuing. Never move a published tag.

## 4. Publish the prerelease

In the same terminal session, run:

```sh
make check-release VERSION="$release_version"
gh release create "$release_version" \
  --repo digital-land/planning-application-data-specification \
  --verify-tag \
  --prerelease \
  --title "$release_version" \
  --generate-notes
```

This publishes a prerelease using the tag you pushed and generates release notes from the repository history. `--verify-tag` stops the command if that tag is not on GitHub; it does not create a new tag from another commit.

Open the release link returned by the command. Check the version, target commit and release notes.

You do not need to upload the wheel. For now, other projects install from the release tag using `pip`, which builds and installs the package for them. See [Find and install a release](installing-specification-package.md#find-and-install-a-release).

## Build the package without creating a release

To check the package files without making a commit or tag, run:

```sh
make package
```

This creates two files in the ignored `dist/` directory:

- a wheel (`.whl`), which Python tools can install
- a source archive (`.tar.gz`), which contains the files needed to build the package

Both include the Python code and specification data: definitions, guidance, examples, local codelists, usage rules, application types, approved combinations, planning requirements, needs and justifications. They exclude research material and the generated website. Building copies the data into the package without moving the original files.

If you need to build without network access and already have the build tools installed, run:

```sh
make package PACKAGE_BUILD_FLAGS=--no-isolation
```

The same `PACKAGE_BUILD_FLAGS=--no-isolation` option can be added to `make release` to use installed build tools during its build step.

The standalone viewer has its own rules for choosing releases. See the [viewer workflow guide](https://github.com/digital-land/planning-application-specification-viewer/blob/main/WORKFLOW.md).
