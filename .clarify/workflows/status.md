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
   for missing ones the command that produces it — only the **lean set** (Principle
   13.11): the working draft (`urd-draft.md`), `audit-report.md`, `change-impact.md`
   (if a CR is in flight), `urd.md` (the sign-off doc — no "final" in the name; +
   archived `urd.v<N>.md` versions), `wireframes.html`, `urd.html`, and `urd.docx`
   (renderings from finalize/export). Do **not** expect `edge-case-matrix.md`,
   `error-handling.md`, `model-suggestions.md`, `traceability-matrix.md`,
   `decision-log.md`, `stories.md`, `test-scenarios.md`, or `elicitation-pack.md` —
   that analysis now lives inside the draft / sign-off URD, not in separate files.
2. **Document Profile.** Read the `## Document Profile` heading of the draft (or
   sign-off doc): role, `Standard: URD`, domain mode, language. If no draft exists,
   say so.
3. **Outstanding items.** Parse the draft's Assumptions / Open Questions /
   Suggestions / Variant sections and the Answer Sheet: count unresolved
   `A#/Q#/S#/V#` (and list the top blockers). Include audit blockers if an
   audit-report exists, and unapplied CRs if `change-impact.md` exists without a
   matching row in the sign-off doc's Change history / Decisions section.
4. **Pipeline position + next step.** Place the project on
   `from-idea → improve answers → finalize → export` and recommend the single most
   useful next command, with a one-line reason.

## Output
**Reply in chat only** (concise tables/bullets in the Document Profile's
language). Do not write or modify any file. Do not re-derive or fix anything —
status reports; it never repairs.

## Done criteria
- The user can see in one reply: what exists, what's missing (and how to produce
  it), the Document Profile, the count + highlights of unresolved items, and the
  recommended next command.
