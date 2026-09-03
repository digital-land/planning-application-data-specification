---
reference: decision-condition-discharged-by
dataset: decision-condition
field: discharged-by
---

### How to use it

Use this field to link a condition to the later decision notice that discharged it.

The value must be the reference of the corresponding record in the `decision-notice` dataset. It is not the name or identifier of the authority that discharged the condition.

In this example, `dc-23-01234-FUL-4` records condition 4 on the original permission. It links to the reusable planning condition `material-approval-con`. The later decision notice `23-04567-DET-dn` records the decision that discharged that condition.

```json
{
  "reference": "dc-23-01234-FUL-4",
  "planning-condition": "material-approval-con",
  "discharged-by": "23-04567-DET-dn"
}
```

The `decision-notice` dataset must contain a record with the reference `23-04567-DET-dn`. A user or service can follow that reference to find the discharge decision and its date.
