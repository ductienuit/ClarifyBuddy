# CLAUDE.md — Clarify

Project context for Claude Code working in this repository.

## What this repo is

Clarify is an **agent-native requirement-quality skill pack**, NOT a PRD
generator. It turns rough ideas into a clear, testable, traceable **URD (User
Requirements Document)** in the **URD template** shape, and **scores** its quality
against a reproducible rubric. URD is the single document standard — there is no
BRD/PRD path.

## The 6 commands (namespaced `clarify:`)

Defined in `.claude/commands/clarify/`:

- `/clarify:from-idea [idea|path]` — shape an idea into a **URD draft**; captures the
  Document Profile plus journey, user stories, screen matrix & field specs, business
  rules, exceptions, error messages, and state model.
- `/clarify:improve [mode]` — resolve the Answer Sheet (`answers`) or upgrade one
  section (`model` regenerates the Mermaid diagrams; `change-request` analyzes CR
  impact). Modes: answers, change-request, clarity, scope, business-rules, edge,
  stories, acceptance-criteria, risk, traceability, nfr, model.
- `/clarify:audit [path]` — score + findings only.
- `/clarify:finalize [md|html|word|all]` — closing step: compile confirmed outputs into
  the sign-off URD `urd.md` (**never named "final-…"**, Principle 13.1) and render
  `urd.html` (default); `word`/`all` also produce `urd.docx`.
- `/clarify:export [html|word|offline|all]` — render the sign-off doc as **one full HTML
  URD** `clarify-output/urd.html` **from `urd.md`** (one source of truth): client-side
  Mermaid (no PlantUML), banded tables via `colspan`, a TOC, low-fi HTML wireframes, an
  artifact index, and an optional LibreOffice `urd.docx`. Best-effort with fallback;
  never invents; no tool labels in displayed content.
- `/clarify:status` — read-only: artifact inventory, Document Profile, unresolved
  A/Q/S/V counts + blockers, and the recommended next step. Writes no files.

## Core principles (see `.clarify/principles.md`)

1. Quality over generation — improve and score, don't fabricate.
2. **Never invent business rules** — label `ASSUMPTION` / `OPEN QUESTION`.
3. Separate in-scope / out-of-scope / open questions.
4. Testable, build-ready wording (actor + trigger + outcome; acceptance criteria).
5. Always surface edge cases and handoff risk.
6. Traceability both directions.
7. Reproducible scoring — show the math.
8. Don't hard-block on clarification.
9. Domain-agnostic core; domain logic only in domain packs.
10. Analyze from every stakeholder perspective (operations, accounting,
    reconciliation, partners, risk, maintenance, data, security) — not just
    user + system.
11. Proactively propose completeness as labeled `SUGGESTION:` items (additional
    capabilities the feature + domain imply), never as confirmed requirements.
12. Domain pack is an optional accelerator, not a gate — auto-detect the domain,
    load a matching pack if any, else proceed with **labeled inference** (never
    force-fit a wrong pack or block on a missing one).
13. Document presentation & naming conventions (URD template) — the default for
    from-idea, finalize, and export: (13.1) output is `urd.md`, **never "final-…"**,
    archive `urd.v<semver>.md`, renderings `urd.html`/`urd.docx`; (13.2) the HTML/Word
    are a full URD rendered from `urd.md` (pandoc + navy skin + client-side Mermaid,
    **no PlantUML**, banded tables → `colspan`, TOC + artifact index, LibreOffice docx;
    no tool labels) — not a "review pack"; (13.3) headings render `Tiếng Việt (English)`
    when Language=vi (default), machine anchors always English; (13.4) the URD skeleton
    (cover → §1–§5, diagram conventions, §3 repeating per process); (13.5) §3 is a
    capability-repeating block (3.1 desc · 3.2 user stories · 3.3 sequence · 3.4 state ·
    3.5 rules · 3.6 screens · 3.7 errors · 3.8 NFR); (13.6) flows named `F0n-Name`
    (stable number, appended name); (13.7) user stories table (`ID | Là | Tôi muốn | Để |
    Tiêu chí chấp nhận`); (13.8) errors in §3.7 (`Trường hợp/Mã | Điều kiện | Thông báo
    VN | EN | Xử lý`) and the whole edge analysis in-document; (13.9) diagrams are
    Mermaid-only (sequence autonumber/no-color + colored state) and traceability is
    in-document — **no `traceability-matrix.md` file**; (13.10) open questions
    consolidated in §5, decisions in Lịch sử thay đổi — **no `decision-log.md` file**;
    (13.11) lean deliverable set (`urd.md`/`urd.html`/`urd.docx`, wireframes,
    audit-report, version archive) with a "Dùng khi" artifact index — user-stories/
    edge/error/model/traceability/decision-log/elicitation are folded into the doc, not
    emitted; (13.12) a blank line between any label/paragraph and a following table;
    (13.13) screen field specs + one-source-of-truth + BA altitude. Scored under
    `clarity`/structure.

