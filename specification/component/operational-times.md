---
component: operational-times
name: Operational times
description: Opening times structure for operational hours by day
entry-date: 2025-07-16
end-date: ''
note: ''
fields:
  - field: schedule-days
    required: true
  - field: closed
    default: true
  - field: time-ranges
    required-if:
      - field: closed
        value: false
        description: required if field `closed` is false
---

For example

```
schedule-days: [monday, tuesday, wednesday, thursday, friday]
time-ranges: [
    { open-time: 0900, close-time: 1200 },
    { open-time: 1300, close-time: 1700 }
]
```
and
```
schedule-days: [sunday]
closed: closed
```
