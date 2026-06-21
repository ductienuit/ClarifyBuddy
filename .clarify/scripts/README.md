# Clarify Scripts — deterministic helpers

`clarify_tools.py` (Python 3, stdlib-only) does the mechanical parts of a few
steps so the LLM doesn't have to count or grep by hand. **The engine prompts stay
the source of rules** — these scripts are aids, not replacements.

## Invocation
Try `python3`, then `python`. Run from the project root (paths default to
`clarify-output/`; override with `--dir`). Add `--json` for machine output.

| Subcommand | Used by | Does |
| --- | --- | --- |
| `status` | `workflows/status.md` | Artifact inventory (lean set — Principle 13.11), Document Profile, outstanding `A/Q/S/V` ids in the draft, archived versions. |
| `answers <file\|->` | `workflows/improve.md` (mode `answers`) | Parse a filled Answer Sheet → normalized decisions JSON. Writes **no file** — applying decisions to the draft's Decisions made table + Change history is the LLM's job (no `decision-log.md`; Principle 13.10). |
| `integrity` | `engine/trace.md` | Mechanical dangling-reference pass: collect defined ids (BR / F / US / ERR codes) vs referenced ids across clarify-output; print a Dangling references table. Best-effort regex — the LLM still does the semantic review. |

## Fallback rule (non-negotiable)
If no Python runtime is available, perform the same steps **manually** per the
engine/workflow checklist. **Never fail a command because this script can't
run**, and never skip the step — fall back, don't drop.
