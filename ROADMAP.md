# Clarify Roadmap

## MVP 1 (current)

- 6 commands: `from-idea`, `audit`, `improve`, `finalize`, `export`, `status`.
- 12 engines, 13 templates, 6 workflows.
- Single output standard: **URD (User Requirements Document)** in the URD template
  shape (cover → §1–§5, diagram conventions, §3 repeating per process).
- BA-workflow layer: output language follows the Document Profile (default `vi`,
  bilingual headings); questions carry elicitation owners (folded into §5); applied
  decisions recorded in Decisions made + Lịch sử thay đổi; final docs are versioned
  with Change history; `improve change-request` analyzes CR impact via traceability.
- Document Profile (BA/PO role + `Standard: URD` + domain + language) drives the
  sign-off URD via `finalize`.
- `modeling` emits **Mermaid-only** diagrams: sequence (autonumber, no color) +
  colored state — no PlantUML.
- `finalize`/`export` render the full URD from `urd.md`: `urd.html` (navy skin,
  Mermaid client-side, banded tables, TOC, low-fi wireframes, artifact index) and
  `urd.docx` (LibreOffice round-trip, on request).
- 36-entry anti-pattern catalog (yaml source of truth + human catalog).
- Reproducible 100-point / 10-dimension scoring rubric with bands.
- 3 mini domain packs (ecommerce, saas-b2b, fintech) + domain-pack template.
- Golden eval tests for the skill itself.
- Codex support via `AGENTS.md`.

## v1.1 (planned)

- Higher-fidelity Word export (native `docx` generation) beyond the current
  LibreOffice round-trip.
- Expand domain packs (healthcare, gov, marketplace).
- Harden diagram rendering in `export` (bundled offline Mermaid) beyond the current
  best-effort client-side + fallback.
- More golden eval cases + automated diffing harness.

## v2 (exploratory, OUT of MVP 1)

- Web app and/or CLI binary.
- Real Jira / Confluence / Linear integration.
- Accounts, persistence, team rubric customization.

## Non-goals

- Clarify will not become a generic PRD/document generator.
- Core stays domain-agnostic; domain knowledge lives only in domain packs.
