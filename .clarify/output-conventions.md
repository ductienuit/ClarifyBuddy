# Clarify — Output Conventions

All generated artifacts are written to **`clarify-output/`** at the repo root.
Create the directory if it does not exist. Never scatter outputs elsewhere.

## Canonical output files

| File | Written by | Contains |
| --- | --- | --- |
| `clarify-output/audit-report.md` | `audit`, `from-spec` | Score, band, blockers/major/minor, detected anti-patterns linked to dimensions. |
| `clarify-output/prd-draft.md` *or* `brd-draft.md` | `from-idea` | Shaped **working draft** at the standard's altitude (PRD product-focus / BRD business-focus): Document Profile, scope, journey, screen matrix, business rules, **edge cases**, error/message summary, state summary, flow diagrams, assumptions, open questions, suggestions, answer sheet. Intermediate — superseded by `brd.md`/`prd.md` at finalize; not a final deliverable. |
| `clarify-output/stories.md` | `from-spec` | User stories + acceptance criteria. |
| `clarify-output/test-scenarios.md` | `from-spec` | Step-level test scenarios (the in-doc §Test scenarios summarizes these). |
| `clarify-output/api-data-impact.md` | `from-spec` | API and data impact analysis. |
| `clarify-output/handoff-pack.md` | `handoff` | Dev pack + QA pack, traced to requirements (optional). |
| `clarify-output/prd.md` *or* `brd.md` | `finalize` | Standard sign-off document (PRD or BRD per the Document Profile). **No "final" in the name** — version lives in the Change history + archive name (Principle 13.1). |
| `clarify-output/prd.html` *or* `brd.html` | `export` | Full HTML BRD/PRD rendered **from `brd.md`/`prd.md`** (one source of truth): rendered diagrams, merged requirement group cells, TOC, artifact index. Not a "review pack" (Principle 13.2). |
| `clarify-output/brd.v<N>.md` *or* `prd.v<N>.md` | `finalize` | Archived prior versions (`finalize` never overwrites silently; Version bumps + Change history row). The canonical `brd.md`/`prd.md` always holds the latest. |
| `clarify-output/wireframes.html` | `finalize` / `export` | Low-fidelity HTML wireframe widget when screen/flow requirements exist and inline HTML is unavailable. |

## Lean deliverable set (Principle 13.11) — analysis folds into the document

There is **no separate file** for edge cases, error handling, models/diagrams,
traceability, decisions, or elicitation. Each analysis is written **inside** the draft
and then the sign-off document, so the final `clarify-output/` is exactly the set
above. The following files are **no longer produced**:

| Folded analysis | Now lives in | (was) file — not produced |
| --- | --- | --- |
| Edge cases (error + no-error) | §Edge cases (error table + "Edge cases without errors") | `edge-case-matrix.md` |
| Error → message → action map | §Error code & message table | `error-handling.md` |
| Activity / sequence / state diagrams | §Functional Flows (embedded) | `model-suggestions.md` |
| Requirement ↔ flow ↔ rule ↔ error traceability | §Requirements ↔ §Flow Catalog ↔ §Test scenarios + coverage paragraph | `traceability-matrix.md` |
| Applied decisions / CRs | §Decisions & open items + Document control → Change history | `decision-log.md` |
| Open questions grouped by owner | §Open items | `elicitation-pack.md` |

## Other working files (created as needed)

- `clarify-output/change-impact.md` — CR impact analysis read from the in-document
  traceability chain (written by `improve change-request`; analysis only, transient).

## HTML BRD/PRD (written by `export`)

`export` renders the sign-off doc as **one full, openable HTML document
`clarify-output/brd.html` (or `prd.html`) from `brd.md`/`prd.md`** — a single
source of truth, not a separate "review pack". `brd.md`/`prd.md` stays the master;
`brd.html` is its rendering and never the place edits are made.

```
clarify-output/
  brd.html  (or prd.html)   # full BRD/PRD: pandoc md→html + rendered diagrams + merged
                            #   requirement cells + TOC + Artifact index; no tool labels
  brd.offline.html          # mermaid.js inlined; images embedded; no network (mode all/offline)
  brd-assets/               # rendered diagram .svg + supporting files when produced
  wireframes.html           # low-fi HTML screen wireframes (derive-only, "not final UI")
```

