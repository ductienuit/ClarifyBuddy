# Configurations: <Domain>

Tunable parameters this domain exposes (rates, fees, limits, thresholds). Present
as candidates to confirm — never invent the values.

For each parameter give: where it is configured, who owns it, validation,
whether it is effective-dated/versioned, and how a change propagates.

| Parameter | Config store / screen | Owner role | Validation | Effective-dated? | Propagation |
| --- | --- | --- | --- | --- | --- |
| <…> | <…> | <…> | <range / format> | <yes/no> | <immediate / on effective date / next job run> |

## Change-over-time notes
- Effective dating / versioning: <how a change is dated and which version applies>
- Existing-vs-new (cohort) strategy: <grandfather vs apply-forward; backfill?>
