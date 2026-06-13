# Engine: handoff

Purpose: assemble build-ready Dev and QA packs from prior Clarify outputs. Do
not re-derive — read `clarify-output/`.

## Do
1. Read available outputs: prd-draft / brd-draft, audit-report, edge-case-matrix,
   error-handling, stories, test-scenarios, api-data-impact, traceability-matrix.
2. **Dev pack:** scope, build-ready requirements table (with business rules and
   API/data impact), the **error → code → message → action** map, the
   authentication/confirmation step, sequencing/dependencies, and open questions
   blocking build.
3. **QA pack:** acceptance criteria, test scenarios, edge cases to verify, the
   error/message map (expected user messages + transaction status per failure),
   and risk-based focus areas.
4. Include a traceability summary (Req → Story → AC → Test).
5. List any missing inputs and the command that produces each.

## Rules
- Do not invent content absent from prior outputs; surface gaps instead.
- Preserve ASSUMPTION / OPEN QUESTION labels so handoff readers see them.

## Output
Write `clarify-output/handoff-pack.md` using
`templates/handoff-pack-template.md`.
