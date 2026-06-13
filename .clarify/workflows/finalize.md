# Workflow: finalize

## When to use
The spec is confirmed ("chốt") and you need the **final, standard document** — a
PRD or a BRD — to deliver to stakeholders / approvers. This is the closing step
after `from-idea` / `improve answers` / `from-spec` (and optionally `handoff`).

## Inputs
- Prior outputs in `clarify-output/`: prd-draft **or** brd-draft, plus whatever
  companions exist: audit-report, edge-case-matrix, error-handling,
  model-suggestions, api-data-impact, stories, test-scenarios,
  traceability-matrix. Read them; do not re-derive.
- `$ARGUMENTS`: optional `prd` | `brd` to force the standard. If absent, read the
  Document Profile from `prd-draft.md` or `brd-draft.md` section 0.

## Engine sequence (ordered)
1. `trace` — include/update traceability only when stories/AC/tests exist or when
   the user requested Dev/QA handoff readiness. Do not require traceability for a
   business sign-off document from a resolved `from-idea` draft.
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
- Section order (BRD): Executive summary → **§0 How to read** (0.1 intro + quick
  read, 0.2 symbol conventions, 0.3 glossary moved to front) → business context →
  objectives → scope → **How the system works (overview)** → stakeholders →
  **Business requirements (ONE grouped table: `ID | Requirement | Why | Priority`)**
  → business rules → **Functional Flows (`F0n-Name`)** → screen matrix → data →
  errors → constraints/risks/NFR → **Traceability (with Source ← A#/BR#/S#/Q#)** →
  open items → sign-off blockers → approval → Appendix: Artifact index.
- Document control block; audit score + band stamp when available; Error Handling &
  Message Mapping; entity vs transaction/operation state summary; Sign-off blockers
  listing every unresolved OPEN QUESTION. Status never `Approved` while a
  blocker-level finding exists.
- Requirements are a single grouped table (capability bands, Must→Should→Could);
  `Why` is a business reason, not a cross-reference; flow/rule/test/source links live
  only in Traceability; every requirement (incl. deferred) appears once.
- **Functional Flows (process-centric), flows named `F0n-Name`:**
  - Flow Catalog comes **before** the detailed flows.
  - Each key in-scope process has at least a step-by-step description.
  - Decision-rich processes have an Activity diagram (PlantUML); multi-system
    processes have a Sequence diagram (Mermaid) — or state "Sequence diagram not
    required" + a short reason.
  - **No 7.x block mixes process A's activity with process B's sequence.**
  - Flow steps map to business rule / validation / error code where relevant.
  - Each Flow maps to ≥1 requirement and appears in `traceability-matrix.md`.
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
- BRD has an **Executive summary** before §0; Assumptions/Open Questions/Suggestions
  are grouped in the **Open items** section (§13) with blockers called out in
  **Sign-off blockers** (§14).
- Error mapping has a **Flow / Step** column (using `F0n-Name`); the **State
  summary** has trigger / owner / terminal; the **Traceability summary** has Flow
  (`F0n-Name`) / Business rule / Error-State / **Source (← A#/BR#/S#/Q#)** columns.
- An **Appendix: Artifact index (source)** lists only `clarify-output/` files that
  exist (no fabricated `*.svg`/wireframe references); `brd.html`/`prd.html` listed
  when rendered.
- Missing build-ready inputs (stories/AC/tests/API-data/traceability) are listed
  as optional unless the user requested Dev/QA handoff readiness.
