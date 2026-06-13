# Engine: export (Visual Review Pack)

Purpose: assemble a **regenerable, openable Review Pack** from the finalized
document — so BA/PO/Design/Dev/QA can review without copying diagram code into
plantuml.com / mermaid.live, and so Design gets screen flow + low-fi HTML
wireframes. This engine **composes from prior outputs and never invents** business
content; the only newly synthesized artifact is the low-fi HTML wireframe,
generated under strict derive-only rules. `final-brd.md` / `final-prd.md` stays
the single source of truth; the pack is derived and never edited as the master.

## Inputs (read; do not re-derive)
`clarify-output/final-brd.md` or `final-prd.md` (preferred) — else the draft
(`brd-draft.md`/`prd-draft.md`) — plus whatever companions exist:
`model-suggestions.md` (per-flow activity/sequence/state), `error-handling.md`,
`traceability-matrix.md`, `edge-case-matrix.md`, `stories.md`, `test-scenarios.md`,
`api-data-impact.md`. A missing companion does not block the pack — its section
becomes an `OPEN QUESTION` naming the command that produces it.

## Output
`clarify-output/review-pack/` (see `output-conventions.md` for the file tree).
Always produce `index.html` + `manifest.json`. Other artifacts per phase/mode.

## Modes & environment probe
- `$ARGUMENTS`: `html` (default, Phase 1–2 only) | `all` (attempt render + offline +
  signoff) | `offline`.
- **Probe the environment, then choose** (record the chosen mode in `manifest.json`):
  is there a Mermaid CLI (`mmdc`)? a `plantuml.jar` + Java? network access?
- **Never assume.** If a capability is absent, fall back (below) — never fail the step.

## Phase 1 — HTML pack (always)
1. Parse the final doc into sections (Document control, Executive summary, §7 Flow
   Catalog + per-flow blocks, §9.1 error map, §9.2 state, §13 traceability, §14/§15
   open items, Appendix). Do not rewrite content — transform/repackage it.
2. Fill `templates/review-pack-template.html` → `review-pack/index.html`:
   - **Mermaid (sequence/state/journey/screen-flow): render CLIENT-SIDE** via
     `mermaid.js` (CDN in `index.html`). Nothing leaves the machine.
   - **PlantUML activity:** embed a rendered `.svg` if available (Phase 3); else a
     PlantUML-server image URL **only if online + allowed**; else FALLBACK to the
     code block + viewer link with a visible "not rendered" badge.
   - Each diagram keeps a "view source / copy" affordance and a deep-link to the
     source section (e.g. "from final-brd §7.3.2").
3. Write `manifest.json` from `templates/review-manifest-template.json`: one entry
   per artifact `{type, source_section, path, render_status: rendered|source-only|
   open-question, viewer_link}`. This drives the in-page **Artifact Index** and the
   fallback display. After writing the pack files, prefer
   `python .clarify/scripts/clarify_tools.py manifest` to verify every manifest
   entry against what actually exists on disk (it merges your descriptive fields);
   if Python is unavailable, verify manually — never list a file that does not exist.

## Phase 2 — Screens & wireframes (derive-only)
4. `screens/screen-inventory.md` from the **Screen/Display Matrix (§7.5)** — one row
   only per matrix row; never invent a screen.
5. `screens/screen-flow.mmd` (Mermaid flowchart) — nodes = screens, edges =
   transitions taken from **flow steps**; no step → no edge.
6. `screens/wireframes.html` — a single self-contained **low-fi HTML visualization
   widget** per `templates/wireframe-template.html` and the rules below. Embed the
   same widget markup inside `review-pack/index.html` under **Low-fi Wireframes**.
   `screens/wireframe-brief.md` summarizes the screen set for Design handoff.

### Wireframe rendering (low-fidelity)
- **Trigger:** after the screen/flow requirements are defined, or when the user asks
  to draw, sketch, or visualize wireframes for a BRD/PRD flow.
- **Method:** render low-fidelity wireframes as an inline HTML visualization widget
  in `index.html` and as one self-contained `screens/wireframes.html` file. Do not
  use ASCII art as the primary wireframe output.
