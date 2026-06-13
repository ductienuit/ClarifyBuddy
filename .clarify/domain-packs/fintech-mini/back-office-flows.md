# Back-Office Flows: Fintech

Non-customer-facing actors and the accounting/operational flows that consume the
outputs of customer activity and scheduled jobs. User-facing deposit specs
routinely omit these. (`missing-system-actor`)

## Back-office actors
- **Rate Administrator** — configures interest rates / fees with effective dates.
- **Accounting / GL** — posts interest expense and movements to the general ledger.
- **Operations** — investigates and resolves reconciliation discrepancies.
- **Compliance officer** — reviews KYC/AML flags.
- **Auditor** — reads immutable audit trails of config changes and money movements.

## Common back-office flows

### Rate change (config) flow
- **Actors:** Rate Administrator, (approver), Accounting.
- **Main path:** 1) propose new rate + effective date 2) validate range 3)
  approve 4) store as new effective-dated version 5) accrual job picks it up on
  the effective date.
- **Branches:** rejected on validation; cohort decision (grandfather existing vs
  apply-forward); notify affected holders.

### GL posting flow
- **Actors:** Accounting/GL, Interest-Posting Job.
- **Main path:** 1) read posted interest transactions 2) map to GL accounts
  (interest expense vs liability) 3) post double-entry 4) close period.
- **Branches:** unmapped account → exception queue; period already closed.

### Daily reconciliation flow
- **Actors:** Operations, Accounting, Reconciliation Job.
- **Main path:** 1) compare accrued vs posted interest and ledger vs provider
  2) flag discrepancies 3) investigate 4) resolve / compensate.
- **Branches:** unresolved discrepancy → escalation + audit entry.
