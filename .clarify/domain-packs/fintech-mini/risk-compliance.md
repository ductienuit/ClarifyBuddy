# Risk & Compliance: Fintech

- **Risk:** double spend on retry → **Control:** mandatory idempotency key +
  ledger uniqueness constraint.
- **Risk:** debit succeeds, settlement fails → **Control:** compensating reversal
  + daily reconciliation.
- **Risk:** balance drift → **Control:** ledger is source of truth; reconcile
  against provider.
- **Compliance:** KYC/AML required before high-value transfers; suspicious
  activity must be flagged and auditable (confirm thresholds — OPEN QUESTION).
  PCI-DSS for card data; data retention rules apply.
- **Audit:** every money movement, AML decision, and limit override is logged
  immutably with actor, amount, timestamp.
- **Risk:** rate hard-coded / changed with no owner or effective date → wrong
  interest, disputes → **Control:** effective-dated versioned Rate Config owned by
  a Rate Administrator; audited config changes (`missing-configuration-ownership`,
  `missing-effective-dating`).
- **Risk:** accrual job reruns or fails midway → double/zero interest →
  **Control:** idempotency per (account, accrual-date) + resume-from-checkpoint;
  reconcile accrued vs posted daily (`missing-batch-job-spec`).
- **Risk:** rate change silently re-evaluates existing deposits →
  **Control:** explicit cohort strategy (grandfather term deposits), holder
  notification (`missing-cohort-treatment`).
