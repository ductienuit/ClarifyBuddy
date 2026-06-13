---
name: clarify-export
description: >-
  Clarify · Export — package a Visual Review Pack from a finalized BRD/PRD so
  BA/PO/Design/Dev/QA can open and review it without copying diagram code into
  plantuml.com / mermaid.live. Use after finalize when the user wants a shareable,
  openable review artifact: an HTML pack with client-side-rendered diagrams,
  customer journey, per-flow activity + sequence, screen flow, low-fi HTML wireframes,
  state models, error/message mapping, traceability map, review checklist, and
  open questions. The final doc stays the source of truth; the pack is derived and
  never invents content. Part of the Clarify requirement-quality pack.
---

# Clarify: Export (Visual Review Pack)

Package an openable Review Pack from the finalized BRD/PRD. Compose from prior
outputs; never invent business content. The final doc is the source of truth.

## Steps
1. Read `.clarify/principles.md`.
2. Determine the mode: `html` (default) | `all` (render + offline + signoff) |
   `offline`. Probe the environment (Mermaid CLI? plantuml.jar+Java? network?).
3. Run the workflow `.clarify/workflows/export.md` (engines: `trace` → `export`).
4. Write `clarify-output/review-pack/` per `.clarify/output-conventions.md`.

## Rules
- Read `final-brd.md`/`final-prd.md` (or the draft) + companions; do not re-derive.
  Missing companion → its section is an OPEN QUESTION naming the command that
  produces it; the pack still builds.
- Render Mermaid **client-side** in the HTML; PlantUML rendered if a renderer is
  available, else code + viewer link with a "not rendered" badge.
- **Fallback-first**: pack always opens even with no renderer/network; record
  `render_status` in `manifest.json`. Never fail on render.
- Screens/wireframes are derive-only and low-fi HTML ("not final UI"); unknowns →
  ASSUMPTION / OPEN QUESTION. Render the wireframes as an inline HTML widget in
  `index.html` and one self-contained `screens/wireframes.html` file, never as
  ASCII art. Traceability map: Requirement → Flow → Screen → Rule → Error/State →
  Test, with orphans flagged.
- Domain-agnostic; idempotent.

## Phases
1. HTML pack (client-side Mermaid + PlantUML fallback) + manifest + artifact index.
2. Screen inventory + screen-flow + low-fi HTML wireframes (derive-only).
3. Static SVG render (local-first) + `index-offline.html`.
4. `signoff-pack.pdf/.docx` from rendered images.
