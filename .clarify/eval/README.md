# Clarify Eval — Golden Tests for the Skill Itself

These are deliberately weak requirement docs plus the findings Clarify should
produce. Use them to verify the skill behaves consistently.

## Files

- `weak-prd-checkout.md` — a weak e-commerce checkout PRD.
- `weak-prd-checkout.expected.md` — the anti-patterns and band an audit should
  flag for it.
- `weak-prd-roles.md` — a weak B2B role-management PRD (no expected file yet;
  exercise `from-spec`).
- `weak-brd-savings.md` — a weak savings-deposit BRD that exercises the
  **product/operational lenses** (anti-patterns 27–36: config ownership,
  effective dating, cohort, batch job, system actors, authentication, error
  mapping, operation state, jargon, mixed-process diagrams).
- `weak-brd-savings.expected.md` — its golden findings (the 10 newer ids are
  must-flag).

## How to run

```
/clarify:audit .clarify/eval/weak-prd-checkout.md
```

Then diff the findings in `clarify-output/audit-report.md` against
`weak-prd-checkout.expected.md`. Every **must-flag** anti-pattern listed in the
expected file should appear. The band should match (or be at least as severe).

## Pass criteria

- All `must_flag` anti-pattern ids are detected.
- At least one `blocker` is found → band capped at "Not ready for handoff".
- No core domain logic was required (the doc is audited domain-agnostically;
  selecting `ecommerce-mini` may add detail but must not change the verdict).
