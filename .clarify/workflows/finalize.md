# Workflow: finalize

## When to use
The spec is confirmed ("chốt") and you need the **final, standard document** — a
PRD or a BRD — to deliver to stakeholders / approvers. This is the closing step
after `from-idea` / `improve answers` / `from-spec` (and optionally `handoff`).

## Inputs
- Prior outputs in `clarify-output/`: prd-draft **or** brd-draft (which now carries
  the edge / error / flow-diagram / state / traceability analysis inline), plus the
  build-ready companions that exist: audit-report, api-data-impact, stories,
  test-scenarios. Read them; do not re-derive. There are no separate edge /
  error-handling / model / traceability / decision-log files to read.
- `$ARGUMENTS`: optional `prd` | `brd` to force the standard. If absent, read the
  Document Profile from `prd-draft.md` or `brd-draft.md` section 0.

## Engine sequence (ordered)
1. `trace` — verify in-document traceability (Requirements ↔ Flow Catalog ↔ Test
   scenarios) and the coverage paragraph; report orphans/dangling refs. Writes **no
   separate file**. Do not require traceability for a business sign-off document from
   a resolved `from-idea` draft.
2. `finalize` — pick the standard (PRD/BRD), then assemble the final document
   from prior outputs, embedding diagrams + viewer links, the screen wireframe
   HTML preview when screen/flow requirements exist, and a sign-off section.

## Templates to fill
- `templates/final-prd-template.md` (when standard = PRD)
- `templates/final-brd-template.md` (when standard = BRD)
- `templates/wireframe-template.html` (when screen/flow requirements exist)

## Outputs written
- `clarify-output/brd.md` **or** `clarify-output/prd.md` (the sign-off doc — **no
  "final" in the name**, Principle 13.1).
- `clarify-output/brd.html` **or** `prd.html` — the HTML rendering produced from the
  Markdown (best-effort; see `export`).
- `clarify-output/wireframes.html` — when the doc has screen/flow requirements and
  inline HTML visualization is not appropriate for the target Markdown renderer.

