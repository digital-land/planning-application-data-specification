# The difference between the planning application data and submission specifications

## The core distinction: authoritative records and structured collection

The planning application data specification defines the authoritative
information that a planning authority creates and maintains through the planning
permission process.

The submission specification provides a structured route for collecting the
information needed when an application is made. It defines the forms, fields and
rules that help applicants and systems provide consistent data.

The specifications are connected, but they have different roles. The planning
application data specification defines what should be recorded and maintained.
The submission specification defines how information is collected at
submission.

## Planning application data specification: authoritative records

The planning application data specification defines linked records about a
planning application and its progress. These can include the application,
site, documents, process events, decision notices, conditions and section 106
agreements.

The record starts when the planning authority receives an application. It is
not limited to the decision or to information that is published.

It is a relational model because the records can exist independently, change
over time and refer to one another. It does not define the form structure or
conditional questions used to collect information from an applicant.

Its purpose is to make planning application information authoritative,
traceable and reusable across registers, reporting, publication and connected
systems.

## Submission specification: structured collection

The submission specification defines the information an applicant must provide
to make a valid planning application. It is based on the purpose of planning
application forms and expresses their questions, groups of information and
requirements as structured data.

It uses modules, fields and conditional rules to describe what needs to be
asked for a particular application type. For example, if an applicant says
that residential units will change, a residential-unit summary may be required.

It is an object model because a submission is a single structured payload. Its
purpose is to help applicants, planning authorities and software suppliers
collect good data consistently when an application is made.

## Summary comparison

| Feature | Planning application data specification | Submission specification |
| --- | --- | --- |
| Primary role | Defines the authoritative information a planning authority records and maintains | Defines the information and structure used to collect a valid application |
| Scope in the process | From receipt through the planning permission process | When an application is made |
| Structure | Linked, relational records | Structured application payload |
| Logic | Defines the records and their relationships | Defines form structure, requirements and conditional collection rules |
| Main use | Maintaining, reusing, publishing and analysing planning application information | Collecting consistent information and validating a submission |
| Examples | Application record, site, document, event, decision notice, condition | Application type, module, field and conditional requirement |

## Analogy

The planning application data specification is like the authoritative case
record for a planning application. The submission specification is like the
structured application form and the rules that help complete it correctly.
