# Engine: risk

Purpose: surface risk and control gaps — permissions, audit, idempotency,
timeouts/retries, compensation, and relevant NFRs.

## Do
For each requirement that mutates state, calls externally, touches sensitive
data, **runs on a schedule / as a batch**, or **changes a configuration or rule**,
check:
1. **Permission** — who is authorized? (`missing-permission`)
1b. **Authentication / confirmation** — for a sensitive or financial action, does
   the user confirm a summary and pass **step-up auth** (OTP/PIN/biometric) before
   the mutation, with defined handling for wrong/expired code, retry-limit, and
   cancel? (`missing-authentication-step`)
2. **Audit** — is the action logged with who/what/when? (`missing-audit-log`)
3. **Idempotency** — safe to retry? (`missing-idempotency`)
4. **Timeout/retry** — external calls bounded? (`missing-timeout-retry`)
5. **Compensation** — rollback for partial failure? (`missing-reconciliation-compensation`)
6. **Configuration control** — for tunable parameters (rates, fees, limits): who
   configures, what validation, how the change propagates?
   (`missing-configuration-ownership`)
7. **Effective dating / versioning** — does a changing rule/config carry an
   effective date and version, and is it clear which version applies to a given
   event date? (`missing-effective-dating`)
8. **Existing-vs-new cohort** — when a rule changes, are existing entities
   grandfathered or migrated, with timing and notification?
   (`missing-cohort-treatment`)
9. **Scheduled/batch job** — schedule/trigger, idempotency & resume-on-failure,
   outputs, and downstream consumers (e.g. reconciliation/accounting)?
   (`missing-batch-job-spec`)
10. **NFRs** — performance, security, availability, accessibility, compliance.
11. **Success metric** — is there one? (`missing-analytics-success-measurement`)

## Rules
- Pull `risk-compliance.md` from the selected domain pack if present.
- Recommend controls; do not assert a compliance obligation that isn't stated —
  mark uncertain obligations as OPEN QUESTION.

## Output
A risk & control section feeding `write-urd` (§12 Non-functional requirements and the
per-process §3.8) and the audit findings. List each gap with its anti-pattern id and a
concrete fix.