`export` **composes** from `brd.md` + companions and never invents content:
(a) Mermaid renders client-side, PlantUML via plantuml.com hex `~h` encoding with a
code fallback; (b) requirement group-band rows become `colspan` merged header cells;
(c) a TOC and an **Artifact index (source)** link back to `brd.md` + companions;
(d) the HTML round-trips through LibreOffice (`soffice --convert-to docx`) so Word
export validates. Rendering is best-effort with fallback to diagram code + viewer
link; no tool label ("Clarify", "Visual Review Pack") appears in the displayed
content (Principle 13.2).

**Markdown→HTML hygiene (Principle 13.12):** in `brd.md`/`prd.md`, always keep one
blank line between a bold label or paragraph and a pipe table directly below it.
Without it pandoc folds the label into the table and the table breaks in `brd.html`.
This applies to every label-then-table spot (step-by-step, screen matrix, symbol
table, glossary, requirements, artifact index, …).

**Read-by-flow & deep-link anchors (Principle 13.13):** each §8.x flow reads
*overview → diagram(s) → Steps (3-col, below the diagram) → pointer line*; the pointer
deep-links to that flow's error sub-header in §11.1 (`[…](#err-f0n)`). The §11.1
register is split by flow, each under `#### F0n-Name {#err-f0n}`. `export` must keep
pandoc's `header_attributes` enabled so those ids survive into `brd.html` and the
deep-links resolve. Keep one fact in one place (rule → §7, error → §11.1 anchor, screen
→ §Screens, step → flow only); APIs are named at the business level, never
path/method/schema.

## Composability rules

- `improve`, `handoff`, and `finalize` **read** prior files from `clarify-output/` rather
  than re-deriving them. If a required input file is missing, say so and suggest
  the command that produces it (e.g. run `/clarify:from-spec` first).
- When `from-spec` runs on a Clarify **draft** already in `clarify-output/`, it
  **reuses** the draft's own edge / error / model / state sections (which now live
  inside the draft, not in separate files) and adds only the build-ready layer
  (scored audit, stories, AC, tests, api-data-impact, in-document traceability) — it
  does not start over and does not re-emit dropped companion files.
- `from-idea` and `from-spec` are **entry points**, not a forced sequence. After a
  `from-idea` draft, the next step is `improve answers`; `from-spec` is optional
  for Dev/QA build-ready elaboration.
- Re-running a command **overwrites** its canonical output file. Preserve user
  edits by warning before overwrite when the file appears hand-modified.

## Labeled items & answer sheet (must be answerable in-place)

Every labeled item the user must decide on is **numbered with a stable ID** so the
user can reference it and reply fast on the first draft:

- `A#` — Assumption (e.g. `A1`)
- `Q#` — Open Question / Clarifying Question (e.g. `Q1`)
- `S#` — Suggested Additional Capability (e.g. `S1`)
- `V#` — Variant / option to select (e.g. `V1`)

Render each as `- **A1** — <text>` (keep the label word too, e.g.
`**A1** — ASSUMPTION: …`, for back-compat). IDs are stable: never renumber an
existing item on re-run; append new ones.

**Language:** documents render in the Document Profile's `Language` (headings +
content), but the machine-readable anchors ALWAYS stay in English so re-runs and
`improve answers` can parse them: the labels `ASSUMPTION:` / `OPEN QUESTION:` /
`SUGGESTION:`, every ID (`A#/Q#/S#/V#/F#/BR#/CR#`, error codes), and file names.

Any output that contains these items ends with a single **Answer sheet** — a
fenced ```text block the user can copy, fill in, and paste back in one action:

```text
# Copy this block, fill after each ID, send back.
# Assumptions — keep | override: <value>
A1: keep
A2: keep
# Open questions — your answer (or "skip"):
Q1:
Q2:
# Suggestions — yes | no | later:
S1:
S2:
# Variant — pick one id:
Variant: V1
```

`improve answers` and re-runs **read this answer sheet** and apply it as a
resolved-draft pass: `override` updates the assumption; a `Q#` answer becomes a
confirmed rule/scope item (no longer OPEN QUESTION); `S# = yes` moves the
suggestion into scope; `Variant` fixes the chosen option. Map strictly by ID, and
refresh affected draft sections such as journey, screen matrix, business rules,
error/message summary, state summary, business-level NFRs, assumptions, and open
questions.

## File header

Every generated file starts with:

```
<!-- Generated by Clarify <command> on <date>. Source: <input>. -->
```
