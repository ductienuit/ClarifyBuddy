# Changelog

All notable changes to Clarify are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added

- `/clarify:finalize [prd|brd]` — closing step that compiles confirmed outputs
  into a final, standard sign-off document (`final-prd.md` / `final-brd.md`) for
  a BA or PO. Includes document control, audit-score stamp, and a Sign-off
  blockers section.
- **Document Profile** (role BA/PO + target standard PRD/BRD) captured during
  `clarify` and carried through to `finalize`.
- `modeling` now emits a **PlantUML activity diagram** and a **Mermaid sequence
  diagram** as code blocks, each with a viewer link (https://mermaid.live/ /
  https://plantuml.com/). New `model-suggestions` template.
- New templates: `model-suggestions`, `final-prd`, `final-brd` (8 → 11).
- New `finalize` engine (13 → 14) and `finalize` workflow (5 → 6).
- `improve model` mode regenerates the diagrams.
- **Product/operational lenses** so specs are no longer user-flow-only. Five new
  anti-patterns (catalog 26 → 31): `missing-system-actor`,
  `missing-configuration-ownership`, `missing-effective-dating`,
  `missing-cohort-treatment`, `missing-batch-job-spec` — each mapped to an
  existing dimension (rubric weights unchanged, still sum 100).
- PRD template gains **System & External Actors**, **Configuration & Settings**,
  and **Scheduled Jobs / Batch** sections, plus effective-date/version and
  applies-to (new/existing/both) columns on Business Rules. Edge-case matrix gains
  temporal/rule-change and batch/schedule categories; acceptance-criteria template
  gains effective-date boundary, cohort/backfill, and scheduled-job blocks.
- Engines updated to prompt these lenses: clarify, shape, edge, risk, modeling,
  data, story, acceptance-criteria, write-prd.
- Domain packs gain `configurations.md`, `scheduled-operations.md`,
  `back-office-flows.md` (scaffold in `domain-pack-template`, filled in
  `fintech-mini` with a savings-deposit worked example: configurable effective-
  dated interest rate, Rate Administrator, daily interest-accrual job, GL/
  reconciliation consumers, grandfathering on a rate change).
- **Principle 10 — multi-stakeholder analysis:** every write/analysis walks
  operations, accounting, reconciliation, partners, risk, maintenance, data, and
  security perspectives, not just user + system. New PRD "Stakeholder
  Perspectives" section + audit "Stakeholder coverage"; clarify/write-prd/audit
  checklist updated.
- **Principle 11 — proactive completeness:** Clarify proposes the additional
  capabilities a complete product needs (config/admin, reconciliation, reporting,
  jobs…) as labeled `SUGGESTION:` items, grounded in the domain pack, kept
  separate from confirmed scope (does not override "never invent business rules").
  New "Suggested Additional Capabilities" sections in the PRD, final PRD/BRD, and
  audit-report templates.
- **BRD vs PRD at draft stage (altitude fix):** `from-idea` now picks the template
  by the Document Profile — new `brd-draft-template.md` (title "BRD Draft", output
  `brd-draft.md`, business altitude with a "Downstream Technical Notes (for
  PRD/SRS)" section) vs `prd-template.md` (PRD). Fixes the bug where a BRD-profile
  run produced a "PRD Draft". Deep technical mechanics (idempotency keys, batch
  resume, ledger internals) are kept but lowered to downstream notes in BRD — no
  lens is dropped. Templates 11 → 12. `shape`/`write-prd`/`finalize`/`improve`
  read/write the correct draft file.
- **User guide redesigned to production grade** — `docs/index.html` rebuilt on a
  committed design system (PRODUCT.md + DESIGN.md added): ink-blue drench hero
  with an Answer Sheet facsimile, Literata + Be Vietnam Pro (Vietnamese subsets,
  offline fallbacks), divided feature list instead of card grids, 6-step pipeline
  (horizontal → vertical rail on mobile), in-container scrolling tables (zero page
  horizontal scroll at 375/768/1280 — verified by screenshot), enhance-only
  reveals honoring `prefers-reduced-motion`, and the skill's own wireframe
  language as imagery. Fixed journey-step grid collapse, variant-table squeeze,
  and install code overflow found during in-browser inspection.
- **User guide landing page** — `docs/index.html`: a self-contained static page
  (Vietnamese, no external dependencies) for BA/PO users: what Clarify is, install
  for Claude Desktop / Claude Code, the end-to-end journey with a worked
  savings-deposit example (questions → Variant Matrix → Answer Sheet → finalize →
  review pack), core concepts (Document Profile, A/Q/S/V labels, scoring bands,
  anti-patterns, traceability), output catalog, command cheat-sheet, and FAQ.
  Linked from README. Not bundled into the skill zips (documentation only).
- **Hardening: invariant lint + deterministic helpers.** New `lint-skill.ps1`
  (dev-time) verifies every count/sync invariant — doc counts vs filesystem,
  anti-pattern yaml↔md sync, rubric dimensions + weights sum, referenced
  templates/workflows/engines exist, eval ids, detect keys — and `build-skill.ps1`
  now runs it first (refuses to package on violations; `-SkipLint` to bypass).
  New bundled `.clarify/scripts/clarify_tools.py` (stdlib Python) does the
  mechanical parts of four steps — `status` (inventory + outstanding A/Q/S/V),
  `answers` (parse Answer Sheet + append decision-log), `integrity` (dangling-ID
  scan), `manifest` (verify review-pack entries on disk) — wired into the
  status/improve/trace/export prompts with a mandatory manual fallback when
  Python is unavailable. No architecture/count changes (scripts are neither
  engines nor templates).
- **Senior-BA workflow layer (UX + governance + skill QA).**
  *UX:* new read-only `/clarify:status` (8th command — artifact inventory,
  Document Profile, unresolved A/Q/S/V + blockers, recommended next step);
  Document Profile gains **Language** (all output renders in the user's language;
  ASSUMPTION/OPEN QUESTION/SUGGESTION labels + IDs stay English as parse anchors);
  every question carries an elicitation owner (`→ ask: <stakeholder>`) and a new
  `elicitation-pack.md` regroups questions per stakeholder for workshops.
  *Governance:* `improve answers` appends applied decisions to an append-only
  `decision-log.md`; `finalize` never overwrites silently (archives
  `final-*.v<N>.md`, bumps Version, adds a Change history row — new table in both
  final templates); new `improve change-request` mode produces `change-impact.md`
  (CR impact walked from the traceability chain; analysis only).
  *Skill QA:* `trace` gains a referential-integrity check (dangling BR/F/S/CODE
  references reported, counted against `traceability`); new golden eval
  `weak-brd-savings(.expected).md` covering anti-patterns 27–36.
  Counts: commands 7→8, workflows 7→8, templates 19→22 (elicitation-pack,
  decision-log, change-impact), skills 8→9 zips; engines stay 16, anti-patterns
  stay 36.
- **Wireframes are HTML-first (no more ASCII).** Low-fi wireframes now render as a
  grayscale HTML widget (phone/card frames numbered ① ② ③ in flow order, real
  labels from the BRD/PRD, error regions mapped to error codes, ASSUMPTION badges
  where the doc is silent, source footer per screen) — emitted by `finalize`
  (inline widget or self-contained `clarify-output/wireframes.html`) and by
  `export` (embedded in `index.html` + standalone `screens/wireframes.html`).
  `wireframe-template.md` (ASCII) replaced by `wireframe-template.html`; the
  review-pack template gained the wireframe CSS + sample markup.
- **`/clarify:export` — Visual Review Pack (new 7th command).** Packages a derived,
  openable review artifact under `clarify-output/review-pack/` so BA/PO/Design/Dev/QA
  review without copying diagram code into plantuml.com / mermaid.live. Phase 1: a
  self-contained `index.html` (sidebar nav; **Mermaid renders client-side** — no data
  leaves the machine; PlantUML rendered or code+link with a status badge) + `manifest.json`
  + artifact index. Phase 2: screen inventory + screen-flow + **low-fi HTML
  wireframes** (inline widget in `index.html` plus self-contained
  `screens/wireframes.html`, derive-only from Screen Matrix + flow steps + rules +
  error map + state; stamped "not final UI"; unknowns → ASSUMPTION / OPEN QUESTION;
  no ASCII primary wireframes). Phase 3: best-effort static SVG render
  (local-first) + `index-offline.html`. Phase 4: optional `signoff-pack.pdf/.docx` from
  rendered images. Fallback-first (pack always opens; render status in the manifest);
  composes from the final doc and never invents; the final doc stays source of truth.
  New `export` engine + workflow + command + `clarify-export` skill, and templates
  `review-pack-template.html`, `review-manifest-template.json`,
  `screen-inventory/wireframe/traceability-map/review-checklist` (engines 15→16,
  templates 13→19, commands 6→7, skills 7→8 zips).
- **Final BRD/PRD polished into a build-ready package:** BRD gains an Executive
  summary and Scope-before-Stakeholders (PRD already had both); Assumptions / Open
  Questions / Suggestions grouped into a §14 "Open items" cluster with blockers in
  §15. Error mapping gains a **Flow / Step** column (synced in `error-handling`
  engine + template + draft summaries); the State summary gains **trigger / owner /
  terminal** columns (synced in `model-suggestions`); Traceability expands to
  **Req → Flow → Business rule → Error/State → Story → AC → Test** (synced in
  `trace` engine + audit checklist). Both final templates get an **Appendix:
  Generated artifacts** that indexes only the real `clarify-output/` files (diagram
  source + viewer links — no fabricated `*.svg`/wireframe references). `finalize`
  composes the Executive summary and artifact index; data→tables and NFR→table were
  intentionally left out of this pass. No anti-pattern/engine/template count change.
- **Process-centric Functional Flows (§7):** fixed the bug where the activity
  (PlantUML) and sequence (Mermaid) diagrams were two separate sections of
  different processes, breaking the reading flow. §7 is now "Functional Flows
  (process-centric)" in both BRD and PRD final templates: a Flow Catalog, then one
  block per business process keeping step-by-step + activity + sequence for the
  SAME process, with the Screen / Display Matrix placed **after** the flows.
  `model-suggestions` template and `modeling` engine reorganized the same way;
  `from-spec`/`improve model` produce per-process pairs (from-idea stays
  discovery-level); `finalize` re-renders per process and emits an `OPEN QUESTION`
  for any missing key-process diagram instead of pairing unrelated diagrams. Fixed
  tool conventions (activity=PlantUML/plantuml.com, sequence & state=Mermaid/
  mermaid.live). New anti-pattern `mixed-process-diagram-block` (clarity); clarity
  rubric anchor and audit checklist reward process-centric structure. Traceability
  gains a `Flow` column and flags orphan flows. Catalog 35 → 36.
- **Fixed misleading next-step after `from-idea`:** it no longer tells the user to
  run `from-spec` "from scratch". `from-idea` and `from-spec` are sibling entry
  points; the immediate next step after a draft is `improve answers` (apply the
  Answer Sheet). `from-spec` is optional (build-ready stories/AC/tests/API/
  traceability + score) and now **reuses** the draft's edge/error/model instead of
  regenerating them (composability). Path: from-idea → improve answers → (optional
  from-spec) → handoff/finalize.
- **`from-idea` now generates full artifacts:** engine sequence is
  `clarify → shape → risk → edge → error-handling → modeling → write-prd`, so a
  thin idea produces `error-handling.md` and `model-suggestions.md` (with entity vs
  transaction/operation state) — not just an in-draft summary. Thin input yields
  `OPEN QUESTION` rows rather than skipped artifacts.
- **Two anti-patterns added (33 → 35):** `missing-operation-state` (edge-coverage)
  for flows that define only an entity lifecycle but omit the transaction/operation
  lifecycle, and `technical-jargon-in-business-requirement` (clarity) for BRD bodies
  that overuse implementation/accounting terms.
- **BRD readability + Customer Journey + Screens:** BRD requirements must be written
  in business language (jargon like ledger/GL/accrual/idempotency/cohort goes to
  Downstream Technical Notes, not the body). Draft templates gain an end-to-end
  **Customer Journey** and a **Screen / Information Display** section; `shape`/
  `write-prd` produce them.
- **Error Handling & Message Mapping (new engine + template):** new `error-handling`
  engine (engines 14 → 15) and `error-handling-template.md` (templates 12 → 13) map
  each failure → code → transaction status → internal message → **user-facing
  message** → retryable → action → needs-ops. Wired into `from-spec` and the QA
  handoff. New anti-pattern `missing-error-message-mapping`. `edge` now includes
  user-facing failures.
- **Authentication step + dual state model:** `risk` requires step-up auth
  (OTP/PIN/biometric) + confirmation for sensitive/financial actions with failure
  handling (new anti-pattern `missing-authentication-step`); `modeling` distinguishes
  the **transaction/operation** state machine from the **entity** state machine.
- Anti-pattern catalog 31 → 33.
- **Numbered, answerable labels + Answer Sheet:** assumptions/open questions/
  suggestions/variants now carry stable IDs (`A#`/`Q#`/`S#`/`V#`) and each draft &
  audit report ends with a copyable ```text **Answer Sheet** the user fills in-place
  and sends back. New `improve answers` mode ingests a filled sheet and applies it
  by ID (override assumption, resolve open question → confirmed rule/scope, accept
  suggestion, fix variant). Convention documented in `output-conventions.md`.
- **Smarter clarify for thin input:** lead with the 5 highest-impact,
  scope-blocking questions (channel, variant/type, segment, lifecycle ops, depth)
  and proactively emit a **Variant / Options Matrix** for the user to select,
  instead of only asking. New matrix section in clarify output and both draft
  templates.
- **Principle 12 — domain pack optional, infer-and-label:** packs are accelerators,
  not gates. Clarify auto-detects the domain, loads a matching pack if one exists,
  else proceeds with **labeled inference** (ASSUMPTION/SUGGESTION/OPEN QUESTION) —
  never force-fitting a wrong pack or blocking on a missing one. Document Profile
  now records the domain mode (`pack: <name>` vs `inferred (no pack)`). Wired into
  `clarify`, the from-idea/from-spec/audit workflows, and the domain-packs README.
  Core principles 9 → 12.

### Changed

- Renamed `/clarify:from-prd` → `/clarify:from-spec`; it now accepts a PRD
  **or** a BRD as input. Command count 5 → 6.
- `finalize` can emit a BRD document; standalone `write-brd` / `write-srs`
  (generate-from-scratch) engines remain deferred to v1.1.

## [0.1.0] - 2026-05-23

### Added

- MVP 1 of the Clarify requirement-quality skill pack.
- 5 namespaced slash commands: `from-idea`, `from-prd`, `audit`, `improve`,
  `handoff`.
- 13 engines, 8 templates, 5 workflows.
- 26-entry anti-pattern catalog (yaml source of truth + human-readable catalog).
- Reproducible 100-point / 10-dimension scoring rubric with full/half/zero
  anchors and band thresholds.
- Anti-pattern → dimension deduction model.
- `domain-pack-template` plus 3 mini packs: ecommerce, saas-b2b, fintech.
- Golden eval tests (`weak-prd-checkout`, `weak-prd-roles`).
- 4 worked examples.
- `CLAUDE.md` and `AGENTS.md` adapters.

### Notes

- `write-brd` and `write-srs` deferred to v1.1.
- `flow` + `sequence` + `state` merged into a single `modeling` engine.
