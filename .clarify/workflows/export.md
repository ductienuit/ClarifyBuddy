# Workflow: export (Visual Review Pack)

## When to use
After `finalize` (or after `from-spec`), to package an **openable Review Pack** so
reviewers don't copy diagram code into web viewers and Design gets screen flow +
low-fi HTML wireframes. The final doc remains the source of truth; the pack is
derived.

## Inputs
- Prior outputs in `clarify-output/`: `final-brd.md`/`final-prd.md` (preferred) or
  the draft, plus companions (`model-suggestions.md`, `error-handling.md`,
  `traceability-matrix.md`, `edge-case-matrix.md`, `stories.md`, `test-scenarios.md`,
  `api-data-impact.md`). Read; do not re-derive.
- `$ARGUMENTS`: `html` (default) | `all` (render + offline + signoff) | `offline`.

## Engine sequence (ordered)
1. `trace` — ensure the traceability matrix is current (build if missing) and extend
   it with a Screen column for the pack.
2. `export` — probe the environment, then assemble `clarify-output/review-pack/`:
   HTML pack (client-side Mermaid + PlantUML fallback), manifest, screen inventory +
   screen-flow + low-fi HTML wireframes (derive-only), static render + offline HTML
   (best-effort), optional sign-off pack, review checklist, open questions.

## Templates to fill
- `templates/review-pack-template.html`, `templates/review-manifest-template.json`,
  `templates/screen-inventory-template.md`, `templates/wireframe-template.html`,
  `templates/traceability-map-template.md`, `templates/review-checklist-template.md`.

## Outputs written
- `clarify-output/review-pack/index.html` + `manifest.json` (always).
- `diagrams/`, `screens/` (inventory + screen-flow + `wireframes.html`),
  `traceability/`, `review/` — per phase.
- `index-offline.html`, rendered `.svg/.png`, `signoff-pack.pdf` — when mode/env allow.

## Phasing
- **Phase 1:** HTML pack (client-side Mermaid, PlantUML fallback-to-code), manifest,
  artifact index — parse-only.
- **Phase 2:** screen inventory + screen-flow + low-fi HTML wireframes
  (derive-only, embedded in `index.html` and saved as `screens/wireframes.html`).
- **Phase 3:** static SVG render (local-first) + `index-offline.html`.
- **Phase 4:** `signoff-pack.pdf/.docx` from rendered images.

## Done criteria
- BA can open `index.html` and see every diagram rendered (Mermaid client-side;
  PlantUML rendered or code+link) — **no copy-paste to web viewers needed**.
- Each flow has diagram source AND a rendered output OR a recorded fallback.
- Screen flow derives from the screen inventory; wireframes derive from the
  Screen/Display Matrix + flow steps + rules + error map + state (derive-only;
  unknowns → ASSUMPTION / OPEN QUESTION; stamped low-fi, not final UI). Wireframes
  render as a responsive grayscale HTML widget, not ASCII art.
- Traceability map covers Requirement → Flow → Screen → Rule → Error/State → Test;
  orphans flagged.
- Review checklist + artifact index present; manifest records render status.
- Fallback works (pack opens even with no renderer/network); nothing invented; the
  final doc is unchanged; re-running `export` is idempotent.
