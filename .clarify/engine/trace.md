# Engine: trace

Purpose: **verify in-document traceability** linking user stories → flows → rules →
errors. There is **no separate `traceability-matrix.md` file** (Principle 13.9/13.11):
the trace spine is the document itself — the **User stories** (§3.2 / draft §7), the
**Flow Catalog** (whose rule / error-code / user-story columns carry the links), and each
process's **error table** (§3.7).

## Do
1. Collect ids from the URD: user stories (`US-#`), the Flow Catalog (`F0n-Name`), business
   rules (`BR#`), and error codes (`ERR-*`).
2. Confirm the in-document links resolve: each user story maps to a Flow in the Flow
   Catalog, each Flow row carries its governing **Business rule** and relevant **Error
   code / state**. Do not build a separate matrix file; fix gaps in the document's own tables.
3. Flag **orphans** in all directions:
   - User story with no flow (forward gap).
   - User story with no governing rule where one is expected.
   - **Flow (`F0n-Name`) not mapped to any user story (orphan flow)** — report it.
4. **Referential-integrity check** — every ID that is REFERENCED must EXIST. Prefer the
   mechanical pass via `python .clarify/scripts/clarify_tools.py integrity` (best-effort
   regex scan), then ADD the semantic review yourself; if Python is unavailable, do the
   whole check manually — never skip it. Checks:
   - `BR#` cited in flow steps / error tables exist in the Business rules (§3.5).
   - `ERR-*` codes cited in flow steps / screen matrix / wireframes exist in the §3.7 error
     table.
   - `F0n-Name` used anywhere exists in the Flow Catalog; screen names used exist in the
     Screen matrix (§3.6).
   - `A/Q/S/V` ids referenced in prose exist in their lists.
   Report violations under a **Dangling references** section (ID, where cited, what's
   missing). These count against the `traceability` dimension — no new anti-pattern.
5. Report coverage: % of user stories mapped to a flow, and whether every Flow maps to ≥1
   user story.

## Rules
- Every user story should trace to ≥1 flow; every flow should map to ≥1 user story. Gaps and
  orphan flows deduct from the `traceability` dimension.

## Output
**No file.** Ensure the document's own tables carry the links (Flow Catalog rule / error-code
/ user-story columns; §3.7 error tables), then report — in chat or in §4.2 — the coverage
figure, any orphan flows/stories, and a **Dangling references** list (empty = state "none
found"). Fix dangling refs in the document, do not create a side matrix.
