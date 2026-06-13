---
name: clarify-export
description: >-
  Clarify · Export — render the sign-off BRD/PRD as one full, openable HTML
  document (brd.html / prd.html) from brd.md / prd.md, so BA/PO/Design/Dev/QA can
  read, share, and Word-export it without copying diagram code into plantuml.com /
  mermaid.live. Use after finalize when the user wants the HTML version of the
  document: diagrams rendered (Mermaid client-side, PlantUML via plantuml.com),
  requirement groups as banded tables, a table of contents, low-fi HTML wireframes,
  and an artifact index linking back to the source. The Markdown stays the single
  source of truth; the HTML is its rendering and never invents content. Part of the
  Clarify requirement-quality pack.
---

# Clarify: Export (HTML BRD/PRD)

Render the sign-off document as one full, openable HTML BRD/PRD **from** `brd.md` /
`prd.md` (single source of truth). Compose from the Markdown; never invent content;
never author in or edit the HTML as a master. Not a "review pack".

## Steps
1. Read `.clarify/principles.md` (esp. Principle 13.2 — the HTML is a full BRD/PRD).
2. Determine the mode: `html` (default) | `all` (static render + offline + docx
   round-trip + wireframes) | `offline`. Probe the environment (pandoc? Mermaid CLI?
   plantuml.jar+Java? `soffice`/LibreOffice? network?).
3. Run the workflow `.clarify/workflows/export.md` (engines: `trace` → `export`).
4. Write `clarify-output/brd.html` (or `prd.html`) per `.clarify/output-conventions.md`.

## Rules
- Read `brd.md`/`prd.md` (or the draft) + companions; do not re-derive. Missing
  companion → its section is an OPEN QUESTION naming the command that produces it;
  the HTML still builds.
- Render **from** the Markdown via pandoc (fallback: minimal built-in converter) into
  the HTML shell `templates/review-pack-template.html`. **No tool label** ("Clarify",
  "Visual Review Pack") and **no "final"** in the displayed content or file names.
- Render Mermaid **client-side**; PlantUML via the plantuml.com hex `~h` scheme with
  the code kept inline as a fallback + a badge (or a locally rendered `.svg` when
  `plantuml.jar` is present).
- Turn requirement **group-band rows** into `colspan` merged cells; add a TOC and an
  **Artifact index (source)** linking back to `brd.md` + companions.
- **Fallback-first**: the HTML always opens even with no pandoc/renderer/network;
  record what was skipped in the build log. Never fail on render.
- Screens/wireframes are derive-only and low-fi HTML ("not final UI"); unknowns →
  ASSUMPTION / OPEN QUESTION. Render them inline in `brd.html` and as one
  self-contained `wireframes.html`, never as ASCII art.
- Domain-agnostic; idempotent (same Markdown → same HTML).

## Phases
1. md→html into the HTML shell + diagrams (Mermaid client-side, PlantUML hex `~h`
   fallback) + requirement group-bands → `colspan` + TOC + Artifact index.
2. Low-fi HTML wireframes (derive-only), embedded + saved as `wireframes.html`.
3. Static SVG render (local-first) + `brd.offline.html`.
4. LibreOffice `soffice --convert-to docx` round-trip → `brd.docx` (Word-export
   validation).
