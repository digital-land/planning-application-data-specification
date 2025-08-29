# Advert period

Module for capturing the time period that consent to advertisement is sought


**Advert period module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| advert-start-date | Advert start date | The start of the time period that consent to advertisement is sought |  | MUST |  |
| advert-end-date | Advert end date | The end of the time period that consent to advertisement is sought |  | MUST |  |

**Validation rules**

- advert-start-date must be a valid date in YYYY-MM-DD format
- advert-end-date must be a valid date in YYYY-MM-DD format
- advert-end-date must be after advert-start-date