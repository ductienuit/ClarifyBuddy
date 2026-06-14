# Engine: test

Purpose: derive concrete test scenarios from stories, AC, and the edge-case
matrix.

## Do
1. For each AC, write at least one test scenario with preconditions, steps, and
   expected result.
2. Cover types: functional, negative, boundary, integration, and (where
   relevant) security and performance.
3. Pull every uncovered case from the doc's Edge cases section into a test.
4. For every error/message mapping row, add or link a negative test that verifies:
   code/status, entity state, transaction/operation state, user-facing message,
   retryability, required action, and Ops/CS flag where applicable.
5. For every authentication/confirmation requirement, add tests for success,
   wrong credential/code, expired challenge, retry-limit, and user cancellation.
6. Add a **Traces to: <Requirement id>/<Story id>/<AC id>** line to each test, naming
   the `R#`/`BRD-R#` it verifies and the flow (`F0n-Name`) it belongs to.
7. Give each test a stable id (T1, T2, …).

## Rules
- Every AC must have at least one test (`traceability`).
- Expected results must be observable, not subjective.

## Output
Write the **full** scenarios (preconditions + steps + expected result) to
`clarify-output/test-scenarios.md` using `templates/test-scenario-template.md`. The
sign-off doc's §Test scenarios is a **summary** built by `finalize` — one numbered
table `# | Requirement | Flow (F0n-Name) | Scenario | Expected result | Test` (Principle
13.9); full preconditions/steps are **not** duplicated into the doc.
