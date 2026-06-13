# Engine: edge

Purpose: systematically enumerate edge cases per requirement and produce the
edge-case matrix.

## Do
For each requirement, probe these categories and define expected behavior:
1. **Boundary** — min, max, zero, empty, off-by-one.
2. **Negative/invalid** — bad input, wrong type, malformed.
3. **Exception/failure** — downstream error, timeout, declined, partial failure.
   Include **user-facing** failures (what the customer sees and does next), not
   only backend errors. Each user-facing failure needs a message + next action —
   detailed in the `error-handling` engine (`missing-error-message-mapping`).
4. **State** — illegal transitions, repeated actions, already-final states.
5. **Concurrency** — simultaneous updates, retries, races.
6. **Permission** — unauthorized actor attempts the action.
7. **Empty/null** — no data, first-run, deleted dependency.
8. **Temporal / rule-change** — an event dated before vs on/after a rule or
   config effective date (which version applies?); existing vs new entities under
   the changed rule; retroactive vs forward-only application.
9. **Batch / schedule** — job rerun / duplicate run, partial-batch failure and
   resume, out-of-order or late-arriving events, an empty run, and a downstream
   consumer that reads mid-run.

For each row, mark covered (yes/no) and the anti-pattern id if uncovered
(`missing-edge-case`, `missing-exception-flow`, `undefined-state`,
`missing-permission`, `missing-idempotency`, `missing-effective-dating`,
`missing-cohort-treatment`, `missing-batch-job-spec`).

## Rules
- If a domain pack is selected, pull its `common-edge-cases.md` first.
- Do not invent business outcomes; if the correct behavior is unknown, mark the
  expected behavior as OPEN QUESTION.

## Output
Write `clarify-output/edge-case-matrix.md` using
`templates/edge-case-matrix-template.md`, including a Gaps section.
