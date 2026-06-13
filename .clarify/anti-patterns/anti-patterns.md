# Clarify Anti-Pattern Catalog (36)

Human-readable rendering of
[`anti-patterns.yaml`](anti-patterns.yaml), which is the **source of truth**. If
the two ever disagree, the yaml wins. Each anti-pattern maps to one scoring
dimension (see [`../evaluators/scoring-rubric.yaml`](../evaluators/scoring-rubric.yaml)).

Severity: **blocker** | **major** | **minor**.

## Index by dimension

- **clarity:** ambiguous-actor, missing-trigger, missing-outcome,
  technical-jargon-in-business-requirement, mixed-process-diagram-block
- **completeness:** hidden-assumption, missing-scope, missing-out-of-scope,
  missing-notification, scope-creep-disguised-as-requirement, missing-system-actor,
  missing-cohort-treatment
- **testability:** non-testable-requirement, missing-acceptance-criteria,
  weak-acceptance-criteria
- **business-rule-quality:** missing-business-rule,
  duplicate-conflicting-requirement, missing-configuration-ownership,
  missing-effective-dating
- **edge-coverage:** missing-edge-case, missing-exception-flow, undefined-state,
  missing-operation-state
- **api-data-impact:** missing-api-data-impact, missing-source-of-truth,
  ui-only-requirement
- **risk-control:** missing-permission, missing-audit-log, missing-idempotency,
  missing-timeout-retry, missing-reconciliation-compensation, missing-batch-job-spec,
  missing-authentication-step
- **nfr:** missing-analytics-success-measurement
- **handoff-readiness:** api-only-requirement, missing-error-message-mapping

---

## 1. Ambiguous Actor — `ambiguous-actor`
- **Severity:** major · **Dimension:** clarity
- **Definition:** The requirement does not say who performs the action.
- **Bad:** "The order can be cancelled."
- **Why dangerous:** Dev cannot wire permissions; QA cannot pick a test user.
- **Fix:** Name the actor/role responsible.
- **Good:** "A customer with a pending order can cancel that order."

## 2. Missing Trigger — `missing-trigger`
- **Severity:** major · **Dimension:** clarity
- **Definition:** States an outcome but not what initiates it.
- **Bad:** "Inventory is updated."
- **Why dangerous:** Unclear event means unclear timing and missed sequencing.
- **Fix:** State the triggering event (When …).
- **Good:** "When an order is confirmed, inventory for each line item is decremented."

## 3. Missing Outcome — `missing-outcome`
- **Severity:** major · **Dimension:** clarity
- **Definition:** Names an action but no observable result.
- **Bad:** "The user submits the form."
- **Why dangerous:** No outcome means nothing to verify or build toward.
- **Fix:** State the observable result.
- **Good:** "When the user submits the form, the system persists the record and shows a confirmation."

## 4. Hidden Assumption — `hidden-assumption`
- **Severity:** major · **Dimension:** completeness
- **Definition:** Relies on an unstated precondition or rule.
- **Bad:** "Refund the customer."
- **Why dangerous:** Unstated conditions (window, eligibility) surface as bugs.
- **Fix:** Make preconditions explicit, or label ASSUMPTION / OPEN QUESTION.
- **Good:** "ASSUMPTION: refunds allowed within 30 days. Within that window, refund to the original payment method."

## 5. Missing Scope — `missing-scope`
- **Severity:** major · **Dimension:** completeness
- **Definition:** The document does not state what is in scope.
- **Bad:** "Build the checkout."
- **Why dangerous:** Scope ambiguity drives rework and disagreement.
- **Fix:** Add an explicit in-scope section.
- **Good:** "In scope: single-currency card checkout for logged-in users."

## 6. Missing Out-of-Scope — `missing-out-of-scope`
- **Severity:** minor · **Dimension:** completeness
- **Definition:** Never states what is deliberately excluded.
- **Bad:** "(no out-of-scope section)"
- **Why dangerous:** Without exclusions, scope silently creeps.
- **Fix:** Add an out-of-scope section.
- **Good:** "Out of scope: multi-currency, gift cards, guest checkout."

