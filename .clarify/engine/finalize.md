# Engine: finalize

Purpose: after the spec is confirmed, assemble the **final sign-off document** —
a PRD or a BRD — in a standard, professional shape for a BA or PO. This can be a
business/product sign-off document from a resolved `from-idea` draft, or a
handoff-ready document when `from-spec` artifacts also exist. Do NOT re-derive
content: compose from prior `clarify-output/` files. Do NOT invent business rules.

## Decide the standard
1. Read the **Document Profile** (role + target standard + Language) from the draft —
   the `## Document Profile` heading in `prd-draft.md` or `brd-draft.md` — or from
   `$ARGUMENTS` (`prd` / `brd`).
2. If still unknown: ask. If not live, default by role (BA→BRD, PO→PRD) and label
   the choice `ASSUMPTION:` in the document.
3. `prd` → use `templates/final-prd-template.md`.
   `brd` → use `templates/final-brd-template.md`.

## Do
1. Read available outputs: prd-draft **or** brd-draft, plus any companions that
   exist: audit-report, edge-case-matrix, error-handling, model-suggestions,
   api-data-impact, stories, test-scenarios, traceability-matrix.
2. Compose the chosen template, pulling each section from the matching prior
   output. Keep wording testable and build-ready. Follow the **document presentation
   & naming conventions** (Principle 13):
   - **§0 "How to read this document"** up front (after the Executive summary):
     0.1 what-this-is + quick-read hint, 0.2 the **symbol-conventions** table
     (`F0n-Name`/`BRD-R#`/`BR#`/`T-#`/`A#/Q#/S#`, "codes stable across versions"),
     0.3 the **Glossary** moved to the front (carry the draft's §0.3 glossary).
   - **"How the system works (overview)"** before the requirements: an end-to-end
     narrative + ONE representative diagram (per-flow detail stays in the Functional
     Flows section).
   - **Business requirements = ONE grouped table** (Principle 13.7), columns
     `ID | Requirement | Why | Priority`, grouped by capability in journey order
     with a bold band row per group, Must → Should → Could within a group. `Why` is
     the business reason, never a `Source: BRx` cross-reference. Do NOT put
     flow/rule/test/source in this section — they live in §12 Traceability. Carry
     the draft's requirement sentences verbatim; never collapse them to a bare
     one-liner with no Why. Every requirement (including deferred) appears once and
     stays mapped in §12 traceability.
3. Assemble the **Functional Flows (process-centric)** section: build the Flow
   Catalog, then one block per business process, mapping each flow to its OWN
   step-by-step + Activity (PlantUML) + Sequence (Mermaid) from
   `model-suggestions.md`. Name flows **`F0n-Name`** (Principle 13.6): keep the
   number stable, append a short English feature name (Login/Consent/Token/Revoke/…),
   and lead the block heading with the Profile-language name (e.g. "Luồng F02-Login
   — Định danh người dùng"). Use `F0n-Name` consistently in the flow catalog, error
   map, screen matrix, traceability, and inside the diagrams. The activity and
   sequence in a block must be the **same** process — never pair process A's
   activity with process B's sequence (`mixed-process-diagram-block`). **Re-render
   only from the confirmed step-by-step**; do not invent new flow/logic/rules. If a
   key in-scope process has no diagram/flow, write an `OPEN QUESTION` naming the
   missing flow and the command that produces it (`from-spec` / `improve model`) —
   do not fabricate a diagram and do not drop in two unrelated diagrams. Place the
   Screen / Display Matrix **after** the flows. Viewer links: Mermaid
   `https://mermaid.live/`, PlantUML `https://www.plantuml.com/plantuml`
   (ref `https://plantuml.com/`).
3b. When the Screen / Display Matrix or flow steps define screens, add
   **Screen Wireframes (low-fidelity HTML)** right after the matrix. Render an
   inline HTML visualization widget from `templates/wireframe-template.html`
   whenever the final Markdown target supports inline HTML. If inline
   visualization is unavailable, write a single self-contained
   `clarify-output/wireframes.html` using the same template and link it from the
   final document and Appendix. Do not create ASCII wireframes as the primary
   artifact.
4. Preserve every `ASSUMPTION` / `OPEN QUESTION` / `SUGGESTION`. Group them into the
   **Open items** cluster (Assumptions / Open Questions / Suggested capabilities —
   BRD §13, PRD §13); then list the **blocker subset** of open questions + blocker
   audit findings in the **Sign-off blockers** section (BRD §14, PRD §14).
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
7. Put the high-level Customer/User Journey into the **"How the system works
   (overview)"** section (overview only + one representative diagram — detailed
   per-flow blocks live in the Functional Flows section). Carry over Error Handling
   & Message Mapping and the entity vs transaction/operation state summary. If a
   source artifact is missing, mark the section `OPEN QUESTION` and name the command
   that produces it.
8. Carry over the expanded columns from source files, using `F0n-Name` for every
   flow reference: the **Flow / Step** column in the error map (from
   `error-handling.md`), **trigger / owner system / terminal** in the state summary
   (from `model-suggestions.md`), and **Flow / Business rule / Error-State** plus a
   **Source** column (`← A#/BR#/S#/Q#` that produced each requirement) in the
   Traceability summary (from `traceability-matrix.md` + the draft's §18 register).
   Every requirement, including deferred ones, appears once in Traceability.
9. Emit the **Appendix: Artifact index (source)** listing only the `clarify-output/`
   companion files that actually exist — diagrams are referenced as source +
   viewer link, never as image files Clarify did not produce. List
   `clarify-output/wireframes.html`, `clarify-output/brd.html`/`prd.html`, and
   `clarify-output/decision-log.md` only when they were actually written.
9b. **Versioning — never overwrite silently.** If the target file already exists:
   (1) archive the existing file as `brd.v<N>.md` / `prd.v<N>.md` (N = its current
   Version); (2) bump the Version in Document control (1.0 → 1.1, or as the user
   directs); (3) add a **Change history** row (version, date, summary of what
   changed, driver — `answer sheet vN` / `CR-nn`). The canonical `brd.md` / `prd.md`
   always holds the latest version. **Never** use the word "final" in the file name
   (Principle 13.1). If a file appears hand-edited since Clarify wrote it, warn
   before overwriting.
9c. **Render the HTML document.** After writing `brd.md` / `prd.md`, render the
   companion `clarify-output/brd.html` / `prd.html` **from that Markdown** (one
   source of truth) following the `export` engine and Principle 13.2: pandoc
   md→html, Mermaid client-side + PlantUML plantuml.com hex `~h` with code fallback,
   requirement group-band rows → `colspan` merged cells, a TOC + an Artifact index,
   and no tool labels in the displayed content. This is best-effort: if the render
   toolchain is unavailable, say so and leave `brd.md` as the deliverable — never
   fail finalize because the HTML render could not run.
10. List any missing inputs and the command that produces each.

## Rules
- **Render headings in the Document Profile's Language** (Principle 13.3): when
  Language=vi, each heading is `Vietnamese (English term)`; when en, English only.
  Keep the machine-readable anchors in English ALWAYS: ASSUMPTION/OPEN QUESTION/
  SUGGESTION labels, all IDs (`A#/Q#/S#/V#/F0n-Name/BRD-R#/BR#/T-#/CR#`, error
  codes), and file names.
- Final ≠ invented: if a section has no source in prior outputs, mark it
  `OPEN QUESTION` rather than fabricating it.
- A `blocker`-level audit finding means status = `Draft — not approved`; never
  stamp a document `Approved`.
- Keep in-scope / out-of-scope / open questions clearly separated.
- The Functional Flows section is process-centric: Flow Catalog first (flows named
  `F0n-Name`), then per-process blocks (each with its own activity+sequence for the
  same process), then the Screen Matrix. Never mix two processes' diagrams in one
  block; re-render diagrams only from confirmed step-by-step, never invent.
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
Write `clarify-output/brd.md` or `clarify-output/prd.md` (matching the chosen
standard, **no "final" in the name**) using the corresponding template, then render
the companion `clarify-output/brd.html` / `prd.html` from it (best-effort, step 9c).
