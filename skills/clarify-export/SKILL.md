---
name: clarify-export
description: >-
  Clarify · Export — render the sign-off URD as one full, openable HTML document
  (urd.html) from urd.md, plus an optional Word file (urd.docx), so BA/PO/Design/
  Dev/QA can read, share, and Word-export it without copying diagram code into
  mermaid.live. Use after finalize when the user wants the HTML/Word version:
  Mermaid diagrams rendered client-side, banded tables, a table of contents, low-fi
  HTML wireframes, and an artifact index linking back to the source. The Markdown
  stays the single source of truth; the rendering never invents content. Part of the
  Clarify requirement-quality pack.
---

# Clarify: Export (HTML / Word URD)

Render the sign-off document as one full, openable HTML URD **from** `urd.md`
(single source of truth). Compose from the Markdown; never invent content; never
author in or edit the rendered files as a master. Not a "review pack".

## Steps
1. Read `.clarify/principles.md` (esp. Principle 13.2 — the HTML/Word is a full URD).
2. Determine the mode: `html` (default) | `word` (also `urd.docx`) | `offline` |
   `all`. Probe the environment (pandoc? `soffice`/LibreOffice? network?).
3. Run the workflow `.clarify/workflows/export.md` (engines: `trace` → `export`).
4. Write `clarify-output/urd.html` (and `urd.docx` on word/all) per
   `.clarify/output-conventions.md`.

## Rules
- Read `urd.md` (or the draft); do not re-derive. Missing section → an OPEN QUESTION
  naming the command that produces it; the HTML still builds.
- Render **from** the Markdown via pandoc (fallback: minimal built-in converter) into
  the navy shell `templates/urd-pack-template.html`. **No tool label** ("Clarify",
  "Review Pack") and **no "final"** in the displayed content or file names.
- Render Mermaid **client-side** (`mermaid@10`, `theme:"neutral" securityLevel:"loose"`).
  **No PlantUML.**
- Turn group-band rows into `colspan` merged cells; add a TOC and render the §4.2
  Artifact index as-is.
- **Fallback-first**: the HTML always opens even with no pandoc/`soffice`/network;
  record what was skipped in the build log. Never fail on render.
- Screens/wireframes are derive-only and low-fi HTML ("not final UI"); unknowns →
  ASSUMPTION / OPEN QUESTION. Render them inline in `urd.html` and as one
  self-contained `wireframes.html`, never as ASCII art.
- Domain-agnostic; idempotent (same Markdown → same HTML).

## Phases
1. md→html into the navy shell + Mermaid (client-side) + group-bands → `colspan` +
   TOC + Artifact index.
2. Low-fi HTML wireframes (derive-only), embedded + saved as `wireframes.html`.
3. `urd.offline.html` (mermaid.js inlined).
4. LibreOffice `soffice --convert-to docx` → `urd.docx` (Word export).