## 7. Non-Testable Requirement — `non-testable-requirement`
- **Severity:** major · **Dimension:** testability
- **Definition:** Cannot be verified objectively.
- **Bad:** "The page should be fast."
- **Why dangerous:** Subjective wording cannot pass or fail a test.
- **Fix:** Replace subjective terms with measurable thresholds.
- **Good:** "First contentful paint within 1.5s on 4G."

## 8. Missing Acceptance Criteria — `missing-acceptance-criteria`
- **Severity:** major · **Dimension:** testability
- **Definition:** Describes behavior but defines no observable pass/fail.
- **Bad:** "User can manage their account settings."
- **Why dangerous:** Dev and QA cannot tell when it's done.
- **Fix:** Add testable AC covering happy, negative, and boundary paths.
- **Good:** "Given logged in, when updating email with a valid address, then it saves and sends a verification message."

## 9. Weak Acceptance Criteria — `weak-acceptance-criteria`
- **Severity:** minor · **Dimension:** testability
- **Definition:** AC exist but only cover the happy path.
- **Bad:** "Given valid input, when submitted, then it saves."
- **Why dangerous:** Negative and boundary behavior is left undefined.
- **Fix:** Add negative and boundary AC.
- **Good:** "Includes AC for invalid input, duplicate submission, and max-length boundaries."

## 10. Missing Business Rule — `missing-business-rule`
- **Severity:** major · **Dimension:** business-rule-quality
- **Definition:** A decision depends on a rule that is never stated.
- **Bad:** "Apply the discount."
- **Why dangerous:** The rule gets invented inconsistently across the team.
- **Fix:** State the rule, or mark OPEN QUESTION.
- **Good:** "Apply a 10% discount when cart subtotal exceeds $100 (excluding tax)."

## 11. Missing Edge Case — `missing-edge-case`
- **Severity:** major · **Dimension:** edge-coverage
- **Definition:** Boundary or unusual inputs are not addressed.
- **Bad:** "Add items to the cart."
- **Why dangerous:** Empty, max, and concurrent cases break in production.
- **Fix:** Enumerate boundary and unusual-input cases.
- **Good:** "Defines empty cart, max 100 line items, and out-of-stock behavior."

## 12. Missing Exception Flow — `missing-exception-flow`
- **Severity:** major · **Dimension:** edge-coverage
- **Definition:** Only the success path is described; failures undefined.
- **Bad:** "Charge the card and confirm the order."
- **Why dangerous:** Payment/network failures have undefined behavior.
- **Fix:** Define behavior for each failure mode.
- **Good:** "If the charge is declined, the order stays pending and the user is prompted to retry."

## 13. Undefined State — `undefined-state`
- **Severity:** major · **Dimension:** edge-coverage
- **Definition:** An entity's states and legal transitions are not defined.
- **Bad:** "The order is processed."
- **Why dangerous:** Illegal transitions and stuck states become bugs.
- **Fix:** Define the state set and allowed transitions.
- **Good:** "pending → paid → shipped → delivered; cancellation only from pending or paid."

## 14. Missing Permission — `missing-permission`
- **Severity:** major · **Dimension:** risk-control
- **Definition:** Authorization for an action is not specified.
- **Bad:** "Allow editing the invoice."
- **Why dangerous:** Unbounded access is a security and compliance risk.
- **Fix:** State who is authorized and under what conditions.
- **Good:** "Only Finance-role users may edit an invoice, and only while in draft."

## 15. Missing Audit Log — `missing-audit-log`
- **Severity:** minor · **Dimension:** risk-control
- **Definition:** A sensitive action records no audit trail.
- **Bad:** "Admin deletes a user."
- **Why dangerous:** No accountability for sensitive/destructive actions.
- **Fix:** Specify what is logged: who, what, when, before/after.
- **Good:** "Deleting a user records actor, target, timestamp, and reason."

