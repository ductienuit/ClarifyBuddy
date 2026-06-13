# Engine: trace

Purpose: build and verify the traceability matrix linking requirements →
stories → acceptance criteria → tests.

## Do
1. Collect ids from prd-draft/brd-draft (R*), the Flow Catalog (F*), stories (S*),
   AC, and test-scenarios (T*).
2. Build a matrix row per requirement: Req → **Flow** → **Business rule** →
   **Error/State** → Story → AC → Test. The `Flow` column shows the business
   flow(s) that realize the requirement; `Business rule` and `Error/State` link the
   governing rule(s) and the relevant error code / state. (A `Screen` column is
   optional — add only if it stays readable.)
3. Flag **orphans** in all directions:
   - Requirement with no flow/story/test (forward gap).
   - Requirement with no flow or no governing rule where one is expected.
   - Story/test with no requirement (backward gap).
   - **Flow (Fxx) not mapped to any requirement (orphan flow)** — report it.
4. **Referential-integrity check** — every ID that is REFERENCED must EXIST.
   Prefer the mechanical pass via
   `python .clarify/scripts/clarify_tools.py integrity` (best-effort regex scan),
   then ADD the semantic review yourself; if Python is unavailable, do the whole
   check manually — never skip it. Checks:
   - BR ids cited in flow steps / error map exist in Business Rules.
   - Error codes cited in flow steps / screen matrix / wireframes exist in the
     error map (§9.1 / error-handling.md).
   - Flow ids (Fxx) used anywhere exist in the Flow Catalog; Screen ids (Sxx)
     exist in the Screen Matrix / screen inventory.
   - A/Q/S/V ids referenced in prose exist in their lists.
   Report violations under a **Dangling references** section (ID, where cited,
   what's missing). These count against the `traceability` dimension — no new
   anti-pattern.
5. Report coverage: % of requirements with at least one test, and whether every
   Flow maps to ≥1 requirement.

## Rules
- Every requirement should trace forward to ≥1 test; every test should trace
  back to a requirement; every Flow should map to ≥1 requirement. Gaps and orphan
  flows deduct from the `traceability` dimension.

## Output
Write `clarify-output/traceability-matrix.md` with the matrix table (including the
`Flow` column), an orphan/coverage summary that lists any orphan flows, and a
**Dangling references** section (empty = explicitly state "none found").
