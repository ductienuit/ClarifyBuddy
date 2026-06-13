# Scheduled Operations: Fintech

Batch / scheduled jobs. Present as candidates to confirm. Each job needs a
schedule, idempotency & resume strategy, defined outputs, and named downstream
consumers (accounting/reconciliation routinely depend on these).

| Job | Schedule / Trigger | Idempotency / Resume | Inputs | Outputs | Downstream consumers |
| --- | --- | --- | --- | --- | --- |
| Interest-Accrual Job | daily 02:00 UTC | idempotent per (account, accrual-date); resumes from last processed account | active deposit accounts, rate config in effect | daily accrual ledger entries (accrued interest) | GL posting, daily reconciliation, customer statement |
| Interest-Posting / Capitalization | monthly / at maturity | idempotent per (account, period) | accumulated accruals | posted interest transaction (double-entry) | ledger, statement, tax reporting |
| Maturity Processing | daily | idempotent per (deposit, maturity-date) | matured term deposits | renewal or payout transaction | ledger, notification, GL |
| Daily Reconciliation | daily after posting | idempotent per (date) | ledger entries + provider statement | discrepancy report | Operations, Accounting |

## Job state model
- **States:** scheduled → running → completed / failed → retried.
- **Idempotency:** keyed by (account/deposit, date/period) so a rerun never
  double-accrues or double-posts.
- **Resume:** on failure mid-run, resume from the last successfully processed key;
  do not restart the whole batch blindly.
- **Risky / illegal:** overlapping accrual runs for the same date; posting before
  accrual completes; reconciliation reading a half-finished posting run.

## Why this matters for accounting
Accrual and posting outputs are the inputs to GL and reconciliation. If the job
is underspecified (no idempotency, unclear outputs, no consumer list), accounting
cannot reconcile accrued vs posted interest. (`missing-batch-job-spec`)
