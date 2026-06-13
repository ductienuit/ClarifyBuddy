# Engine: test

Purpose: derive concrete test scenarios from stories, AC, and the edge-case
matrix.

## Do
1. For each AC, write at least one test scenario with preconditions, steps, and
   expected result.
2. Cover types: functional, negative, boundary, integration, and (where
   relevant) security and performance.
3. Pull every uncovered row from the edge-case-matrix into a test.
4. For every error/message mapping row, add or link a negative test that verifies:
   code/status, entity state, transaction/operation state, user-facing message,
   retryability, required action, and Ops/CS flag where applicable.
5. For every authentication/confirmation requirement, add tests for success,
   wrong credential/code, expired challenge, retry-limit, and user cancellation.
6. Add a **Traces to: <Story id>/<AC id>** line to each test.
7. Give each test a stable id (T1, T2, …).

## Rules
- Every AC must have at least one test (`traceability`).
- Expected results must be observable, not subjective.

## Output
Write `clarify-output/test-scenarios.md` using
`templates/test-scenario-template.md`.
