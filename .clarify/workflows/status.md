# Workflow: status

## When to use
Any time the BA wants to re-orient: "where am I in the pipeline, what exists, what
is still unresolved, what should I do next?" — typically when returning to a
project after a break. Read-only: **writes no files, changes nothing**.

## Inputs
- `clarify-output/` (read everything that exists; nothing is required).
- No `$ARGUMENTS`.

## Steps (no engine — self-contained)
0. **Prefer the script.** If a Python runtime is available, run
   `python .clarify/scripts/clarify_tools.py status` (add `--json` if you want to
   post-process) and use its output for steps 1–3; otherwise perform them manually
   as written. Never fail this command because the script can't run.
1. **Inventory artifacts.** For each known artifact, report exists / missing, and
   for missing ones the command that produces it:
   draft (`prd-draft.md`/`brd-draft.md`), `elicitation-pack.md`,
   `edge-case-matrix.md`, `error-handling.md`, `model-suggestions.md`,
   `audit-report.md`, `stories.md`, `test-scenarios.md`, `api-data-impact.md`,
   `traceability-matrix.md`, `decision-log.md`, `change-impact.md`,
   `brd.md`/`prd.md` (the sign-off doc — no "final" in the name; + archived
   `brd.v<N>.md`/`prd.v<N>.md` versions), `wireframes.html`,
   `brd.html`/`prd.html` (HTML rendering from export).
2. **Document Profile.** Read the `## Document Profile` heading of the draft (or
   sign-off doc): role, target standard, domain mode, language. If no draft exists,
   say so.
3. **Outstanding items.** Parse the draft's Assumptions / Open Questions /
   Suggestions / Variant sections and the Answer Sheet: count unresolved
   `A#/Q#/S#/V#` (and list the top blockers). Include audit blockers if an
   audit-report exists, and unapplied CRs if `change-impact.md` exists without a
   matching decision-log entry.
4. **Pipeline position + next step.** Place the project on
   `from-idea → improve answers → (from-spec) → finalize → export` and recommend
   the single most useful next command, with a one-line reason.

## Output
**Reply in chat only** (concise tables/bullets in the Document Profile's
language). Do not write or modify any file. Do not re-derive or fix anything —
status reports; it never repairs.

## Done criteria
- The user can see in one reply: what exists, what's missing (and how to produce
  it), the Document Profile, the count + highlights of unresolved items, and the
  recommended next command.
