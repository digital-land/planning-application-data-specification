

These dataset definitions follow the same approach/schema as datasets on planning.data.gov.uk, for compatibility

which means they inherit a lot of pre defined things from there

for example, each dataset has a typology attribute, this describes at a high level what the type of thing the dataset is for, this helps ensure datasets describe a discreet thing and is less likley to conflate multiple things htat would be better separated out into linked datasets.

Common typologies are document, geography, timeline and organisation. The complete list can be found in the [digital-land/specification repository](https://github.com/digital-land/specification/tree/main/content/typology)


It also includes other attributes that are carried over from the planning.data ecosystem. Such as `entity-maximum` and `entity-minimum`. These are used to give a range on entities number (ids) that will be assigned when that platform ingests the data. Keeping them in the definition here makes it easier when we port the dataset definitions over.

