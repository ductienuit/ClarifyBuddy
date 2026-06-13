# Clarify Roadmap

## MVP 1 (current)

- 8 commands: `from-idea`, `from-spec`, `audit`, `improve`, `handoff`,
  `finalize`, `export`, `status`.
- 16 engines, 22 templates, 8 workflows.
- BA-workflow layer: output language follows the Document Profile; questions carry
  elicitation owners (+ `elicitation-pack.md`); decisions append to
  `decision-log.md`; final docs are versioned with Change history;
  `improve change-request` analyzes CR impact via traceability.
- Document Profile (BA/PO + PRD/BRD) drives a final sign-off document via
  `finalize`.
- `modeling` emits PlantUML activity + Mermaid sequence diagrams with viewer
  links.
- `export` packages a Visual Review Pack (openable HTML; Mermaid rendered
  client-side; PlantUML rendered best-effort with fallback; screen flow + low-fi
  wireframes + traceability map).
- 36-entry anti-pattern catalog (yaml source of truth + human catalog).
- Reproducible 100-point / 10-dimension scoring rubric with bands.
- 3 mini domain packs (ecommerce, saas-b2b, fintech) + domain-pack template.
- Golden eval tests for the skill itself.
- Codex support via `AGENTS.md`.

## v1.1 (planned)

- Standalone `write-brd` / `write-srs` (generate-from-scratch) engines —
  `finalize` already compiles a BRD/PRD from confirmed outputs.
- Expand domain packs (healthcare, gov, marketplace).
- Harden diagram rendering in `export` (bundled offline Mermaid, local PlantUML/
  Kroki) beyond the current best-effort client-side + fallback.
- More golden eval cases + automated diffing harness.

## v2 (exploratory, OUT of MVP 1)

- Web app and/or CLI binary.
- Real Jira / Confluence / Linear integration.
- Accounts, persistence, team rubric customization.

## Non-goals

- Clarify will not become a generic PRD/document generator.
- Core stays domain-agnostic; domain knowledge lives only in domain packs.
