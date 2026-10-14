# Contributing

See [making changes to the specification](documentation/making-changes-to-the-specification.md) for the design and review process. Keep each change in a focused commit so it can be reviewed on its own.

## Commits and changelog

Use a commit message in the form `type: description`. The types included in the changelog are `spec`, `app`, `tool`, `fix`, `docs`, `req`, `need` and `guidance`. See the [changelog configuration](.chglog/config.yml) for the current grouping.

To generate the changelog, fetch release tags and run `git-chglog -o CHANGELOG.md`. Review and commit the result separately.

## Releases

A release groups a series of reviewed commits. One versioned tag identifies the exact commit on `main` that contains those changes. Tags also give the changelog boundaries between groups of changes; a GitHub release makes the tagged version available to others.

Follow [build and release the specification package](documentation/releasing-specification-package.md) to choose the current development version, run checks, create the matching tag and publish a GitHub prerelease.
