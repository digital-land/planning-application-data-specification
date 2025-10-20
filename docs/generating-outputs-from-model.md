# Generating outputs from the model

The declarative model is our machine-readable single source of truth for the planning application submission specification.  

It enables us to automatically generate a range of outputs for both humans and machines that bring the specification to life.

This demonstrates how a declarative approach makes the specifications easier to maintain and use.  

Others can build on the model to produce their own tools, documentation or outputs.

### Current outputs

🧩 **Information models**

Comprehensive, human-readable documents detailing the specification requirements for each application type.
They provide an accessible entry point into the data model and explain what fields are included and why.

* Status: Beta
* Code: /bin/generate_info_model.py
* Output folder: /generated/info_model

📊 **Spreadsheets**

Spreadsheet versions of each application type specification.
These make it easier to scan all fields for a given type and compare across modules.

* Status: Alpha
* Code: /bin/generate_spec_spreadsheets.py
* Output folder: /generated/spreadsheet

💻 **JSON Schemas**

A JSON Schema for each application type.
These define the expected structure of a planning application payload, allowing data producers and consumers to check validity and completeness.
They are also useful for testing whether example submissions match the model.

* Status: Alpha
* Code: /bin/generate_json_schema.py
* Output folder: /generated/json-schema

<hr />

### Contribute or build your own

Because everything is generated from the declarative model, anyone can build new outputs to meet their own needs — visualisations, validators, documentation, APIs, and more.

If you have an idea for an improvement or new output, build it and contribute it back.
The best way to improve the ecosystem is to try things out and share what works.

You can open a pull request to contribute code or enhancements, or open [an issue](https://github.com/digital-land/planning-application-data-specification/issues) if you want to explore an idea first.

### Concept diagram

Below is a diagram showing how the declarative model acts as the foundation for these outputs.

<img width="4178" height="2825" alt="3-items-built-on-specifications-repo-locations" src="https://github.com/user-attachments/assets/ae7040d7-f0a6-406b-a7f7-0df1b82a9d01" />

Each of these outputs is generated automatically from the same underlying definitions, keeping everything consistent and easier to maintain.
