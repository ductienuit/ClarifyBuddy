# Engine: acceptance-criteria

Purpose: write observable, pass/fail acceptance criteria for each story, covering
happy, negative, and boundary paths.

## Do
1. For each story, write AC in Given / When / Then form.
2. Always include: **happy path**, at least one **negative path**, and at least
   one **boundary** case.
3. Add **permission** AC where authorization applies.
4. When the story involves a rule/config that changes over time, add:
   - an **effective-date boundary** AC — an event dated just before vs on/after
     the effective date selects the correct rule version
     (`missing-effective-dating`).
   - a **cohort / backfill** AC — distinguish an OLD (existing) entity from a NEW
     entity under the changed rule (grandfather vs apply-forward)
     (`missing-cohort-treatment`).
5. For a **scheduled/batch job** story, add AC for idempotency (a rerun produces
   no duplicate effect) and resume-after-failure (`missing-batch-job-spec`).
6. For user-facing failures, add AC that verifies the mapped user-facing message,
   retryability, required action, and transaction/operation status after the
   error (`missing-error-message-mapping`). User messages must avoid technical
   jargon.
7. For risky/sensitive/financial/irreversible actions, add AC for confirmation,
   step-up authentication success, wrong/expired/cancelled authentication, and
   retry-limit behavior (`missing-authentication-step`).
8. Tie each AC group to its story id.

## Rules
- AC must be objectively verifiable; no subjective terms
  (`non-testable-requirement`).
- Happy-path-only AC is a gap (`weak-acceptance-criteria`) — flag and fill it.
- Pull boundary/negative cases from the edge-case-matrix to stay consistent.

## Output
Append AC into `clarify-output/stories.md` (or a companion section) using
`templates/acceptance-criteria-template.md`.
