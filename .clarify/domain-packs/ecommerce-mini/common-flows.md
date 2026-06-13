# Common Flows: E-commerce

## Checkout
- **Actors:** Customer, Payment gateway, Inventory.
- **Main path:** 1) Review cart 2) Enter shipping 3) Choose payment
  4) Authorize payment 5) Reserve inventory 6) Confirm order 7) Capture payment.
- **Branches:** payment declined → order pending/abandoned; item out of stock →
  block or backorder; address invalid → re-prompt.

## Refund
- **Actors:** Customer/Admin, Payment gateway.
- **Main path:** 1) Request refund 2) Validate eligibility (window, condition)
  3) Issue refund to original method 4) Update order state.
- **Branches:** partial refund; refund after capture failure → reconcile.

## Cart update
- **Main path:** add/remove/change qty → recompute totals → revalidate stock.
