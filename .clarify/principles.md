# Clarify — Operating Principles

These principles govern every workflow and engine. Load this first in every
command.

## 1. Quality over generation

Clarify improves and scores requirements. It does not invent a product. When
input is thin, expose the gaps — do not paper over them with plausible fiction.

## 2. Never invent business rules

If a rule, constraint, or value is not stated and cannot be safely derived, mark
it as:

- `ASSUMPTION:` — a reasonable default you are proceeding with, clearly labeled.
- `OPEN QUESTION:` — something only a human stakeholder can resolve.

Never silently assume a rule into existence.

## 3. Separate scope explicitly

Every output distinguishes:

- **In scope** — what this requirement covers.
- **Out of scope** — what it deliberately excludes.
- **Open questions** — unresolved items blocking confidence.

## 4. Testable, build-ready wording

Prefer requirements with a clear **actor**, **trigger**, and **observable
outcome**. Acceptance criteria should be expressible as pass/fail (Given / When /
Then). Vague verbs ("manage", "handle", "support") are flagged, not accepted.

## 5. Always surface edge cases and handoff risk

Happy path is necessary but never sufficient. Surface negative paths, boundary
conditions, exception flows, permissions, state transitions, and the risks a Dev
or QA engineer would hit at build time.

## 6. Traceability

Every story, acceptance criterion, and test scenario should trace back to a
requirement. Every requirement should trace forward to at least one test.

## 7. Reproducible scoring

Scores come from `evaluators/scoring-rubric.yaml` and the deduction model in
`evaluators/requirement-quality-score.md`. The same input should yield the same
score and band. Show the math.

## 8. Don't hard-block on clarification

`clarify` presents questions, then proceeds using clearly-labeled assumptions —
unless the user is live and answers. Do not stall a workflow waiting for input.

## 9. Domain-agnostic core

Engines, workflows, templates, anti-patterns, and the rubric contain no
domain-specific logic. Domain knowledge is loaded only from a selected domain
pack.

## 10. Analyze from every stakeholder perspective

Whether **writing** or **analyzing** a URD, never stop at "user ↔ system".
Walk the feature through each stakeholder class and capture what it needs, what it
fears, and what it consumes:

- **End user / customer** — the primary flow.
- **Operations** — runbooks, monitoring, manual interventions, support tooling.
- **Accounting / finance** — GL postings, revenue/fees, statements, tax.
- **Reconciliation** — matching internal vs external records, discrepancy handling.
- **Partners / external systems** — integrations, contracts, SLAs, webhooks.
- **Risk / compliance** — limits, fraud, KYC/AML, audit, regulatory obligations.
- **Maintenance / engineering** — configuration, migrations, observability, on-call.
- **Data / analytics** — events, reporting, source of truth.
- **Security** — authz, sensitive data, retention.

A stakeholder with no stated need is itself a finding (`missing-system-actor`).
Tailor depth to the Document Profile role (BA → business/process emphasis; PO →
product/value emphasis), but cover every relevant stakeholder either way — they
populate §2.2 (user groups) and §16 (stakeholder perspectives) of the URD.

## 11. Proactively propose completeness

Based on the stated feature **and** the selected domain, proactively recommend the
**additional capabilities a complete product needs** but the input omits — e.g.
configuration screens, the back-office/admin side, reconciliation, reporting,
notifications, audit, migration of existing data, and the scheduled jobs that
serve accounting/ops.

This does **not** override Principle 2. Every proposal is a clearly-labeled
`SUGGESTION:` (a recommended addition for the user to confirm or reject), grounded
in the domain pack's common flows where one is selected — never written as a
confirmed requirement or an invented business rule. Suggestions live in their own
section so they never masquerade as agreed scope.

## 12. Domain context: pack optional, otherwise infer-and-label

A domain pack is an **optional accelerator, never a gate**. The domain-agnostic
core (engines, anti-patterns, rubric, the lenses in Principles 5/10/11) carries
most of the value and always runs. Handle domain context in this order:

1. **Auto-detect** the domain from the input (terms, entities, flows). State the
   detected domain in one line.
2. **If a matching pack exists** under `domain-packs/`, load it — its glossary,
   common flows, and **candidate** rules give consistent, reviewable,
   confirmable knowledge. Offer it rather than forcing a manual selection.
