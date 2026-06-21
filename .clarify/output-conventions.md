# Clarify — Output Conventions

All generated artifacts are written to **`clarify-output/`** at the repo root.
Create the directory if it does not exist. Never scatter outputs elsewhere.

## Canonical output files

| File | Written by | Contains |
| --- | --- | --- |
| `clarify-output/audit-report.md` | `audit` | Score, band, blockers/major/minor, detected anti-patterns linked to dimensions. |
| `clarify-output/urd-draft.md` | `from-idea` | Shaped **working URD draft** at business altitude: Document Profile, scope, journey, user stories + acceptance criteria, screen matrix & field specs, business rules, **edge cases**, error/message table, state model, assumptions, open questions, suggestions, answer sheet. Intermediate — superseded by `urd.md` at finalize. |
| `clarify-output/urd.md` | `finalize` | The sign-off **URD** (URD skeleton). **No "final" in the name** — version lives in the Lịch sử thay đổi + archive name (Principle 13.1). |
| `clarify-output/urd.html` | `finalize` / `export` | Full HTML URD rendered **from `urd.md`** (one source of truth): rendered Mermaid diagrams, banded tables, TOC, artifact index. Navy skin (Principle 13.2). |
| `clarify-output/urd.docx` | `finalize word` / `export word` | Word rendering via LibreOffice round-trip (best-effort). |
| `clarify-output/urd.v<N>.md` | `finalize` | Archived prior versions (`finalize` never overwrites silently; Version bumps + Lịch sử thay đổi row). The canonical `urd.md` always holds the latest. |
| `clarify-output/wireframes.html` | `finalize` / `export` | Low-fidelity HTML wireframe widget when screen/flow requirements exist and inline HTML is unavailable. |

## Lean deliverable set (Principle 13.11) — analysis folds into the document

There is **no separate file** for edge cases, error handling, models/diagrams, user
stories, traceability, decisions, or elicitation. Each analysis is written **inside**
the draft and then the sign-off URD, so the final `clarify-output/` is exactly the set
above. The following files are **no longer produced**:

| Folded analysis | Now lives in | (was) file — not produced |
| --- | --- | --- |
| User stories + acceptance criteria | §7 (draft) / §3.2 (per process) | `stories.md` |
| Edge cases (error + no-error) | §11 (draft) / §3.7 (per process) | `edge-case-matrix.md` |
| Error → message → action map | §3.7 Thông báo / lỗi table | `error-handling.md` |
| Sequence / state diagrams | §3.3 / §3.4 (embedded Mermaid) | `model-suggestions.md` |
| User-story ↔ flow ↔ rule ↔ error traceability | Flow Catalog + §4.2 traceability note | `traceability-matrix.md` |
| Applied decisions / CRs | Decisions made + Lịch sử thay đổi | `decision-log.md` |
| Open questions grouped by owner | §5 Câu hỏi mở / draft §14 | `elicitation-pack.md` |

## Other working files (created as needed)

- `clarify-output/change-impact.md` — CR impact analysis read from the in-document
  trace spine (written by `improve change-request`; analysis only, transient).

## HTML / Word URD (written by `finalize` / `export`)

`export` (and `finalize` step 9c) render the sign-off doc as **one full, openable
document `clarify-output/urd.html` from `urd.md`** — a single source of truth, not a
separate "review pack". `urd.md` stays the master; the rendered files are its rendering
and never the place edits are made.

```
clarify-output/
  urd.html          # full URD: pandoc md→html + Mermaid (rendered client-side) + banded
                    #   tables + TOC + Artifact index; navy skin; no tool labels
  urd.docx          # LibreOffice round-trip of the HTML (mode word/all)
  urd.offline.html  # mermaid.js inlined; no network (mode offline/all)
  wireframes.html   # low-fi HTML screen wireframes (derive-only, "not final UI")
```

`export` **composes** from `urd.md` and never invents content: (a) Mermaid renders
client-side (no PlantUML); (b) group-band rows become `colspan` merged header cells;
(c) a TOC and the §4.2 **Artifact index** link back to `urd.md`; (d) `urd.docx` is the
LibreOffice round-trip of the HTML. Rendering is best-effort with fallback to diagram
code; no tool label ("Clarify", "Review Pack") appears in the displayed content
(Principle 13.2).

**Markdown→HTML hygiene (Principle 13.12):** in `urd.md`, always keep one blank line
between a bold label or paragraph and a pipe table directly below it. Without it pandoc
folds the label into the table and the table breaks in `urd.html`. This applies to every
label-then-table spot (steps, screen field specs, glossary, symbol table, error table,
artifact index, …).

**Diagrams & one-fact-one-place (Principle 13.13):** each §3 process block reads
*description → user stories → sequence (§3.3) → state (§3.4) → rules (§3.5) → screens
(§3.6) → errors (§3.7) → NFR (§3.8)*. Keep one fact in one place (rule → §3.5, error →
§3.7, screen → §3.6, step → §3.3). Diagrams are Mermaid-only and render client-side in
`urd.html`.

## Composability rules

- `improve` and `finalize` **read** prior files from `clarify-output/` rather than
  re-deriving them. If a required input file is missing, say so and suggest the command
  that produces it (e.g. run `/clarify:from-idea` first).
- `from-idea` is the entry point. After a `from-idea` draft, the next step is
  `improve answers`, then `finalize`.
- Re-running a command **overwrites** its canonical output file. Preserve user edits by
  warning before overwrite when the file appears hand-modified.

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
content; default `vi`, bilingual `Tiếng Việt (English)`), but the machine-readable
anchors ALWAYS stay in English so re-runs and `improve answers` can parse them: the
labels `ASSUMPTION:` / `OPEN QUESTION:` / `SUGGESTION:`, every ID
(`A#/Q#/S#/V#/F0n-Name/US-#/BR#/CR#`, error codes), field EN names, and file names.

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
refresh affected draft sections such as journey, user stories, screen matrix,
business rules, error/message table, state model, business-level NFRs, assumptions,
and open questions.

## File header

Every generated file starts with:

```
<!-- Generated by Clarify <command> on <date>. Source: <input>. -->
```
