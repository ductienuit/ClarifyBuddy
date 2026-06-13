# Example: Fintech Payment / Transfer

Demonstrates `/clarify:from-spec` → `/clarify:handoff` → `/clarify:finalize`
using the `fintech-mini` domain pack.

## Run

```
/clarify:from-spec examples/fintech-payment/input-prd.md
/clarify:handoff
/clarify:finalize brd
```

(Select `fintech-mini` when prompted.)

## What Clarify surfaces
- Mandatory idempotency on transfers (missing-idempotency).
- Compensation when the provider fails after debit
  (missing-reconciliation-compensation).
- Ledger as the single source of truth for balances (missing-source-of-truth).
- KYC threshold + AML review (missing-business-rule, risk/compliance).
- Audit of every money movement (missing-audit-log).

See `input-prd.md` for the starting document.
