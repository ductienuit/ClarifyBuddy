# Clarify Domain Packs

Domain packs add domain-specific knowledge — glossary, common flows, business
rules, edge cases, state models, API/data patterns, and compliance notes — that
engines reuse **only when a pack is explicitly selected**.

## Rule

The Clarify core (engines, workflows, templates, anti-patterns, rubric) is
**domain-agnostic**. No domain logic lives in core, and it carries most of the
value on its own.

A pack is an **optional accelerator, not a gate** (see Principle 12). Clarify
auto-detects the domain and:

- **loads a matching pack** when one exists — for consistent, reviewable,
  *confirmable* candidate knowledge; or
- **proceeds with labeled inference** when no pack matches — the model uses its own
  domain knowledge, but every inferred rule/flow/edge case is labeled
  `ASSUMPTION:` / `SUGGESTION:` / `OPEN QUESTION:`, never asserted as fact.

Never force-fit a wrong pack and never block because a pack is missing. Maintain a
pack only for domains used repeatedly or with org-specific rules/compliance.

## How engines use a pack

| Engine | Reads from the selected pack |
| --- | --- |
| `edge` | `common-edge-cases.md` |
| `risk` | `common-business-rules.md`, `risk-compliance.md`, `configurations.md`, `scheduled-operations.md` |
| `modeling` | `common-flows.md`, `state-models.md`, `scheduled-operations.md`, `back-office-flows.md` |
| `data` / `api` | `api-data-patterns.md`, `configurations.md` |
| `clarify` / `shape` | `back-office-flows.md` (non-user actors), `configurations.md` |
| all | `GLOSSARY.md`, `DOMAIN.md` for terminology and context |

A complete pack also includes `configurations.md` (tunable parameters with owners
and effective dating), `scheduled-operations.md` (batch/scheduled jobs and their
consumers), and `back-office-flows.md` (accounting/ops/admin actors and flows).
These carry the product/config/job/back-office lenses into a domain.

## Available packs

- `domain-pack-template/` — copy this to start a new pack.
- `ecommerce-mini/` — carts, checkout, orders, refunds.
- `saas-b2b-mini/` — orgs, roles, permissions, billing.
- `fintech-mini/` — payments, ledgers, reconciliation, KYC, savings/term deposits
  with configurable interest and scheduled accrual.

## Creating a pack

Copy `domain-pack-template/`, rename, and fill each file. Keep entries concrete
and example-driven. Do not encode anything that contradicts core principles
(e.g. never invent rules — provide *common* rules as candidates to confirm).
