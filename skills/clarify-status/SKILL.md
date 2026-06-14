---
name: clarify-status
description: >-
  Clarify · Status — show where the requirements work stands. Use when the user
  asks "what's left?", "where were we?", "what's the status of the BRD/PRD?",
  "what should I do next?", or returns to a Clarify project after a break.
  Read-only: inventories clarify-output/ artifacts (exists/missing + which command
  produces each), shows the Document Profile (role, standard, domain, language),
  counts unresolved Answer Sheet items (A/Q/S/V) and audit blockers, and
  recommends the next command on the pipeline from-idea → improve answers →
  (from-spec) → finalize → export. Writes no files. Part of the Clarify
  requirement-quality pack.
---

# Clarify: Status

Re-orient the BA: what exists, what's unresolved, what to do next. **Read-only.**

## Steps
1. Run the workflow `.clarify/workflows/status.md`.
2. Reply in chat (no files written) with:
   - Artifact inventory — exists / missing, and the producing command for each
     missing one — the **lean set** (Principle 13.11): draft, audit-report, stories,
     test-scenarios, api-data-impact, change-impact, sign-off doc + archived versions,
     wireframes, HTML. Do not expect edge-case-matrix / error-handling /
     model-suggestions / traceability-matrix / decision-log / elicitation-pack — that
     analysis lives inside the draft / sign-off doc.
   - Document Profile (role, target standard, domain mode, language).
   - Unresolved items: counts of open `A#/Q#/S#/V#` + top blockers; audit blocker
     findings; unapplied CRs.
   - Pipeline position and the single recommended next command, with a one-line
     reason.

## Rules
- Never write or modify anything; status reports, it never repairs.
- Reply in the Document Profile's language.
- Empty/absent `clarify-output/` → recommend **clarify-from-idea** (new idea) or
  **clarify-from-spec** (existing doc).
