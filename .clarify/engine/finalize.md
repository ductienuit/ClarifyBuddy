# Engine: finalize

Purpose: after the spec is confirmed, assemble the **final sign-off URD** (User
Requirements Document) in the standard shape, from a resolved `from-idea` draft.
Do NOT re-derive content: compose from prior `clarify-output/` files. Do NOT invent
business rules.

## Template & output
- Always use `templates/final-urd-template.md`.
- Write `clarify-output/urd.md` (Markdown master). Then render the requested formats
  (see step 9c): `urd.html` (HTML) and, on request, `urd.docx` (Word).
- **Format argument** (`$ARGUMENTS`): `md | html | word | all` — **default `md + html`**
  (always write `urd.md`; render `urd.html` by default; `word`/`all` also produce
  `urd.docx`).

## Do
1. Read available outputs: `urd-draft.md` (which carries the user-story / rule / flow /
   state / edge / error analysis inline), plus `audit-report.md` if it exists. There are
   no separate edge / error / model / traceability / decision-log files (Principle 13.11) —
   pull that content from the draft's sections.
2. Compose `final-urd-template.md`, pulling each section from the matching draft content.
   Follow the document presentation conventions (Principle 13):
   - **Document control (cover info table)** + **Lịch sử thay đổi (Change history)** at the
     top; include the audit score as the **Quality stamp** when an audit-report exists, else
     `not run`.
   - **§1 Tổng quan** — 1.1 Giới thiệu (from the draft background/problem + audience), 1.2
     Đối tượng/Phạm vi (from scope), 1.3 Glossary (carry the draft's glossary) + the
     symbol-conventions table.
   - **§2 Tổng quan hệ thống** — 2.1 Mục tiêu (from objectives), 2.2 Nhóm người dùng (from the
     user-group/stakeholder table), 2.3 overview narrative + ONE representative Mermaid
     sequence diagram (from the draft journey).
   - **Quy ước trình bày sơ đồ** — carry the Diagram conventions block (Mermaid sequence
     no-color + autonumber; colored state).
3. Assemble the **§3 capability blocks — one per business process** (from the draft Flow
   Catalog). For each process, in this order:
   - **3.1 Mô tả nghiệp vụ** — criteria table (Mục tiêu / Phạm vi / Đối tượng / Nền tảng).
   - **3.2 User stories** — carry the draft's `US-#` for this process (`ID | Là | Tôi muốn |
     Để | Tiêu chí chấp nhận`). If a confirmed requirement has no story, synthesize one from
     it (no invention); a gap → `ASSUMPTION` / `OPEN QUESTION`.
   - **3.3 Luồng xử lý** — the Mermaid `sequenceDiagram` (autonumber, no color) for THIS
     process, then the steps table below it; end with the pointer line `Quy định: BR.. (§3.5).
     Lỗi / thông báo / xử lý: §3.7.` Re-render only from the confirmed step-by-step; never
     invent. If a key in-scope process has no flow, write an `OPEN QUESTION` naming the missing
     flow and the command that produces it (`improve model`) — do not fabricate a diagram.
   - **3.4 Trạng thái** — the colored Mermaid `stateDiagram-v2` for THIS process, then the
     VN/EN state table below it.
   - **3.5 Quy định & ràng buộc** — the business rules (`BR#`) applying to this process.
   - **3.6 Danh sách & đặc tả màn hình** — one sub-block per screen (blockquote Nền tảng·
     Actor·Mục đích + field table `Tên trường (EN) | VN | Kiểu | M/O | Mô tả / Ràng buộc`),
     enriched from the draft Screen matrix. Where the doc is silent, label `ASSUMPTION`.
   - **3.7 Thông báo / lỗi** — the error table (`ERR-*` code → điều kiện → thông báo VN/EN →
     xử lý) for this process, plus any non-error edges.
   - **3.8 Yêu cầu phi chức năng** — security, performance/sync, i18n, audit log.
   The sequence (3.3) and state (3.4) in one block must be the **same** process
   (`mixed-process-diagram-block` otherwise).
3b. When screens are defined, add low-fidelity **wireframes** — an inline HTML widget from
   `templates/wireframe-template.html` when the Markdown target supports inline HTML, else a
   self-contained `clarify-output/wireframes.html` linked from §4.2. Grayscale, derive-only;
   real labels from the URD; trace each screen to its flow/step + user story. No ASCII
   wireframes as the primary artifact.
4. **§4 Phụ lục** — 4.1 ref-code rules (`ERR-<MODULE>-xxx`); 4.2 Artifact index (the lean
   deliverable set that actually exists, with a "Dùng khi" column) + in-document traceability
   note (US ↔ Flow ↔ BR ↔ ERR). Do not list files that are not emitted.
5. **§5 Câu hỏi mở** — consolidate every remaining `OPEN QUESTION` into the table
   (`# | Câu hỏi | Người phụ trách | Trạng thái`); mark the blocking subset `BLOCKER`. Resolved
   assumptions/answers become decisions reflected in the body (rules/stories); the dated history
   lives in **Lịch sử thay đổi**. Hide internal `A#`/`S#` codes from displayed tables.
6. Carry over **Stakeholder perspectives** into §2.2 / §3, and **Suggested additional
   capabilities** (`SUGGESTION:`) as clearly-marked recommendations (never agreed scope).
9b. **Versioning — never overwrite silently.** If `urd.md` already exists: (1) archive it as
   `urd.v<N>.md` (N = its current Version); (2) bump the Version in Document control; (3) add a
   **Lịch sử thay đổi** row (version, date, summary, driver — `answer sheet vN` / `CR-nn`). The
   canonical `urd.md` always holds the latest. **Never** use the word "final" in the file name
   (Principle 13.1). If the file appears hand-edited since Clarify wrote it, warn before
   overwriting.
9c. **Render the requested formats.** After writing `urd.md`, follow the `export` engine and
   Principle 13.2: pandoc md→html wrapped in `templates/urd-pack-template.html` (Mermaid
   client-side, navy skin, TOC), no tool labels. By default also render `urd.html`. For `word`
   / `all`, additionally produce `urd.docx` via LibreOffice round-trip (`soffice --headless
   --convert-to docx`). Best-effort: if a renderer is unavailable, say so and leave `urd.md` as
   the deliverable — never fail finalize because a render tool is missing.
10. List any missing inputs and the command that produces each.

## Rules
- **Render headings in the Document Profile's Language** (Principle 13.3): default `vi` →
  each heading `Tiếng Việt (English term)`. Keep machine-readable anchors in English ALWAYS:
  ASSUMPTION/OPEN QUESTION/SUGGESTION labels, all IDs (`US-#/F0n-Name/BR#/ERR-*/A#/Q#/S#`),
  field EN names, and file names.
- Final ≠ invented: if a section has no source in prior outputs, mark it `OPEN QUESTION`.
- **Markdown→HTML hygiene (Principle 13.12):** always leave one blank line between a bold label
  or paragraph and a pipe table directly below it. Without it pandoc folds the label into the
  table and the table breaks in `urd.html`.
- A `blocker`-level audit finding means Trạng thái = `Draft — chưa duyệt`; never stamp `Đã duyệt`.
- Keep in-scope / out-of-scope / open questions clearly separated.
- §3 is process-centric and **Mermaid-only**: sequence (3.3) + colored state (3.4) for the SAME
  process; re-render diagrams only from confirmed step-by-step, never invent. No PlantUML.
- Wireframe rendering is derive-only and HTML-first (grayscale; real labels; trace each screen
  to its flow/step + user story; placeholders labeled `ASSUMPTION`; never invent fields/rules).

## Output
Write `clarify-output/urd.md` (**no "final" in the name**) using `final-urd-template.md`, then
render `urd.html` (default) and `urd.docx` (on `word`/`all`) from it (best-effort, step 9c).
