# spec CLI

## What the CLI is for

`spec.py` is the human-facing project CLI for inspecting and understanding the planning application specification repository.

It provides:

- human-readable inspection of the canonical specification model
- lightweight project reporting views derived from the repository
- clearly labelled access to selected non-canonical analysis datasets

It does not replace the Python package interface.
Reusable Python queries belong in `planning_application_specification/`.
`spec.py` is the project CLI built on top of those queries.

## Why this CLI is needed

The repository contains the canonical source material for the specification, but the source files are not the easiest way to answer everyday questions about it.

Contributors and users need a simple way to:

- inspect the current specification model
- understand how applications, modules, fields, components and codelists relate to each other
- access a small number of repeatable project reports
- explore clearly labelled analysis data that sits alongside the canonical specification

`spec.py` provides that human-facing interface.

It exists to make the specification easier to explore, understand and use from the command line, while the reusable Python package remains the main interface for building software on top of the specification.

This supports production readiness by making the repository easier to use in practice for:

- contributors maintaining the specification
- people reviewing how the specification fits together
- implementers building tools, forms, services and validations from the specification

## Design principles

- optimise for human exploration rather than exposing every internal script
- group commands by user intent
- prefer package-backed queries for canonical specification inspection
- keep workflow-specific reporting and output assembly outside the package
- label non-canonical analysis data clearly
- keep the top-level CLI small and memorable
- avoid compatibility aliases as part of the long-term interface
- keep `spec.py` focused on command structure and dispatch
- move reusable presentation helpers into `bin/markdown_utils.py` where that keeps the CLI readable
- do not move specification-query logic into formatting modules

## Command taxonomy

The CLI should be organised around three top-level purposes.

### `inspect`

Use `inspect` for questions about the canonical specification model.

This includes:

- looking up a specific application, module, component, field or codelist
- understanding how canonical elements relate to each other
- finding where a field, module or component is used

`inspect` should be mostly backed by `planning_application_specification/`.

### `report`

Use `report` for repository-derived summaries and progress views.

This includes:

- overall specification summaries
- completeness reporting
- decision-stage reporting

`report` is project reporting logic. It may use package queries, but the reporting layer belongs in the CLI and `bin/`.

### `analysis`

Use `analysis` for non-canonical or derived datasets that are useful to explore but are not the core specification model.

This includes:

- analysed 2025 forms data
- any future sidecar analysis datasets that need CLI access

Analysis commands must always make their status clear and should not be presented as canonical specification truth.

## Intended command tree

The long-term command tree should be:

```text
spec.py
  inspect
    application <ref>
    module <ref>
    component <ref>
    field <ref>
    codelist <ref>
    uses
      module <module_ref>
      field <field_ref>
      component <component_ref>

  report
    summary
    completeness
      summary
      scope
    decision
      summary

  analysis
    forms
      urls <application_type>
      list <application_type>
      show <form_ref>
      for-module <module_ref>
      modules <form_ref>
```

## Boundaries

### What belongs in the package

Reusable domain queries over the specification, for example:

- application lookup
- field lookup
- module lookup
- field usage lookup
- applications using a module
- resolved container traversal

### What belongs in the CLI and `bin/`

Workflow-specific behaviour, for example:

- command structure
- output formatting
- report assembly
- markdown rendering
- analysis-data presentation
- file-writing and export tasks

## Current live dependencies to review during migration

At the time of writing, the current `spec.py` interface is used by:

- `Makefile` target `declarative-progress`
- `.github/workflows/daily-issue-tracking.yml` via `make declarative-progress`
- `.github/workflows/generate-spec-outputs.yml` via `make declarative-progress`
- `tests/test_spec_cli.py`
- `README.md`

These need to be updated as part of any CLI restructure.
