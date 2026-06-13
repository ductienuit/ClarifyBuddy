# PRD: Guest Checkout

## Summary
Let logged-in customers buy items in their cart with a credit card.

## In scope
- Single-currency card checkout for logged-in users with a non-empty cart.

## Requirements
- When a customer confirms checkout, the system authorizes their card.
- On successful authorization, reserve inventory for each line item and create
  an order in `pending`.
- Capture payment once the order is confirmed.
- Email the customer a confirmation when the order is created.

## Business rules
- Orders may be cancelled only while `pending` or `paid`.
- Inventory is reserved at confirmation and released on cancellation.

## Open questions
- OPEN QUESTION: is guest (not logged-in) checkout in scope? (assumed no)

## Notes
- Payment uses an external gateway.
