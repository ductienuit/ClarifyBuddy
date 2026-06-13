# PRD: Money Transfer

## Summary
Let customers transfer money from their account to another account.

## Requirements
- A customer can transfer money to another account.
- The balance is updated.
- The recipient is notified.

## Notes
- Transfers use an external payment provider.
- There are daily limits.

(Deliberately incomplete — missing actor ownership checks, idempotency,
compensation, source of truth, KYC, and audit. Run `/clarify:from-spec` to
expose these.)
