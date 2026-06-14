# Engine: trace

Purpose: **verify in-document traceability** linking requirements → flows → rules →
errors → tests. There is **no separate `traceability-matrix.md` file** (Principle
13.9/13.11): the trace spine is the document itself — the Requirements table, the
**Flow Catalog** (whose rule / error-code / requirement columns carry the links), and
the **Test scenarios** table + its **Coverage & traceability** paragraph.

## Do
1. Collect ids from prd-draft/brd-draft (R*), the Flow Catalog (F*), stories (S*),
   AC, and test-scenarios (T*).
2. Confirm the in-document links resolve: each requirement maps to a Flow in the Flow
   Catalog, each Flow row carries its governing **Business rule** and relevant
   **Error code / state**, and each requirement reaches ≥1 test in the Test scenarios
   table. Do not build a separate matrix file; fix gaps in the document's own tables.
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
     in-document Error code & message table.
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
**No file.** Ensure the document's own tables carry the links (Flow Catalog rule /
error-code / requirement columns; Test scenarios + Coverage paragraph), then report —
in chat or as the document's **Coverage & traceability** paragraph — the coverage
figure, any orphan flows/requirements, and a **Dangling references** list (empty =
state "none found"). Fix dangling refs in the document, do not create a side matrix.
