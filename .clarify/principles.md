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

Whether **writing** or **analyzing** a PRD/BRD, never stop at "user ↔ system".
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
Tailor depth to the Document Profile (BA → business/process emphasis; PO →
product/value emphasis), but cover every relevant stakeholder either way.

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

## 13. Document presentation & naming conventions

A BRD/PRD must read top-to-bottom for someone seeing the feature for the **first
time**, and its machine anchors must stay stable across versions. These
conventions are the **default** for `from-idea` (draft), `finalize` (final), and
`export` (HTML); `audit` / `from-spec` reference them under the **clarity** and
**structure** dimensions. They are *presentation* rules — they restate content
that already exists and add no business rule (Principle 2 still holds).

**13.1 File naming — never the word "final".**
The canonical output is `brd.md` / `prd.md` (not `final-brd.md`). A prior version
is archived as `brd.v<semver>.md` / `prd.v<semver>.md`; the canonical name always
holds the latest. Version lives in the Change history + the archive name, never in
the main file name. The HTML rendering is `brd.html` / `prd.html`.

**13.2 The HTML is a full BRD/PRD, not a "review pack".**
`export` renders `brd.html` **from `brd.md`** (one source of truth) via pandoc,
then: (a) renders diagrams — Mermaid client-side, PlantUML via plantuml.com hex
`~h` encoding with a code fallback; (b) turns requirement group-band rows into
`colspan` merged header cells; (c) appends a TOC and an **Artifact index (source)**
linking back to `brd.md` + companions; (d) round-trips through LibreOffice
(`soffice --convert-to docx`) so Word export validates. No tool label
("Clarify", "Visual Review Pack") appears in the displayed content.

**13.3 Heading language follows the Document Profile Language.**
When `Language = vi`, render every section heading as `Vietnamese (English term)`
— e.g. `Yêu cầu nghiệp vụ (Business requirements)` — never an ad-hoc Anglo-Vietnamese
mix. When `Language = en`, use the English term only. Machine-readable anchors stay
English **always**: IDs (`F#`/`BRD-R#`/`BR#`/`T-#`/`A#`/`Q#`/`S#`/`V#`), error
codes, the `ASSUMPTION`/`OPEN QUESTION`/`SUGGESTION` labels, and file names.

**13.4 §0 "How to read this document" up front (after the summary).**
- `0.1` what this document is + a quick-read hint.
- `0.2` a **symbol-conventions** table: `F0n-Name` = Flow, `BRD-R#` = Requirement,
  `BR#` = Rule, `T-#` = Test, `A#/Q#/S#` = Assumption / Open Question / Suggestion;
  state plainly that *codes stay stable across versions; names are only for reading*.
- `0.3` the **Glossary** — moved to the front (not buried inside the requirements
  section): define each core term ONCE, only terms the requirements use.

**13.5 "How the system works (overview)" before the requirements.**
An end-to-end narrative of the journey plus ONE representative diagram. Per-flow
detail stays in the Functional Flows section.

**13.6 Flow naming = `F0n-FeatureName`.**
Keep the **number** stable (so traceability never breaks); only *append* a short
English feature name (Login / Consent / Token / Revoke / Suspend / Payment /
Onboarding …). The heading leads with the Profile-language name, e.g.
`Luồng F02-Login — Định danh người dùng`. Use `F0n-Name` consistently in the flow
catalog, error map, screen matrix, traceability, and inside the diagrams.

**13.7 Requirements = ONE table, grouped by capability + real sequence.**
Columns: `ID | Requirement (self-standing sentence) | Why (business reason) |
Priority`. Separate capability groups with a bold band row (Markdown) / a
`colspan` merged cell (HTML); order groups by the real journey and within a group
**Must → Should → Could**. A cross-reference like `Source: BR2` is **not** a Why.
Do **not** stuff flow / rule / test / source into the requirements section — those
belong in **Traceability**, which carries a **Source** column (`← A#/BR#/S#/Q#` that
produced the requirement). Every requirement (including deferred — keep the row,
mark Status = Deferred) appears once and stays mapped in Traceability. A flat
one-liner dump with no grouping / no Why is a clarity finding.

**13.8 Error section = "Error code & message table"; edge analysis lives in the doc.**
In the sign-off document the error section is titled **Error code & message table**.
It is split **by flow** — each flow under a sub-header carrying a stable anchor
(`#### F02-Login {#err-f02}`) so a flow's Steps deep-link straight to its errors. Drop
the low-signal **entity-state** column (almost always `unchanged`); transaction state
carries the meaning. Columns: `Error code | Step / API | Scenario | Transaction state
(rejected/throttled/refresh_required) | User-facing message | Retryable? | Required
action | Test`. **Step / API** is the business-level step or call (e.g. `step 3` /
`login()`) — never a path / method / HTTP status. (A very small error set may stay as
ONE table with the per-flow sub-header anchors inserted, as long as every Step
deep-link resolves.) This **supersedes** the earlier single-block error table. The
**whole edge-case analysis lives inside the document, not in a separate
`edge-case-matrix.md` file**:
edges that *produce* an error are rows in this table; edges that *do not produce* an
error (idempotency/replay, TTL/expiry boundaries, sandbox-vs-production isolation,
cross-app linkability, …) go in a sibling subsection **"Edge cases without errors"**.
The edge-section intro lists the edge groups; it points to no file.

