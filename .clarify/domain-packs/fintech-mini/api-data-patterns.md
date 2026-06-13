# API & Data Patterns: Fintech

## Entities & source of truth
- Ledger — the single source of truth for balances; balances are derived by
  summing entries, never stored as a mutable field of record.
- KYC status — owned by the compliance service.
- Rate Config — effective-dated, versioned rows
  (`rate_config(product, rate, effective_from, effective_to, version, owner)`);
  the rate for an event is the version in effect on the event date. Owned by the
  Rate Administrator; never hard-coded in code or a requirement.
- Accrual entries — daily earned-but-unposted interest, keyed by
  (account, accrual_date) for idempotency; source for posting and reconciliation.

## Common endpoints
- POST /transfers — initiate a transfer (Idempotency-Key REQUIRED).
- GET /accounts/{id}/balance — derived from the ledger.
- POST /reconciliations — run/inspect reconciliation.
- POST /deposits — open a savings/term deposit (captures open-date rate version).
- GET /deposits/{id} — includes accrued interest and maturity date.
- POST /rate-configs — create a new effective-dated rate version (Rate Admin).

## Integration patterns
- Every money mutation is idempotent (key-based dedup) and double-entry.
- Provider calls: bounded timeout + retry; on post-debit failure, run a
  compensating reversal.
- Settlement webhooks: signature-verified, idempotent, reconciled daily.
