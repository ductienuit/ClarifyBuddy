# Expected Findings — weak-prd-checkout.md

This is the golden reference for `/clarify:audit .clarify/eval/weak-prd-checkout.md`.

## Band
- **Expected band:** "Not ready for handoff" (blocker-capped — no acceptance
  criteria anywhere, requirements not testable).
- Numeric total should land in the < 60 range regardless.

## Must-flag anti-patterns

| Anti-pattern id | Where | Dimension |
| --- | --- | --- |
| non-testable-requirement | "fast and easy to use" | testability |
| missing-acceptance-criteria | entire doc — no AC | testability |
| missing-outcome | "The user can check out." | clarity |
| missing-trigger | "Payment is processed." / "Inventory is updated." | clarity |
| ambiguous-actor | "Payment is processed." (passive, no actor) | clarity |
| non-testable-requirement | "manage their orders" (vague verb) | testability |
| missing-business-rule | "Apply discounts when appropriate." | business-rule-quality |
| missing-business-rule | "when appropriate" undefined | business-rule-quality |
| duplicate-conflicting-requirement | "within 30 days" vs "no refunds after 14 days" | business-rule-quality |
| scope-creep-disguised-as-requirement | "add a recommendation engine" | completeness |
| missing-out-of-scope | no out-of-scope section | completeness |
| missing-edge-case | no boundary/empty-cart cases | edge-coverage |
| missing-exception-flow | "Payment is processed" — no decline/failure path | edge-coverage |
| missing-idempotency | payment with no retry-safety | risk-control |
| missing-api-data-impact | "Inventory is updated" — no data/contract analysis | api-data-impact |
| missing-notification | "Send a confirmation" — no who/channel/when | completeness |
| missing-analytics-success-measurement | no success metric | nfr |

## Notes for the auditor
- At least one `blocker`-level deduction is not required by severity in the yaml
  (these are major/minor), so the blocker cap is driven by **total < 60** here;
  if the auditor classifies "no AC at all" as a blocker, the cap applies
  explicitly. Either way the band must be "Not ready for handoff".
- A correct run lists fixes for each finding and a top-3 actions list.
