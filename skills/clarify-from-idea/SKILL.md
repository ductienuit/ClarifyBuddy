---
name: clarify-from-idea
description: >-
  Clarify · From-Idea — shape a raw idea or thin concept into a structured URD
  (User Requirements Document) draft. Use when the user has an idea (not a written
  spec yet) and wants it turned into scope, user groups, user stories, business
  rules, screens, flows, states, edge cases, and open questions. Establishes the
  Document Profile (requester is BA or PO; standard is always URD). Never invents
  business rules — labels them ASSUMPTION or OPEN QUESTION. Part of the Clarify
  requirement-quality pack.
---

# Clarify: From-Idea

Shape a raw idea into a structured, business-ready URD draft. You are NOT a PRD
generator and you never invent business rules.

## Steps
1. Read `.clarify/principles.md` (operating contract).
2. Establish the **Document Profile**: the standard is always **URD**; ask whether
   the requester is a **BA** or **PO** (shapes tone), the domain, and the Language
   (default `vi`). Record it in section 0 of the draft.
3. If the input is thin, ask the **5 highest-impact, scope-blocking questions**
   (channel, product variant/type, customer segment, lifecycle ops in scope,
   depth) and offer a **Variant / Options Matrix** to choose from before drafting.
4. Run the workflow `.clarify/workflows/from-idea.md` (engines: clarify → shape →
   risk → edge → error-handling → story → modeling → write-urd).
5. Write **one working draft** per `.clarify/output-conventions.md` (`urd-draft.md`)
   with user stories, edge cases, the error & message table, flow diagrams/state,
   open items, and the Answer Sheet folded in. No separate `edge-case-matrix.md` /
   `error-handling.md` / `model-suggestions.md` / `stories.md` / `elicitation-pack.md`
   files (Principle 13.11).

## Rules
- Title the draft "URD Draft" using `templates/urd-draft-template.md`, output
  `clarify-output/urd-draft.md`, business altitude. Headings bilingual `Tiếng Việt
  (English)` when Language=vi; IDs/labels/error codes/field-EN-names stay English.
- Separate in-scope / out-of-scope / open questions.
- User stories use role + want + benefit + acceptance criteria.
- UI drafts include the end-to-end journey and a Screen matrix & field specs.
- Transactional/process drafts include error/message mapping and distinguish
  entity state from transaction/operation state. Diagrams are **Mermaid-only**.
- Before finishing, verify business draft completeness: journey, user stories,
  screen matrix, business rules, business-altitude risk/control, error/customer
  messages, authentication/confirmation, state model, business-level measurable
  NFRs, and separated assumptions/open questions/suggestions.
- When done, the immediate next step is **clarify-improve** with the `answers` mode
  (apply the Answer Sheet), then **clarify-finalize** to produce the URD. Never tell
  the user to re-analyze from scratch.
