# Engine: write-prd

Purpose: assemble the full draft — a **PRD or BRD** per the Document Profile —
from shaped structure + downstream engine outputs (business rules, edge cases,
NFRs). Produces `prd-draft.md` or `brd-draft.md`.

## Altitude by standard
- **BRD**: keep the body at business altitude. Configuration, scheduled jobs,
  ledger/data-integrity, and API/event detail are summarized as *operational
  requirements*; their deep mechanics (idempotency keys, batch resume, config-row
  schema, double-entry internals) go under **§19 Downstream Technical Notes**,
  labeled non-BRD. Never drop these lenses — just lower their altitude.
- **PRD**: include configuration, scheduled jobs, and technical detail inline in
  their sections where it aids the build.

## Do
1. Start from the `shape` output: carry the **Document Profile** (the
   `## Document Profile` heading: role + target standard + Language) verbatim, then
   Summary, Goals, Scope, Actors/Roles (both the user table and the **System &
   External Actors** table), and Requirements. Apply the **document presentation &
   naming conventions** (Principle 13):
   - **§0 "How to read this draft"** after the Document Profile: 0.1 what-this-is +
     quick-read, 0.2 a **symbol-conventions** table, 0.3 the **Glossary** (define
     each core term once; only terms the requirements use).
   - **"How the system works (overview)"** before the requirements: the end-to-end
     journey as plain narrative (one representative diagram optional at draft altitude).
   - **Requirements = ONE grouped table** (Principle 13.7), columns
     `ID | Requirement | Why | Priority`, grouped by capability in journey order with
     a bold band row per group, Must → Should → Could within a group. Each requirement
     is a self-standing sentence; `Why` is the business reason (not `Source: BRx`).
     Do NOT put flow/rule/test/source here — they go in the draft **Traceability**
     section, which carries a **Source** column (`← A#/BR#/S#/Q#`). Name flows
     **`F0n-Name`** (number stable, short English feature name appended) everywhere
     they appear. Never a flat one-liner table with no grouping / no Why.
2. Integrate business rules (from `risk`/domain pack) into the Business Rules
   section — explicit or OPEN QUESTION, never invented. Fill the **Effective
   from / Version** and **Applies to (new/existing/both)** columns for any rule
   that can change over time.
3. Fill the **Configuration & Settings** section from `risk`/`data`: each tunable
   parameter with its config store, owner, validation, effective-dating, and
   propagation (`missing-configuration-ownership`).
4. Fill the **Scheduled Jobs / Batch** section from `risk`/`modeling`: each job
   with schedule/trigger, idempotency/resume, inputs, outputs, and downstream
   consumers (`missing-batch-job-spec`).
5. Fill the **Customer Journey** (end-to-end steps incl. authentication) and the
   **Screen Information / Display Matrix** sections from `shape`. For BRD, keep
   them at business altitude. A UI feature with no screen matrix is a handoff gap.
6. Write the edge cases (from `edge`) into the **Edge cases** section — error-producing
   edges in the **Error code & message table** (failure → transaction state → user
   message → action; entity-state column dropped) and non-error edges in **"Edge cases
   without errors"** (no separate file; Principle 13.8). Add Dependencies & Risks and
   NFRs.
7. Fill **Stakeholder Perspectives** (Principle 10): one row per stakeholder class
   (operations, accounting, reconciliation, partners/external, risk/compliance,
   maintenance, data/analytics, security) with its need/concern, or OPEN QUESTION.
8. Fill **Suggested Additional Capabilities** (Principle 11) with the `SUGGESTION:`
   items from `clarify` — kept separate from agreed scope, each as a recommended
   addition for confirmation, never a confirmed requirement.
9. Ensure every requirement still has actor + trigger + outcome.
10. For BRD output, run a **business-language pass** before writing:
    - Requirement/body sections speak in business terms first.
    - Implementation terms such as `ledger`, `double-entry`, `GL`, `accrual`,
      `posting`, `idempotency`, `cohort`, `grandfathered`, `API`, `schema`, and
      `batch resume` appear only when needed for business alignment; otherwise
      move them to Downstream Technical Notes.
    - If technical wording remains in a business-facing requirement, flag
      `technical-jargon-in-business-requirement` and provide a plain-language
      replacement.
11. When invoked after `improve answers`, run a **resolved draft pass**:
    - Apply confirmed answers throughout the draft, not only in the assumptions /
      open questions lists.
    - Update Customer/User Journey, Screen Information / Display Matrix,
      Business Rules, Error Handling & Customer Messages summary, State Summary,
      and business-level NFRs when answers changed scope, variants, rules, or
      suggestions.
    - Remove stale `OPEN QUESTION` items that have been answered; keep unresolved
      questions visible with stable IDs.
    - Keep build-ready artifacts out of the draft unless they already exist as
      companions; do not add full stories, AC, tests, API/data impact, or
      traceability here.

## Rules
- **Render headings in the Document Profile's Language** (Principle 13.3): when
  Language=vi, each heading is `Vietnamese (English term)`; when en, English only.
  Keep the machine-readable anchors in English ALWAYS: ASSUMPTION/OPEN QUESTION/
  SUGGESTION labels, all IDs (`A#/Q#/S#/V#/F0n-Name/BRD-R#/BR#/T-#`, error codes),
  and file names.
- Do not duplicate or contradict requirements; reconcile conflicts.
- Keep ASSUMPTION / OPEN QUESTION labels intact and visible.
- Each requirement is uniquely id'd (`BRD-R01`/`R01`, …) for traceability; IDs are
  stable — append, never renumber.
- For BRD, technical detail is preserved, not deleted: move it into Downstream
  Technical Notes or a companion artifact.
- A resolved `from-idea` draft may be finalized for business sign-off without
  first running `from-spec`.

## Output
- **PRD** → `clarify-output/prd-draft.md` using `templates/prd-template.md`.
- **BRD** → `clarify-output/brd-draft.md` using `templates/brd-draft-template.md`
  (deep technical content under §19 Downstream Technical Notes).
