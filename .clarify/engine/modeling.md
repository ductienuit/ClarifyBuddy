# Engine: modeling (process-centric: flow sequence + state)

Purpose: expose missing behavior through models, organized **by business
process** (use case), not by diagram type. Models are a gap-finding tool, not
decoration. The diagrams are written **into the URD's §3.3 (process flow) and §3.4
(state)** — there is no separate `model-suggestions.md` file (Principle 13.11). Use
`templates/model-suggestions-template.md` as the working structure.

## Tool conventions (fixed — MERMAID ONLY)
The URD is **Mermaid-only** — no PlantUML.
- **Process flow = Mermaid `sequenceDiagram`** + `autonumber`, **no color** (participant
  phẳng) — viewer `https://mermaid.live/`. Goes in **§3.3**.
- **State diagram = Mermaid `stateDiagram-v2`**, **colored** via `classDef` (khởi tạo = xanh
  dương, trung gian/chờ = vàng, thành công = xanh lá, từ chối/lỗi = đỏ) — viewer
  `https://mermaid.live/`. Goes in **§3.4**.
Always attach the matching viewer link directly beneath each fenced block. Follow the
"Quy ước trình bày sơ đồ (Diagram conventions)" section of the URD.

## Stage role
- **from-idea (discovery):** keep models light. You MAY pick a few diverse processes to probe
  different gap types while scope is unconfirmed. Full per-process diagrams are not required yet.
- **improve model (process-centric):** build a **Flow Catalog** from the scope, then model
  **each key business process** with a `sequenceDiagram` (§3.3) and, where the process has a
  lifecycle, a colored `stateDiagram-v2` (§3.4). Cover the important lifecycle processes in
  scope (e.g. create → approve/reject → process → result, plus pending/unknown/reversal when
  money moves through core banking). Take the flow list from scope — never add out-of-scope flows.

## Per flow (read-by-flow order — Principle 13.13)
Lay each flow block out so the reader sees the picture first, then its reading:
1. **Flow overview** — one line: `Goal — …; Primary actor — …; Trigger — …; Outcome — …`.
2. **Sequence diagram (Mermaid)** — `sequenceDiagram` + `autonumber`, no color, for the process
   and its `alt/else` branches.
3. **Steps (reading of the diagram above)** — placed **below** the diagram, a plain step-by-step
   of the sequence. Table `Bước | Vai trò | Hành động | Mô tả xử lý / Kết quả`; step numbers
   match `autonumber`; branch points as bullets (`• Nếu … → …`). Put **no** error codes in steps
   and do **not** restate rules / screen behaviour — only the flow and its branches. End with one
   pointer line: `Quy định: BR.. (§3.5). Lỗi / thông báo / xử lý: §3.7.`

## State
- Model **entity state** and/or **transaction/operation state** as a colored `stateDiagram-v2`
  in **§3.4** when the feature has a process / async / risky / transactional action. A
  transactional feature with only entity state is `missing-operation-state`; flag it and add
  `OPEN QUESTION` for timeout / unknown / reversal handling. Entities named by lifecycle words
  with no defined states are `undefined-state`. Place the diagram **before** the state table.

## Rules
- **Coherence:** the sequence (§3.3) and state (§3.4) in one §3 block describe the **same**
  process. Mixing two processes' diagrams in one block is `mixed-process-diagram-block`.
- Diagrams are code the reader renders; never introduce steps/participants/branches not in the
  requirements — mark unknown branches `OPEN QUESTION` in the diagram (a note) and in the gaps
  list. Never invent a step to make a diagram look complete.
- Use the standard actor names (`Backend`, `Core Banking`, `App/Web`, `Đối tác ngoài`) from the
  Diagram conventions section.
- If a domain pack is selected, reuse its `common-flows.md` / `state-models.md`.

## Output
Write **into the URD** (no separate file): for each business process, a `sequenceDiagram` + Steps
table in **§3.3** and a colored `stateDiagram-v2` + state table in **§3.4**. The Flow Catalog
(in the draft §9.1) carries rule / error-code / user-story columns as the in-document
traceability spine.
