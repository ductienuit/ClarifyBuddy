# Engine: modeling (process-centric: flow + activity + sequence + state)

Purpose: expose missing behavior through models, organized **by business
process** (use case), not by diagram type. Models are a gap-finding tool, not
decoration. Output is `model-suggestions.md` using its template.

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

## Per flow (in the catalog)
1. **Step-by-step**: numbered steps, each with actor, action, system response, and
   the related rule / validation / error code (or `—`).
2. **Activity (PlantUML)** for the process + its decision/exception branches.
3. **Sequence (Mermaid)** for the SAME process; if the flow is simple/single-system
   write "Sequence diagram not required — <reason>" instead.
4. **Gaps revealed / Open questions** for that flow.

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
Write `clarify-output/model-suggestions.md` using
`templates/model-suggestions-template.md`: a **Flow Catalog**, then one block per
flow (step-by-step + activity + sequence + gaps, all for the same process), then
the entity and transaction/operation state models.
