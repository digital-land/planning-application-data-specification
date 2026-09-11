# Components

Components are reusable substructures or data shapes made up of multiple [fields](fields.md) (e.g. a person, an address).

They group fields into logical, structured units that can be reused across contexts.

Having a consistent structure for how components are described and reused across modules enables shared definitions, clarity, and better validation

A field that uses a component can have an `applies-if` condition on its module field entry. When that field is out of scope, the whole component response must be absent. Missing fields inside it do not produce errors, but supplying the out-of-scope response is invalid. When it is in scope, the component’s normal validation rules apply, including its required fields.

For conditional rules that affect whether component fields apply or become required, see [co-constraints](co-constraints.md).
