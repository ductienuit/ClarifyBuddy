# Domain: Fintech (mini)

Movement and accounting of money: payments, transfers, balances, ledgers,
reconciliation, and regulatory checks (KYC/AML).

## Primary actors / roles
- Customer — initiates payments/transfers; opens savings/term deposits.
- Compliance officer — reviews KYC/AML flags.
- Rate Administrator — configures interest rates/fees with effective dates.
- Operations — investigates and resolves reconciliation discrepancies.
- Accounting / GL — posts interest and money movements to the general ledger.
- Interest-Accrual Job (scheduled) — accrues and posts interest.
- System — maintains the ledger and reconciles with providers.
- Payment provider / bank — external rails (ACH, card, wire).

## Core entities
- Account, Ledger, Transaction, Transfer, Payment, Hold, Reconciliation,
  KYC record, Savings/Term-Deposit Product, Rate Config (effective-dated),
  Accrual entry.

## Typical goals
- Money transfer, balance display, payment processing, statements, payouts,
  **savings/term deposits with configurable interest and scheduled accrual**.

## When to select this pack
- The PRD mentions payments, transfers, balances, ledgers, settlement,
  reconciliation, KYC/AML, **savings/term deposits, interest rates, or interest
  accrual/posting**.
