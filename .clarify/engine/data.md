# Engine: data

Purpose: analyze the data-model impact of the requirements and identify the
source of truth.

## Do
1. List entities touched (new or modified) and the fields each requirement
   implies.
2. For each change: new table vs. new column, type, nullability, defaults, and
   whether a **schema migration** is required. Separately, when a rule/config
   changes, define the **semantic migration / backfill**: are existing rows
   re-evaluated, grandfathered, or left as-is? (`missing-cohort-treatment`)
3. Treat **configuration as data**: tunable parameters (rates, fees, limits) are
   stored as **effective-dated, versioned config rows** (e.g. `effective_from`,
   `version`, owner), not hard-coded; flag config used with no such store
   (`missing-configuration-ownership`, `missing-effective-dating`).
4. Identify the **source of truth** for each piece of data; flag duplicated data
   with no authoritative owner (`missing-source-of-truth`).
5. Note derived/cached copies and how they are revalidated.
6. Flag requirements that imply data changes but state none
   (`missing-api-data-impact`).

## Rules
- Reuse the domain pack's `api-data-patterns.md` if a pack is selected.
- Do not design the full schema; surface impact and ownership, mark unknowns as
  OPEN QUESTION.

## Output
Feed the Data section of `templates/api-data-impact-template.md` (written by the
`api` engine to `clarify-output/api-data-impact.md`).
