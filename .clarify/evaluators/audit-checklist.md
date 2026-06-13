# Clarify Audit Checklist

A fast, ordered pass an agent runs during `audit` / `from-spec`. For each item,
note pass / partial / fail and the anti-pattern id(s) it maps to.

Apply the checklist through the Document Profile. For a BRD/business-facing draft
from `from-idea`, journey, screens, rules, exceptions, messages, state summary,
business NFRs, and stakeholder coverage are core readiness checks. Full stories,
AC, tests, API/data impact, and traceability are Dev/QA build-ready layer checks;
report their absence separately unless the user requested handoff readiness.

## Clarity
- [ ] Every requirement names an **actor** (`ambiguous-actor`).
- [ ] Every requirement names a **trigger** (`missing-trigger`).
- [ ] Every requirement states an **outcome** (`missing-outcome`).
- [ ] No subjective/vague verbs like "manage", "fast" (`non-testable-requirement`).
- [ ] BRD/business-facing requirements use business language first; technical
      mechanics are moved to downstream notes (`technical-jargon-in-business-requirement`).

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

## Functional Flows (process-centric)
- [ ] §7 has a **Flow Catalog** before the detailed flows.
- [ ] Each flow block keeps step-by-step + activity + sequence for the **same**
      process; no block mixes process A's activity with process B's sequence
      (`mixed-process-diagram-block`).
- [ ] Decision-rich flows have a PlantUML activity; multi-system flows have a
      Mermaid sequence (or "Sequence diagram not required" + reason).
- [ ] Flow steps map to business rule / validation / error code where relevant.
- [ ] Each Flow (Fxx) maps to ≥1 requirement and appears in the traceability
      matrix; orphan flows are flagged.
- [ ] Each requirement maps to ≥1 flow and, where relevant, to a business rule and
      an error/state (traceability has Flow / Business rule / Error-State columns).
- [ ] No dangling ID references: every BR / Fxx / Sxx / error code cited anywhere
      exists in its source list (counts against `traceability`).
- [ ] Screen / Display Matrix is placed **after** the flows (or a clear reason).

## Stakeholder coverage & completeness (Principles 10–11)
- [ ] Each stakeholder class walked (operations, accounting, reconciliation,
      partners, risk, maintenance, data, security); needs captured or flagged.
- [ ] Proactive `SUGGESTION:` items proposed for capabilities the feature +
      domain imply but the doc omits (kept separate from confirmed scope).
