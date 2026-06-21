# Engine: error-handling

Purpose: turn the failure modes of a user-facing or transactional flow into an
explicit **error → entity state → transaction status → message → action** map, so
FE, BE, QA, support, and legal align on the same codes and wording. Pairs with
`edge` (which finds the cases) — this engine assigns codes, user messages, and
handling.

## Do
1. Collect every failure from the requirements, `edge` matrix, and `risk` engine.
   Group them: eligibility/input, balance/account, product/config, authentication,
   money/processing, system.
2. For each, define: error code (`ERR-<MODULE>-NNN`), **the flow/step it occurs in**
   (Flow F0n-Name / step #), the condition that triggers it, **user-facing message in
   VN and EN**, and the handling (xử lý: chặn submit / fallback / cho thử lại), plus
   retryable? and owner. For "money moved but record not created", say it is processing
   and how to check / contact support — never assert a wrong final state.
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
Write the map **into each business process's §3.7 "Thông báo / lỗi / exception cases"
table** of the URD (Principle 13.8) — there is no separate `error-handling.md` file.
Columns (standard shape): `Trường hợp / Mã | Điều kiện xảy ra | Thông báo (VN) | Thông báo
(EN) | Xử lý`. Error codes (`ERR-*`) stay English; user messages are written in both VN
and EN at business-readable wording. Use `templates/error-handling-template.md` as the
working checklist while enumerating, and keep a coverage / Gaps list
(`missing-error-message-mapping`).
