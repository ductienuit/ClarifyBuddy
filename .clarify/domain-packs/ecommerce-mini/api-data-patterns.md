# API & Data Patterns: E-commerce

## Entities & source of truth
- Inventory — owned by the inventory service (authoritative for stock counts).
- Price — owned by the pricing/catalog service; cart caches at add-time.
- Order — owned by the order service.

## Common endpoints
- POST /carts/{id}/items — add item.
- POST /orders — create order from cart.
- POST /orders/{id}/payments — charge (must accept Idempotency-Key).
- POST /orders/{id}/refunds — refund.

## Integration patterns
- Payment charge/refund: idempotency key required; 5s timeout, retries w/ backoff.
- Reserve-then-charge: compensation = release inventory on charge failure.
- Emit order.confirmed / order.shipped events for notifications.