## 16. Missing Notification — `missing-notification`
- **Severity:** minor · **Dimension:** completeness
- **Definition:** A state change that should notify someone does not.
- **Bad:** "The order ships."
- **Why dangerous:** Stakeholders are left uninformed.
- **Fix:** Specify who is notified, through which channel, and when.
- **Good:** "When the order ships, the customer receives a shipping email with tracking."

## 17. Missing API/Data Impact — `missing-api-data-impact`
- **Severity:** major · **Dimension:** api-data-impact
- **Definition:** A change's effect on APIs or data model is not analyzed.
- **Bad:** "Store the user's preferred language."
- **Why dangerous:** Schema/contract changes get discovered mid-build.
- **Fix:** Identify affected endpoints, schema changes, migrations.
- **Good:** "Adds users.locale column (migration); extends GET/PATCH /users contract."

## 18. Missing Source of Truth — `missing-source-of-truth`
- **Severity:** major · **Dimension:** api-data-impact
- **Definition:** Data exists in multiple places with no authoritative owner.
- **Bad:** "Price shown on the product page and in the cart."
- **Why dangerous:** Divergent copies cause inconsistency and disputes.
- **Fix:** Name the authoritative source and how others derive from it.
- **Good:** "Pricing service is source of truth; cart caches at add-time, revalidates at checkout."

## 19. Missing Idempotency — `missing-idempotency`
- **Severity:** major · **Dimension:** risk-control
- **Definition:** An operation that may be retried is not idempotent.
- **Bad:** "POST /charge to bill the customer."
- **Why dangerous:** Retries cause double charges or duplicate records.
- **Fix:** Require an idempotency key or define dedup semantics.
- **Good:** "POST /charge accepts an Idempotency-Key; repeated keys return the original result."

## 20. Missing Timeout/Retry — `missing-timeout-retry`
- **Severity:** minor · **Dimension:** risk-control
- **Definition:** External calls lack timeout and retry policy.
- **Bad:** "Call the payment gateway."
- **Why dangerous:** Hung calls and unbounded retries degrade reliability.
- **Fix:** Specify timeout, retry count, and backoff.
- **Good:** "Gateway call: 5s timeout, 3 retries with exponential backoff."

## 21. Missing Reconciliation/Compensation — `missing-reconciliation-compensation`
- **Severity:** major · **Dimension:** risk-control
- **Definition:** A multi-step operation has no rollback or reconciliation.
- **Bad:** "Reserve inventory, then charge the card."
- **Why dangerous:** Partial failure leaves an inconsistent state.
- **Fix:** Define compensation/reconciliation for partial failure.
- **Good:** "If the charge fails after reservation, release the reserved inventory."

## 22. Duplicate/Conflicting Requirement — `duplicate-conflicting-requirement`
- **Severity:** major · **Dimension:** business-rule-quality
- **Definition:** Two requirements overlap or contradict each other.
- **Bad:** "Refunds within 30 days. / No refunds after 14 days."
- **Why dangerous:** Ambiguous which rule wins; inconsistent implementation.
- **Fix:** Reconcile into a single authoritative statement.
- **Good:** "Refunds allowed within 30 days; the 14-day note is removed as outdated."

## 23. Scope Creep Disguised as Requirement — `scope-creep-disguised-as-requirement`
- **Severity:** minor · **Dimension:** completeness
- **Definition:** An item expands scope beyond the stated goal.
- **Bad:** "Also add a recommendation engine to the checkout."
- **Why dangerous:** Hidden scope inflates effort and risk.
- **Fix:** Move to out-of-scope or a separate initiative unless justified.
- **Good:** "Recommendations moved to a future initiative; checkout scope unchanged."

## 24. UI-Only Requirement — `ui-only-requirement`
- **Severity:** minor · **Dimension:** api-data-impact
- **Definition:** Describes UI without backend/data behavior.
- **Bad:** "Add a 'Save for later' button."
- **Why dangerous:** Backend persistence and rules are left undefined.
- **Fix:** Specify backend behavior, persistence, and rules behind the UI.
- **Good:** "'Save for later' moves the item to a saved list (new table), removable, persists across sessions."

