---
name: clarify-from-idea
description: >-
  Clarify · From-Idea — shape a raw idea or thin concept into a structured
  PRD/BRD draft. Use when the user has an idea (not a written spec yet) and wants
  it turned into scope, actors, requirements, business rules, edge cases, and
  open questions. Establishes the Document Profile (requester is BA or PO; target
  standard PRD or BRD). Never invents business rules — labels them ASSUMPTION or
  OPEN QUESTION. Part of the Clarify requirement-quality pack.
---

# Clarify: From-Idea

Shape a raw idea into a structured, business/product-ready PRD/BRD draft. You are
NOT a PRD generator and you never invent business rules.

## Steps
1. Read `.clarify/principles.md` (operating contract).
2. Establish the **Document Profile**: ask whether the requester is a **BA** or
   **PO**, and whether the target standard is a **PRD** or **BRD** (default
   BA→BRD, PO→PRD as an ASSUMPTION). Record it in section 0 of the draft.
3. If the input is thin, ask the **5 highest-impact, scope-blocking questions**
   (channel, product variant/type, customer segment, lifecycle ops in scope,
   depth) and offer a **Variant / Options Matrix** to choose from before drafting.
4. Run the workflow `.clarify/workflows/from-idea.md` (engines: clarify → shape →
   risk → edge → error-handling → modeling → write-prd).
5. Write **one working draft** per `.clarify/output-conventions.md` (`prd-draft.md`
   for PRD **or** `brd-draft.md` for BRD) with the edge cases, Error code & message
   table, flow diagrams/state, open items, and Answer Sheet folded in. No separate
   `edge-case-matrix.md` / `error-handling.md` / `model-suggestions.md` /
   `elicitation-pack.md` files (Principle 13.11).

## Rules
- **Title/structure the draft by the target standard.** BRD →
  `templates/brd-draft-template.md`, title "BRD Draft", business altitude (deep
  technical mechanics under "Downstream Technical Notes"). PRD →
  `templates/prd-template.md`, title "PRD Draft". Never title/structure a BRD as a
  PRD/SRS.
- Separate in-scope / out-of-scope / open questions.
- Requirements use actor + trigger + observable outcome.
- User-interaction drafts include Customer/User Journey and Screen Information /
  Display Matrix.
- Transactional/process drafts include error/message mapping and distinguish
  entity state from transaction/operation state.
- Before finishing, verify business draft completeness: journey, screen matrix,
  business rules, business-altitude risk/control, error/customer messages,
  authentication/confirmation, state summary, business-level measurable NFRs, and
  separated assumptions/open questions/suggestions.
- When done, the immediate next step is **clarify-improve** with the `answers`
  mode (apply the Answer Sheet). **clarify-from-spec** is *optional* — only to add
  build-ready stories/AC/tests/API/traceability + score by elaborating this same
  draft and **reusing** its edge/error/model (not starting over). Then
  **clarify-finalize**. Never tell the user to re-analyze from scratch.
