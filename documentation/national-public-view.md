# National public view

The national public view is the open publication view of the wider planning
application data standard.

The planning application data specification defines the authoritative
information that a planning authority creates and maintains through the planning
permission process. The national public view is more cautious. It includes only
the datasets, records and fields that the standard explicitly says should be
published as open data.

This matters because the wider planning application data standard can include
controlled records, operational records and evidence that may be needed by a
planning authority but should not automatically become open data.

## Publication approach

The starting rule is:

> Nothing is included in the national public view unless the public-view schema
> explicitly includes it.

This means:

- datasets are included only when listed in `national-public-view.schema.md`
- fields are included only when listed under an included dataset
- records are included by default only for datasets without a record inclusion rule
- document records are included only when `public-register-status` is `publish`
- timeline records are included only when the event value is included for the
  `national-public-view` profile

The first version intentionally starts from a cautious publication boundary.
Fields can be added later when there is a clear publication need and the
publication risk is understood.

## National public view table

Rows without an exclusion rule are included in full for that dataset and field.
The record-inclusion-rule column is used only where records from an included dataset
are filtered before publication.

| dataset | field | description | record-inclusion-rule |
| --- | --- | --- | --- |
| planning-application |  |  |  |
|  | reference | Reference for the planning application. |  |
|  | description | Description of the proposed development. |  |
|  | application-types | One or more codelist values describing the application type. |  |
|  | site | Reference for the related site. |  |
|  | received-date | Date the planning authority received the application. |  |
|  | development-scale | Local planning authority classification of a full or outline application by development scale, where applicable. |  |
|  | planning-performance-agreement | Whether the application was subject to a Planning Performance Agreement. |  |
|  | withdrawn-date | Date the planning application was withdrawn. |  |
|  | linked-applications | References to earlier applications this application directly links to. |  |
|  | document-url | URL to the completed application form published by the planning authority, where available. |  |
|  | documentation-url | URL to the planning authority page where the completed application form or supporting application information can be accessed, where available. |  |
| site |  |  |  |
|  | reference | Reference for the site. |  |
|  | name | Plain-language name for the site. |  |
|  | address-text | Plain-language address for the site, where available. |  |
|  | postcode | Postcode for the site, where available. |  |
|  | description | Plain-language description of the site, where this helps identify the land or buildings. |  |
|  | site-boundary | Boundary geometry for the site. |  |
| decision-notice |  |  |  |
|  | reference | Reference for the decision notice. |  |
|  | planning-application | Reference for the related planning application. |  |
|  | decision | Decision outcome for the planning application. |  |
|  | decision-date | Date the decision notice was issued. |  |
|  | organisation | Organisation issuing the decision notice. |  |
|  | decision-maker | Who made the decision. |  |
|  | planning-officer-recommendation | Recommendation made by the planning officer for this application. |  |
|  | document-url | URL to the published decision notice. |  |
|  | documentation-url | URL of the page where the decision notice can be found. |  |
| planning-condition |  |  |  |
|  | reference | Reference for the planning condition. |  |
|  | name | Plain-language label for the condition. |  |
|  | description | Text of the condition that must be met. |  |
|  | reason | Explanation of why the condition was imposed. |  |
|  | organisation | Organisation responsible for this condition. |  |
| decision-condition |  |  |  |
|  | reference | Reference for the decision condition. |  |
|  | decision-notice | Reference for the decision notice this condition is attached to. |  |
|  | planning-condition | Reference for the linked planning condition record. |  |
|  | organisation | Organisation responsible for this condition within the decision. |  |
|  | requested-by | Identifier of the body requesting the condition. |  |
|  | discharged-by | Identifier of the body discharging the condition. |  |
| section-106 |  |  |  |
|  | reference | Reference for the section 106 agreement. |  |
|  | decision-notice | Reference for the decision notice tied to the section 106 agreement. |  |
|  | document-url | URL to the published section 106 agreement document. |  |
|  | documentation-url | URL of the page where the section 106 agreement can be found. |  |
| planning-application-document |  | Application document records. | Include only records where `public-register-status` is `publish`. |
|  | reference | Reference for the document record. |  |
|  | planning-application | Reference for the related planning application. |  |
|  | document-url | URL to the document file. |  |
|  | documentation-url | URL of the page where the document can be found. |  |
|  | name | Title or label used to identify the document. |  |
|  | replaces | Reference to an earlier document record replaced by this document. |  |
| planning-permission-timeline |  | Timeline records for included process events. | Include only records where `permission-process-event` is included for the `national-public-view` profile. |
|  | reference | Reference for the timeline entry. |  |
|  | planning-application | Reference for the related planning application. |  |
|  | permission-process-event | Type of event in the permission process. |  |
|  | event-date | Date the event occurred. |  |

## Notes on excluded fields

The `planning-application-data` dataset is excluded from this view. It points to
submitted and validated application data artefacts that may be needed for audit,
appeals, compliance or internal use. Those artefacts are not public by default.

The `public-register-status` field is not included in the output because it is a
control field. It decides whether a document record is extracted. Document
records with `withhold` or `not-assessed` are excluded entirely.

The `planning-permission-timeline.notes` field is excluded from the first view
because it is free text. It may contain personal, commercially sensitive,
private or security-sensitive information. It can be added later if there is a
clear publication need and suitable controls.
