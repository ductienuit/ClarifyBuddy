# Engine: write-urd

Purpose: assemble the full **URD draft** from shaped structure + downstream engine
outputs (user stories, business rules, flows, states, edge cases, errors, NFRs).
Produces `clarify-output/urd-draft.md` using `templates/urd-draft-template.md`.

## Altitude
Keep the body at **business altitude** (BA-facing). Deep technical mechanics (idempotency
keys, batch resume, config-row schema, double-entry internals, API design) are summarized
as operational/non-functional points (§12) or surfaced as `OPEN QUESTION` for the technical
team — never invented and never the primary content. The URD describes **what** users and the
business need, plus the screens, flows, rules, states, and messages — not the build design.

## Do
1. Start from the `shape` output: carry the **Document Profile** (the `## Document Profile`
   heading: Role + `Standard: URD` + Domain + Language) verbatim, then the background/problem,
   objectives (multi-perspective), scope, and the user-group/stakeholder table. Apply the
   document presentation conventions (Principle 13):
   - **§0 "Cách đọc bản nháp (How to read)"** after the Document Profile: 0.1 what-this-is +
     quick-read, 0.2 a **symbol-conventions** table (`F0n-Name`/`US-#`/`BR#`/`ERR-*`/`A#/Q#/S#`),
     0.3 the **Glossary** (define each core term once; only terms actually used).
   - **§6 "Cách hệ thống vận hành (How the system works — overview)"** before the detail: the
     end-to-end journey as plain narrative + one representative Mermaid sequence diagram.
2. Write **§7 User stories / Use cases** from the requirement intent: each story
   `Là <vai trò> / Tôi muốn <hành động> / Để <lợi ích> / Tiêu chí chấp nhận <điều kiện>`,
   stable `US-#` ids. This is the URD's expression of requirements. Missing info → `ASSUMPTION`
   / `OPEN QUESTION`; never invent.
3. Integrate **§8 Business rules** (from `risk`/domain pack) — explicit or `OPEN QUESTION`,
   never invented. Fill **Hiệu lực từ / Phiên bản** and **Áp dụng cho (mới/cũ/cả hai)** for any
   rule that can change over time (`missing-effective-dating`, `missing-cohort-treatment`).
4. Fill **§9 Functional flows & screens**: the **Flow Catalog** (whose columns map every `US-#`
   to a flow — the in-document traceability spine), the per-flow Mermaid sequence + steps (from
   `modeling`), and the **Screen matrix & field specs** (from `shape`) — each screen as a
   sub-block with a `Tên trường (EN) | Tên trường (VN) | Kiểu dữ liệu | M/O | Mô tả / Ràng buộc`
   table. A UI feature with no screen matrix is a gap.
5. Fill **§10 State model** (from `modeling`): colored Mermaid `stateDiagram-v2` + state table,
   distinguishing entity state from transaction/operation state. Unknowns → `OPEN QUESTION`.
6. Write the edge cases (from `edge`) into **§11**: error-producing edges in the **Error code &
   message table** (`ERR-*` code → điều kiện → thông báo VN/EN → xử lý) and non-error edges in
   **§11.2 Edges without errors** (no separate file; Principle 13.8).
7. Fill **§12 Non-functional requirements** (security/privacy, performance/sync, i18n, audit log)
   from `risk`. Fill **§16 Stakeholder perspectives** (Principle 10): one row per stakeholder
   class (operations, accounting, reconciliation, partners/external, risk/compliance,
   maintenance, data/analytics, security) with its need/concern, or `OPEN QUESTION`.
8. Fill **§15 Suggested additional capabilities** (Principle 11) with the `SUGGESTION:` items
   from `clarify` — kept separate from agreed scope, never confirmed requirements.
9. Ensure every user story has actor + want + benefit + acceptance criteria.
10. When invoked after `improve answers`, run a **resolved draft pass**:
    - Apply confirmed answers throughout the draft, not only in the assumptions / open-question
      lists. Update user stories, screen matrix, business rules, flows, state, errors, and NFRs
      when answers changed scope, variants, rules, or suggestions.
    - Remove stale `OPEN QUESTION` items that have been answered; keep unresolved questions with
      stable IDs.

## Rules
- **Render headings in the Document Profile's Language** (Principle 13.3): default `vi` →
  each heading `Tiếng Việt (English term)`. Keep machine-readable anchors in English ALWAYS:
  ASSUMPTION/OPEN QUESTION/SUGGESTION labels, all IDs (`A#/Q#/S#/V#/F0n-Name/US-#/BR#`, error
  codes), field EN names, and file names.
- Do not duplicate or contradict requirements; reconcile conflicts.
- Each user story is uniquely id'd (`US-01`, …); IDs are stable — append, never renumber.
- A resolved `from-idea` draft may be finalized for sign-off directly.

## Output
`clarify-output/urd-draft.md` using `templates/urd-draft-template.md`.