3. **If no pack matches (or the pack is thin),** do **not** stop and do **not**
   force-fit a wrong pack. Proceed using your own domain knowledge, but every
   domain-specific rule, flow, edge case, or entity you infer **must** be labeled
   `ASSUMPTION:` / `SUGGESTION:` / `OPEN QUESTION:` — never asserted as fact.
   Inference is safe precisely *because* it is labeled (Principle 2 still holds).

Note in the output which mode was used: `domain pack: <name>` or
`domain: <inferred> (no pack — items below are labeled inferences)`. Packs are
worth maintaining only for domains used repeatedly or with org-specific
rules/compliance; rely on labeled inference for the long tail.

## 13. Document presentation & naming conventions (URD template)

The single document Clarify produces is a **URD (User Requirements Document)** in the
**URD template** shape. It must read top-to-bottom for someone seeing the feature for the
**first time**, and its machine anchors must stay stable across versions. These
conventions are the **default** for `from-idea` (draft), `finalize` (final), and `export`
(HTML/Word); `audit` references them under the **clarity** and **structure** dimensions.
They are *presentation* rules — they restate content that already exists and add no
business rule (Principle 2 still holds).

**13.1 File naming — never the word "final".**
The canonical output is `urd.md` (not `final-urd.md`). A prior version is archived as
`urd.v<semver>.md`; the canonical name always holds the latest. Version lives in the
Lịch sử thay đổi (Change history) + the archive name, never in the main file name. The
renderings are `urd.html` (HTML) and `urd.docx` (Word).

**13.2 The HTML/Word are a full URD, not a "review pack".**
`export` (and `finalize` step 9c) render `urd.html` **from `urd.md`** (one source of
truth) via pandoc into the navy shell `urd-pack-template.html`, then: (a) render
diagrams — **Mermaid client-side only, no PlantUML**; (b) turn group-band rows into
`colspan` merged header cells; (c) add a TOC (Mục lục) and render the §4.2 **Artifact
index**; (d) on request produce `urd.docx` via LibreOffice (`soffice --convert-to docx`).
No tool label ("Clarify", "Review Pack") appears in the displayed content.

**13.3 Heading language follows the Document Profile Language (default `vi`).**
When `Language = vi`, render every section heading as `Tiếng Việt (English term)` — e.g.
`Tổng quan (Overview)` — never an ad-hoc mix. When `Language = en`, the English term only.
Machine-readable anchors stay English **always**: IDs (`F0n-Name`/`US-#`/`BR#`/`ERR-*`/
`A#`/`Q#`/`S#`/`V#`), error codes, the `ASSUMPTION`/`OPEN QUESTION`/`SUGGESTION` labels,
**field EN names**, and file names.

**13.4 The URD skeleton (fixed order).**
Cover info table (Document control) → **Lịch sử thay đổi** (Change history) → **Mục lục**
(TOC) → **§1 Tổng quan** (1.1 Giới thiệu · 1.2 Đối tượng/Phạm vi · 1.3 Glossary + symbol
table) → **§2 Tổng quan hệ thống** (2.1 Mục tiêu · 2.2 Nhóm người dùng · 2.3 overview +
one Mermaid diagram) → **Quy ước trình bày sơ đồ** (Diagram conventions) → **§3 [Tên
nghiệp vụ]** repeating per process → **§4 Phụ lục** (4.1 ref-code · 4.2 Artifact index +
traceability) → **§5 Câu hỏi mở** → Phê duyệt (Sign-off).

**13.5 §3 is a capability-repeating block — one per business process.**
Copy the whole §3 for each process, keeping the sub-order: 3.1 Mô tả · 3.2 User stories +
Tiêu chí chấp nhận · 3.3 Luồng xử lý (Mermaid sequence + steps) · 3.4 Trạng thái (colored
Mermaid state + table) · 3.5 Quy định & ràng buộc · 3.6 Danh sách & đặc tả màn hình · 3.7
Thông báo / lỗi · 3.8 Yêu cầu phi chức năng.

**13.6 Flow naming = `F0n-FeatureName`.**
Keep the **number** stable (so traceability never breaks); only *append* a short English
feature name (Login / Approve / Transfer / …). The §3 heading leads with the
Profile-language name, e.g. `3. Phê duyệt chuyển tiền lương (Payroll approval)`. Use
`F0n-Name` consistently in the Flow Catalog, steps, screen specs, and inside the diagrams.

