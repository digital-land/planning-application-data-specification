---
attribution: crown-copyright
collection: planning-applications
consideration: planning-applications-decisions
dataset: site
description: 'Records of development sites linked to planning applications'
end-date: ''
entity-maximum: ''
entity-minimum: ''
entry-date: '2026-01-19'
fields:
- field: name
  description: Plain-language name for the site so it can be referenced in discussions and reports
- field: reference
- field: site-boundary
  notes: should this field be geometry?
key-field: ''
licence: ogl3
name: Site
notes:
phase: alpha
plural: Sites
prefix: ''
realm: dataset
replacement-dataset: ''
start-date: ''
themes:
- development
- administrative
typology: geography
version:

semantics:
  aligns_to:
    - iri: "https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/OWL#IfcSite"
      relation: "closeMatch"
      description: >
        A planning Site represents the land or areas of land that an application
        relates to. In planning practice this may comprise one or more separate
        plots and may be discontiguous. It aligns closely with the IFC IfcSite
        concept, but reflects the administrative and legal grouping used in
        planning decision-making rather than a strictly physical construction site.
---
