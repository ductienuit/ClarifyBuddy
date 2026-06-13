---
name: clarify-finalize
description: >-
  Clarify · Finalize — the closing step. Compile confirmed Clarify outputs into a
  final, standard sign-off document: a PRD or a BRD for a BA/PO. Use when the user
  says the spec is confirmed and wants the final deliverable ("produce the final
  PRD/BRD", "finalize as BRD", "export the sign-off doc"). Includes a document
  control block, an audit score/band stamp when available, embedded
  PlantUML/Mermaid diagrams with viewer links, Customer/User Journey, Screen
  Information / Display Matrix, Error Handling & Message Mapping, optional
  traceability summary, and a Sign-off blockers section.
  Part of the Clarify requirement-quality pack.
---

# Clarify: Finalize

Compile prior Clarify outputs into a final PRD or BRD for sign-off.

## Steps
1. Read `.clarify/principles.md`.
2. Decide the standard: explicit `prd`/`brd` from the user → else the **Document
   Profile** in `clarify-output/prd-draft.md` section 0 → else ask (default
   BA→BRD, PO→PRD, labeled ASSUMPTION).
3. Run the workflow `.clarify/workflows/finalize.md` (include traceability only
   when stories/AC/tests exist or Dev/QA handoff readiness was requested; then
   assemble with the `finalize` engine).
4. Write `clarify-output/final-prd.md` (template `final-prd-template.md`) or
   `clarify-output/final-brd.md` (template `final-brd-template.md`).

## Rules
- Compose from prior outputs; never invent business rules or fabricate missing
  sections (mark them OPEN QUESTION). If an input is missing, name the
  command/skill that produces it.
- Embed the PlantUML activity + Mermaid sequence diagrams from
  `model-suggestions.md`, each with its viewer link.
- Carry over journey, screen matrix, error/message map, and entity vs
  transaction/operation state summary; mark missing sources OPEN QUESTION.
- When screen/flow requirements exist, add low-fidelity screen wireframes as an
  inline HTML widget after the Screen Matrix, or write `clarify-output/wireframes.html`
  and link it when inline HTML is unavailable. Use real BRD/PRD labels, grayscale
  only, no images or brand colors, no ASCII primary wireframes, and trace every
  screen back to its flow/step and requirement.
- Gather every ASSUMPTION / OPEN QUESTION into a Sign-off blockers section. Never
  stamp the document `Approved` while a blocker-level finding exists.
- Do not require **clarify-from-spec** artifacts for business sign-off. Missing
  stories/AC/tests/API-data/traceability are optional build-ready layer inputs
  unless the user requested Dev/QA handoff readiness.
