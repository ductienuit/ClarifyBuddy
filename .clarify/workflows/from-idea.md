# Workflow: from-idea

## When to use
A raw idea or thin concept with no real spec. Goal: a shaped **URD draft** with explicit
scope, user stories, business rules, screens, flows, states, edge cases, and open questions
at business altitude — enough to resolve into a complete URD.

## Inputs
- `$ARGUMENTS`: an idea string or a path to a rough note. If empty, ask the user for the idea.
- Domain context (Principle 12): auto-detect the domain; load a matching pack from
  `.clarify/domain-packs/<pack>/` if one exists, otherwise proceed with **labeled inference**
  (no pack required, never force-fit). Record the mode.

## Engine sequence (ordered)
1. `clarify` — establish the **Document Profile** (Role BA/PO + `Standard: URD` + domain mode +
   Language, default `vi`). For thin input, ask the 5 highest-impact, scope-blocking questions
   and offer a **Variant / Options Matrix** to choose from.
2. `shape` — idea → URD skeleton at business altitude (incl. journey, user stories, screen
   matrix with field detail).
3. `risk` — business rules + risk/control + NFRs + success metric.
4. `edge` — edge-case enumeration.
5. `error-handling` — for user-facing or transactional flows, create the error → condition →
   user-message (VN/EN) → handling map. Unknown handling → `OPEN QUESTION`, never omit.
6. `story` — user stories + acceptance criteria (the URD's §7 / per-process §3.2).
7. `modeling` — **discovery-level** at this stage: light Mermaid sequence/state suggestions to
   probe gaps (full per-process diagrams come from `improve model`). Distinguish entity state
   from transaction/operation state.
8. `write-urd` — assemble the full URD draft.

## Templates to fill
- `templates/urd-draft-template.md` — this single draft holds the user-story / edge / error /
  model / state analysis inline. `edge-case-matrix-template.md`, `error-handling-template.md`,
  `model-suggestions-template.md`, `user-story-template.md`, `acceptance-criteria-template.md`
  are **working structures** for those draft sections, not separate output files.

## Outputs written
- `clarify-output/urd-draft.md` — the single working draft, with user stories, business rules,
  screen matrix, flow diagrams/state, edge cases, the error & message table, open questions
  (grouped by owner), and the Answer Sheet folded in. **No separate** `edge-case-matrix.md`,
  `error-handling.md`, `model-suggestions.md`, `stories.md`, or `elicitation-pack.md` files
  (Principle 13.11).

## Done criteria
- Draft titled "URD Draft".
- Has: Document Profile, clarifying questions, Variant/Options Matrix (if applicable),
  assumptions, in/out scope, user groups & stakeholders, user stories + acceptance criteria,
  business rules (explicit or OPEN QUESTION), end-to-end journey, Screen matrix & field specs
  for UI flows, state model, edge cases, error & message table, NFRs, open questions, suggested
  capabilities.
- User-facing or transactional failures have an `ERR-*` code / condition / VN+EN message /
  handling, or an explicit `OPEN QUESTION` row explaining what must be confirmed.
- Process / transaction features distinguish **entity state** from **transaction/operation
  state**.
- No business rule invented silently.

## Business Draft Completeness checklist
Before finishing `from-idea`, verify the draft includes these business-facing items:
- End-to-end journey.
- User stories + acceptance criteria.
- Screen matrix & field specs for UI flows.
- Business rules and policy decisions, with unknowns marked `OPEN QUESTION`.
- Risk & control at business altitude.
- Error & message map (VN/EN).
- Authentication / confirmation step for risky, sensitive, financial, contract,
  account-change, or irreversible actions.
- Entity state vs Transaction/Operation state for process/transaction features.
- Business-level measurable NFRs: availability, response expectation, security/privacy,
  auditability, compliance, accessibility where applicable.
- Open Questions, Assumptions, Variant choices, and Suggested Additional Capabilities clearly
  separated.

## Next steps (offer in this order)
1. **Resolve the draft**: fill the Answer Sheet and apply it with `/clarify:improve answers`
   (picks variants, confirms assumptions, answers open questions, accepts suggestions, and
   refreshes the draft). This is the immediate next step.
2. **Sign-off**: once confirmed, `/clarify:finalize` emits the URD (`urd.md` + `urd.html`; add
   `word` for `urd.docx`). Use `/clarify:audit` any time for a quality score.
