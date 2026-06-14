# Engine: modeling (process-centric: flow + activity + sequence + state)

Purpose: expose missing behavior through models, organized **by business
process** (use case), not by diagram type. Models are a gap-finding tool, not
decoration. The diagrams are written **into the document's Functional Flows section**
— there is no separate `model-suggestions.md` file (Principle 13.11). Use
`templates/model-suggestions-template.md` as the working structure.

## Tool conventions (fixed — never ambiguous)
- **Activity diagram = PlantUML** — viewer `https://www.plantuml.com/plantuml`
  (ref `https://plantuml.com/`).
- **Sequence diagram = Mermaid** — viewer `https://mermaid.live/`.
- **State diagram = Mermaid** — viewer `https://mermaid.live/`.
Always attach the matching viewer link directly beneath each fenced block.

## Stage role
- **from-idea (discovery):** keep models light. You MAY pick a few diverse
  processes to probe different gap types while scope is unconfirmed. Pairs are
  NOT required at this stage.
- **from-spec and improve (process-centric):** build a **Flow Catalog** from the
  scope/spec, then model **each key business process**. For every decision-rich or
  multi-system process, produce a **pair** for that SAME process:
  - Activity (PlantUML) = business/process flow + decision branches.
  - Sequence (Mermaid) = system interaction.
  Cover at least the important lifecycle processes that exist in scope (e.g. for a
  deposit product: open, full early withdrawal, partial early withdrawal,
  maturity & renewal, and pending/unknown/reversal handling if money moves through
  core banking). Take the flow list from scope — never add out-of-scope flows.

## Per flow (read-by-flow order — Principle 13.13)
Lay each flow block out so the reader sees the picture first, then its reading:
1. **Flow overview** — one line right after the heading: `Goal — …; Primary actor —
   …; Trigger — …; Outcome — …`.
2. **Activity (PlantUML)** for the process + its decision/exception branches.
3. **Sequence (Mermaid)** for the SAME process; if the flow is simple/single-system
   write "Sequence diagram not required — <reason>" instead.
4. **Steps (reading of the diagram above)** — placed **below** the diagram, a plain
   step-by-step of the **sequence** diagram (or the **activity** when there is no
   sequence). Table is **three columns** `Step | Actor | Action / processing`; branch
   points are bullets (`• If … → …`). Put **no** error codes in steps and do **not**
   restate rules or screen behaviour — only the flow and its branches. End with one
   pointer line: `Rules: BR.. (§7). Errors / messages / retry & tests: [§11.1 —
   F0n-Name](#err-f0n).`
5. **Gaps revealed / Open questions** for that flow.

## State
- Model **entity state** and **transaction/operation state** as two distinct
  Mermaid diagrams when the feature has a process / async / risky / transactional
  action. Only-entity-state for such a feature is `missing-operation-state`; flag
  it and add `OPEN QUESTION` for timeout / unknown / reversal handling. Entities
  named by lifecycle words with no defined states are `undefined-state`.

## Rules
- **Coherence:** within one flow block, activity and sequence describe the **same**
  process. Placing activity of process A beside sequence of process B is
  `mixed-process-diagram-block`.
- Diagrams are code the reader renders; never introduce steps/participants/branches
  not in the requirements — mark unknown branches `OPEN QUESTION` in the diagram
  (a note) and in the gaps list. Never invent a step to make a diagram look complete.
- If a domain pack is selected, reuse its `common-flows.md` / `state-models.md`.

## Output
Write **into the document's Functional Flows section** (no separate file): a **Flow
Catalog** (with rule / error-code / requirement columns — the in-document traceability
spine), then one block per flow in read-by-flow order (overview → activity → sequence
→ Steps below the diagram → gaps, all for the same process), then the entity and
transaction/operation state summary.
