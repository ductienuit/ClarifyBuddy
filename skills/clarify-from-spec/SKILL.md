---
name: clarify-from-spec
description: >-
  Clarify · From-Spec — analyze an existing spec (a PRD OR a BRD) or optionally
  elaborate a resolved Clarify draft into Dev/QA build-ready artifacts. Use when
  the user has a written document and wants it scored, or wants stories,
  acceptance criteria, tests, API/data impact, and traceability. Never invents
  business rules — labels them ASSUMPTION or OPEN QUESTION. Part of the Clarify
  requirement-quality pack.
---

# Clarify: From-Spec

Audit and elaborate an existing PRD or BRD into build-ready artifacts. After
`clarify-from-idea`, this is optional and should be used only when the user wants
Dev/QA handoff readiness.

## Steps
1. Read `.clarify/principles.md`.
2. Establish the **Document Profile** (BA/PO + target standard PRD/BRD); detect
   from the input or ask (default BA→BRD, PO→PRD as ASSUMPTION).
3. Run the workflow `.clarify/workflows/from-spec.md` (engines: audit → edge →
   error-handling → modeling → data → api → story → acceptance-criteria → test →
   trace).
4. Write artifacts per `.clarify/output-conventions.md`: the build-ready companions
   `audit-report.md`, `api-data-impact.md`, `stories.md`, `test-scenarios.md`, and
   fold the edge / error / model / flow / state / traceability analysis **into the
   draft** (`brd-draft.md` / `prd-draft.md`). No separate edge-case-matrix /
   error-handling / model-suggestions / traceability-matrix files (Principle 13.11).

## Rules
- Accepts a PRD **or** a BRD — including a Clarify draft already in
  `clarify-output/` (`prd-draft.md` / `brd-draft.md`). If the draft already carries
  its edge / error / model / state sections, **reuse** them and add only the
  build-ready layer (audit score, stories, AC, tests, API/data, in-document
  traceability) — do not regenerate from scratch or re-emit dropped files.
- Detect or ask the target standard — never assume it.
- Do not describe this as required to make a `from-idea` BRD readable or
  business-complete.
- `modeling` emits a PlantUML activity diagram + a Mermaid sequence diagram, each
  with a viewer link (https://mermaid.live/ · https://www.plantuml.com/plantuml).
- Scoring: total /100, band, per-dimension table, findings grouped
  blocker/major/minor with concrete fixes; any blocker caps the band.
- When done, suggest **clarify-handoff** and **clarify-finalize** as next steps.
