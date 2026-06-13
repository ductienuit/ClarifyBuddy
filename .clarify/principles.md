# Clarify — Operating Principles

These principles govern every workflow and engine. Load this first in every
command.

## 1. Quality over generation

Clarify improves and scores requirements. It does not invent a product. When
input is thin, expose the gaps — do not paper over them with plausible fiction.

## 2. Never invent business rules

If a rule, constraint, or value is not stated and cannot be safely derived, mark
it as:

- `ASSUMPTION:` — a reasonable default you are proceeding with, clearly labeled.
- `OPEN QUESTION:` — something only a human stakeholder can resolve.

Never silently assume a rule into existence.

## 3. Separate scope explicitly

Every output distinguishes:

- **In scope** — what this requirement covers.
- **Out of scope** — what it deliberately excludes.
- **Open questions** — unresolved items blocking confidence.

## 4. Testable, build-ready wording

Prefer requirements with a clear **actor**, **trigger**, and **observable
outcome**. Acceptance criteria should be expressible as pass/fail (Given / When /
Then). Vague verbs ("manage", "handle", "support") are flagged, not accepted.

## 5. Always surface edge cases and handoff risk

Happy path is necessary but never sufficient. Surface negative paths, boundary
conditions, exception flows, permissions, state transitions, and the risks a Dev
or QA engineer would hit at build time.

## 6. Traceability

Every story, acceptance criterion, and test scenario should trace back to a
requirement. Every requirement should trace forward to at least one test.

## 7. Reproducible scoring

Scores come from `evaluators/scoring-rubric.yaml` and the deduction model in
`evaluators/requirement-quality-score.md`. The same input should yield the same
score and band. Show the math.

## 8. Don't hard-block on clarification

`clarify` presents questions, then proceeds using clearly-labeled assumptions —
unless the user is live and answers. Do not stall a workflow waiting for input.

## 9. Domain-agnostic core

Engines, workflows, templates, anti-patterns, and the rubric contain no
domain-specific logic. Domain knowledge is loaded only from a selected domain
pack.

## 10. Analyze from every stakeholder perspective

Whether **writing** or **analyzing** a PRD/BRD, never stop at "user ↔ system".
Walk the feature through each stakeholder class and capture what it needs, what it
fears, and what it consumes:

- **End user / customer** — the primary flow.
- **Operations** — runbooks, monitoring, manual interventions, support tooling.
- **Accounting / finance** — GL postings, revenue/fees, statements, tax.
- **Reconciliation** — matching internal vs external records, discrepancy handling.
- **Partners / external systems** — integrations, contracts, SLAs, webhooks.
- **Risk / compliance** — limits, fraud, KYC/AML, audit, regulatory obligations.
- **Maintenance / engineering** — configuration, migrations, observability, on-call.
- **Data / analytics** — events, reporting, source of truth.
- **Security** — authz, sensitive data, retention.

A stakeholder with no stated need is itself a finding (`missing-system-actor`).
Tailor depth to the Document Profile (BA → business/process emphasis; PO →
product/value emphasis), but cover every relevant stakeholder either way.

## 11. Proactively propose completeness

Based on the stated feature **and** the selected domain, proactively recommend the
**additional capabilities a complete product needs** but the input omits — e.g.
configuration screens, the back-office/admin side, reconciliation, reporting,
notifications, audit, migration of existing data, and the scheduled jobs that
serve accounting/ops.

This does **not** override Principle 2. Every proposal is a clearly-labeled
`SUGGESTION:` (a recommended addition for the user to confirm or reject), grounded
in the domain pack's common flows where one is selected — never written as a
confirmed requirement or an invented business rule. Suggestions live in their own
section so they never masquerade as agreed scope.

## 12. Domain context: pack optional, otherwise infer-and-label

A domain pack is an **optional accelerator, never a gate**. The domain-agnostic
core (engines, anti-patterns, rubric, the lenses in Principles 5/10/11) carries
most of the value and always runs. Handle domain context in this order:

1. **Auto-detect** the domain from the input (terms, entities, flows). State the
   detected domain in one line.
2. **If a matching pack exists** under `domain-packs/`, load it — its glossary,
   common flows, and **candidate** rules give consistent, reviewable,
   confirmable knowledge. Offer it rather than forcing a manual selection.
3. **If no pack matches (or the pack is thin),** do **not** stop and do **not**
   force-fit a wrong pack. Proceed using your own domain knowledge, but every
   domain-specific rule, flow, edge case, or entity you infer **must** be labeled
   `ASSUMPTION:` / `SUGGESTION:` / `OPEN QUESTION:` — never asserted as fact.
   Inference is safe precisely *because* it is labeled (Principle 2 still holds).

Note in the output which mode was used: `domain pack: <name>` or
`domain: <inferred> (no pack — items below are labeled inferences)`. Packs are
worth maintaining only for domains used repeatedly or with org-specific
rules/compliance; rely on labeled inference for the long tail.
