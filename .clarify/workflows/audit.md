# Workflow: audit

## When to use
You want a quality score and findings for a requirement doc, fast — without
generating downstream artifacts.

## Inputs
- `$ARGUMENTS`: path to the doc. If empty, ask for it.
- Document Profile: detect whether the target is BRD or PRD and whether it is a
  business/product draft or a Dev/QA build-ready handoff package. If the input is
  a Clarify `from-idea` draft, score **business draft readiness** first and treat
  stories, AC, tests, API/data impact, and traceability as optional build-ready
  layer artifacts unless the user explicitly asks for handoff readiness.
- Domain context (Principle 12): auto-detect the domain; use a matching pack if one
  exists, otherwise score with the domain-agnostic core and treat any
  domain-specific expectation as a labeled inference — never force-fit a pack.

## Engine sequence (ordered)
1. Read `evaluators/audit-checklist.md` and run every check.
2. Detect anti-patterns using `anti-patterns/anti-patterns.yaml` `detect`
   heuristics; record id, severity, dimension, offending text.
3. Score using `evaluators/requirement-quality-score.md`:
   - start each dimension at full weight, deduct per occurrence
     (blocker −6 / major −3 / minor −1), cap per dimension at its weight.
   - sanity-check against rubric anchors; sum; assign band.
   - if any blocker exists, cap band at "Not ready for handoff".

## Templates to fill
- `templates/audit-report-template.md`

## Outputs written
- `clarify-output/audit-report.md`

## Done criteria
- Total /100 + band (noting blocker cap), per-dimension table, findings grouped
  blocker/major/minor with each anti-pattern linked to a dimension and a fix,
  plus top 3 actions.
- For a BRD/business draft, call out "Build-ready layer not generated" separately
  from business-content findings. Do not imply the BRD is unreadable or incomplete
  merely because user stories, AC, tests, API/data impact, or traceability have not
  been generated yet.
