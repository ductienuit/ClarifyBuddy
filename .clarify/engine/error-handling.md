# Engine: error-handling

Purpose: turn the failure modes of a user-facing or transactional flow into an
explicit **error → entity state → transaction status → message → action** map, so
FE, BE, QA, support, and legal align on the same codes and wording. Pairs with
`edge` (which finds the cases) — this engine assigns codes, user messages, and
handling.

## Do
1. Collect every failure from the requirements, `edge` matrix, `risk`, and `api`
   engines. Group them: eligibility/input, balance/account, product/config,
   authentication, money/processing, system.
2. For each, define: error code, **the flow/step it occurs in** (Flow Fxx / step #
   from `model-suggestions.md`), HTTP/API status (if applicable), **transaction
   status left behind** (e.g. Failed / Pending / Reversed / Timeout), entity state
   left behind (if any), internal message, **user-facing message**, retryable?,
   required action, needs-ops?, owner.
3. Pay special attention to the "money moved but record not created" case: the
   user message must not assert a wrong final state — say it is processing and how
   to check or contact support. Tie it to a defined transaction status.
4. Flag any failure with no code/message as `missing-error-message-mapping`.

## Rules
- User-facing messages are plain language — no `ledger`, `idempotency`, `GL`,
  `accrual`, `debit`, `schema`, `API`, `timeout code`, or internal service names.
  Do not invent message copy that implies a business rule; mark uncertain copy
  `OPEN QUESTION`.
- Reuse the domain pack's error examples if a pack is selected.
- Keep codes stable and namespaced (e.g. `<FEATURE>_<NNN>`).

## Output
Write the map **into the document's "Error code & message table"** (Principle 13.8) —
there is no separate `error-handling.md` file. **Split it by flow:** each flow under a
sub-header with a stable anchor (`#### F0n-Name {#err-f0n}`) so the flow's Steps
deep-link straight to its errors. Columns: `Error code | Step / API | Scenario |
Transaction state | User-facing message | Retryable? | Required action | Test`. The
entity-state column is dropped (almost always `unchanged`); **Step / API** is the
business-level step or call (e.g. `step 3` / `login()`), never a path / method / HTTP
status. (A very small error set may stay as ONE table with per-flow sub-header anchors
inserted, as long as every Step deep-link resolves.) Use
`templates/error-handling-template.md` as the working checklist while enumerating, and
keep a coverage / Gaps list (`missing-error-message-mapping`).
