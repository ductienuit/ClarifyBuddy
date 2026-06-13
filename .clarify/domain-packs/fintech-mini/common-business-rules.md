# Common Business Rules: Fintech

Candidate rules — present as ASSUMPTION / OPEN QUESTION until confirmed.

- The ledger is the single source of truth for balances; never compute balance
  from a cached field.
- Every money movement is double-entry (debits = credits).
- All mutating money operations require an idempotency key.
- Transfers blocked if they breach per-transaction or daily limits.
- KYC must be complete before a customer can transfer above a threshold.
- Negative balances are disallowed (or allowed with overdraft?) — confirm.
- Currency rounding/precision rules — confirm (e.g. minor units, banker's
  rounding).
- Interest rates/fees live in an effective-dated, versioned config owned by a
  Rate Administrator — never hard-coded (`missing-configuration-ownership`).
- A rate change uses the version in effect on the relevant date; a term deposit
  keeps its open-date rate (grandfathered); variable savings may apply forward —
  confirm per product (`missing-effective-dating`, `missing-cohort-treatment`).
- Interest accrual is computed daily and is idempotent per (account, accrual
  date); posting/capitalization is idempotent per (account, period)
  (`missing-batch-job-spec`, `missing-idempotency`).
- Accrued and posted interest are double-entry and post to the GL; accounting
  reconciles accrued vs posted daily.
