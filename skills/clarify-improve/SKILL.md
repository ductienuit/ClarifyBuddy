---
name: clarify-improve
description: >-
  Clarify · Improve — resolve Answer Sheet decisions or upgrade ONE weak section
  of prior Clarify output instead of re-running everything. Use `answers`
  immediately after from-idea to apply A/Q/S/V decisions and refresh the business
  draft; use `change-request` after sign-off to analyze a change's impact across
  the traceability chain; use other modes for clarity, scope, business-rules,
  edge, acceptance-criteria, stories, api-data, risk, traceability, nfr, or
  model. Reads prior outputs from clarify-output/ and overwrites the relevant
  file. Part of the Clarify requirement-quality pack.
---

# Clarify: Improve

Upgrade a single requested section from prior Clarify output.

## Steps
1. Read `.clarify/principles.md`.
2. Determine the **mode** from the user (one of: `answers`, `change-request`,
   `clarity`, `scope`, `business-rules`, `edge`, `acceptance-criteria`, `stories`,
   `api-data`, `risk`, `traceability`, `nfr`, `model`). For `answers`, the user
   pastes a filled **Answer Sheet**; apply each `A/Q/S/V` decision to the draft by
   ID and resolve the draft, not just the answer list — then record the decisions in
   the draft's **Decisions made** table + a **Change history** row (no
   `decision-log.md`), and keep open questions grouped by owner in the draft's Open
   items section (no `elicitation-pack.md`). For `change-request`, the user describes
   the change; walk the in-document trace spine (Requirements ↔ Flow Catalog ↔ Test
   scenarios) and write `change-impact.md` (analysis only — applying is a separate
   confirmed step).
3. Run the workflow `.clarify/workflows/improve.md` for that mode (it names the
   engine to run, e.g. `model` → `modeling`).
4. Overwrite the relevant file in `clarify-output/`; warn before overwriting a
   hand-edited file.

## Rules
- Read prior outputs; do not re-derive the whole spec. If a needed input is
  missing, say which command/skill produces it (e.g. **clarify-from-spec**).
- `model` mode regenerates the PlantUML activity + Mermaid sequence diagrams, each
  with a viewer link.
- `answers` mode refreshes the business-facing draft sections affected by the
  answers: scope, journey, screen matrix, business rules, error/customer-message
  summary, state summary, business-level NFRs, assumptions, open questions, and
  suggestions. It may refresh edge/error/model companions when affected.
- `answers` mode does not generate full stories, AC, tests, API/data impact, or
  traceability; those belong to optional **clarify-from-spec** for Dev/QA
  build-ready elaboration.
- The targeted section's anti-patterns should be resolved or downgraded, and the
  change kept consistent with the other outputs.
