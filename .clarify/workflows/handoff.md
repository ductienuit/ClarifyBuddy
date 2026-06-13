# Workflow: handoff

## When to use
The spec is in good shape and you need Dev + QA packs to start work.

## Inputs
- Prior outputs in `clarify-output/`: prd-draft, audit-report,
  edge-case-matrix, error-handling, model-suggestions, stories, test-scenarios,
  api-data-impact, traceability-matrix. Read them; do not re-derive.
- `$ARGUMENTS`: optional override path to a primary spec.

## Engine sequence (ordered)
1. `trace` — ensure traceability matrix is current (build if missing).
2. `handoff` — assemble Dev pack + QA pack from prior outputs.

## Templates to fill
- `templates/handoff-pack-template.md`

## Outputs written
- `clarify-output/handoff-pack.md`

## Done criteria
- Dev pack (scope, build-ready requirements, sequencing, error/message map,
  authentication/confirmation, blocking questions) and QA pack (AC, tests, edge
  cases, error-message tests, risk focus) present, with a traceability summary.
  Missing inputs are listed with the command that produces each.
