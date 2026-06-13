# Common Flows: Fintech

## Transfer money
- **Actors:** Customer, Ledger, Payment provider.
- **Main path:** 1) Validate sender balance + limits 2) Run AML check
  3) Place hold 4) Post double-entry transaction 5) Settle via provider
  6) Release hold / finalize.
- **Branches:** insufficient funds; AML flag → manual review; provider failure →
  reverse hold and compensate.

## Payment
- **Main path:** authorize → capture → post to ledger → reconcile.
- **Branches:** decline; partial settlement; chargeback.

## Reconciliation
- **Main path:** fetch provider statement → match against ledger → flag
  discrepancies → resolve.

## Open savings / term deposit
- **Actors:** Customer, Product Config, Ledger.
- **Main path:** 1) validate min opening balance + KYC 2) read the rate in effect
  on the open date 3) create the deposit (term deposits store maturity date)
  4) post the opening double-entry.
- **Branches:** below minimum; rate change before funding; early withdrawal
  (penalty); maturity → renew or pay out.

## Interest accrual & posting (scheduled)
- **Actors:** Interest-Accrual Job, Ledger, Accounting/GL.
- **Main path:** 1) daily 02:00 UTC, for each active deposit read the effective
  rate 2) compute accrual (idempotent per account+date) 3) write accrual entries
  4) periodically post/capitalize 5) GL posting + reconciliation consume outputs.
- **Branches:** job rerun (no double-accrual); partial-batch failure → resume;
  rate version changed mid-period (apply by effective date).
