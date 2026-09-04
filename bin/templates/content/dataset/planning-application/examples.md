---
dataset: planning-application
---

## Examples

These examples show how to record information about a planning application.

### Basic planning application

This example shows the core information recorded for a full planning application. The application, its site and its planning authority each use their own reference.

{{ example("basic-planning-application") }}

### Combined planning application

This example shows one application seeking both full planning permission and listed building consent. Include both values in `application-types`; do not create a second planning application record solely because more than one consent is sought.

{{ example("combined-full-and-listed-building-consent") }}
