# Example: Bad vs. Good Requirement

A side-by-side showing how Clarify transforms weak requirements, and which
anti-patterns each fix resolves.

| # | Bad | Good | Anti-patterns fixed |
| --- | --- | --- | --- |
| 1 | "The order can be cancelled." | "A customer with a `pending` or `paid` order can cancel it; cancellation is disallowed once shipped, and the action is audit-logged." | ambiguous-actor, undefined-state, missing-audit-log |
| 2 | "The page should be fast." | "First contentful paint occurs within 1.5s on a 4G connection (p95)." | non-testable-requirement, missing-analytics-success-measurement |
| 3 | "User can manage account settings." | "Given a logged-in user, when they submit a valid new email, then the system saves it and sends a verification message; invalid emails are rejected with an inline error." | missing-acceptance-criteria, non-testable-requirement |
| 4 | "Charge the card and confirm the order." | "Authorize the card (5s timeout, idempotency key). On success, reserve inventory and create the order; on decline, leave the cart intact and prompt retry. If the charge succeeds but the order write fails, reverse the charge (compensation)." | missing-exception-flow, missing-idempotency, missing-reconciliation-compensation |
| 5 | "Store the user's preferred language." | "Add `users.locale` (migration); extend `GET`/`PATCH /users` to read/write it; default to `en`. Source of truth: the users table." | missing-api-data-impact, missing-source-of-truth |

## Takeaway
Good requirements name an **actor**, a **trigger**, and an **observable
outcome**, define failure and boundary behavior, and make data/contract impact
explicit — exactly what Clarify audits for.
