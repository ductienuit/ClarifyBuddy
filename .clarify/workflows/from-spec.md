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
If a Clarify draft already exists in `clarify-output/`, **reuse its edge / error /
model / state / flow sections** (they live inside the draft now, not in separate
files) — refresh only where the source changed. `from-spec` then focuses on the
**build-ready layer** `from-idea` does not produce: the scored audit, user stories,
acceptance criteria, test scenarios, API/data impact, and in-document traceability.
When analyzing a fresh external spec (no draft yet), write the edge / error / model /
flow analysis **into a working draft** (`brd-draft.md`/`prd-draft.md`) rather than
separate companion files. Do not regenerate edge/error/model from scratch just to
re-emit them, and do not emit dropped companion files (Principle 13.11).
- Document Profile: requester role (BA / PO) and target standard (PRD / BRD).
  Detect from the input or ask; default BA→BRD, PO→PRD as an ASSUMPTION.
- Domain context (Principle 12): auto-detect the domain; load a matching pack if
  one exists, otherwise proceed with **labeled inference** (no pack required,
  never force-fit a wrong pack). Record the mode in the Document Profile.

## Engine sequence (ordered)
1. `audit` (via audit workflow logic) — score, band, findings, **stakeholder
   coverage** (Principle 10) and **Suggested Additional Capabilities**
   (Principle 11, `SUGGESTION:` items) appended to the audit report.
2. `edge` — edge-case analysis **into the draft's Edge cases section** (error and
   non-error edges; include user-facing failures).
3. `error-handling` — error → transaction status → user-message → action map **into
   the draft's Error code & message table**.
4. `modeling` — **process-centric**: a Flow Catalog, then one block per key
   in-scope process pairing the SAME process's step-by-step + activity (PlantUML)
   + sequence (Mermaid); plus entity vs transaction/operation state (Mermaid) —
   written **into the draft's Functional Flows section**. Never mix two processes in
   one block. Place any Screen/Display Matrix **after** the flows.
5. `data` — data-model impact + source of truth.
6. `api` — API contract impact + side effects (writes api-data-impact.md).
7. `story` — user stories traced to requirements.
8. `acceptance-criteria` — AC per story (happy/negative/boundary).
9. `test` — test scenarios.
10. `trace` — **in-document** traceability check (Requirements ↔ Flow Catalog ↔ Test
    scenarios) + orphan/coverage report; writes no separate file.

## Templates to fill
- audit-report, api-data-impact, user-story, acceptance-criteria, test-scenario;
  the draft template's Edge / Error / Flows / State sections for the analysis above.

## Outputs written
- `clarify-output/audit-report.md`
- `clarify-output/api-data-impact.md`
- `clarify-output/stories.md` (stories + AC)
- `clarify-output/test-scenarios.md`
- `clarify-output/brd-draft.md`/`prd-draft.md` — updated/created with the edge /
  error / model / flow / state analysis folded in (no separate companion files).

## Done criteria
- Document Profile recorded (role + target standard).
- Score with band, gap analysis, edge cases, flow diagrams (with viewer links),
  API/data impact, stories, AC, test scenarios all present (analysis folded into the
  draft, build-ready layer as companions) and cross-traced in-document.
- Stakeholder coverage assessed and Suggested Additional Capabilities listed
  (`SUGGESTION:`, kept separate from confirmed scope).
- If the input is a Clarify BRD/PRD draft, explain that missing stories, AC, tests,
  API/data impact, or traceability are **build-ready layer gaps**, not proof that
  the business draft is incomplete. Do not tell the user the BRD needs `from-spec`
  to become readable or business-complete.
- Next steps offered: `/clarify:handoff` and `/clarify:finalize`.
