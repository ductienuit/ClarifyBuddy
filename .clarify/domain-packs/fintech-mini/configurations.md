# Configurations: Fintech

Tunable parameters — present as ASSUMPTION / OPEN QUESTION until confirmed. Never
hard-code these in a requirement; they belong in a configuration store owned by a
role, and changes are effective-dated and versioned.

| Parameter | Config store / screen | Owner role | Validation | Effective-dated? | Propagation |
| --- | --- | --- | --- | --- | --- |
| Savings interest rate (APY) | Rate Config | Rate Administrator | 0–10%, two decimals | yes | applies on effective date; picked up by the accrual job |
| Term-deposit rate by tenor | Rate Config | Rate Administrator | per-tenor table | yes | new deposits use rate in effect on open date |
| Monthly maintenance fee | Fee Config | Product/Finance | ≥ 0 | yes | next billing cycle |
| Minimum opening balance | Product Config | Product | ≥ 0 | yes | new accounts only (existing grandfathered) |
| Daily withdrawal limit | Limit Config | Risk/Ops | ≥ 0 | yes | immediate |
| Early-withdrawal penalty | Product Config | Product/Finance | % or fixed | yes | per deposit's open-date version |

## Change-over-time notes
- **Effective dating / versioning:** every rate/fee/limit row carries
  `effective_from` (+ optional `effective_to`) and a `version`; the value used for
  an event is the version in effect on that event's date. Prior versions retained
  for audit and recomputation.
- **Existing-vs-new (cohort) strategy:** by default a rate change applies to
  **new** deposits only; existing fixed-term deposits keep their open-date rate
  (grandfathered). Variable-rate savings may apply forward from the effective
  date — confirm per product (OPEN QUESTION). Always notify holders before a
  change that affects them.
