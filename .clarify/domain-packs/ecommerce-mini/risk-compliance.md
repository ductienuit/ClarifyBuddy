# Risk & Compliance: E-commerce

- **Risk:** double charge on retry → **Control:** idempotency key on payment.
- **Risk:** overselling last unit → **Control:** atomic inventory reservation.
- **Risk:** partial failure (charged, no order) → **Control:** reconciliation job
  + compensation.
- **Compliance:** PCI-DSS — never store raw card data; use the gateway's token
  (confirm scope). Tax/VAT rules vary by jurisdiction (OPEN QUESTION).
- **Audit:** log price changes, refunds, and admin order edits.
