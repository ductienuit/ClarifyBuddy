# Engine: finalize

Purpose: after the spec is confirmed, assemble the **final sign-off document** —
a PRD or a BRD — in a standard, professional shape for a BA or PO. This can be a
business/product sign-off document from a resolved `from-idea` draft, or a
handoff-ready document when `from-spec` artifacts also exist. Do NOT re-derive
content: compose from prior `clarify-output/` files. Do NOT invent business rules.

## Decide the standard
1. Read the **Document Profile** (role + target standard) from the draft —
   `prd-draft.md` or `brd-draft.md` section 0 — or from `$ARGUMENTS` (`prd` / `brd`).
2. If still unknown: ask. If not live, default by role (BA→BRD, PO→PRD) and label
   the choice `ASSUMPTION:` in the document.
3. `prd` → use `templates/final-prd-template.md`.
   `brd` → use `templates/final-brd-template.md`.

## Do
1. Read available outputs: prd-draft **or** brd-draft, plus any companions that
   exist: audit-report, edge-case-matrix, error-handling, model-suggestions,
   api-data-impact, stories, test-scenarios, traceability-matrix.
2. Compose the chosen template, pulling each section from the matching prior
   output. Keep wording testable and build-ready.
3. Assemble the **Functional Flows (process-centric)** section: build the Flow
   Catalog, then one block per business process, mapping each flow to its OWN
   step-by-step + Activity (PlantUML) + Sequence (Mermaid) from
   `model-suggestions.md`. The activity and sequence in a block must be the **same**
   process — never pair process A's activity with process B's sequence
   (`mixed-process-diagram-block`). **Re-render only from the confirmed
   step-by-step**; do not invent new flow/logic/rules. If a key in-scope process
   has no diagram/flow, write an `OPEN QUESTION` naming the missing flow and the
   command that produces it (`from-spec` / `improve model`) — do not fabricate a
   diagram and do not drop in two unrelated diagrams. Place the Screen / Display
   Matrix **after** the flows. Viewer links: Mermaid `https://mermaid.live/`,
   PlantUML `https://www.plantuml.com/plantuml` (ref `https://plantuml.com/`).
3b. When the Screen / Display Matrix or flow steps define screens, add
   **Screen Wireframes (low-fidelity HTML)** right after the matrix. Render an
   inline HTML visualization widget from `templates/wireframe-template.html`
   whenever the final Markdown target supports inline HTML. If inline
   visualization is unavailable, write a single self-contained
   `clarify-output/wireframes.html` using the same template and link it from the
   final document and Appendix. Do not create ASCII wireframes as the primary
   artifact.
4. Preserve every `ASSUMPTION` / `OPEN QUESTION` / `SUGGESTION`. For the BRD, group
   them into the **§14 Open items** cluster (14.1 Assumptions, 14.2 Open Questions,
   14.3 Suggested capabilities); then list the **blocker subset** of open questions
   + blocker audit findings in **§15 Sign-off blockers**.
4b. Compose a short **Executive summary** (BRD) from the business context,
   objectives, scope, and key blockers — 1–2 paragraphs / bullets, composed from
   those sections, introducing no new claims.
5. Include the audit score + band near the top as a quality stamp when an
   audit-report exists. If no audit-report exists, state `Quality stamp: not run`
   and do not block finalization solely because the optional build-ready layer was
   not generated.
6. Carry over the **Stakeholder Perspectives** and the **Suggested Additional
   Capabilities** (`SUGGESTION:` items) from prd-draft / audit-report into their
   sections. Keep suggestions clearly marked as recommendations for confirmation,
   never as agreed scope.
7. Carry over the high-level Customer/User Journey (overview only — detail lives in
   the per-flow blocks of §7), Error Handling & Message Mapping, and the entity vs
   transaction/operation state summary. If a source artifact is missing, mark the
   section `OPEN QUESTION` and name the command that produces it.
8. Carry over the expanded columns from source files: the **Flow / Step** column in
   the error map (from `error-handling.md`), **trigger / owner system / terminal**
   in the state summary (from `model-suggestions.md`), and **Flow / Business rule /
   Error-State** in the traceability summary (from `traceability-matrix.md`).
9. Emit the **Appendix: Generated artifacts** listing only the `clarify-output/`
   companion files that actually exist — diagrams are referenced as source +
   viewer link, never as image files Clarify did not produce. List
   `clarify-output/wireframes.html` and `clarify-output/decision-log.md` only when
   they were actually written.
9b. **Versioning — never overwrite silently.** If the target final file already
   exists: (1) archive the existing file as `final-brd.v<N>.md` /
   `final-prd.v<N>.md` (N = its current Version); (2) bump the Version in Document
   control (1.0 → 1.1, or as the user directs); (3) add a **Change history** row
   (version, date, summary of what changed, driver — `answer sheet vN` / `CR-nn`).
   The canonical file name always holds the latest version.
10. List any missing inputs and the command that produces each.

## Rules
- **Render in the Document Profile's Language** (headings + content). Keep the
  machine-readable anchors in English: ASSUMPTION/OPEN QUESTION/SUGGESTION labels,
  all IDs (A#/Q#/S#/V#/F#/BR#/CR#, error codes), and file names.
- Final ≠ invented: if a section has no source in prior outputs, mark it
  `OPEN QUESTION` rather than fabricating it.
- A `blocker`-level audit finding means status = `Draft — not approved`; never
  stamp a document `Approved`.
- Keep in-scope / out-of-scope / open questions clearly separated.
- §7 is process-centric: Flow Catalog first, then per-process blocks (each with its
  own activity+sequence for the same process), then the Screen Matrix. Never mix
  two processes' diagrams in one block; re-render diagrams only from confirmed
  step-by-step, never invent.
- Wireframe rendering is derive-only and HTML-first:
  - Trigger after screen/flow requirements are defined, or when the user asks to
    draw, sketch, or visualize wireframes for a flow.
  - Render low-fidelity wireframes as an inline HTML widget; if inline
    visualization is unavailable, write one self-contained HTML file in
    `clarify-output/`.
  - Use the platform from the BRD/PRD (mobile by default; web only when specified).
    Lay screens side by side in a responsive grid on a neutral background. Each
    screen is a phone/card frame with header (back + title), content area, and
    primary action button. Number screens ① ② ③ in flow order.
  - Use grayscale only: neutral placeholder fills, no brand colors, no images.
    Use real labels from the BRD/PRD for field names and buttons; use gray
    bars/dots for body copy and sensitive/masked values.
  - Only render fields, actions, and states the BRD/PRD specifies. Where the doc is
    silent, render a placeholder labeled `ASSUMPTION`; never invent a business
    rule, field, validation, or state.
  - Default to happy path. If the BRD/PRD lists alternate or error flows, add one
    screen per case and label it.
  - Map every wireframe screen back to its source requirement / BRD or PRD section
    in the screen footer and traceability summary.
- Do not require `from-spec` artifacts for a business BRD/PRD sign-off. Missing
  stories, AC, tests, API/data impact, or traceability are noted as optional
  build-ready layer inputs, not as blockers to a business-facing final document
  unless the user requested Dev/QA handoff readiness.

## Output
Write `clarify-output/final-prd.md` or `clarify-output/final-brd.md`
(matching the chosen standard) using the corresponding template.
