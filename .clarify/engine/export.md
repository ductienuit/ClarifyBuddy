# Engine: export (HTML BRD/PRD)

Purpose: render the sign-off document as **one full, openable HTML BRD/PRD**
(`clarify-output/brd.html` / `prd.html`) **from `brd.md` / `prd.md`** — a single
source of truth. The HTML is the *same document*, rendered for reading and Word
export; it is **not** a separate "review pack". This engine **composes from the
Markdown and never invents** business content; the only newly synthesized artifact
is the low-fi HTML wireframe, generated under strict derive-only rules. `brd.md` /
`prd.md` stays the master; the HTML is derived and is never the place edits are made.

## Inputs (read; do not re-derive)
`clarify-output/brd.md` or `prd.md` (preferred — it already carries the edge / error /
flow-diagram / state / traceability / decisions content inline) — else the draft
(`brd-draft.md`/`prd-draft.md`) — plus the kept companions that exist: `stories.md`,
`test-scenarios.md`, `api-data-impact.md`. There are no separate
`model-suggestions.md` / `error-handling.md` / `traceability-matrix.md` /
`edge-case-matrix.md` / `decision-log.md` files (Principle 13.11). A missing section
in the source becomes an `OPEN QUESTION` naming the command that produces it.

## Output
`clarify-output/brd.html` (or `prd.html`) — always. Plus, per mode/env:
`brd.offline.html`, a `brd-assets/` folder (rendered diagram `.svg` + supporting
files), `wireframes.html`, and a validated `brd.docx`.

## Modes & environment probe
- `$ARGUMENTS`: `html` (default) | `all` (attempt static render + offline + docx
  round-trip + wireframes) | `offline`.
- **Probe the environment, then choose** (note what ran in a short build log):
  is `pandoc` present? a Mermaid CLI (`mmdc`)? `plantuml.jar` + Java? `soffice`
  (LibreOffice)? network access?
- **Never assume.** If a capability is absent, fall back (below) — never fail the step.

## Step 1 — Markdown → HTML (always)
1. Render `brd.md` → HTML. Prefer `pandoc brd.md -o brd.html --toc --standalone`
   for a correct TOC + sectioning; if `pandoc` is unavailable, fall back to a
   minimal built-in Markdown→HTML conversion. Wrap the body in the HTML shell
   `templates/review-pack-template.html` (CSS + a CDN `mermaid.js` include).
2. **Headings follow the Document Profile Language** already baked into `brd.md`
   (Principle 13.3) — render them verbatim; do not re-translate.
3. **Strip tool labels from the displayed content** (Principle 13.2): no "Clarify",
   no "Visual Review Pack", no generator chrome appears on screen. Source comments
   (`<!-- … -->`) are dropped by the HTML render.

## Step 2 — Render diagrams
4. **Mermaid (sequence/state/journey/screen-flow): render CLIENT-SIDE** via
   `mermaid.js`. Nothing leaves the machine.
5. **PlantUML activity:** encode the diagram with the **plantuml.com hex `~h`**
   scheme (raw UTF-8 → deflate → hex, prefixed `~h`) and embed
   `https://www.plantuml.com/plantuml/svg/~h<hex>` as the image, **with the PlantUML
   code kept inline as a fallback** + a "view source" affordance and a visible
   "rendered via plantuml.com" / "not rendered" badge. If a local `plantuml.jar` +
   Java is present (mode `all`), prefer a locally rendered `.svg` in `brd-assets/`
   instead of the server URL. Treat diagram content as sensitive: only use
   plantuml.com when online is allowed, and note its use in the build log.

## Step 3 — Requirement table → merged cells
6. In the **Business requirements** table, convert each **group-band row** (the bold
   `**Group A — …**` row spanning the table) into an HTML header row with a single
   `colspan` merged cell, so the grouping reads as a banded table rather than a row
   with empty cells. Keep `ID | Requirement | Why | Priority` columns intact.

## Step 4 — TOC + Artifact index
7. Ensure a **table of contents** at the top (from pandoc `--toc`, or built inline
   from the headings).