## Done criteria
- Section order — numbers AUTO-FOLLOW the template skeleton (do not hardcode); with
  §0 + §4 present, edge=§11, test=§15, decisions=§16 fall out naturally:
  front matter (title → Document control + Change history → Executive summary) →
  **§0 How to read** (0.1 intro + quick-read + diagram-render note, 0.2 symbol
  conventions, 0.3 glossary) → §1 context → §2 objectives & success criteria → §3
  scope → §4 **How the system works (overview)** → §5 stakeholders (RACI, ≥1 (A)) →
  §6 **Business requirements (ONE grouped table: `ID | Requirement | Why | Priority`)**
  → §7 business rules → §8 **Functional Flows (`F0n-Name`)** (8.1 Flow Catalog lists
  every R#) → §9 **Screens & wireframe** → §10 data & systems impact → §11 **Edge
  cases** (11.1 Error code & message table, 11.2 State summary, 11.3 Edge cases
  without errors) → §12 constraints & dependencies → §13 risks & compliance → §14
  NFR & legal → §15 **Test scenarios (numbered table) + Coverage & traceability** →
  §16 **Decisions & open items** → §17 sign-off blockers → §18 approval → Appendix:
  Artifact index (lean set, with a "Used when" column).
- Document control block; audit score + band stamp when available; **Error code &
  message table** (no entity-state column; Principle 13.8); entity vs
  transaction/operation state summary; Sign-off blockers listing every blocking
  OPEN QUESTION. Status never `Approved` while a blocker-level finding exists.
- Requirements are a single grouped table (capability bands, Must→Should→Could);
  `Why` is a business reason, not a cross-reference; traceability is expressed
  in-document (Requirements ↔ Flow Catalog ↔ Test scenarios; Principle 13.9), never in
  a body grid or a separate file; every requirement (incl. deferred) appears once.
- **Functional Flows (process-centric), flows named `F0n-Name`:**
  - Flow Catalog comes **before** the detailed flows.
  - Each key in-scope process has at least a step-by-step description.
  - Decision-rich processes have an Activity diagram (PlantUML); multi-system
    processes have a Sequence diagram (Mermaid) — or state "Sequence diagram not
    required" + a short reason.
  - **No 7.x block mixes process A's activity with process B's sequence.**
  - Flow steps map to business rule / validation / error code where relevant.
  - The Flow Catalog carries the rule / error-code / requirement columns (it is the
    in-document traceability spine); each Flow maps to ≥1 requirement.
  - The Screen / Display Matrix is **after** the detailed flows (or a clear reason).
  - If the Screen / Display Matrix contains screens, add **Screen Wireframes
    (low-fidelity HTML)** immediately after it: an inline HTML visualization
    widget using real labels from the BRD/PRD, or a link to
    `clarify-output/wireframes.html` if inline visualization is unavailable.
  - Every flow-revealed gap is recorded under "Gaps revealed" or `OPEN QUESTION`.
  - A missing diagram for a key process is an `OPEN QUESTION` pointing to
    `from-spec` / `improve model` — never fabricated, never filled with unrelated
    diagrams.
- No rule/logic added beyond confirmed scope.
- **No silent overwrite:** if the doc already existed, the previous version is
  archived as `brd.v<N>.md` / `prd.v<N>.md`, the Version is bumped, and Change
  history gained a row citing the driver (answer sheet vN / CR-nn). The canonical
  `brd.md`/`prd.md` holds the latest; warn before overwriting a hand-edited file.
- The HTML companion `brd.html`/`prd.html` is rendered **from** `brd.md`/`prd.md`
  (best-effort; never blocks the Markdown deliverable).
- No dangling ID references (every BR/`F0n-Name`/S/CODE referenced exists) — or they
  are listed as findings.
- Wireframes follow strict derive-only rules: grayscale only, no brand colors or
  images, one phone/card frame per key flow step, numbered in flow order, with
  source traceability back to the requirement / BRD or PRD section.
- BRD has an **Executive summary** before §0; assumptions/answered questions/
  suggestions are resolved into the **Decisions & open items** section (§16;
  Principle 13.10 — **Decisions made is a three-column** `Topic | Decision | Reflected
  in (BR/R)` table / Suggestions dispositioned / non-blocking Open items, `A#`/`S#`
  codes hidden, no decision-log reference — history is in Change history), with
  blockers called out in **Sign-off blockers** (§17).
- Edge analysis is in the document: error-producing edges in the **Error code &
  message table** (a **Flow / Step** column using `F0n-Name`, no entity-state column);
  non-error edges in an **"Edge cases without errors"** subsection; the **State
  summary** has trigger / owner / terminal. The body has **Test scenarios (by
  context)** as **one numbered table** (`# | Flow | Scenario | Expected | T-xx`,
  grouped by flow, countable) + a self-standing **Coverage & traceability** paragraph
  pointing to the Flow Catalog + `test-scenarios.md` — NOT to a traceability-matrix
  file and NOT a body grid (Principle 13.9).
- An **Appendix: Artifact index (source)** with a **Used when (who / when)** column
  lists only the lean deliverable set that exists (source `brd.md`/`prd.md`,
  audit-report, api-data-impact, stories, test-scenarios, version archive,
  wireframes/HTML when written). No `edge-case-matrix.md`, `error-handling.md`,
  `model-suggestions.md`, `traceability-matrix.md`, `decision-log.md`,
  `elicitation-pack.md`, or draft is emitted or linked (Principle 13.11).
- **Blank line before every table** that follows a label or paragraph (Principle
  13.12), so pandoc does not break the table in the HTML render.
- Missing build-ready inputs (stories/AC/tests/API-data/traceability) are listed
  as optional unless the user requested Dev/QA handoff readiness.
