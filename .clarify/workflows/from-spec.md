# Workflow: from-spec

## When to use
An existing spec — a **PRD or a BRD** — that needs quality analysis and optional
elaboration into build-ready artifacts. Use this directly for a document the user
already has, or after `from-idea` + `improve answers` only when the user wants the
Dev/QA build-ready layer.

## Inputs
- `$ARGUMENTS`: path to the spec. If empty, ask for it. The "spec" may be a doc the
  user already wrote **or** a Clarify draft already in `clarify-output/`
  (`prd-draft.md` / `brd-draft.md`) produced by `from-idea`.

## Reuse prior outputs (composability — do not redo work)
If a Clarify draft and its companions already exist in `clarify-output/`
(`edge-case-matrix.md`, `error-handling.md`, `model-suggestions.md`), **reuse
them** — refresh only where the source changed. `from-spec` then focuses on the
**build-ready layer** `from-idea` does not produce: the scored audit, user
stories, acceptance criteria, test scenarios, API/data impact, and traceability.
Do not regenerate edge/error/model from scratch just to re-emit them.
- Document Profile: requester role (BA / PO) and target standard (PRD / BRD).
  Detect from the input or ask; default BA→BRD, PO→PRD as an ASSUMPTION.
- Domain context (Principle 12): auto-detect the domain; load a matching pack if
  one exists, otherwise proceed with **labeled inference** (no pack required,
  never force-fit a wrong pack). Record the mode in the Document Profile.

## Engine sequence (ordered)
1. `audit` (via audit workflow logic) — score, band, findings, **stakeholder
   coverage** (Principle 10) and **Suggested Additional Capabilities**
   (Principle 11, `SUGGESTION:` items) appended to the audit report.
2. `edge` — edge-case matrix (include user-facing failures).
3. `error-handling` — error → entity state → transaction status → user-message →
   action map.
4. `modeling` — **process-centric**: a Flow Catalog, then one block per key
   in-scope process pairing the SAME process's step-by-step + activity (PlantUML)
   + sequence (Mermaid); plus entity vs transaction/operation state (Mermaid).
   Never mix two processes in one block. Place any Screen/Display Matrix **after**
   the flows (same structure as the final doc, so draft and final do not drift).
5. `data` — data-model impact + source of truth.
6. `api` — API contract impact + side effects (writes api-data-impact.md).
7. `story` — user stories traced to requirements.
8. `acceptance-criteria` — AC per story (happy/negative/boundary).
9. `test` — test scenarios.
10. `trace` — traceability matrix + orphan/coverage report.

## Templates to fill
- audit-report, edge-case-matrix, error-handling, model-suggestions,
  api-data-impact, user-story, acceptance-criteria, test-scenario.

## Outputs written
- `clarify-output/audit-report.md`
- `clarify-output/edge-case-matrix.md`
- `clarify-output/error-handling.md`
- `clarify-output/model-suggestions.md`
- `clarify-output/api-data-impact.md`
- `clarify-output/stories.md` (stories + AC)
- `clarify-output/test-scenarios.md`
- `clarify-output/traceability-matrix.md`

## Done criteria
- Document Profile recorded (role + target standard).
- Score with band, gap analysis, edge matrix, model suggestions (with diagrams +
  viewer links), API/data impact, stories, AC, test scenarios all present and
  cross-traced.
- Stakeholder coverage assessed and Suggested Additional Capabilities listed
  (`SUGGESTION:`, kept separate from confirmed scope).
- If the input is a Clarify BRD/PRD draft, explain that missing stories, AC, tests,
  API/data impact, or traceability are **build-ready layer gaps**, not proof that
  the business draft is incomplete. Do not tell the user the BRD needs `from-spec`
  to become readable or business-complete.
- Next steps offered: `/clarify:handoff` and `/clarify:finalize`.
