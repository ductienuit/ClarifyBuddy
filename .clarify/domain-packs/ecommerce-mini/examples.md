# Examples: E-commerce

## Checkout
- **Weak:** "User checks out and pays."
- **Strong:** "When a logged-in customer with a non-empty cart confirms checkout,
  the system authorizes payment (5s timeout, idempotency key), atomically
  reserves inventory, and creates an order in `pending`. If authorization is
  declined, no inventory is reserved and the cart is preserved."
- **Anti-patterns fixed:** missing-trigger, missing-exception-flow,
  missing-idempotency, missing-reconciliation-compensation.

## Refund
- **Weak:** "Refund the customer."
- **Strong:** "ASSUMPTION: 30-day window. A customer (or admin) may refund a
  `paid` order within 30 days to the original payment method; the order moves to
  `refunded` and the action is audit-logged."
- **Anti-patterns fixed:** ambiguous-actor, hidden-assumption, missing-audit-log.
