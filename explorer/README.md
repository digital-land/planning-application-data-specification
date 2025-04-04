
## Application types

Show details about an application type. Details include name, reference, description, legislation and modules (currently worked on) required.

```
python pacli.py app-type --ref {app_ref} 
```

Generate list of modules for combined applications
```
python pacli.py app-type --combine "lbc;hh" 
```

Show list of application types if you have a list of refs
```
python pacli.py app-type --refs "advertising;demolition-con-area;extraction-oil-gas;full;hh;lbc;outline"
```

List the sub types by application types
```
python pacli.py app-type --show-sub-types
```

List complete set of modules for a app-type and sub-type
```
python pacli.py app-type --ref outline --sub-type-ref outline-some
```

Generate a complete 'spec' file based on app and sub type provided
```
python pacli.py app-type --ref prior-approval --sub-type-ref pa-storey --generate-application
```

Generate the specification index file with:
```
python pacli.py app-type --generate-specification-index
```

Generate all app type specifications files with
```
python pacli.py app-type --all --generate-application
```


## Form

Print details, including list of sections, about an application form
```
python pacli.py form --form-ref {form.reference}
```

Show which forms cover a given application type
```
python pacli.py form --app-type lbc
```

List all the forms a named module appears in
```
python pacli.py form --module-name "Planning application requirements - checklist"  
```


## Module

Show summary of progress with
```
python pacli.py module --show summary
```
With end-date count shows how many modules we have decided are not required.
With reference is how many modules we've published a draft info model for. We are adding a reference once done.

Show the application types that have a particular module
```
python pacli.py module --ref {module_ref} --show app-types
```

Command to help make application - module records

```
python pacli.py module --ref {module-ref} --make
```
_We will eventually remove this command_


## Check

Summarise modules with
```
python pacli.py check --module
```

Check no issues with codelists
```
python pacli.py check --codelist
```

## CSV

There are numerous csv files in the repo you may want to interact with

Print out the csv in a markdown table
```
python pacli.py csv --filename {path to csv} --markdown --fields {list of fields separated by ,}
```
**--filename** is a path to the csv file from the explorer directory
**--markdown** is needed to print the table out to the terminal
**--fields** is an option list of the fields, without it all fields will be printed out

