# CLAUDE.md — Clarify

Project context for Claude Code working in this repository.

## What this repo is

Clarify is an **agent-native requirement-quality skill pack**, NOT a PRD
generator. It turns rough ideas and weak PRDs into clear, testable, traceable,
handoff-ready specs and **scores** their quality against a reproducible rubric.

## The 8 commands (namespaced `clarify:`)

Defined in `.claude/commands/clarify/`:

- `/clarify:from-idea [idea|path]` — shape an idea into a business/product-ready
  PRD/BRD draft; captures the Document Profile plus journey, screen matrix,
  business rules, exceptions, error messages, and state summary.
- `/clarify:from-spec [path]` — optional Dev/QA build-ready elaboration for an
  existing PRD/BRD or resolved Clarify draft: audit score, stories, AC, tests,
  API/data impact, traceability. (Renamed from `from-prd`.)
- `/clarify:audit [path]` — score + findings only.
- `/clarify:improve [mode]` — upgrade one section from prior output
  (`answers` resolves the Answer Sheet after `from-idea`; `model` regenerates the
  diagrams).
- `/clarify:handoff` — emit Dev + QA packs from prior output.
- `/clarify:finalize [prd|brd]` — closing step: compile confirmed outputs into the
  standard sign-off document `brd.md`/`prd.md` (PRD or BRD per the Document Profile;
  **never named "final-…"**, Principle 13.1).
- `/clarify:export [html|all|offline]` — render the sign-off doc as **one full HTML
  BRD/PRD** `clarify-output/brd.html` **from `brd.md`** (one source of truth):
  client-side Mermaid + PlantUML (plantuml.com hex `~h` + code fallback), requirement
  group-bands as `colspan` banded tables, a TOC, low-fi HTML wireframes, an artifact
  index, and a LibreOffice docx round-trip. Best-effort with fallback; never invents;
  no tool labels in displayed content.
- `/clarify:status` — read-only: artifact inventory, Document Profile, unresolved
  A/Q/S/V counts + blockers, and the recommended next step. Writes no files.

## Core principles (see `.clarify/principles.md`)

1. Quality over generation — improve and score, don't fabricate.
2. **Never invent business rules** — label `ASSUMPTION` / `OPEN QUESTION`.
3. Separate in-scope / out-of-scope / open questions.
4. Testable, build-ready wording (actor + trigger + outcome; Given/When/Then).
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
13. Document presentation & naming conventions — the default for from-idea,
    finalize, and export: (13.1) output is `brd.md`/`prd.md`, **never "final-…"**,
    archive `brd.v<semver>.md`; (13.2) the HTML is a full BRD/PRD rendered from
    `brd.md` (pandoc + client-side Mermaid + PlantUML hex `~h`, requirement
    group-bands → `colspan`, TOC + artifact index, LibreOffice docx round-trip; no
    tool labels) — not a "review pack"; (13.3) headings render `Vietnamese (English)`
    when Language=vi, machine anchors always English; (13.4) a §0 "How to read"
    (intro + symbol table + front glossary); (13.5) a "How the system works
    (overview)" before requirements; (13.6) flows named `F0n-Name` (stable number,
    appended name); (13.7) requirements are ONE grouped table (`ID | Requirement |
    Why | Priority`), with flow/rule/test/source moved to Traceability (+Source).
    Scored under `clarity`/structure.

## Where things live

- `.clarify/workflows/` — ordered engine sequences per command.
- `.clarify/engine/` — 16 imperative engines (clarify, shape, write-prd, edge,
  error-handling, risk, modeling, data, api, story, acceptance-criteria, test,
  trace, handoff, finalize, export). `modeling` emits a PlantUML activity diagram +
  a Mermaid sequence diagram, each with a viewer link; `export` packages the Visual
  Review Pack.
