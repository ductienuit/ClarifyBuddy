# AGENTS.md — Clarify for Codex and other agents

Clarify is a **requirement-quality skill pack**, NOT a PRD generator. Use it to
audit, improve, score, and hand off software requirements. Never invent business
rules — label uncertain items `ASSUMPTION` or `OPEN QUESTION`.

## Trigger → workflow map

| If the user says… | Run workflow | Reads | Writes |
| --- | --- | --- | --- |
| "shape this idea", "draft a PRD/BRD from this idea" | `.clarify/workflows/from-idea.md` | the idea | `prd-draft.md` or `brd-draft.md` (with Document Profile), edge, error-handling, models when applicable |
| "analyze / break down this PRD or BRD", "make this build-ready" | `.clarify/workflows/from-spec.md` | existing PRD/BRD or resolved Clarify draft | audit, build-ready layer: api-data, stories, AC, tests, traceability; reuse edge/error/models when present |
| "audit this spec", "score these requirements", "how good is this spec" | `.clarify/workflows/audit.md` | the doc | `audit-report.md` |
| "improve the acceptance criteria / edge cases / clarity / diagrams …" | `.clarify/workflows/improve.md` | prior `clarify-output/` | overwrites the relevant file |
| "create the dev/QA handoff", "hand this off" | `.clarify/workflows/handoff.md` | prior `clarify-output/` | `handoff-pack.md` |
| "finalize the doc", "produce the final PRD/BRD", "we've confirmed, export it" | `.clarify/workflows/finalize.md` | prior `clarify-output/` | `final-prd.md` or `final-brd.md` |
| "make a review pack", "render the diagrams", "something I can open and review", "hand off to design" | `.clarify/workflows/export.md` | final doc + companions | `clarify-output/review-pack/` (HTML + diagrams + screens + HTML wireframes + traceability) |
| "where were we?", "what's left?", "status of the BRD" | `.clarify/workflows/status.md` | everything in `clarify-output/` | chat reply only (read-only) |
| "we have a change request", "what does this change affect?" | `.clarify/workflows/improve.md` (mode `change-request`) | traceability + catalogs | `change-impact.md` (analysis only) |

## Core files to read first

1. `.clarify/principles.md` — operating rules (always read first).
2. The selected workflow under `.clarify/workflows/`.
3. The engines that workflow names, under `.clarify/engine/`.
4. `.clarify/anti-patterns/anti-patterns.yaml` — detection (source of truth).
5. `.clarify/evaluators/scoring-rubric.yaml` +
   `requirement-quality-score.md` — scoring (source of truth + procedure).
6. `.clarify/output-conventions.md` — where to write outputs.

## Output style

- Write all artifacts to `clarify-output/` at repo root.
- Use the templates in `.clarify/templates/`.
- For audits: show total /100, band (cap at "Not ready for handoff" if any
  blocker), per-dimension table, findings grouped blocker/major/minor with each
  anti-pattern linked to a dimension and a concrete fix.
- When auditing a BRD/business draft from `from-idea`, score business draft
  readiness first. Missing stories, AC, tests, API/data impact, or traceability
  are optional build-ready layer gaps unless the user asked for Dev/QA handoff.
- Keep in-scope / out-of-scope / open questions separate.
- Analyze from every stakeholder perspective (operations, accounting,
  reconciliation, partners, risk, maintenance, data, security), not just user +
  system. Proactively add `SUGGESTION:` items for capabilities the feature +
  domain imply but the input omits — kept separate from confirmed scope.
- For models: emit a PlantUML activity diagram and a Mermaid sequence diagram as
  fenced code blocks, each followed by its viewer link (https://mermaid.live/ and
  the PlantUML server https://www.plantuml.com/plantuml, ref https://plantuml.com/).
- For wireframes: after screen/flow requirements are defined, `finalize` or
  `export` must render low-fidelity screen wireframes as an HTML visualization
  widget. If inline visualization is unavailable, write one self-contained
  `wireframes.html` file in the output directory. Use grayscale only, real BRD/PRD
  labels, placeholders marked `ASSUMPTION` where the doc is silent, one screen per
  key flow step, alternate/error screens only when specified, and trace every
  screen back to its source requirement / BRD or PRD section.
- After `from-idea`, tell the user to fill the Answer Sheet and run
  `improve answers` first. Do not position `from-spec` as required to make the
  BRD/PRD business-complete; it is optional for Dev/QA build-ready artifacts.
- `improve`, `handoff`, and `finalize` read prior outputs instead of re-deriving.
- `finalize` picks PRD vs BRD from the Document Profile (or `$ARGUMENTS`) and
  never stamps `Approved` while a blocker-level finding exists.

## Domain packs

Core is domain-agnostic and carries most of the value. A pack is an **optional
accelerator, not a gate** (Principle 12): auto-detect the domain, load a matching
pack from `.clarify/domain-packs/<pack>/` if one exists, otherwise proceed with
**labeled inference** (ASSUMPTION / SUGGESTION / OPEN QUESTION) — never force-fit a
wrong pack or block because none exists. Never hardcode domain logic into engines.

Keep this file consistent with `CLAUDE.md`.