- **Layout:** mobile screens by default, or web frames when the BRD/PRD platform is
  web. Place screens side by side in a responsive grid on a neutral background.
  Each screen is a phone/card frame with a header (back + title), content area, and
  primary action button. Number screens ① ② ③ in flow order.
- **Low-fi style:** grayscale only. Use neutral placeholder fills, no brand colors,
  no images, sparse boxes/lines/simple outline icons only. Use real field names and
  button text from the BRD/PRD; use gray bars/dots for body copy and
  sensitive/masked values.
- **Fidelity:** only render fields, actions, and states the BRD/PRD specifies.
  Mirror the screen sequence and field list from the flow / screen-information
  section. Match the BRD/PRD language for all on-screen labels. Where the doc is
  silent, render a placeholder and label it `ASSUMPTION`; never invent business
  rules, fields, validations, actions, or states.
- **Coverage:** default to the happy path. If the BRD/PRD lists alternate or error
  flows (for example insufficient balance, failed OTP, eKYC for new customers), add
  one screen per case and label it.
- **Traceability:** each screen records the `Flow / Step` it serves. Every CTA maps
  to an `action` in the step-by-step; no match → `OPEN QUESTION`. Every field
  validation / error region maps to an error code in §9.1; none → `OPEN QUESTION`.
  Empty/loading/error/success regions come from §9.2 state; do not invent states.
  Footer lists sources used (Screen Sxx · Flow Fxx step n · requirement ids · BR ids
  · error codes). Add these screen mappings to the traceability map.
- **After rendering:** offer to add edge-case screens, switch platform, or upgrade
  to high-fidelity.

## Phase 3 — Static render + offline HTML (best-effort)
7. If a renderer is present: Mermaid `.mmd` → `.svg` via `mmdc`; PlantUML `.puml` →
   `.svg` via `plantuml.jar`. Save sources AND rendered files under `diagrams/` /
   `screens/`. If online + allowed and no local CLI, `mermaid.ink` / PlantUML server
   may be used — but treat diagram content as sensitive and record server use in the
   manifest.
8. `index-offline.html`: same content with **mermaid.js inlined** and rendered images
   embedded, so it opens with no network. If render failed, offline HTML still works
   via inlined mermaid.js for Mermaid; PlantUML falls back to code.

## Phase 4 — Sign-off pack (optional, mode=all)
9. `signoff-pack.pdf` (or `.docx`): a print-ready compile using the **rendered static
   images** (Phase 3). If images are unavailable, include the code blocks and note
   "diagram not rendered". Carry Document control, Executive summary, scope,
   requirements, rules, per-flow (step-by-step + images), error map, traceability,
   open items, sign-off blockers, approval table.

## Traceability map
10. `traceability/traceability-map.md` + `.csv`: extend the matrix to
    `Requirement → Flow → Screen → Rule → Error/State → Story → Test`. Flag orphans
    both directions (req with no flow/screen; flow/screen with no req).

## Review artifacts
11. `review/review-checklist.md` from `templates/review-checklist-template.md`
    (pre-filled from the finalize done-criteria + audit findings).
12. `review/open-questions.md`: consolidate §14 Open items + §15 Sign-off blockers.

## Rules (non-negotiable)
- **Render in the Document Profile's Language** (HTML pack headings + content
  follow the final doc's language). Keep the machine-readable anchors in English:
  ASSUMPTION/OPEN QUESTION/SUGGESTION labels, all IDs, error codes, file names.
- **Compose, never invent.** No business rule / screen / error / state beyond what
  the source files contain; unknowns → `ASSUMPTION` / `OPEN QUESTION`.
- **Fallback-first.** No renderer / no network / disallowed → the pack still opens;
  diagrams degrade to code + viewer link; `render_status: source-only` + a badge.
  Never fail `export` because rendering failed.
- **Do not edit** the final doc; `export` is idempotent (same inputs → same pack).
- **Domain-agnostic.** No feature/domain hardcoding.
- **Privacy.** Prefer client-side Mermaid + local PlantUML; gate any third-party
  server behind online mode and disclose it in the manifest.
