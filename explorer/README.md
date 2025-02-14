
Show details about an application type. Details include name, reference, description, legislation and modules required.

```
python pacli.py app-type --ref {app_ref} 
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
