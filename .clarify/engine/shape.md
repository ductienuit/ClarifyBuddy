# Engine: shape

Purpose: turn a raw idea (plus clarify output) into the skeleton of a structured
PRD **or BRD** (per the Document Profile). Shape structure only — do not fabricate
rules or scope.

## Altitude by standard (read first)
- **BRD** → business altitude: business background/problem, objectives, scope,
  stakeholders, business process, business rules, business requirements (with
  Must/Should/Could), success metrics. Deep technical mechanics (idempotency keys,
  batch resume, ledger internals, config row schema, API design) do **not** go in
  the body — route them to the **Downstream Technical Notes (for PRD/SRS)**
  section, labeled as non-BRD.
- **PRD** → product altitude: user flow, functional requirements, configuration,
  scheduled jobs, state, with technical detail inline where it aids the build.
- Either way, never drop a lens (config / jobs / cohort / stakeholders); only
  change the altitude at which it appears.

## Business-language rule (BRD)
Write each BRD requirement as a **business outcome a stakeholder would say**, not
as a system mechanism. Avoid implementation jargon in the body — `ledger`,
`double-entry`, `GL`, `accrual`, `posting`, `idempotency`, `cohort`,
`grandfathered`, `batch resume`. Use plain equivalents and footnote the mechanism
to Downstream Technical Notes. Example:
- Avoid: "A daily job reads the effective rate and writes accrual entries per
  active account, idempotent on (account, date)."
- Prefer: "The system calculates interest daily for each active deposit using the
  product's applicable rate." (note: "interest must not be double-counted if the
  daily calculation re-runs" → Downstream Technical Notes.)

## Do
1. Take the idea + assumptions from `clarify`.
2. Draft: Summary, Goals, Success metric, In-scope, Out-of-scope, Actors/roles.
   Actors are **two tables**: (a) user roles, and (b) **system & external
   actors** — admin/configurator, operations, accounting/back-office, external
   systems, and scheduled jobs. If a non-user actor is plausible but unconfirmed,
   list it as OPEN QUESTION rather than omitting it (`missing-system-actor`).
3. Convert the idea's intent into requirement statements in the form:
   "When <trigger>, <actor> can <action>, resulting in <outcome>." Include
   non-user actors here too (e.g. "Daily at <time>, the <job> processes <input>,
   producing <output> for <consumer>").
3b. Draft the **end-to-end Customer Journey** — the ordered steps the user takes
   from entry to result (e.g. menu → choose product → see terms/rate → enter
   amount → choose source/options → preview → confirm terms → **authenticate** →
   process → result → view detail). Don't start the flow mid-way; include the
   steps before and after the core action. Mark unknown steps OPEN QUESTION.
3c. For each journey screen the feature implies, fill the **Screen Information /
   Display Matrix**: screen name, purpose, display fields, user actions,
   validation, error/empty/loading states, and UX/content notes. Keep it at
   information level (not pixel design), but make it detailed enough for Dev and
   QA to picture the behavior.
4. For any requirement missing actor/trigger/outcome, flag inline (do not guess).
5. List **configurable parameters** the product implies (rates, fees, limits,
   thresholds) with an owner placeholder; unknowns → OPEN QUESTION
   (`missing-configuration-ownership`). For any rule that may change over time,
   surface effective-dating and the existing-vs-new cohort strategy as
   OPEN QUESTION (`missing-effective-dating`, `missing-cohort-treatment`).
6. Mark every unstated rule as OPEN QUESTION; every default as ASSUMPTION.

## Rules
- Out-of-scope must be non-empty; if unknown, list candidate exclusions as
  OPEN QUESTION.
- Keep requirements atomic (one actor, one trigger, one outcome each).

## Output
Pick the template by the Document Profile's target standard:
- **BRD** → `templates/brd-draft-template.md` (title "BRD Draft").
- **PRD** → `templates/prd-template.md` (title "PRD Draft").

Carry the **Document Profile** (role + target standard + domain mode) into
section 0. Fill the standard's business/product sections including the
**Customer Journey** and **Screen Information / Display Matrix** sections, and carry over
from `clarify`: the **Variant / Options Matrix**, the **Stakeholder Perspectives**,
and the **Suggested Additional Capabilities** (`SUGGESTION:` items) — keep
suggestions and the variant matrix clearly separate from agreed scope. Write BRD
requirements in business language (see the Business-language rule); place deep
technical content under **Downstream Technical Notes**, not the body. Leave
business rules / edge cases / API impact / error mapping to later engines.
