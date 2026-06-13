# Requirement Quality Score — How to Score

This file defines the **reproducible** scoring procedure. The numbers live in
[`scoring-rubric.yaml`](scoring-rubric.yaml); the anti-patterns live in
[`../anti-patterns/anti-patterns.yaml`](../anti-patterns/anti-patterns.yaml).
Always show the math so the same input yields the same score.

## Procedure

1. **Start each dimension at its full weight.** Ten dimensions, weights sum to
   100 (clarity 12, completeness 12, testability 10, traceability 10,
   edge-coverage 10, business-rule-quality 10, api-data-impact 10, risk-control
   10, nfr 8, handoff-readiness 8).

2. **Detect anti-patterns.** For each requirement, apply the `detect` heuristics
   in `anti-patterns.yaml`. Record every occurrence with its `id`, `severity`,
   and `dimension`. This includes the product/operational heuristics
   `actors_user_only`, `tunable_param_without_config_owner`,
   `rule_change_without_effective_date`, `rule_change_without_cohort_strategy`,
   `batch_job_underspecified`, `errors_without_message_mapping`, and
   `sensitive_action_without_authentication`,
   `only_entity_state_without_operation_state`,
   `business_requirement_contains_technical_jargon`, and
   `mixed_process_diagram_block` (each documented in
   `anti-patterns.yaml`) — apply them at the **document** level, not only per
   requirement, since they often surface as whole missing perspectives.

   **Document-profile calibration:** If the target is a BRD or business-facing
   draft produced by `from-idea`, distinguish core business-readiness gaps from
   optional Dev/QA build-ready artifacts. Missing user stories, acceptance
   criteria, test scenarios, API/data impact, or traceability should be reported
   as "build-ready layer not generated" unless the user asked for handoff
   readiness. They may affect the handoff-readiness note, but they should not be
   framed as proof that the BRD is business-incomplete.

3. **Deduct per occurrence** from the anti-pattern's `dimension`:
   - `blocker` → −6
   - `major` → −3
   - `minor` → −1

4. **Cap per dimension.** A dimension cannot drop below 0. (Its weight is the
   maximum it can lose.)

4b. **Separate score notes from next-step artifact gaps.** When the score is
    lower because optional build-ready artifacts are absent, label that as
    "optional build-ready layer" and recommend `/clarify:from-spec` only if the
    user needs Dev/QA handoff. Do not present `/clarify:from-spec` as required to
    make a resolved business draft valid.

5. **Sanity-check against anchors.** After deductions, confirm each dimension's
   remaining points are consistent with its `full` / `half` / `zero` anchor in
   the rubric. Adjust within the anchor if heuristics over/under-counted, and
   note why.

6. **Sum** the dimension scores → total out of 100.

7. **Assign a band** from the rubric:
   - 90–100 → Build-ready
   - 75–89 → Good, minor gaps
   - 60–74 → Needs major clarification
   - < 60 → Not ready for handoff

8. **Apply the blocker cap.** If **any** detected anti-pattern has
   `severity: blocker`, the band is forced to **"Not ready for handoff"**
   regardless of the numeric total. State the total AND the capped band.

## Output shape

Report, in this order:

1. **Total score / 100** and **band** (note if band was blocker-capped).
2. **Per-dimension table**: dimension, points (earned/weight), one-line reason.
3. **Findings**, grouped by severity (blocker → major → minor). Each finding:
   anti-pattern `id`, the offending text, the mapped dimension, and the `fix`.
4. **Top 3 actions** to raise the score the most.
5. **Optional build-ready layer gaps** when applicable: stories / AC / tests /
   API-data / traceability not generated yet, with wording that these are
   optional for Dev/QA handoff rather than mandatory for business sign-off.

## Worked mini-example

> "User can manage their account settings."

- `missing-acceptance-criteria` (major, testability) → −3
- `non-testable-requirement` (major, testability) "manage" is vague → −3
- `ambiguous-actor`? actor present ("User") → no.

testability starts at 10 → 10 − 3 − 3 = 4. Other dimensions assessed similarly.
No blocker → band from total. Show the table and the fixes.