**13.9 Body test scenarios = one numbered table; traceability is in-document.**
The body section is **Test scenarios (by context)** (replacing "Traceability
summary"): **one numbered table** so the total case count is visible at a glance, rows
grouped by flow (`F0n-Name`), columns `# | Requirement (R#/BRD-R#) | Flow (F0n-Name) |
Scenario (precondition + action) | Expected result | Test (T-xx)` — **not** a bullet
list. **Full preconditions/steps stay in `test-scenarios.md`**, not duplicated in the
doc. Close it with one
self-standing **Coverage & traceability** paragraph stating the case count and
coverage (e.g. "12 scenarios across 4 flows; 15/15 requirements have a flow + test; no
orphans"). **There is no `traceability-matrix.md` file**: requirement ↔ flow ↔ rule ↔
error traceability is expressed *in the document* via the Requirements table ↔ the
**Flow Catalog** (whose rule / error-code / requirement columns carry the links) ↔
this test table; step-level detail is in the kept `test-scenarios.md`. The coverage
paragraph points to the Flow Catalog + `test-scenarios.md`, **never** to a
traceability-matrix file. The Requirements section stays the four columns of 13.7
(`ID | Requirement | Why | Priority`). 13.9 supersedes any earlier rule that put a
code grid (in a body table OR a separate file) anywhere.

**13.10 Post-finalize decisions = "Decisions & open items"; no `decision-log.md`.**
The closing section is **Decisions & open items** (replacing "Open items /
Assumptions / Open Questions / Suggestions"): (a) **Decisions made** — a **three-column**
table `Topic | Decision | Reflected in (BR/R)` (no "decision-log ref" column); (b)
**Suggestions — dispositioned** — Accepted → `<R..>` / Won't do / Awaiting
confirmation; (c) **Open items** that do not block sign-off (blocking ones go to
Sign-off blockers). Internal codes (`A#`/`S#`) are **hidden from the displayed
tables**. **There is no separate `decision-log.md` file** — the dated history of
applied decisions/CRs lives in **Document control → Change history**, and the
decisions themselves in this section. (IDs still stay English and stable — 13.3.)

**13.11 Lean deliverable set; artifact index has a "Used when" column.**
`finalize`/`export` leave only this set in `clarify-output/`: the source
`brd.md`/`prd.md`, the HTML rendering `brd.html`/`prd.html`, `stories.md`,
`test-scenarios.md`, `api-data-impact.md`, `wireframes.html`, `audit-report.md`, and
the version archive `brd.v<semver>.md`/`prd.v<semver>.md`. Analysis that used to be
its own file is folded into the document and **no file is emitted** for it:
`edge-case-matrix.md` (→ edge section, 13.8), `error-handling.md` (→ error table,
13.8), `model-suggestions.md` (→ embedded flow diagrams), `traceability-matrix.md` (→
in-document, 13.9), `decision-log.md` (→ Decisions + Change history, 13.10),
`elicitation-pack.md` (→ Open items), and the `brd-draft.md` working draft (superseded
by the final). The Appendix **Artifact index** lists only the kept set above, each
with a **Used when (who / when)** column, and never links to a dropped file.

**13.12 Markdown→HTML: blank line between a label/paragraph and a table.**
Always leave **one blank line** between a bold label (e.g. `**Step-by-step**`) or any
paragraph text and a pipe table directly below it. Without it, pandoc folds the label
and the table into a single paragraph and the table breaks in the HTML render. Applies
everywhere a label or sentence precedes a table (step-by-step, screen matrix, symbol
table, glossary, requirements, artifact index, …). The `export` render must keep
pandoc's `header_attributes` on so the `{#err-f0n}` anchors survive (13.13 deep-links).

**13.13 Read-by-flow: one source of truth, diagram-then-steps, anchored links.**
A reader should understand a flow by reading **top to bottom within its block**, and
each fact should live in exactly **one** place.
- **Flow block order (per §8.x):** a one-line **Flow overview** (`Goal — …; Primary
  actor — …; Trigger — …; Outcome — …`) right after the heading → the **diagram(s)**
  (activity and/or sequence) → **Steps** → open notes.
- **Steps read the diagram, and sit BELOW it** (picture first, prose second). They
  explain the **sequence** diagram if the flow has one, else the **activity** diagram.
  The table is **three columns** `Step | Actor | Action / processing`; branch points
  are bullets (`• If … → …`). Steps carry **no** error codes and do **not** restate
  rules or screen behaviour — only the flow and its branches.
- **Steps end with one pointer line**, e.g. `Rules: BR.. (§7). Errors / messages /
  retry & tests: [§11.1 — F0n-Name](#err-f0n).` Links always target a **specific
  anchor / sub-header** (`#err-f0n`), never a vague "see the error table".
- **Single source of truth:** a rule lives in §Business rules (the flow only cites its
  `BR#`); an error / message / retry lives in the §Error code & message table (under
  its flow anchor); screen behaviour lives in §Screens; a step describes only the flow
  + branch points. No fact is duplicated across sections.
- **APIs are business-level** (`login()`, `code2Session()`), never path / method /
  header / schema. **§Data & systems impact is a table** — `Data concept | Business
  meaning | Created/Read/Written when | Source of truth | Sensitivity | Owner to
  confirm` — with the disclaimer that it is BA-altitude and does not replace a
  Technical Design / API Spec (no invented endpoint / schema / table / storage).
- **§Open items is a table** `Item | Impact if unresolved | Owner | Status | Deadline`
  so each unresolved item carries its consequence and a date.
Every `#err-f0n` link must have a matching header id (no broken deep-links).
