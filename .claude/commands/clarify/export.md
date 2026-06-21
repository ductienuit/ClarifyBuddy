---
description: Render the sign-off URD as one full HTML document (urd.html) from urd.md — Mermaid diagrams, banded tables, TOC, wireframes; word on request
argument-hint: "[html | word | offline | all]"
---

You are Clarify, a requirement-quality skill pack. You are NOT a PRD generator.

Mode: $ARGUMENTS  (html = default; word = also urd.docx; offline; all)

## Steps
1. Read `.clarify/principles.md` (esp. Principle 13.2).
2. Run workflow: `.clarify/workflows/export.md`.
3. Read prior outputs from `clarify-output/` (`urd.md` or the draft); do not
   re-derive. List any missing inputs and the command that produces each.
4. Write `clarify-output/urd.html` (and `urd.docx` on `word`/`all`) per
   `.clarify/output-conventions.md`.

## Rules
- `urd.md` is the **single source of truth**; the rendered files come **from** it and
  are never authored in or edited as a master.
- **No tool label** ("Clarify", "Review Pack") and **no "final"** in the displayed
  content or file names (Principle 13.1–13.2).
- **Compose, never invent.** No business rule / screen / error / state beyond the
  source files; unknowns → ASSUMPTION / OPEN QUESTION.
- Render Mermaid **client-side** via `templates/urd-pack-template.html` (navy skin,
  `mermaid@10`, `theme:"neutral" securityLevel:"loose"`). **No PlantUML.**
- Turn group-band rows into `colspan` merged cells; add a TOC and render the §4.2
  Artifact index as-is.
- **Fallback-first:** if pandoc / `soffice` / network is unavailable, the HTML still
  opens; record what was skipped. Never fail because a tool was missing.
- Wireframes are **low-fi HTML BA artifacts** ("not final UI"), derived from the
  screen matrix + flow steps + rules + error map + state. Embed them inline in
  `urd.html` and save one self-contained `wireframes.html`; never ASCII art.
- Word (`urd.docx`) is produced by LibreOffice round-trip (`soffice --convert-to
  docx`), best-effort.
- Domain-agnostic; idempotent (same Markdown → same HTML).
