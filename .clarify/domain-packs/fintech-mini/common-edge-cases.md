# Common Edge Cases: Fintech

- **Boundary:** transfer of 0; amount at exactly the daily limit; max precision /
  rounding; balance exactly equal to amount.
- **Negative/invalid:** negative amount; unsupported currency; transfer to self.
- **Exception/failure:** provider timeout after debit; settlement webhook lost;
  partial settlement.
- **State:** transfer already settled; reverse an unsettled transaction;
  double-post on retry.
- **Concurrency:** two transfers draining the same balance simultaneously.
- **Permission:** customer initiates a transfer from an account they don't own;
  non-compliance user clears an AML flag; non-admin edits a rate.
- **Temporal/rule-change:** deposit opened the day before a rate change (which
  rate applies?); rate version changes mid-accrual-period; existing term deposit
  when the rate drops (grandfathered) vs new deposit.
- **Batch/schedule:** accrual job rerun for a date already processed (no
  double-accrual); job fails after N of M accounts (resume from N+1); posting
  runs before accrual completes; reconciliation reads a half-finished posting run.
