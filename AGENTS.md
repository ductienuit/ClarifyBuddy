# AGENTS.md — Clarify for Codex and other agents

Clarify is a **requirement-quality skill pack**, NOT a PRD generator. Use it to
shape, audit, improve, score, and finalize software requirements into a **URD (User
Requirements Document)** in the URD template shape. Never invent business rules —
label uncertain items `ASSUMPTION` or `OPEN QUESTION`.

## Trigger → workflow map

| If the user says… | Run workflow | Reads | Writes |
| --- | --- | --- | --- |
| "shape this idea", "draft a URD from this idea" | `.clarify/workflows/from-idea.md` | the idea | `urd-draft.md` (with Document Profile; user stories / edge / error / model folded in) |
| "audit this spec", "score these requirements", "how good is this spec" | `.clarify/workflows/audit.md` | the doc | `audit-report.md` |
| "improve the acceptance criteria / edge cases / clarity / diagrams …", "apply my answers" | `.clarify/workflows/improve.md` | prior `clarify-output/` | overwrites the relevant file |
| "finalize the doc", "produce the URD", "we've confirmed, export it" | `.clarify/workflows/finalize.md` | prior `clarify-output/` | `urd.md` (never "final-…") + `urd.html`; `urd.docx` on word/all |
| "make the HTML version", "render the diagrams", "Word-export", "hand off to design" | `.clarify/workflows/export.md` | `urd.md` | `clarify-output/urd.html` (full HTML URD from the Markdown), `urd.docx` on word |
| "where were we?", "what's left?", "status of the URD" | `.clarify/workflows/status.md` | everything in `clarify-output/` | chat reply only (read-only) |
| "we have a change request", "what does this change affect?" | `.clarify/workflows/improve.md` (mode `change-request`) | in-document trace spine | `change-impact.md` (analysis only) |

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
- Keep in-scope / out-of-scope / open questions separate.
- Analyze from every stakeholder perspective (operations, accounting,
  reconciliation, partners, risk, maintenance, data, security), not just user +
  system. Proactively add `SUGGESTION:` items for capabilities the feature +
  domain imply but the input omits — kept separate from confirmed scope.
- For models: emit **Mermaid only** — a `sequenceDiagram` (autonumber, no color)
  for §3.3 and a colored `stateDiagram-v2` for §3.4, each followed by its viewer
  link (https://mermaid.live/). No PlantUML.
- For wireframes: after screen/flow requirements are defined, `finalize` or
  `export` must render low-fidelity screen wireframes as an HTML visualization
  widget. If inline visualization is unavailable, write one self-contained
  `wireframes.html` file in the output directory. Use grayscale only, real URD
  labels, placeholders marked `ASSUMPTION` where the doc is silent, one screen per
  key flow step, alternate/error screens only when specified, and trace every
  screen back to its source flow/step and user story.
- After `from-idea`, tell the user to fill the Answer Sheet and run
  `improve answers`, then `finalize` to produce the URD.
- `improve` and `finalize` read prior outputs instead of re-deriving.
- `finalize` composes the URD from confirmed outputs and never stamps `Đã duyệt`
  (Approved) while a blocker-level finding exists. Headings render bilingual
  `Tiếng Việt (English)` when Language=vi (default); IDs/codes stay English.

## Domain packs

Core is domain-agnostic and carries most of the value. A pack is an **optional
accelerator, not a gate** (Principle 12): auto-detect the domain, load a matching
pack from `.clarify/domain-packs/<pack>/` if one exists, otherwise proceed with
**labeled inference** (ASSUMPTION / SUGGESTION / OPEN QUESTION) — never force-fit a
wrong pack or block because none exists. Never hardcode domain logic into engines.

Keep this file consistent with `CLAUDE.md`.
