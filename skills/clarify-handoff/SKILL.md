---
name: clarify-handoff
description: >-
  Clarify · Handoff — assemble build-ready Dev and QA packs from prior Clarify
  output. Use when the spec is in good shape and the user wants to hand it to
  engineering and QA: a Dev pack (scope, build-ready requirements, sequencing,
  error/message map, authentication/confirmation, blocking questions) and a QA
  pack (acceptance criteria, test scenarios, edge cases, error-message tests,
  risk focus), with a traceability summary. Reads clarify-output/; does not
  re-derive. Part of the Clarify requirement-quality pack.
---

# Clarify: Handoff

Emit a Dev pack and a QA pack from prior Clarify outputs.

## Steps
1. Read `.clarify/principles.md`.
2. Run the workflow `.clarify/workflows/handoff.md` (verify in-document
   traceability via `trace`, then assemble with `handoff`).
3. Read prior outputs from `clarify-output/`: the draft / sign-off doc (carrying the
   edge / error / model / flow / traceability content inline), audit-report, stories,
   test-scenarios, api-data-impact. No separate edge / error / model / traceability
   files (Principle 13.11).
4. Write `clarify-output/handoff-pack.md` per `.clarify/output-conventions.md`.

## Rules
- Never invent content absent from prior outputs; surface gaps instead, and list
  any missing input with the command/skill that produces it.
- Preserve ASSUMPTION / OPEN QUESTION labels so handoff readers see them.
- For the final stakeholder sign-off document (PRD/BRD), use **clarify-finalize**.