## 25. API-Only Requirement — `api-only-requirement`
- **Severity:** minor · **Dimension:** handoff-readiness
- **Definition:** Describes an endpoint with no user-facing context or AC.
- **Bad:** "Expose GET /recommendations."
- **Why dangerous:** Unclear who consumes it, why, or how success is measured.
- **Fix:** State the consumer, the user value, and acceptance criteria.
- **Good:** "GET /recommendations powers the homepage rail; returns ≤10 items in <300ms; AC defined."

## 26. Missing Analytics / Success Measurement — `missing-analytics-success-measurement`
- **Severity:** minor · **Dimension:** nfr
- **Definition:** No metric defines whether the feature succeeds.
- **Bad:** "Launch the new onboarding flow."
- **Why dangerous:** No way to know if the feature achieved its goal.
- **Fix:** Define the success metric, event tracking, and target.
- **Good:** "Success: +10% activation within 14 days; track onboarding_completed events."

## 27. Missing System / Back-Office Actor — `missing-system-actor`
- **Severity:** major · **Dimension:** completeness
- **Definition:** The spec models only the end user and omits back-office, operations, accounting, external-system, or scheduled-job actors.
- **Bad:** "The user opens a savings deposit and the system confirms it."
- **Why dangerous:** Whole actor classes (config admin, ops, accounting, integrations, jobs) go unowned and unbuilt.
- **Fix:** Enumerate non-user actors (admin/configurator, operations, accounting/back-office, external systems, scheduled jobs) and their responsibilities.
- **Good:** "Actors: Customer; Rate Administrator; Operations; Accounting/GL; Interest-Accrual Job; Core-Banking System."

## 28. Missing Configuration Ownership — `missing-configuration-ownership`
- **Severity:** major · **Dimension:** business-rule-quality
- **Definition:** A tunable parameter (rate, fee, limit, threshold) is used but the spec never says where it is configured, who configures it, how it is validated, or how the change propagates.
- **Bad:** "Apply a 2% monthly interest rate."
- **Why dangerous:** The value gets hard-coded; nobody owns changes; no validation or propagation path exists.
- **Fix:** State the config store/screen, the owning role, validation rules, and how the change propagates to runtime.
- **Good:** "Interest rate is set in Rate Config by a Rate Administrator (0–10%, two decimals); changes propagate to the accrual job on the effective date."

## 29. Missing Effective Dating / Versioning — `missing-effective-dating`
- **Severity:** major · **Dimension:** business-rule-quality
- **Definition:** A rule or configuration can change over time but the spec gives no effective date or version, so it is unclear which value applies when.
- **Bad:** "The fee can be updated by an admin."
- **Why dangerous:** Past events get recomputed with new values; disputes and reconciliation breaks ensue.
- **Fix:** Require an effective-from (and optional end) date and a version; define which version applies to a given event date.
- **Good:** "Fee changes carry an effective-from date; a transaction uses the fee version in effect on its date; prior versions are retained."

## 30. Missing Existing-vs-New Treatment — `missing-cohort-treatment`
- **Severity:** major · **Dimension:** completeness
- **Definition:** When a rule or configuration changes, the spec does not say whether existing entities are grandfathered or have the new value applied forward, nor define any migration/backfill.
- **Bad:** "Raise the minimum balance to $500."
- **Why dangerous:** Existing records are silently re-evaluated (or silently skipped); behavior diverges per developer.
- **Fix:** State the cohort strategy (grandfather vs apply-forward) and any migration/backfill, with timing and notification.
- **Good:** "New minimum applies to accounts opened on/after the effective date; existing accounts grandfathered; no backfill; holders notified 30 days ahead."

## 31. Missing Scheduled-Job / Batch Spec — `missing-batch-job-spec`
- **Severity:** major · **Dimension:** risk-control
- **Definition:** A scheduled or batch operation is implied or named but its trigger/schedule, idempotency/resume, outputs, and downstream consumers are not specified.
- **Bad:** "An interest-accrual job runs to update balances."
- **Why dangerous:** Reruns double-post; partial failures leave gaps; accounting consumers receive incomplete data.
- **Fix:** Specify schedule/trigger, idempotency and resume-on-failure, the outputs produced, and every downstream consumer.
- **Good:** "Interest-Accrual Job runs daily 02:00 UTC; idempotent per (account, accrual-date); outputs accrual ledger entries; consumed by GL posting and daily reconciliation."

