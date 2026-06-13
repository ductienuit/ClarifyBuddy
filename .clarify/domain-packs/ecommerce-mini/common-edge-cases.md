# Common Edge Cases: E-commerce

- **Boundary:** empty cart; max line items; quantity 0 or negative; max quantity
  per SKU; price = 0.
- **Negative/invalid:** invalid coupon; expired card; invalid address.
- **Exception/failure:** payment gateway timeout/decline; inventory service down;
  charge succeeds but order write fails.
- **State:** cancel an already-shipped order; refund an unpaid order; double
  checkout of the same cart.
- **Concurrency:** two customers buy the last unit; user double-clicks "Place
  order" (idempotency).
- **Permission:** customer refunds someone else's order; non-admin edits price.
