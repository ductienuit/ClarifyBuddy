# Workflow: export (URD — HTML / Word)

## When to use
After `finalize`, to render the sign-off URD as **one full, openable document** — `urd.html`
(HTML) and, on request, `urd.docx` (Word) — **from `urd.md`** — for easy reading, sharing, and
Word export, without anyone copying diagram code into web viewers. The Markdown stays the single
source of truth; the rendered files are its rendering, **not** a separate "review pack".

## Inputs
- Prior outputs in `clarify-output/`: `urd.md` (preferred — it carries the user-story / edge /
  error / diagram / state content inline) or the draft `urd-draft.md`. No separate model /
  error-handling / traceability / edge / decision-log files exist (Principle 13.11). Read; do
  not re-derive.
- `$ARGUMENTS`: `html` (default) | `word` (also produce `urd.docx`) | `offline` | `all`.

## Engine sequence (ordered)
1. `trace` — verify in-document traceability (User stories ↔ Flow Catalog ↔ rules ↔ errors);
   report orphans/dangling refs. No separate traceability file is built.
2. `export` — probe the environment, then render `clarify-output/urd.html` **from** `urd.md`:
   pandoc md→html (fallback minimal converter) wrapped in the navy `urd-pack-template.html`,
   Mermaid client-side (no PlantUML), banded tables → `colspan`, TOC + Artifact index, low-fi
   HTML wireframes (derive-only), optional LibreOffice docx, optional offline variant.

## Templates to fill
- `templates/urd-pack-template.html` (the navy HTML shell: CSS + mermaid@10),
  `templates/wireframe-template.html` (low-fi screen wireframes).

## Outputs written
- `clarify-output/urd.html` — always.
- `wireframes.html` — when screens exist.
- `urd.docx` (LibreOffice round-trip) — on `word`/`all`.
- `urd.offline.html` — on `offline`/`all`.

## Phasing
- **Phase 1:** md→html (pandoc/fallback) into the navy shell; strip tool labels; Mermaid
  client-side; banded tables → `colspan`; TOC + Artifact index. Always runs.
- **Phase 2:** low-fi HTML wireframes (derive-only), embedded in `urd.html` and saved as
  `wireframes.html`.
- **Phase 3:** `urd.offline.html` (mermaid.js inlined).
- **Phase 4:** LibreOffice `soffice --convert-to docx` → `urd.docx`.

## Done criteria
- A reader can open `urd.html` and see the **full URD** — same content as `urd.md` — with every
  Mermaid diagram rendered client-side, no copy-paste to web viewers needed, navy skin, and
  **no tool label** on screen.
- The HTML is generated **from** `urd.md` (one source of truth); the Markdown is unchanged;
  re-running `export` is idempotent.
- Banded tables render as `colspan` merged cells; a TOC and the **Artifact index (§4.2)** link
  back to `urd.md` + the lean set only — no link to a dropped file (Principle 13.11).
- Wireframes derive from the Screen matrix + flow steps + rules + error map + state (derive-only;
  unknowns → ASSUMPTION / OPEN QUESTION; stamped low-fi, not final UI); responsive grayscale
  HTML widget, not ASCII art.
- Fallback works (the HTML opens even with no pandoc/`soffice`); the build log records what was
  skipped.
- When `soffice` is available and `word`/`all` is requested, `urd.docx` is produced and its
  PASS/skip is recorded; nothing is invented.
