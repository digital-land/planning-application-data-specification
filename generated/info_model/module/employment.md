# Employment

How the proposed development will impact existing and proposed employee numbers

**Employment module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| existing-employees | Existing employees{} | Counts of existing employees |  | MUST |  |
| proposed-employees | Proposed employees{} | Counts of proposed employees |  | MUST |  |
| employment-impact | Employment impact | Summary of net employment change (gain/loss) |  | MAY |  |


**Employees component**

field | name | description | required | notes
-- | -- | -- | -- | --
full-time | Full-time | Number of full-time employees | MUST | 
part-time | Part-time | Number of part-time employees | MUST | 
total-fte | Total FTE | Total full-time equivalent (FTE) | MUST | 

**Validation rules**

- Existing-employees is required for all non-residential applications
- Proposed-employees is required if the proposal affects employment capacity
- Employment-impact is calculated based on existing and proposed values
- Full-time and part-time employee counts must be positive integers or 0
- FTE is calculated as full-time + (part-time ÷ 2)