---
name: clarify-finalize
description: >-
  Clarify · Finalize — the closing step. Compile confirmed Clarify outputs into the
  final URD (User Requirements Document) for a BA/PO sign-off. Use when the user
  says the spec is confirmed and wants the final deliverable ("produce the URD",
  "finalize it", "export the sign-off doc"). Renders urd.md + urd.html by default
  (urd.docx on request). Includes a cover info table, an audit score/band stamp when
  available, embedded Mermaid sequence + colored state diagrams, user stories, a
  Screen matrix & field specs, an error & message table, and a consolidated open
  questions section. Part of the Clarify requirement-quality pack.
---

# Clarify: Finalize

Compile prior Clarify outputs into the sign-off URD (the file is named `urd.md` —
never with the word "final").

## Steps
1. Read `.clarify/principles.md` (esp. Principle 13 — document presentation &
   naming conventions, URD template).
2. Read the resolved draft `clarify-output/urd-draft.md` (Document Profile in its
   section 0) and `audit-report.md` if it exists. Determine the requested format from
   the user: `md | html | word | all` (default `md + html`).
3. Run the workflow `.clarify/workflows/finalize.md` (verify in-document
   traceability — User stories ↔ Flow Catalog ↔ rules ↔ errors; no separate matrix
   file; then assemble with the `finalize` engine).
4. Write `clarify-output/urd.md` (template `final-urd-template.md`). **Numbers
   auto-follow the URD skeleton — do not hardcode/renumber.** Order: Document control
   (cover info table) → Lịch sử thay đổi → Mục lục → §1 Tổng quan (1.1–1.3) → §2 Tổng
   quan hệ thống (2.1–2.3) → Quy ước trình bày sơ đồ → §3 [Tên nghiệp vụ] repeating
   (3.1 mô tả · 3.2 user stories · 3.3 sequence + steps · 3.4 colored state + table ·
   3.5 rules · 3.6 screens + field specs · 3.7 errors · 3.8 NFR) → §4 Phụ lục → §5 Câu
   hỏi mở → Phê duyệt.
5. Render the requested formats **from** the Markdown (best-effort, per `export` /
   Principle 13.2): `urd.html` by default, `urd.docx` on word/all. If `urd.md` already
   exists, archive it as `urd.v<N>.md`, bump the Version, and add a Lịch sử thay đổi row.

## Rules
- Compose from prior outputs; never invent business rules or fabricate missing
  sections (mark them OPEN QUESTION). If an input is missing, name the command/skill
  that produces it.
- Diagrams are **Mermaid-only**: §3.3 sequence (autonumber, no color), §3.4 colored
  `stateDiagram-v2`, each with its viewer link. **No PlantUML.**
- §3 is capability-repeating (one block per process); sequence (3.3) and state (3.4)
  in one block must be the same process. Carry over journey, user stories, screen
  field specs (EN/VN/Kiểu/M-O), the error & message table (VN/EN), and entity vs
  transaction/operation state; mark missing sources OPEN QUESTION. Emit only the lean
  deliverable set (Principle 13.11).
- When screens exist, add low-fidelity wireframes as an inline HTML widget after the
  screen matrix, or write `clarify-output/wireframes.html`. Real URD labels, grayscale
  only, no images/brand colors, no ASCII primary wireframes; trace every screen to its
  flow/step and user story.
- Consolidate every ASSUMPTION / OPEN QUESTION into §5 (blocking subset marked
  BLOCKER). Never stamp `Đã duyệt` (Approved) while a blocker-level finding exists.
