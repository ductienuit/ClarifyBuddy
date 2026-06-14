# Workflow: improve

## When to use
After a `from-idea`, `audit`, or `from-spec` run, to resolve answers or upgrade a
specific weak section instead of re-running everything.

## Inputs
- `$ARGUMENTS`: a **mode** naming the section to improve. Supported modes:
  `clarity`, `scope`, `business-rules`, `edge`, `acceptance-criteria`,
  `stories`, `api-data`, `risk`, `traceability`, `nfr`, `model`, `answers`,
  `change-request`.
- For `answers` mode, `$ARGUMENTS` (or the pasted message) is a filled **Answer
  Sheet** from a prior draft.
- Prior outputs in `clarify-output/` (read, do not re-derive). If the needed
  input is missing, say which command produces it.

## Engine sequence (by mode)
- `answers` → **resolve the draft**, not just replace text. Ingest the filled
  Answer Sheet and apply it by ID (per `output-conventions.md`):
  - `Variant` fixes the chosen option and prunes rejected options.
  - `A# keep` leaves the assumption visible; `A# override` updates it and removes
    stale contradictory wording.
  - An answered `Q#` becomes confirmed scope, rule, constraint, NFR, or
    out-of-scope item as appropriate; remove the corresponding `OPEN QUESTION`
    unless the answer creates a narrower follow-up question.
  - `S# = yes` moves the suggestion into confirmed scope and into Requirements /
    Business Rules / Stakeholder Perspectives as appropriate; `no` moves it to
    Out of scope; `later` keeps it as a future suggestion.
  - Re-run/resync the business-facing sections of the draft: Customer/User
    Journey, Screen Information / Display Matrix, Business Rules, Error Handling
    & Customer Messages summary, State Summary, business-level NFRs, Open
    Questions, Assumptions, and Suggested Additional Capabilities.
  - Refresh the draft's own edge / error / model / state sections when affected
    (they live inside the draft now — there are no separate `edge-case-matrix.md`,
    `error-handling.md`, or `model-suggestions.md` files).
  - Do **not** generate full stories, AC, tests, API/data impact, or traceability
    unless the user explicitly chose the optional build-ready layer via
    `from-spec`.
  - Re-flag any follow-on gaps the answers create.
  - **Record each applied decision in the draft itself** (Principle 13.10): add it to
    the **Decisions made** table (`Topic | Decision | Reflected in (BR/R)`) and add a
    **Change history** row (date, summary, source "answer sheet vN") in Document
    control. There is **no `decision-log.md` file**. You MAY still run
    `python .clarify/scripts/clarify_tools.py answers <file> --source "answer sheet vN"`
    to parse the sheet, but apply the result to the draft's Decisions + Change history,
    not to a side log. If Python is unavailable, do it manually.
  - Keep open questions grouped by stakeholder owner **in the draft's Open items
    section** (no separate `elicitation-pack.md`); remove answered ones.
- `change-request` → **impact analysis from traceability** (analysis only — it
  does not silently change the spec). `$ARGUMENTS` (or the pasted message) is the
  CR description. Steps:
  1. Assign the next `CR-<nn>` id and restate the requested change.
  2. Walk the in-document trace spine — the Requirements table, the Flow Catalog
     (rule / error-code / requirement columns), the error table, the Test scenarios,
     and the screen matrix — to list EVERY affected item: Requirement / Flow / Screen
     / Rule / Error / State / Story / Test.
  3. Write `clarify-output/change-impact.md` per
     `templates/change-impact-template.md`: impact table, the update each section
     needs, new `OPEN QUESTION`s the change raises, effort/risk notes (labeled
     ASSUMPTION where estimated).
  4. Applying the change is a separate, user-confirmed step (re-run the relevant
     improve mode); when applied, record the `CR-<nn>` decision in the draft's
     **Decisions made** table, and the next `finalize` bumps the document version with
     a Change history row citing the CR.
- `clarity` / `scope` → `clarify` + edit the draft (prd-draft or brd-draft).
- `business-rules` / `risk` / `nfr` → `risk` + edit the draft (prd-draft or brd-draft).
- `edge` → `edge` (refresh the draft's Edge cases section).
- `stories` → `story`.
- `acceptance-criteria` → `acceptance-criteria` (strengthen happy-only AC).
- `api-data` → `data` + `api`.
- `model` → `modeling` (refresh the draft's Functional Flows section **process-centric**:
  a Flow Catalog, then per-process blocks each pairing the SAME process's PlantUML
  activity + Mermaid sequence + step-by-step, plus entity & transaction/operation
  state in Mermaid; viewer links pinned; never mix two processes in one block —
  `mixed-process-diagram-block`).
- `traceability` → `trace` (verify the in-document trace spine; no separate file).

## Templates to fill
- The template matching the mode.

## Outputs written
- Overwrite the relevant `clarify-output/` file; warn before overwriting
  hand-edited files.

## Done criteria
- The targeted section's anti-patterns are resolved or downgraded, and the
  change is consistent with the rest of the outputs.
- For `answers`, the result is a more resolved business/product draft with fewer
  stale `ASSUMPTION` / `OPEN QUESTION` items, updated journey/screens/errors/state
  where the answers changed scope or rules, and a next-step recommendation of
  either `/clarify:finalize` for business sign-off or optional `/clarify:from-spec`
  for Dev/QA build-ready elaboration.
