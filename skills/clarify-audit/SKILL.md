---
name: clarify-audit
description: >-
  Clarify · Audit — score a requirement document and list its quality issues,
  nothing more. Use when the user asks "how good is this spec", "score these
  requirements", "audit this URD", or wants blockers/major/minor findings.
  Produces a total /100, a band, a per-dimension table, and findings each linked
  to a rubric dimension with a concrete fix, using a 36-entry anti-pattern
  catalog. Does not rewrite the doc. Part of the Clarify requirement-quality pack.
---

# Clarify: Audit

Score a requirement doc and report findings only — do not elaborate or rewrite.

## Steps
1. Read `.clarify/principles.md`.
2. Run the workflow `.clarify/workflows/audit.md`, using:
   - `.clarify/anti-patterns/anti-patterns.yaml` — detection (source of truth).
   - `.clarify/evaluators/scoring-rubric.yaml` + `requirement-quality-score.md` —
     scoring procedure and anti-pattern → dimension model.
   - `.clarify/evaluators/audit-checklist.md` — fast ordered pass.
3. Write `clarify-output/audit-report.md` per `.clarify/output-conventions.md`.

## Rules
- Show the math: total /100, band, per-dimension breakdown.
- Group findings blocker / major / minor; link each anti-pattern to a dimension
  and give a concrete fix. Any `blocker` caps the band at "Not ready for handoff".
- Audit only — to fix a specific section, use **clarify-improve**; to produce the
  sign-off URD, use **clarify-finalize**.