8. Append an **Artifact index (source)** at the end (if `brd.md` already carries one,
   render that — do not duplicate): a **Used when (who / when)** column linking back to
   `brd.md` and the lean deliverable set that exists (audit-report, api-data-impact,
   stories, test-scenarios, version archive, wireframes, HTML). Do not link the draft,
   `edge-case-matrix.md`, `error-handling.md`, `model-suggestions.md`,
   `traceability-matrix.md`, or `decision-log.md` — those files are not produced
   (Principle 13.11). Never emit a link to a file that does not exist.

## Step 5 — Screens & wireframes (derive-only)
9. When the doc has a Screen / Display Matrix or flow steps, render low-fi
   **wireframes** as an inline HTML visualization widget per
   `templates/wireframe-template.html` and the rules below, embedded in `brd.html`
   under a "Wireframes" section and saved as a self-contained `wireframes.html`.

### Wireframe rendering (low-fidelity)
- **Trigger:** after the screen/flow requirements are defined, or when the user asks
  to draw, sketch, or visualize wireframes for a BRD/PRD flow.
- **Method:** inline HTML visualization widget in `brd.html` and one self-contained
  `wireframes.html`. Do not use ASCII art as the primary wireframe output.
- **Layout:** mobile screens by default, or web frames when the BRD/PRD platform is
  web. Side by side in a responsive grid on a neutral background. Each screen is a
  phone/card frame with a header (back + title), content area, and primary action.
  Number screens ① ② ③ in flow order.
- **Low-fi style:** grayscale only. Neutral placeholder fills, no brand colors, no
  images, sparse boxes/lines/simple outline icons. Real field names and button text
  from the BRD/PRD; gray bars/dots for body copy and sensitive/masked values.
- **Fidelity:** only render fields, actions, and states the BRD/PRD specifies.
  Mirror the screen sequence and field list. Match the BRD/PRD language for labels.
  Where the doc is silent, render a placeholder labeled `ASSUMPTION`; never invent
  business rules, fields, validations, actions, or states.
- **Coverage:** default to the happy path; add one labelled screen per alternate /
  error flow the BRD/PRD lists.
- **Traceability:** each screen records the `F0n-Name / step` it serves; every CTA
  maps to a step action (no match → `OPEN QUESTION`); every error region maps to an
  error code (none → `OPEN QUESTION`); footer lists sources used.

## Step 6 — Word-export validation (mode `all`, best-effort)
10. Round-trip the HTML through LibreOffice to confirm the XML is clean for Word:
    `soffice --headless --convert-to docx --outdir clarify-output clarify-output/brd.html`.
    If it produces `brd.docx`, record **docx round-trip: PASS**; if `soffice` is
    absent or conversion fails, record it and continue — the HTML still stands.

## Step 7 — Offline variant (mode `all`/`offline`, best-effort)
11. `brd.offline.html`: the same content with **mermaid.js inlined** and any rendered
    diagram images embedded, so it opens with no network. If render failed, offline
    HTML still works via inlined mermaid.js for Mermaid; PlantUML falls back to code.

## Rules (non-negotiable)
- **One source of truth.** The HTML is rendered **from** `brd.md`/`prd.md`; never
  author content in the HTML, and never edit the Markdown from here. Idempotent
  (same inputs → same HTML).
- **No tool labels in displayed content** ("Clarify", "Visual Review Pack") and
  **no "final" in any file name** (Principle 13.1–13.2).
- **Compose, never invent.** No business rule / screen / error / state beyond what
  the source contains; unknowns → `ASSUMPTION` / `OPEN QUESTION`.
- **Fallback-first.** No pandoc / no renderer / no `soffice` / no network → the HTML
  still opens; diagrams degrade to code + viewer link with a badge; record what was
  skipped. Never fail `export` because a tool was missing.
- **Render in the Document Profile's Language** (the Markdown already is; preserve it).
  Keep machine anchors English: IDs (`F0n-Name`/`BRD-R#`/`BR#`/`T-#`/`A#/Q#/S#`),
  error codes, labels, file names.
- **Domain-agnostic.** No feature/domain hardcoding.
- **Privacy.** Prefer client-side Mermaid + local PlantUML; gate plantuml.com behind
  online mode and disclose it in the build log.
