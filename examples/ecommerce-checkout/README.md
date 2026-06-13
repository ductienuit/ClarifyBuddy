# Example: E-commerce Checkout

Demonstrates `/clarify:from-spec` on a checkout PRD using the `ecommerce-mini`
domain pack.

## Run

```
/clarify:from-spec examples/ecommerce-checkout/input-prd.md
```

(Select the `ecommerce-mini` domain pack when prompted.)

## What you'd get in clarify-output/
- `audit-report.md` — score + band + findings.
- `edge-case-matrix.md` — empty cart, last-unit concurrency, gateway timeout, etc.
- `model-suggestions.md` — checkout activity diagram (PlantUML) + sequence
  (Mermaid) + order state machine, each with a viewer link.
- `api-data-impact.md` — POST /orders, payment idempotency, inventory source of truth.
- `stories.md` — stories + AC.
- `test-scenarios.md`, `traceability-matrix.md`.

Then run `/clarify:finalize prd` to compile a final, sign-off-ready PRD
(`final-prd.md`).

See `input-prd.md` for the starting document.