## Where things live

- `.clarify/workflows/` — ordered engine sequences per command.
- `.clarify/engine/` — 12 imperative engines (clarify, shape, write-urd, edge,
  error-handling, risk, modeling, story, acceptance-criteria, trace, finalize, export).
  `modeling` emits a Mermaid sequence diagram (§3.3) + a colored Mermaid state diagram
  (§3.4), each with a viewer link; `finalize`/`export` render the URD HTML/Word.
- `.clarify/templates/` — 13 output shapes (incl. `urd-draft-template`,
  `final-urd-template`, `urd-pack-template.html`, error-handling, model-suggestions,
  user-story, acceptance-criteria, edge-case-matrix, elicitation-pack, decision-log,
  change-impact, audit-report, `wireframe-template.html`). `from-idea` writes the
  `urd-draft`; `finalize` composes the `final-urd`.
- `.clarify/anti-patterns/anti-patterns.yaml` — **source of truth** for the 36
  anti-patterns (`.md` is the human rendering).
- `.clarify/evaluators/scoring-rubric.yaml` — **source of truth** for scoring;
  `requirement-quality-score.md` defines the procedure and AP→dimension model.
- `.clarify/domain-packs/` — **optional accelerator** (Principle 12): auto-detect
  domain → load matching pack, else labeled inference (never force-fit/block). A
  full pack also has `configurations.md`, `scheduled-operations.md`,
  `back-office-flows.md` (config / batch-job / back-office lenses); filled for
  `fintech-mini` + template.
- `.clarify/eval/` — golden tests for the skill itself.
- `.clarify/scripts/clarify_tools.py` — deterministic helpers (stdlib Python:
  `status`, `answers`, `integrity`), bundled in every zip. Engines prefer them but
  ALWAYS fall back to the manual checklist when Python is absent.
- `lint-skill.ps1` (repo root, dev-time) — checks every count/sync invariant;
  `build-skill.ps1` runs it first and refuses to package on violations
  (`-SkipLint` to bypass).

## Output convention

All artifacts go to `clarify-output/` at repo root (see
`.clarify/output-conventions.md`). `improve`, `finalize`, and `export` READ prior
outputs rather than re-deriving. `finalize` writes `urd.md`; `export` renders
`urd.html` (and `urd.docx` on request) **from** that Markdown and never edits the
master.

Recommended flows:
- Sign-off from idea: `from-idea` → `improve answers` → `finalize` (`urd.md` +
  `urd.html`) → optional `finalize word` / `export word` for `urd.docx`.
- Score only: `audit`.
- Returning to a project / "what's left?": `status` (read-only).
- After sign-off, a change arrives: `improve change-request` (impact analysis) →
  apply via the relevant improve mode → `finalize` (version bump + Lịch sử thay đổi).

Governance conventions: the Document Profile carries a **Language** (default `vi`;
output renders in it; ASSUMPTION/OPEN QUESTION/SUGGESTION labels and all IDs stay
English as parse anchors); questions carry an elicitation owner (`→ ask:
<stakeholder>`) and are consolidated in §5; applied decisions are recorded in the
doc's **Decisions made** table + **Lịch sử thay đổi** (no `decision-log.md`);
`finalize` never overwrites silently (archives `urd.v<N>.md`, bumps Version, adds a
Change history row); `trace` verifies in-document traceability and reports dangling ID
references (no separate matrix file).

## Build/scope notes

- MVP 1: no web app, no CLI binary, no Jira/Confluence integration.
- `finalize` compiles the sign-off URD from confirmed outputs; it does not require
  any separate build-ready layer. Higher-fidelity native Word export is deferred to
  v1.1 (current Word is a LibreOffice round-trip).
- Anti-pattern count is exactly **36**. Keep the yaml and the catalog in sync.
- **§3 is capability-repeating and process-centric** (one block per business process):
  3.1 description, 3.2 user stories, 3.3 Mermaid sequence + steps, 3.4 colored Mermaid
  state + table, 3.5 rules, 3.6 screens & field specs, 3.7 errors, 3.8 NFR. Never mix
  two processes' diagrams in one block (`mixed-process-diagram-block`). Diagrams are
  **Mermaid-only** (sequence + state); **no PlantUML**. Traceability is in-document
  (User stories ↔ Flow Catalog ↔ rules ↔ errors); orphan flows are flagged.
- **Wireframes are HTML-first:** after screen/flow requirements exist, `finalize`
  or `export` renders low-fi grayscale wireframes as an inline HTML widget, or as
  one self-contained `wireframes.html` file if inline HTML is unavailable. Use real
  labels from the URD, mark placeholders `ASSUMPTION`, never invent fields or
  business rules, avoid ASCII wireframes as the primary artifact, and trace every
  screen to its source flow/step and user story.
