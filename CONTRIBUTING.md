# Contributing to Clarify

Thanks for helping improve Clarify. A few conventions keep the skill pack
coherent and agent-friendly.

## Principles

- **Clarify is a requirement-quality skill pack, not a PRD generator.** Every
  change should improve clarity, testability, traceability, or handoff quality.
- **Single sources of truth.** Anti-patterns live in
  `.clarify/anti-patterns/anti-patterns.yaml`; scoring lives in
  `.clarify/evaluators/scoring-rubric.yaml`. The human-readable catalog and
  any docs must be reconciled to these files, not the other way around.
- **Keep core domain-agnostic.** No domain logic in engines, workflows, or
  templates. Domain knowledge belongs in `.clarify/domain-packs/`.

## Engine files

- Imperative instructions, target **< 150 lines**, no filler prose.
- A workflow loads only the engines it needs per step.

## Anti-patterns

- Exactly **36** entries. If you add one, update both the yaml and the human
  catalog, and assign a `dimension` that matches a rubric dimension id.
- Each entry needs: `id`, `name`, `severity`, `dimension`, `definition`,
  `bad_example`, `why_dangerous`, `detect`, `fix`, `good_example`.

## Scoring

- 10 dimensions, weights sum to 100. Each dimension needs `full`/`half`/`zero`
  anchors.
- Deduction model and bands are defined in
  `.clarify/evaluators/requirement-quality-score.md`.

## Testing your change

**Always lint first** — it checks every count/sync invariant (counts in docs,
yaml↔md anti-pattern sync, rubric dimensions/weights, referenced files exist,
eval ids, detect keys):

```
pwsh ./lint-skill.ps1
```

`build-skill.ps1` runs the lint automatically and refuses to package on
violations (`-SkipLint` to bypass — don't).

Then run the self-audits and diff against the expected files:

```
/clarify:audit .clarify/eval/weak-prd-checkout.md
/clarify:audit .clarify/eval/weak-brd-savings.md
```

## Commits & PRs

- Conventional, present-tense commit subjects.
- Update `CHANGELOG.md` under "Unreleased".
