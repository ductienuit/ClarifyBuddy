# Engine: export (URD — HTML / Word)

Purpose: render the sign-off URD as **one full, openable document** — `urd.html` (HTML)
and, on request, `urd.docx` (Word) — **from `clarify-output/urd.md`** (single source of
truth). The rendered files are the *same document*, for reading and Word export; they are
**not** a separate "review pack". This engine **composes from the Markdown and never
invents** business content; the only newly synthesized artifact is the low-fi HTML
wireframe, under strict derive-only rules. `urd.md` stays the master; the rendered files are
derived and are never the place edits are made.

## Inputs (read; do not re-derive)
`clarify-output/urd.md` (preferred — it already carries user stories / rules / flows / states /
edges / errors inline) — else the draft `urd-draft.md`. There are no separate
`model-suggestions.md` / `error-handling.md` / `traceability-matrix.md` / `edge-case-matrix.md` /
`decision-log.md` files (Principle 13.11). A missing section in the source becomes an
`OPEN QUESTION` naming the command that produces it.

## Output
`clarify-output/urd.html` (default). Plus, per mode/env: `urd.docx` (Word), `urd.offline.html`,
`wireframes.html`.

## Modes & environment probe
- `$ARGUMENTS`: `html` (default) | `word` (also produce `urd.docx`) | `offline` | `all`
  (html + word + offline + wireframes).
- **Probe the environment, then choose** (note what ran in a short build log): is `pandoc`
  present? `soffice` (LibreOffice)? network access (for the Mermaid CDN)?
- **Never assume.** If a capability is absent, fall back (below) — never fail the step.

## Step 1 — Markdown → HTML (always)
1. Render `urd.md` → HTML. Prefer `pandoc urd.md -o urd.html --toc --standalone` for a correct
   TOC + sectioning; if `pandoc` is unavailable, fall back to a minimal built-in Markdown→HTML
   conversion. Wrap the body in the HTML shell `templates/urd-pack-template.html` (navy skin +
   a CDN `mermaid@10` include, `theme:"neutral" securityLevel:"loose"`, `lang="vi"`).
2. **Headings follow the Document Profile Language** already baked into `urd.md`
   (Principle 13.3) — render them verbatim; do not re-translate.
3. **Strip tool labels from the displayed content** (Principle 13.2): no "Clarify", no
   generator chrome on screen. Source comments (`<!-- … -->`) are dropped by the HTML render.

## Step 2 — Render diagrams (Mermaid-only)
4. **Mermaid (sequence + state): render CLIENT-SIDE** via `mermaid.js`. Keep each diagram as a
   `<pre class="mermaid">…</pre>` block. Nothing leaves the machine. There is **no PlantUML**.

## Step 3 — Banded tables (where present)
5. If a table has bold group-band rows spanning all columns (e.g. a `**Nhóm A — …**` row),
   convert each band into an HTML header row with a single `colspan` merged cell so the grouping
   reads as a banded table. Keep the data columns intact.

## Step 4 — TOC + Artifact index
6. Ensure a **Mục lục (table of contents)** at the top (from pandoc `--toc`, or built inline
   from the headings).
7. The Artifact index lives in §4.2 of `urd.md` — render it as-is; do not duplicate. Never emit
   a link to a file that does not exist.

## Step 5 — Screens & wireframes (derive-only)
8. When the URD has a Screen matrix (§3.6) or flow steps, render low-fi **wireframes** as an
   inline HTML widget per `templates/wireframe-template.html` and the rules below, embedded under
   a wireframes section and also saved as a self-contained `wireframes.html`.

### Wireframe rendering (low-fidelity)
- **Trigger:** after screen/flow requirements are defined, or when the user asks to draw/sketch/
  visualize wireframes for a flow.
- **Method:** inline HTML widget + one self-contained `wireframes.html`. No ASCII art as the
  primary output.
- **Layout:** mobile screens by default, or web frames when the URD platform is web. Side by
  side in a responsive grid on a neutral background. Each screen is a phone/card frame with a
  header (back + title), content area, and primary action. Number screens ① ② ③ in flow order.
- **Low-fi style:** grayscale only; neutral placeholder fills, no brand colors, no images. Real
  field names and button text from the URD; gray bars/dots for body copy and masked values.
- **Fidelity:** only render fields, actions, and states the URD specifies. Where the doc is
  silent, render a placeholder labeled `ASSUMPTION`; never invent fields/rules/validations/states.
- **Coverage:** default to the happy path; add one labelled screen per alternate/error flow.
- **Traceability:** each screen records the `F0n-Name / step` it serves; CTAs map to a step
  action (no match → `OPEN QUESTION`); error regions map to an `ERR-*` code (none → `OPEN
  QUESTION`); footer lists sources used.

## Step 6 — Word export (mode `word`/`all`, best-effort)
9. Produce `urd.docx` by round-tripping the HTML through LibreOffice:
   `soffice --headless --convert-to docx --outdir clarify-output clarify-output/urd.html`.
   Record **docx: PASS**; if `soffice` is absent or conversion fails, record it and continue —
   the HTML still stands. (Mermaid diagrams appear in Word as their source text/image per the
   converter; the visual render lives in `urd.html`.)

## Step 7 — Offline variant (mode `offline`/`all`, best-effort)
10. `urd.offline.html`: the same content with **mermaid.js inlined** so it opens with no network.

## Rules (non-negotiable)
- **One source of truth.** The rendered files come **from** `urd.md`; never author content in
  them, and never edit the Markdown from here. Idempotent (same inputs → same output).
- **No tool labels in displayed content** and **no "final" in any file name** (Principle 13.1–2).
- **Compose, never invent.** No business rule / screen / error / state beyond the source;
  unknowns → `ASSUMPTION` / `OPEN QUESTION`.
- **Fallback-first.** No pandoc / no `soffice` / no network → the HTML still opens; Mermaid
  needs the CDN (or the inlined offline build); record what was skipped. Never fail `export`.
- **Render in the Document Profile's Language** (the Markdown already is; preserve it). Keep
  machine anchors English: IDs (`F0n-Name`/`US-#`/`BR#`/`ERR-*`/`A#/Q#/S#`), field EN names,
  file names.
- **Domain-agnostic.** No feature/domain hardcoding.
- **Privacy.** Mermaid renders client-side; only the CDN script is fetched. Note network use in
  the build log; the offline build needs no network.
