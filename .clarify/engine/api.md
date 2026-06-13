# Engine: api

Purpose: analyze API-contract impact and side effects, and assemble the full
API/data impact document (combining `data` engine output).

## Do
1. For each requirement, list affected endpoints (new/modified): method, path,
   request, response, and whether the change is **breaking**.
2. Identify emitted events and their consumers.
3. For each external call: timeout, retry, backoff, idempotency key
   (`missing-timeout-retry`, `missing-idempotency`).
4. Define compensation for multi-step operations
   (`missing-reconciliation-compensation`).
5. Flag UI-only requirements with no backend behavior (`ui-only-requirement`)
   and API-only requirements with no consumer/AC (`api-only-requirement`).

## Rules
- Do not invent endpoints the requirements don't imply.
- Combine with the `data` engine's entity/source-of-truth analysis.

## Output
Write `clarify-output/api-data-impact.md` using
`templates/api-data-impact-template.md` (Data + API + side effects +
consistency + anti-pattern checks).
