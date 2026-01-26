# How dates and timestamps are used in this specification

This specification uses two closely related standards to represent time-related values:

- ISO 8601 for dates
- RFC 3339 for timestamps

They serve different purposes and should be used intentionally.

---

## Dates (ISO 8601)

Dates are used where the value represents a calendar concept rather than a precise moment in time. These are typically business or legal concepts such as:

- the date a decision was made
- the date an application was submitted
- a reporting period
- a validity date

ISO 8601 allows different levels of precision. The specification supports:

| Precision | Meaning | Example |
|--------|--------|--------|
| year | The whole year | `2026` |
| month | The whole month | `2026-01` |
| day | A specific day | `2026-01-18` |

Dates do not include a time or timezone. They describe *which day, month, or year* something relates to, not *exactly when* it happened.

---

## Timestamps (RFC 3339)

Timestamps are used where an exact moment in time must be recorded in a way that is globally unambiguous. These are typically technical or operational events such as:

- when a record was created
- when a record was last updated
- when a validation process ran
- when data was ingested by a system

All timestamps must use RFC 3339 format, which is a strict profile of ISO 8601:

```
YYYY-MM-DDTHH:MM:SS[.fraction](Z or ±HH:MM)
```

Examples:

```
2026-01-18T14:32:00Z
2026-01-18T14:32:00+00:00
2026-01-18T17:32:00+03:00
```

A timestamp always includes:

- a full date
- a time
- a timezone

This makes it suitable for precise ordering, comparison, and auditing.

---

## How precision is expressed

Each date or timestamp field declares its required precision using the `date_precision` attribute.

Examples:

```yaml
decision_date:
  datatype: datetime
  date_precision: day
```

```yaml
reporting_period:
  datatype: datetime
  date_precision: month
```

```yaml
created_at:
  datatype: datetime
  date_precision: timestamp
```

The allowed values are:

| date_precision | Meaning |
|--------------|-------|
| `year` | ISO 8601 date with year precision |
| `month` | ISO 8601 date with month precision |
| `day` | ISO 8601 date with day precision |
| `timestamp` | RFC 3339 timestamp |

The `date_precision` attribute describes the *semantic precision* of the field, not the string syntax. Validation rules define the exact format that must be used.

---

## Summary

- Use ISO 8601 dates for calendar concepts
- Use RFC 3339 timestamps for exact moments in time
- Use `date_precision` to declare how precise a field is
- Do not pad or invent missing date parts
- Do not use timestamps where a simple date is sufficient

This keeps the specification semantically clear, machine-safe, and consistent across all datasets.

