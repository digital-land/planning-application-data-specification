
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
With end-date count shows how many modules we are decided are not required.
With reference is how many modules we've published a draft info model for. We are adding a reference once done.

Command to help make application - module records

```
python pacli.py module --ref {module-ref} --make
```
_We will eventually remove this command_
