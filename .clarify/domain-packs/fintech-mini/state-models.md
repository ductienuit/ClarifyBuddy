# State Models: Fintech

## Transaction
- **States:** pending → posted → settled; plus held, reversed, failed.
- **Transitions:** pending → held (AML/limit hold); held → posted (cleared);
  posted → settled (provider confirms); any non-terminal → reversed (compensate).
- **Terminal:** settled, reversed, failed.
- **Illegal:** settled → pending; double-post of the same idempotency key.

## KYC record
- **States:** unverified → pending_review → verified / rejected.
- Transfers above threshold require `verified`.

## Deposit account
- **States:** pending → active → matured → closed; plus on_hold.
- **Transitions:** pending → active (funded); active → matured (term reaches
  maturity); matured → active (renewed) or → closed (paid out); active → closed
  (early withdrawal, penalty applies).
- **Terminal:** closed.
- **Illegal:** accrue interest on a closed deposit; withdraw from pending.

## Interest-Accrual Job run
- **States:** scheduled → running → completed / failed → retried.
- **Idempotent** per (account, accrual-date); a rerun must not double-accrue.
- **Illegal:** overlapping runs for the same date; posting before accrual completes.
