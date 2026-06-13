# State Models: E-commerce

## Order
- **States:** cart → pending → paid → fulfilled → shipped → delivered;
  plus cancelled, refunded.
- **Transitions:** pending → paid (payment captured); paid → fulfilled (picked);
  fulfilled → shipped; shipped → delivered.
- **Cancellation:** allowed only from pending or paid (not shipped+).
- **Terminal states:** delivered, cancelled, refunded.
- **Illegal:** shipped → cancelled; refunded → paid.

## Payment
- **States:** authorized → captured → refunded; or authorized → voided; declined.
