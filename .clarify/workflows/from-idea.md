# Workflow: from-idea

## When to use
A raw idea or thin concept with no real spec. Goal: a shaped **PRD or BRD draft**
(per the Document Profile) with explicit scope, business rules, assumptions, edge
cases, and open questions — at the altitude that matches the chosen standard.
This workflow should produce a **business/product-ready draft**. It is not merely
a pre-step for `from-spec`, and it must not push business-facing content into the
build-ready layer just to raise a score.

## Inputs
- `$ARGUMENTS`: an idea string or a path to a rough note. If empty, ask the user
  for the idea.
- Domain context (Principle 12): auto-detect the domain; load a matching pack from
  `.clarify/domain-packs/<pack>/` if one exists, otherwise proceed with **labeled
  inference** (no pack required, never force-fit). Record the mode.

## Engine sequence (ordered)
1. `clarify` — establish the **Document Profile** (role BA/PO + target standard
   PRD/BRD + domain mode). For thin input, ask the 5 highest-impact, scope-blocking
   questions and offer a **Variant / Options Matrix** to choose from.
2. `shape` — idea → skeleton at the right altitude (BRD business / PRD product).
3. `risk` — business rules + risk/control + NFRs + success metric.
4. `edge` — edge-case matrix.
5. `error-handling` — for user-facing or transactional flows, create the
   error → entity state → transaction status → user-message → action map. If the
   correct handling is unknown, mark `OPEN QUESTION` rather than omitting the row.
6. `modeling` — **discovery-level** at this stage: light activity/sequence/state
   suggestions to probe gaps (pairs not required while scope is unconfirmed). The
   full process-centric Flow Catalog + per-process activity+sequence pairs are
   produced by `from-spec` / `improve model`. Still distinguish entity state from
   transaction/operation state.
7. `write-prd` — assemble the full draft (PRD or BRD), summarizing error handling
   and model/state outputs in the draft without burying business readers in
   implementation detail.

## Templates to fill
- `templates/prd-template.md` (PRD) **or** `templates/brd-draft-template.md` (BRD).
- `templates/edge-case-matrix-template.md`
- `templates/error-handling-template.md` when the feature has user-facing errors,
  exceptions, risky actions, external calls, or transaction/process states.
- `templates/model-suggestions-template.md` when the feature has a user journey,
  stateful entity, process, async operation, risky action, or transaction.

## Outputs written
- `clarify-output/prd-draft.md` **or** `clarify-output/brd-draft.md` (per standard).
- `clarify-output/elicitation-pack.md` — open questions grouped by stakeholder
  owner (whom to ask), for workshops/interviews.
- `clarify-output/edge-case-matrix.md`
- `clarify-output/error-handling.md` when applicable.
- `clarify-output/model-suggestions.md` when applicable.

## Done criteria
- Draft titled per standard (BRD → "BRD Draft", PRD → "PRD Draft") — never a BRD
  titled/structured as a PRD.
- Has: Document Profile, clarifying questions, Variant/Options Matrix (if
  applicable), assumptions, in/out scope, requirements, business rules (explicit
  or OPEN QUESTION), Customer/User Journey, Screen Information / Display Matrix
  for UI flows, edge cases, open questions, suggested capabilities.
- User-facing or transactional failures have a code/entity-state/operation-state/
  message/action map, or an explicit `OPEN QUESTION` row explaining what must be
  confirmed.
- Process / transaction features distinguish **entity state** from
  **transaction/operation state** in the model output and draft summary.
- BRD keeps deep technical mechanics under Downstream Technical Notes, not the body.
- No business rule invented silently.

## Business Draft Completeness checklist
Before finishing `from-idea`, verify the draft itself includes these
business/product-facing items. Do not defer these to `from-spec`.
- Customer/User Journey end to end.
- Screen Information / Display Matrix for UI flows.
- Business Rules and policy decisions, with unknowns marked `OPEN QUESTION`.
- Risk & Control at business altitude.
- Error Handling & Customer Messages summary.
- Authentication / confirmation step for risky, sensitive, financial, contract,
  account-change, or irreversible actions.
- Entity state vs Transaction/Operation state summary for process/transaction
  features.
- Business-level measurable NFRs: availability, response expectation,
  security/privacy, auditability, compliance, accessibility where applicable.
- Open Questions, Assumptions, Variant choices, and Suggested Additional
  Capabilities clearly separated.

Do **not** put full endpoint contracts, full database/schema design, the full QA
test suite, the full story backlog, or the detailed traceability matrix in
`from-idea`; those belong to the optional build-ready layer.

## Next steps (offer in this order — do NOT tell the user to re-analyze from scratch)
1. **Resolve the draft**: fill the Answer Sheet and apply it with
   `/clarify:improve answers` (picks variants, confirms assumptions, answers open
   questions, accepts suggestions, and refreshes the draft's business-facing
   sections). This is the immediate next step.
2. **Optional — build-ready elaboration**: run `/clarify:from-spec` on **this same
   draft** to add what `from-idea` does not produce — user stories, acceptance
   criteria, test scenarios, API/data impact, traceability — plus a quality score.
   It **reuses** the edge-case matrix, error map, and model already generated here;
   it does not start over. Skip this if you only need the business draft.
3. **Sign-off**: once confirmed, `/clarify:finalize` emits the final PRD/BRD.

`from-spec` is a sibling **entry point** for an existing doc — it is not a forced
successor to `from-idea`.
