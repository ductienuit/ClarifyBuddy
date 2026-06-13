# Workflow: export (HTML BRD/PRD)

## When to use
After `finalize`, to render the sign-off document as **one full, openable HTML
BRD/PRD** (`brd.html` / `prd.html`) **from `brd.md` / `prd.md`** — for easy reading,
sharing, and Word export, without anyone copying diagram code into web viewers. The
Markdown stays the single source of truth; the HTML is its rendering, **not** a
separate "review pack".

## Inputs
- Prior outputs in `clarify-output/`: `brd.md`/`prd.md` (preferred) or the draft,
  plus companions (`model-suggestions.md`, `error-handling.md`,
  `traceability-matrix.md`, `edge-case-matrix.md`, `stories.md`, `test-scenarios.md`,
  `api-data-impact.md`). Read; do not re-derive.
- `$ARGUMENTS`: `html` (default) | `all` (static render + offline + docx round-trip +
  wireframes) | `offline`.

## Engine sequence (ordered)
1. `trace` — ensure the traceability matrix is current (build if missing) and that it
   carries Flow (`F0n-Name`) / Business rule / Error-State / **Source** columns.
2. `export` — probe the environment, then render `clarify-output/brd.html` **from**
   `brd.md`: pandoc md→html (fallback minimal converter), Mermaid client-side,
   PlantUML via plantuml.com hex `~h` + code fallback, requirement group-bands →
   `colspan` merged cells, TOC + Artifact index, low-fi HTML wireframes (derive-only),
   optional LibreOffice docx round-trip, optional offline variant.

## Templates to fill
- `templates/review-pack-template.html` (the HTML shell: CSS + mermaid.js),
  `templates/wireframe-template.html` (low-fi screen wireframes).

## Outputs written
- `clarify-output/brd.html` (or `prd.html`) — always.
- `brd-assets/` (rendered diagram `.svg` + supporting files), `wireframes.html` —
  per phase.
- `brd.offline.html`, `brd.docx` (Word-export validation) — when mode/env allow.

## Phasing
- **Phase 1:** md→html (pandoc/fallback) into the HTML shell; strip tool labels;
  Mermaid client-side + PlantUML hex `~h` fallback-to-code; requirement group-bands
  → `colspan`; TOC + Artifact index. Always runs.
- **Phase 2:** low-fi HTML wireframes (derive-only), embedded in `brd.html` and saved
  as `wireframes.html`.
- **Phase 3:** static SVG render (local-first) + `brd.offline.html`.
- **Phase 4:** LibreOffice `soffice --convert-to docx` round-trip → `brd.docx`
  (validates the XML for Word).

## Done criteria
- A reader can open `brd.html` and see the **full BRD/PRD** — same content as
  `brd.md` — with every diagram rendered (Mermaid client-side; PlantUML rendered or
  code+link), no copy-paste to web viewers needed, and **no tool label** ("Clarify",
  "Visual Review Pack") on screen.
- The HTML is generated **from** `brd.md`/`prd.md` (one source of truth); the
  Markdown is unchanged; re-running `export` is idempotent.
- The Business requirements table renders as a **banded table** (group rows are
  `colspan` merged cells); a TOC and an **Artifact index (source)** link back to
  `brd.md` + companions.
- Wireframes derive from the Screen/Display Matrix + flow steps + rules + error map +
  state (derive-only; unknowns → ASSUMPTION / OPEN QUESTION; stamped low-fi, not
  final UI); responsive grayscale HTML widget, not ASCII art.
- Fallback works (the HTML opens even with no pandoc/renderer/`soffice`/network);
  diagrams degrade to code + viewer link; the build log records what was skipped.
- When `soffice` is available, the docx round-trip is attempted and its PASS/skip is
  recorded; nothing is invented.
