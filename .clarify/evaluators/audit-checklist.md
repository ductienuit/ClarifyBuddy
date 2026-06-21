# Clarify Audit Checklist

A fast, ordered pass an agent runs during `audit`. For each item, note pass /
partial / fail and the anti-pattern id(s) it maps to.

Apply the checklist to the URD. Journey, user stories + acceptance criteria,
screens & field specs, rules, exceptions, messages, state model, business NFRs, and
stakeholder coverage are **core** URD checks. Only deep step-level test scenarios
and a full API/data impact analysis are out of URD scope (BA altitude); report
their absence as out-of-scope, not as defects.

## Clarity
- [ ] Every requirement names an **actor** (`ambiguous-actor`).
- [ ] Every requirement names a **trigger** (`missing-trigger`).
- [ ] Every requirement states an **outcome** (`missing-outcome`).
- [ ] No subjective/vague verbs like "manage", "fast" (`non-testable-requirement`).
- [ ] BRD/business-facing requirements use business language first; technical
      mechanics are moved to downstream notes (`technical-jargon-in-business-requirement`).
- [ ] Requirements are **one grouped table** (Principle 13.7): `ID | Requirement |
      Why | Priority`, grouped by capability in journey order (bold band rows),
      Must → Should → Could within a group. `Why` is a business reason, not a
      `Source: BRx` cross-reference. A flat one-liner dump (no grouping, no `Why`) is
      a clarity finding.

## Structure & readability (Principle 13)
- [ ] **§0 "How to read this document"** is present up front: 0.1 intro + quick
      read, 0.2 a **symbol-conventions** table, 0.3 the **Glossary** moved to the
      front (not buried inside requirements).
- [ ] A **"How the system works (overview)"** section precedes the requirements
      (end-to-end narrative + one representative diagram).
- [ ] Section order matches the URD skeleton (Principle 13.4): cover → Lịch sử
      thay đổi → Mục lục → §1 Tổng quan → §2 Tổng quan hệ thống → Quy ước sơ đồ → §3
      [Tên nghiệp vụ] repeating (3.1–3.8) → §4 Phụ lục → §5 Câu hỏi mở → Sign-off.
- [ ] Flows are named `F0n-Name` consistently (catalog, steps, screen specs,
      diagrams); the number is stable, the name only appended.
- [ ] In-document traceability resolves (User stories ↔ Flow Catalog ↔ rules ↔
      errors); no separate matrix file.
- [ ] Output file is `urd.md` (never "final-…"); HTML is `urd.html` rendered from it;
      no tool label ("Review Pack") in displayed content.

## Completeness
- [ ] In-scope stated (`missing-scope`).
- [ ] Out-of-scope stated (`missing-out-of-scope`).
- [ ] Preconditions explicit, not hidden (`hidden-assumption`).
- [ ] No disguised scope creep (`scope-creep-disguised-as-requirement`).
- [ ] Notifications for relevant state changes (`missing-notification`).
- [ ] Non-user / back-office stakeholders covered — operations, accounting,
      reconciliation, partners, risk, maintenance (`missing-system-actor`).
- [ ] Existing-vs-new treatment defined when a rule changes (`missing-cohort-treatment`).

## Configuration & change-over-time
- [ ] Tunable parameters have a config owner + validation (`missing-configuration-ownership`).
- [ ] Changing rules/config carry an effective date / version (`missing-effective-dating`).
- [ ] Scheduled/batch jobs specify schedule, idempotency, outputs, consumers (`missing-batch-job-spec`).

## Testability
- [ ] Acceptance criteria exist (`missing-acceptance-criteria`).
- [ ] AC cover negative + boundary, not just happy (`weak-acceptance-criteria`).
  For a BRD/business draft, this may be reported as "build-ready layer not
  generated" rather than a business-content defect.

## Business rules
- [ ] Decisions backed by explicit rules (`missing-business-rule`).
- [ ] No duplicate/contradictory requirements (`duplicate-conflicting-requirement`).

## Edge coverage
- [ ] Boundary/unusual inputs covered (`missing-edge-case`).
- [ ] Failure/exception flows defined (`missing-exception-flow`).
- [ ] Entity states and transitions defined (`undefined-state`).
- [ ] Process / transaction features distinguish entity state from
      transaction/operation state (`missing-operation-state`).

## API / data impact
- [ ] API/data impact analyzed (`missing-api-data-impact`).
- [ ] Source of truth named (`missing-source-of-truth`).
- [ ] Not UI-only (`ui-only-requirement`).
  For a BRD/business draft, detailed API/data may be optional; require
  business-level affected systems/source-of-truth only unless handoff readiness
  was requested.

## Risk / control
- [ ] Permissions specified (`missing-permission`).
- [ ] Sensitive/financial actions require step-up auth + confirmation, with
      failure handling (`missing-authentication-step`).
- [ ] Sensitive actions audited (`missing-audit-log`).
- [ ] Retryable mutations idempotent (`missing-idempotency`).
- [ ] External calls have timeout/retry (`missing-timeout-retry`).
- [ ] Multi-step ops have compensation (`missing-reconciliation-compensation`).

## NFR / success
- [ ] Success metric defined (`missing-analytics-success-measurement`).

## Handoff
- [ ] API requirements have consumer context + AC (`api-only-requirement`).
- [ ] Failures mapped to error code + user-facing message + action
      (`missing-error-message-mapping`).
- [ ] User-facing error messages avoid technical jargon and define retryability,
      required action, and Ops/CS ownership where applicable.
- [ ] A Dev and QA engineer could act with no further clarification.

## Functional Flows (§3, process-centric, Mermaid-only)
- [ ] A **Flow Catalog** lists the in-scope processes.
- [ ] Each §3 block keeps user stories + Mermaid sequence (§3.3) + colored state
      (§3.4) for the **same** process; no block mixes two processes' diagrams
      (`mixed-process-diagram-block`). **No PlantUML.**
- [ ] §3.3 sequence uses `autonumber` + no color; §3.4 state uses colored `classDef`.
- [ ] Flow steps (§3.3) map to business rule (§3.5) / error code (§3.7) where relevant.
- [ ] Each Flow (`F0n-Name`) maps to ≥1 user story; orphan flows are flagged.
- [ ] Each user story maps to ≥1 flow and, where relevant, to a business rule and an
      error/state (in-document traceability via the Flow Catalog).
- [ ] No dangling ID references: every BR / `F0n` / `US-#` / `ERR-*` cited anywhere
      exists in its source list (counts against `traceability`).
- [ ] Screen field specs (§3.6) present for UI processes (EN/VN/Kiểu/M-O).

## Stakeholder coverage & completeness (Principles 10–11)
- [ ] Each stakeholder class walked (operations, accounting, reconciliation,
      partners, risk, maintenance, data, security); needs captured or flagged.
- [ ] Proactive `SUGGESTION:` items proposed for capabilities the feature +
      domain imply but the doc omits (kept separate from confirmed scope).
