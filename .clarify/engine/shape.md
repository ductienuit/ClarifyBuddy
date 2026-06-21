# Engine: shape

Purpose: turn a raw idea (plus clarify output) into the skeleton of a structured
**URD** (User Requirements Document). Shape structure only — do not fabricate rules
or scope.

## Altitude (read first)
URD = **business altitude, BA-facing**: background/problem, objectives (multi-perspective),
scope, user groups & stakeholders, business processes, user stories + acceptance criteria,
business rules, screens & field specs, states, messages/errors, NFRs. Deep technical mechanics
(idempotency keys, batch resume, ledger internals, config-row schema, API design) do **not** go
in the body — summarize them as operational/non-functional points or surface as `OPEN QUESTION`
for the technical team. Never drop a lens (config / jobs / cohort / stakeholders); only change
the altitude at which it appears.

## Business-language rule
Write each requirement as a **business outcome a stakeholder would say**, not a system
mechanism. Avoid implementation jargon in the body — `ledger`, `double-entry`, `GL`, `accrual`,
`posting`, `idempotency`, `cohort`, `grandfathered`, `batch resume`. Use plain equivalents and
route the mechanism to NFR/operational notes or an `OPEN QUESTION`. Example:
- Avoid: "A daily job reads the effective rate and writes accrual entries per active account,
  idempotent on (account, date)."
- Prefer: "Hệ thống tính lãi hằng ngày cho mỗi tài khoản tiền gửi đang hoạt động theo lãi suất
  áp dụng của sản phẩm." (ghi chú "không được tính trùng lãi nếu job chạy lại" → NFR / OPEN
  QUESTION cho technical team.)

## Do
1. Take the idea + assumptions from `clarify`.
2. Draft: background/problem, objectives (Khách hàng / Business / Operations / Compliance-risk),
   scope (customer-facing + back-office + out-of-scope), and the **user groups & stakeholders**
   table (RACI; include non-user/back-office actors — admin/configurator, operations,
   accounting/back-office, external systems, scheduled jobs). If a non-user actor is plausible
   but unconfirmed, list it as `OPEN QUESTION` rather than omitting it (`missing-system-actor`).
3. Convert the idea's intent into **user stories**: `Là <vai trò> / Tôi muốn <hành động> / Để
   <lợi ích> / Tiêu chí chấp nhận <điều kiện>`. Include non-user actors too (e.g. "Hằng ngày lúc
   <time>, <job> xử lý <input>, sinh <output> cho <consumer>").
3b. Draft the **end-to-end journey (§6 overview)** — the ordered steps from entry to result
   (menu → choose → see terms/rate → enter amount → choose source/options → preview → confirm →
   **authenticate** → process → result → view detail). Don't start mid-way; include the steps
   before and after the core action. Mark unknown steps `OPEN QUESTION`.
3c. For each screen the feature implies, fill the **Screen matrix & field specs (§9.3)**: screen
   name, platform/actor/purpose (blockquote), and a field table `Tên trường (EN) | Tên trường
   (VN) | Kiểu dữ liệu | M/O | Mô tả / Ràng buộc`. Information level (not pixel design), but
   detailed enough for Dev and QA to picture the behavior.
4. For any user story missing actor/want/benefit/acceptance criteria, flag inline (do not guess).
5. List **configurable parameters** the product implies (rates, fees, limits, thresholds) with
   an owner placeholder; unknowns → `OPEN QUESTION` (`missing-configuration-ownership`). For any
   rule that may change over time, surface effective-dating and the existing-vs-new cohort
   strategy as `OPEN QUESTION` (`missing-effective-dating`, `missing-cohort-treatment`).
6. Mark every unstated rule as `OPEN QUESTION`; every default as `ASSUMPTION`.

## Rules
- Out-of-scope must be non-empty; if unknown, list candidate exclusions as `OPEN QUESTION`.
- Keep user stories atomic (one role, one want, one acceptance criterion thread each).

## Output
Use `templates/urd-draft-template.md` (title "URD Draft"). Carry the **Document Profile**
(Role + `Standard: URD` + Domain mode + Language) into the profile block. Fill the business
sections including the **journey (§6)**, **user stories (§7)**, and **Screen matrix & field
specs (§9.3)**, and carry over from `clarify`: the **Variant / Options Matrix (§5)**, the
**Stakeholder Perspectives (§16)**, and the **Suggested Additional Capabilities (§15)**
(`SUGGESTION:` items) — kept clearly separate from agreed scope. Leave business rules / edge
cases / error mapping / state diagrams to later engines.