**13.7 User stories = the requirement expression (§3.2 / draft §7).**
One grouped table per process: `ID | Là (vai trò) | Tôi muốn | Để | Tiêu chí chấp nhận`,
stable `US-#` ids. Each story is self-standing; acceptance criteria are observable
(pass/fail). Stories are derived from confirmed requirements/intent — never invented;
a gap → `ASSUMPTION` / `OPEN QUESTION`.

**13.8 Errors = §3.7 "Thông báo / lỗi / exception cases"; edge analysis lives in the doc.**
Per process, the error section uses the standard columns: `Trường hợp / Mã | Điều kiện xảy ra |
Thông báo (VN) | Thông báo (EN) | Xử lý`. Error codes (`ERR-<MODULE>-NNN`) stay English;
user messages are written in both VN and EN at business-readable wording. The **whole
edge-case analysis lives inside the document, not a separate `edge-case-matrix.md` file**:
edges that *produce* an error are rows in §3.7; edges that *do not produce* an error
(idempotency/replay, TTL/expiry, sandbox isolation, …) go in the draft's "Edge cases
without errors" subsection.

**13.9 Diagrams are Mermaid-only.**
§3.3 process flow = `sequenceDiagram` + `autonumber`, **no color**; §3.4 state =
`stateDiagram-v2`, **colored** via `classDef` (init=blue, intermediate=amber,
success=green, error=red). The diagram comes first, the table/steps below it. **No
PlantUML anywhere.** In-document traceability (User stories ↔ Flow Catalog ↔ rules ↔
errors) replaces any separate `traceability-matrix.md` file.

**13.10 Open questions consolidated in §5; decisions in Lịch sử thay đổi; no `decision-log.md`.**
Every remaining `OPEN QUESTION` is gathered into **§5 Câu hỏi mở** (`# | Câu hỏi | Người
phụ trách | Trạng thái`), the blocking subset marked `BLOCKER`. Resolved
assumptions/answers become decisions reflected in the body (rules/stories); the dated
history of applied decisions/CRs lives in **Document control → Lịch sử thay đổi**.
Internal `A#`/`S#` codes are hidden from displayed tables. There is **no separate
`decision-log.md` file**.

**13.11 Lean deliverable set; artifact index has a "Dùng khi" column.**
`finalize`/`export` leave only this set in `clarify-output/`: the source `urd.md`, the
renderings `urd.html` / `urd.docx`, `wireframes.html`, `audit-report.md`, and the version
archive `urd.v<semver>.md` (plus transient `change-impact.md` when a CR is in flight).
Analysis that used to be its own file is folded into the document and **no file is
emitted** for it: user stories (→ §3.2), edge cases (→ §3.7 + "Edge cases without
errors"), error map (→ §3.7), diagrams (→ §3.3/§3.4), traceability (→ Flow Catalog +
§4.2), decisions (→ Lịch sử thay đổi), elicitation (→ §5). The §4.2 **Artifact index**
lists only the kept set, each with a **Dùng khi (who / when)** column, and never links to
a dropped file.

**13.12 Markdown→HTML: blank line between a label/paragraph and a table.**
Always leave **one blank line** between a bold label or any paragraph text and a pipe
table directly below it. Without it, pandoc folds the label and the table into a single
paragraph and the table breaks in the HTML render. Applies everywhere a label or sentence
precedes a table (steps, screen field specs, glossary, symbol table, error table, artifact
index, …).

**13.13 Screen field specs + one source of truth; BA-altitude.**
- **§3.6 screen specs** use the field-spec table `Tên trường (EN) | Tên trường (VN) | Kiểu
  dữ liệu | M/O | Mô tả / Ràng buộc`, one sub-block per screen with a `Nền tảng · Actor ·
  Mục đích` blockquote. Where the doc is silent, label the placeholder `ASSUMPTION`; never
  invent a field, validation, or rule.
- **One source of truth:** a rule lives in §3.5 (the flow/step only cites its `BR#`); an
  error/message lives in §3.7; screen behaviour lives in §3.6; a step (§3.3) describes only
  the flow + branch points. No fact is duplicated across sections.
- **BA-altitude:** the URD describes *what* users and the business need — not the build
  design. No invented endpoint / schema / table; technical mechanics are summarized in §3.8
  NFR or surfaced as `OPEN QUESTION` for the technical team.
