Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-employees{} | Counts of existing employees | full;outline;extraction-oil-gas | MUST | Required for all non-residential applications.
proposed-employees{} | Counts of proposed employees | full;outline;extraction-oil-gas | MUST | Required if the proposal affects employment capacity.
employment-impact | Summary of net employment change (gain/loss) | full;outline;extraction-oil-gas | MAY | Calculated based on existing and proposed values.

**Employees**
Field | Description | Notes
-- | -- | --
full-time | Number of full-time employees | Must be a positive integer or 0.
part-time | Number of part-time employees | Must be a positive integer or 0.
total-fte | Total full-time equivalent (FTE) | Calculated as full-time + (part-time ÷ 2).
