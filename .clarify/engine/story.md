# Engine: story

Purpose: decompose requirements/intent into atomic, traceable **user stories** for the
URD's §3.2 (per process) / draft §7.

## Do
1. For each requirement/intent, write one or more stories in the URD shape:
   `Là <vai trò> / Tôi muốn <hành động> / Để <lợi ích> / Tiêu chí chấp nhận <điều kiện>`.
   - For **back-office/admin actors**, use their role explicitly (e.g. "Là Rate
     Administrator, tôi muốn đặt lãi suất kèm ngày hiệu lực…").
   - For **scheduled/batch jobs**, use the job-as-actor form (cover idempotency/resume in
     the acceptance criteria).
2. Keep stories atomic and independently testable.
3. Give each story a stable id (`US-01`, `US-02`, …) and tie it to its flow (`F0n-Name`)
   and any applicable business rules (`BR#`) for in-document traceability.

## Rules
- Every story must trace back to a requirement/intent (split if it spans several).
- No orphan stories; no requirement/intent left without a story (`traceability`).
- Do not invent capability; a gap → `ASSUMPTION` / `OPEN QUESTION`.

## Output
Write the stories **into the URD draft §7 (User stories / Use cases)** — and they flow
into each process's §3.2 at finalize. Use `templates/user-story-template.md` as the
working structure. There is no separate `stories.md` file.
