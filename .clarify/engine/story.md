# Engine: story

Purpose: decompose requirements into atomic, traceable user stories.

## Do
1. For each requirement, write one or more stories:
   "As a <role>, I want <capability>, so that <benefit>."
   - For **back-office/admin actors**, use their role explicitly (e.g. "As a
     Rate Administrator, I want to set the savings rate with an effective date…").
   - For **scheduled/batch jobs**, use the job-as-actor form: "As the <job>
     scheduled <frequency>, I process <input>, producing <output> for
     <downstream consumer>." Cover idempotency/resume in its AC.
2. Keep stories atomic and independently testable.
3. Add a **Traces to: <Req id>** line to every story.
4. Attach any business rules/constraints that apply to the story.
5. Give each story a stable id (S1, S2, …) for downstream AC and tests.

## Rules
- Every story must trace back to exactly one requirement (split if it spans
  several).
- No orphan stories; no requirement left without a story (`traceability`).

## Output
Write `clarify-output/stories.md` using `templates/user-story-template.md`.
