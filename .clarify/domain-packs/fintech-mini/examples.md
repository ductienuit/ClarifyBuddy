# Examples: Fintech

## Transfer
- **Weak:** "User transfers money to another account."
- **Strong:** "When a KYC-verified customer initiates a transfer from an account
  they own, the system validates balance and daily limit, runs an AML check,
  places a hold, and posts a double-entry transaction. The operation requires an
  Idempotency-Key; a repeated key returns the original result. If the provider
  fails after debit, a compensating reversal restores the balance. All movements
  are audit-logged. ASSUMPTION: negative balances disallowed."
- **Anti-patterns fixed:** ambiguous-actor, missing-permission,
  missing-idempotency, missing-reconciliation-compensation, missing-audit-log,
  missing-business-rule.

## Balance
- **Weak:** "Show the user's balance."
- **Strong:** "GET /accounts/{id}/balance returns the balance derived from the
  ledger (source of truth), never a cached field, scoped to the authenticated
  owner."
- **Anti-patterns fixed:** missing-source-of-truth, missing-permission.

## Savings deposit (end-to-end — the product/config/job lenses)
- **Weak:** "User opens a savings deposit and earns 2% interest. The system
  calculates interest."
  - This is user-flow-only. It misses: who configures the rate, how a future rate
    change is handled, existing vs new accounts, and the accrual job + its
    accounting consumers.
- **Strong:**
  - **Config:** "The savings interest rate is set in Rate Config by a Rate
    Administrator (0–10%, two decimals), stored as an effective-dated, versioned
    row. Never hard-coded."
  - **Effective dating / cohort:** "A rate change uses the version in effect on
    the relevant date. Existing fixed-term deposits keep their open-date rate
    (grandfathered); variable savings apply the new rate from the effective date.
    Affected holders are notified 30 days ahead."
  - **Open deposit (Customer):** "A KYC-verified customer opens a deposit meeting
    the minimum opening balance; the deposit records the rate version in effect on
    the open date; opening posts a double-entry."
  - **Accrual job (scheduled):** "The Interest-Accrual Job runs daily 02:00 UTC,
    idempotent per (account, accrual-date); it reads the effective rate, writes
    accrual ledger entries, and resumes from the last processed account on
    failure. Posting/capitalization is idempotent per (account, period)."
  - **Accounting consumers:** "Accrual and posting outputs feed GL posting and
    daily reconciliation (accrued vs posted); Operations resolves discrepancies;
    all config changes and movements are audit-logged."
- **Anti-patterns fixed:** missing-system-actor, missing-configuration-ownership,
  missing-effective-dating, missing-cohort-treatment, missing-batch-job-spec,
  missing-source-of-truth, missing-idempotency, missing-audit-log.
