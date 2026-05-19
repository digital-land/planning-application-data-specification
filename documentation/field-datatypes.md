# Field datatypes

This page is generated from the field definitions in this specification and the upstream planning.data.gov.uk datatype definitions.

Field datatypes should reuse the planning.data.gov.uk datatypes where possible. Datatypes that only exist for this specification's JSON payload structures are marked as local, and datatype values that do not match either source are marked for checking.

Regenerate this page with `make field-datatypes`.

## Datatypes used in this specification

| Datatype | Source | Field count | Example field | Notes |
| --- | --- | --- | --- | --- |
| boolean | Unknown / check | 118 | [Pre-application advice sought](../specification/field/advice-sought.md) | JSON boolean used in local payload structures. |
| Boolean | Unknown / check | 1 | [Unknown proposed](../specification/field/unknown-proposed.md) | Not found in upstream datatypes or local datatype conventions. |
| datetime | Upstream | 25 | [Advert end date](../specification/field/advert-end-date.md) | A combination of a date and a time in the format `YYYY-MM-DDThh:mm:ss[.pppp]Z` as described in chapter 5.4 of [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). The value can be truncated to just the most significant digits, for example "2014-05". Time values, where present, must be in UTC. |
| enum | Local to this specification | 71 | [Advertisement type](../specification/field/advertisement-type.md) | Controlled value from a local codelist. |
| integer | Upstream | 1 | [Condition numbers](../specification/field/condition-numbers.md) | An integer value compatible with XML Schema xs:integer type. |
| number | Local to this specification | 68 | [Advertisement count](../specification/field/advertisement-count.md) | JSON number used in local payload structures. |
| object | Local to this specification | 64 | [Addresses](../specification/field/addresses.md) | JSON object used for fields that reference a component. |
| string | Upstream | 125 | [Additional information](../specification/field/additional-information.md) | A string of [Unicode 6.2.x](http://www.unicode.org/versions/Unicode6.2.0/) characters encoded as [UTF-8](http://en.wikipedia.org/wiki/UTF-8). |
| url | Upstream | 2 | [Document URL](../specification/field/document-url.md) | A [URL](http://en.wikipedia.org/wiki/Uniform_resource_locator) reference to another resource on the Web. |
| wkt | Upstream | 1 | [Site boundary](../specification/field/site-boundary.md) | A geometry encoded in the [OGC Well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format as defined by [ISO/IEC 13249-3:2016](https://www.iso.org/standard/60343.html) Coordinate values should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. |

## Upstream datatypes available to reuse

| Datatype | Description | Example | Source |
| --- | --- | --- | --- |
| blob | Binary data in an internal, possibly proprietary format | SGVsbG8= | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/blob.md) |
| curie | A [CURIE](http://en.wikipedia.org/wiki/CURIE) defines a generic abbreviated syntax for expressing Uniform Resource Identifiers (URIs). eg. `local-authority:DAC`. | prefix:reference | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/curie.md) |
| datetime | A combination of a date and a time in the format `YYYY-MM-DDThh:mm:ss[.pppp]Z` as described in chapter 5.4 of [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). The value can be truncated to just the most significant digits, for example "2014-05". Time values, where present, must be in UTC. | 2026-05-19 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/datetime.md) |
| decimal | A decimal value compatible with XML Schema xs:decimal type. | 51.5074 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/decimal.md) |
| flag | A value which is either `yes`, `no`, or blank. | yes | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/flag.md) |
| hash | A hash value serialised as a hexadecimal string. The default hash function is [SHA2-256](https://en.wikipedia.org/wiki/SHA-2). An alternative hash function may be supplied using a CURIE prefix, or the experimental [multihash](https://multiformats.io/multihash/) code. | sha-256:abc123 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/hash.md) |
| integer | An integer value compatible with XML Schema xs:integer type. | 12 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/integer.md) |
| json | A blob of data encoded as a canonicalised JSON string compatible with [RFC 8259](https://tools.ietf.org/html/rfc8259). | {"reference":"abc"} | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/json.md) |
| latitude | A latitude value which should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. | 51.5074 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/latitude.md) |
| longitude | A longitude value which should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. | -0.1278 | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/longitude.md) |
| multipolygon | A geometry encoded in the [OGC Well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format as defined by [ISO/IEC 13249-3:2016](https://www.iso.org/standard/60343.html) Coordinate values should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. |  | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/multipolygon.md) |
| pattern | A regular expression pattern compatible with the [IEEE POSIX](https://en.wikipedia.org/wiki/POSIX) Basic Regular Syntax (BRE). |  | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/pattern.md) |
| point | A geometry encoded in the [OGC Well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format as defined by [ISO/IEC 13249-3:2016](https://www.iso.org/standard/60343.html) Coordinate values should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. |  | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/point.md) |
| reference | The reference part of a [CURIE](http://en.wikipedia.org/wiki/CURIE) used to abbreviate Uniform Resource Identifiers (URIs). |  | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/reference.md) |
| string | A string of [Unicode 6.2.x](http://www.unicode.org/versions/Unicode6.2.0/) characters encoded as [UTF-8](http://en.wikipedia.org/wiki/UTF-8). | Example text | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/string.md) |
| text | A string of text which may contain [Markdown](http://en.wikipedia.org/wiki/Markdown) formatting instructions. | Longer free text | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/text.md) |
| url | A [URL](http://en.wikipedia.org/wiki/Uniform_resource_locator) reference to another resource on the Web. | https://www.example.com/document.pdf | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/url.md) |
| wkt | A geometry encoded in the [OGC Well-known text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format as defined by [ISO/IEC 13249-3:2016](https://www.iso.org/standard/60343.html) Coordinate values should be 6 or fewer decimal places, using the WGS84 or ETRS89 coordinate system. | POINT(-0.1278 51.5074) | [planning.data.gov.uk specification](https://github.com/digital-land/specification/blob/main/content/datatype/wkt.md) |
