# Expected Findings — weak-brd-savings.md

Golden reference for `/clarify:audit .clarify/eval/weak-brd-savings.md`. This case
exists to exercise the **product/operational lenses** (anti-patterns 27–36) that
the older eval cases predate.

## Band
- **Expected band:** "Not ready for handoff" — numeric total should land < 60.

## Must-flag anti-patterns (the 10 newer lenses)

| Anti-pattern id | Where | Dimension |
| --- | --- | --- |
| missing-system-actor | only "the customer" and "the system"; no rate admin / ops / accounting / job-as-actor table | completeness |
| missing-configuration-ownership | "A 4.8% annual interest rate is applied" — hard-coded, no config store/owner/validation | business-rule-quality |
| missing-effective-dating | the 4.8% rate and the minimum-balance change carry no effective date / version | business-rule-quality |
| missing-cohort-treatment | "raise the minimum opening balance next quarter" — silent on existing vs new deposits | completeness |
| missing-batch-job-spec | "An interest job runs to update balances" — no schedule, idempotency, outputs, consumers | risk-control |
| missing-authentication-step | money moves ("the money is moved") with no confirmation/OTP/PIN step or failure handling | risk-control |
| missing-error-message-mapping | "If opening fails, show an error" — no code/status/user-message/action mapping | handoff-readiness |
| missing-operation-state | only entity states (active/matured/closed); no initiated/pending-auth/processing/failed/timeout | edge-coverage |
| technical-jargon-in-business-requirement | "idempotent double-entry ledger postings to the GL and accrual tables … cohort … grandfathered … posting schema" in the BRD body | clarity |
| mixed-process-diagram-block | activity = open deposit placed beside sequence = early withdrawal as one Flows block | clarity |

## Also expected (older catalog — non-exhaustive)

| Anti-pattern id | Where | Dimension |
| --- | --- | --- |
| missing-outcome / missing-trigger | "The customer opens a savings deposit and the system confirms it." | clarity |
| missing-acceptance-criteria | entire doc | testability |
| missing-out-of-scope | no out-of-scope section | completeness |
| missing-edge-case / missing-exception-flow | no boundary/failure coverage beyond "show an error" | edge-coverage |
| missing-analytics-success-measurement | "customers like the feature" | nfr |

## Notes for the auditor
- The 10 newer ids in the first table are **must-flag**; missing any one is a
  regression in the corresponding engine/heuristic.
- The Flows section must be called out as process-mixing, not silently reorganized.
- Selecting `fintech-mini` may enrich findings but must not change the verdict
  (domain-agnostic core).