- `.clarify/templates/` — 22 output shapes (incl. brd-draft, error-handling,
  model-suggestions, final-prd, final-brd, elicitation-pack, decision-log,
  change-impact, and the review-pack set: `review-pack-template.html`,
  `review-manifest-template.json`, `screen-inventory-template`,
  `wireframe-template.html`, `traceability-map-template`,
  `review-checklist-template`). The draft stage picks `prd-template` (PRD) or
  `brd-draft-template` (BRD) by the Document Profile; BRD keeps deep technical
  mechanics under a "Downstream Technical Notes" section (altitude by standard).
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
  `status`, `answers`, `integrity`, `manifest`), bundled in every zip. Engines
  prefer them but ALWAYS fall back to the manual checklist when Python is absent.
- `lint-skill.ps1` (repo root, dev-time) — checks every count/sync invariant;
  `build-skill.ps1` runs it first and refuses to package on violations
  (`-SkipLint` to bypass).

## Output convention

All artifacts go to `clarify-output/` at repo root (see
`.clarify/output-conventions.md`). `improve`, `handoff`, `finalize`, and `export`
READ prior outputs rather than re-deriving. `finalize` writes `brd.md`/`prd.md`;
`export` renders `brd.html` **from** that Markdown and never edits the master.

Recommended flows:
- Business sign-off from idea: `from-idea` → `improve answers` → `finalize brd`
  → optional `export` (HTML BRD for stakeholders/design).
- Dev/QA handoff: `from-idea` → `improve answers` → optional `from-spec` →
  `handoff` → optional `export`.
- Existing document: `from-spec` when build-ready elaboration is needed, or
  `audit` when score/findings only are needed.
- Returning to a project / "what's left?": `status` (read-only).
- After sign-off, a change arrives: `improve change-request` (impact analysis) →
  apply via the relevant improve mode → `finalize` (version bump + Change history).

Governance conventions: the Document Profile carries a **Language** (output
renders in it; ASSUMPTION/OPEN QUESTION/SUGGESTION labels and all IDs stay
English as parse anchors); questions carry an elicitation owner (`→ ask:
<stakeholder>`) and are regrouped per owner in `elicitation-pack.md`; applied
decisions append to `decision-log.md`; `finalize` never overwrites silently
(archives `brd.v<N>.md`/`prd.v<N>.md`, bumps Version, adds a Change history row);
`trace` reports dangling ID references.

## Build/scope notes

- MVP 1: no web app, no CLI binary, no Jira/Confluence integration.
- `finalize` can emit a final **BRD or PRD** document by compiling confirmed
  outputs. It does not require `from-spec` artifacts for business sign-off; missing
  stories/AC/tests/API/traceability are optional build-ready layer inputs unless
  handoff readiness is requested. Standalone `write-brd` / `write-srs` engines
  (generate-from-scratch) remain deferred to v1.1.
- Anti-pattern count is exactly **36**. Keep the yaml and the catalog in sync.
- The PRD template carries product/operational lenses: System & External Actors,
  Configuration & Settings, Scheduled Jobs / Batch, and effective-date/cohort
  columns on Business Rules. Keep engine prompts and these sections aligned.
- **Functional Flows are process-centric** (one section title everywhere:
  "Functional Flows (process-centric)"): a Flow Catalog, then one block per
  business process with step-by-step + PlantUML activity + Mermaid sequence for the
  SAME process, then the Screen Matrix. Never mix two processes' diagrams in one
  block (`mixed-process-diagram-block`). Tools are fixed: activity=PlantUML,
  sequence=Mermaid, state=Mermaid. Traceability has a `Flow` column; orphan flows
  are flagged.
- **Wireframes are HTML-first:** after screen/flow requirements exist, `finalize`
  or `export` renders low-fi grayscale wireframes as an inline HTML widget, or as
  one self-contained `wireframes.html` file if inline HTML is unavailable. Use real
  labels from the BRD/PRD, mark placeholders `ASSUMPTION`, never invent fields or
  business rules, avoid ASCII wireframes as the primary artifact, and trace every
  screen to its source flow/step and requirement.
