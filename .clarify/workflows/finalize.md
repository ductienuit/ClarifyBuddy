# Workflow: finalize

## When to use
The spec is confirmed ("chốt") and you need the **final URD** to deliver to stakeholders /
approvers. This is the closing step after `from-idea` / `improve answers`.

## Inputs
- Prior outputs in `clarify-output/`: `urd-draft.md` (which carries the user-story / edge /
  error / flow-diagram / state analysis inline), plus `audit-report.md` if it exists. Read
  them; do not re-derive. There are no separate edge / error-handling / model / traceability /
  decision-log files to read.
- `$ARGUMENTS`: optional format — `md | html | word | all` (default `md + html`).

## Engine sequence (ordered)
1. `trace` — verify in-document traceability (User stories ↔ Flow Catalog ↔ rules ↔ errors);
   report orphans/dangling refs. Writes **no separate file**.
2. `finalize` — assemble the URD from prior outputs using `final-urd-template.md`, embedding
   Mermaid diagrams + viewer links, the screen wireframe HTML preview when screens exist, and a
   sign-off section. Then render the requested formats.

## Templates to fill
- `templates/final-urd-template.md`
- `templates/urd-pack-template.html` (HTML render shell)
- `templates/wireframe-template.html` (when screen/flow requirements exist)

## Outputs written
- `clarify-output/urd.md` (the sign-off doc — **no "final" in the name**, Principle 13.1).
- `clarify-output/urd.html` (default) and `urd.docx` (on `word`/`all`) — rendered from the
  Markdown (best-effort; see `export`).
- `clarify-output/wireframes.html` — when the doc has screens and inline HTML is not appropriate.

## Done criteria
- Section order follows the URD skeleton (bilingual headings; default Language=vi):
  Document control (cover info table) → Lịch sử thay đổi → Mục lục → **§1 Tổng quan** (1.1
  Giới thiệu, 1.2 Đối tượng/Phạm vi, 1.3 Glossary + symbols) → **§2 Tổng quan hệ thống** (2.1
  Mục tiêu, 2.2 Nhóm người dùng, 2.3 overview + one Mermaid diagram) → **Quy ước trình bày sơ
  đồ** → **§3 [Tên nghiệp vụ] (repeating per process)** (3.1 Mô tả · 3.2 User stories · 3.3
  Luồng — Mermaid sequence + steps · 3.4 Trạng thái — colored Mermaid state + table · 3.5 Quy
  định · 3.6 Màn hình + field specs · 3.7 Thông báo/lỗi · 3.8 Phi chức năng) → **§4 Phụ lục**
  (4.1 ref-code, 4.2 artifact index + traceability) → **§5 Câu hỏi mở** → Phê duyệt (Sign-off).
- Document control block; audit score + band stamp when available; Trạng thái never `Đã duyệt`
  while a blocker-level finding exists.
- **§3 is process-centric and Mermaid-only:** sequence (3.3) + colored state (3.4) for the SAME
  process (never `mixed-process-diagram-block`); steps read the diagram (branches as bullets,
  no error codes/rules restated); pointer line `Quy định: BR.. (§3.5). Lỗi … §3.7.`; a missing
  diagram for a key process is an `OPEN QUESTION` pointing to `improve model` — never fabricated.
  **No PlantUML anywhere.**
- User stories (§3.2) map every confirmed requirement; the Flow Catalog (draft §9.1) is the
  in-document traceability spine (rule / error-code / user-story columns); each flow maps to ≥1
  user story.
- Screen specs (§3.6) use the EN/VN/Kiểu/M-O field-table shape; where the doc is silent, fields
  are labeled `ASSUMPTION`. Errors (§3.7) use the `Trường hợp/Mã | Điều kiện | Thông báo VN |
  Thông báo EN | Xử lý` shape; `ERR-*` codes stay English.
- All `OPEN QUESTION` consolidated into §5 (blocking subset marked `BLOCKER`); resolved
  answers/assumptions reflected in the body; dated history in Lịch sử thay đổi.
- **No silent overwrite:** if `urd.md` existed, it is archived as `urd.v<N>.md`, the Version is
  bumped, and Lịch sử thay đổi gains a row citing the driver. Warn before overwriting a
  hand-edited file.
- The requested formats render **from** `urd.md` (best-effort; never blocks the Markdown
  deliverable): `urd.html` by default; `urd.docx` on `word`/`all`.
- No dangling ID references (every `BR#`/`F0n-Name`/`ERR-*` referenced exists) — or listed as
  findings.
- Wireframes follow strict derive-only rules: grayscale only, no brand colors/images, one
  phone/card frame per key flow step, numbered in flow order, traced to its flow/step + story.
- **Blank line before every table** that follows a label/paragraph (Principle 13.12).
- An **Artifact index (§4.2)** with a "Dùng khi" column lists only the lean deliverable set that
  exists (source `urd.md`, audit-report, version archive, wireframes/HTML/docx when written).