## 32. Missing Error / Message Mapping — `missing-error-message-mapping`
- **Severity:** major · **Dimension:** handoff-readiness
- **Definition:** A user-facing or transactional flow lists failures only vaguely, with no mapping of each error scenario to a code, a user-facing message, and a follow-up action.
- **Bad:** "Show an error if opening the account fails."
- **Why dangerous:** FE, BE, QA, and support each invent different codes and wording; users get unclear or wrong guidance, especially when money already moved.
- **Fix:** Add an error table — scenario, code, transaction status after error, internal message, user-facing message, retryable?, required action, needs-ops?.
- **Good:** "TD_OPEN_002 / insufficient balance / Failed / user message 'Số dư không đủ để mở sổ' / retryable yes / action: choose another account."

## 33. Missing Authentication / Confirmation Step — `missing-authentication-step`
- **Severity:** major · **Dimension:** risk-control
- **Definition:** A sensitive or financial action proceeds without specifying strong authentication and explicit user confirmation (and their failure handling).
- **Bad:** "The customer opens the deposit and the system debits the source account."
- **Why dangerous:** A money-moving action can run without verifying the user; OTP/PIN/biometric failure, expiry, retry-limit, and cancel are undefined.
- **Fix:** Require step-up authentication (OTP/PIN/biometric) + a confirmation screen before the mutation; define wrong/expired code, retry limit, and cancel handling.
- **Good:** "Before debiting, the customer confirms the summary and authenticates with OTP; 3 wrong attempts lock the transaction; cancel creates no account and no debit."

## 34. Missing Transaction / Operation State — `missing-operation-state`
- **Severity:** major · **Dimension:** edge-coverage
- **Definition:** A feature with a process, async action, risky action, external call, or transaction defines only the business entity state and omits the state of the operation being processed.
- **Bad:** "Deposit account states are pending, active, matured, closed. The opening flow succeeds or fails."
- **Why dangerous:** In-flight, authentication, timeout, duplicate, reversal, and unknown-result states are hidden, so FE, BE, QA, Ops, and CS handle the same operation differently.
- **Fix:** Add a separate transaction/operation state model such as initiated → pending-auth → processing → success / failed / timeout / reversed / unknown, and map errors to those states.
- **Good:** "Entity state: pending → active → closed. Operation state: initiated → pending-auth → processing → success/failed/timeout/unknown."

## 35. Technical Jargon in Business Requirement — `technical-jargon-in-business-requirement`
- **Severity:** major · **Dimension:** clarity
- **Definition:** A BRD or business-facing requirement is written primarily in implementation, accounting-system, or integration jargon instead of business language.
- **Bad:** "The service writes idempotent double-entry ledger postings to GL and accrual tables for each cohort."
- **Why dangerous:** Business reviewers cannot validate intent, while technical details crowd out journey, decisions, and user outcomes.
- **Fix:** Rewrite the body requirement in business language and move implementation mechanics to Downstream Technical Notes or a technical appendix.
- **Good:** "The system records the customer's funds movement and calculates earned interest accurately; technical posting and retry mechanics are captured in Downstream Technical Notes."

## 36. Mixed-Process Diagram Block — `mixed-process-diagram-block`
- **Severity:** minor · **Dimension:** clarity
- **Definition:** Within one flow/use-case block, the activity diagram describes one business process while the adjacent sequence diagram describes a different process.
- **Bad:** "Activity = Open deposit next to Sequence = Early withdrawal, presented as one block."
- **Why dangerous:** Readers lose the process narrative; reviewers cannot tell which diagram belongs to which flow.
- **Fix:** Organize §7 process-centric — Flow Catalog, then one block per process with step-by-step + activity + sequence all for the SAME process; Screen Matrix after the flows.
- **Good:** "Flow F01 Open deposit has its own activity + sequence; Flow F02 Early withdrawal in its own block."
