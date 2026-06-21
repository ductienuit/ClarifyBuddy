#!/usr/bin/env python3
"""Clarify deterministic helpers (stdlib-only).

Usage:
  python clarify_tools.py status    [--dir clarify-output] [--json]
  python clarify_tools.py answers   <answer-sheet-file|-> [--dir clarify-output] [--json] [--by WHO] [--source LABEL]
  python clarify_tools.py integrity [--dir clarify-output] [--json]

These are AIDS for the Clarify engines, not replacements: the engine prompts stay
the source of rules. If Python is unavailable in the environment, the engines
perform the same steps manually — never fail a command because this script can't
run. Output defaults to compact markdown (paste-ready); --json for machines.
"""
import argparse, json, os, re, sys

# ---------------------------------------------------------------- shared
ARTIFACTS = [  # (filename-or-glob, produced-by, description) — lean set (Principle 13.11):
    # user-stories/edge/error/model/traceability/decision-log/elicitation are folded
    # into the draft / sign-off URD, NOT separate files.
    ("urd-draft.md", "/clarify:from-idea", "working URD draft (stories/edge/error/model/flows folded in)"),
    ("audit-report.md", "/clarify:audit", "score + findings"),
    ("change-impact.md", "/clarify:improve change-request", "CR impact analysis"),
    ("urd.md", "/clarify:finalize", "sign-off URD (no 'final' in name)"),
    ("wireframes.html", "/clarify:finalize", "low-fi HTML wireframes"),
    ("urd.html", "/clarify:finalize or export", "full HTML URD (from urd.md)"),
    ("urd.docx", "/clarify:finalize word or export word", "Word URD (from urd.md)"),
]
ID_RE = re.compile(r"\*\*([AQSV]\d+)\*\*")

def read(p):
    try:
        with open(p, encoding="utf-8") as f: return f.read()
    except OSError: return ""

def find_draft(d):
    for n in ("urd-draft.md", "urd.md"):
        p = os.path.join(d, n)
        if os.path.isfile(p): return p
    return None

def section(text, heading_re):
    """Return the body of the first section whose heading matches, up to the next heading of <= level."""
    m = re.search(heading_re, text, re.M)
    if not m: return ""
    level = len(re.match(r"#+", m.group(0)).group(0))
    rest = text[m.end():]
    nxt = re.search(r"(?m)^#{1,%d} " % level, rest)
    return rest[: nxt.start()] if nxt else rest

# ---------------------------------------------------------------- status
def cmd_status(d, as_json):
    rows, missing = [], []
    for spec, cmd, desc in ARTIFACTS:
        hit = next((n for n in spec.split("|") if os.path.exists(os.path.join(d, n))), None)
        rows.append({"artifact": spec, "desc": desc, "exists": bool(hit), "produced_by": cmd})
        if not hit: missing.append((spec, cmd))
    draft = find_draft(d)
    profile = {}
    if draft:
        body = section(read(draft), r"^#+ .*Document Profile.*$")
        for key in ("Role", "Standard", "Domain", "Language"):
            m = re.search(r"-\s*%s:\s*(.+)" % re.escape(key), body)
            if m: profile[key] = m.group(1).strip()
    # outstanding A/Q/S/V = labeled ids still present in the draft (applied decisions
    # are folded into the draft's Decisions/Change history and their OPEN QUESTIONs
    # removed — there is no separate decision-log file to subtract).
    draft_text = read(draft) if draft else ""
    ids = sorted(set(ID_RE.findall(draft_text)), key=lambda s: (s[0], int(s[1:])))
    outstanding = ids
    archived = sorted(n for n in (os.listdir(d) if os.path.isdir(d) else [])
                      if re.match(r"urd\.v\d+.*\.md$", n))
    out = {"dir": d, "artifacts": rows, "profile": profile,
           "outstanding_ids": outstanding, "archived_versions": archived}
    if as_json: print(json.dumps(out, ensure_ascii=False, indent=2)); return 0
    if not os.path.isdir(d) or not any(r["exists"] for r in rows):
        print(f"No Clarify artifacts found in `{d}`. Start with `/clarify:from-idea`.")
        return 0
    print("| Artifact | Exists | Produced by |\n| --- | --- | --- |")
    for r in rows:
        print(f"| {r['desc']} | {'yes' if r['exists'] else 'NO'} | {r['produced_by']} |")
    if profile:
        print("\nDocument Profile: " + "; ".join(f"{k}: {v}" for k, v in profile.items()))
    print(f"\nOutstanding A/Q/S/V ({len(outstanding)}): " + (", ".join(outstanding) or "none"))
    if archived: print("Archived versions: " + ", ".join(archived))
    return 0

# ---------------------------------------------------------------- answers
ANS_RE = re.compile(r"^\s*(Variant|[AQSV]\d+)\s*:\s*(.+?)\s*$")

def cmd_answers(d, src, as_json, by, source_label):
    text = sys.stdin.read() if src == "-" else read(src)
    decisions, warnings = [], []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("```"): continue
        m = ANS_RE.match(s)
        if not m:
            warnings.append(f"unparsed line: {s[:80]}"); continue
        item, val = m.group(1), m.group(2)
        kind = ("variant" if item == "Variant" else
                {"A": "assumption", "Q": "question", "S": "suggestion", "V": "variant"}[item[0]])
        action = val
        if kind == "assumption":
            action = "keep" if val.lower() == "keep" else "override: " + re.sub(r"^override\s*(->|:)?\s*", "", val, flags=re.I)
        if kind == "question" and val.lower() == "skip": action = "skip"
        if kind == "suggestion": action = val.lower().split()[0] if val else val
        decisions.append({"item": item, "kind": kind, "decision": action})
    # Parse only — there is NO separate decision-log.md file (Principle 13.10).
    # Applied decisions are recorded in the draft's Decisions made table + Change
    # history by the improve workflow; this command just structures the answer sheet.
    applied = [x for x in decisions if x["decision"] not in ("keep", "skip")]
    out = {"decisions": decisions, "applied": len(applied), "warnings": warnings,
           "by": by, "source": source_label}
    print(json.dumps(out, ensure_ascii=False, indent=2) if as_json else
          f"Parsed {len(decisions)} decisions ({len(applied)} to apply)."
          + (f" Warnings: {len(warnings)} (" + "; ".join(warnings[:5]) + ")" if warnings else "")
          + "\nNow APPLY them to the DRAFT per the improve workflow: update the Decisions "
            "made table + add a Change history row. Do NOT write a decision-log.md file.")
    return 0

# ---------------------------------------------------------------- integrity
DEF_PATTERNS = {  # id-kind -> (defining file globs, definition regex)
    # URD: business rules are defined as `**BR1 —** …` bullets or `| BR1 |` cells.
    "BR": (["urd-draft.md", "urd.md"], r"(?:\|\s*|\*\*)(BR-?\d+)\b"),
    # User stories defined in the §3.2 / §7 table as `| US-01 |` or `**US-01**`.
    "US": (["urd-draft.md", "urd.md"], r"(?:\|\s*|\*\*)(US-\d+)\b"),
    # Flows are named F0n-Name (number is the stable anchor; -Name is appended): capture the F\d+ part.
    "F":  (["urd-draft.md", "urd.md"], r"\|\s*(F\d+)(?:-\w+)?\s*\|"),
    # Error codes live in each process's §3.7 Error code & message table (ERR-MODULE-NNN).
    "ERR": (["urd-draft.md", "urd.md"], r"(ERR-[A-Z0-9]+-\d+)"),
}
REF_RES = {
    "BR": re.compile(r"\b(BR-?\d+)\b"),
    "US": re.compile(r"\b(US-\d+)\b"),
    "F": re.compile(r"\b(F\d{2,})\b"),
    "ERR": re.compile(r"\b(ERR-[A-Z0-9]+-\d+)\b"),
}

def cmd_integrity(d, as_json):
    defined = {k: set() for k in DEF_PATTERNS}
    for kind, (globs, rx) in DEF_PATTERNS.items():
        for g in globs:
            for m in re.finditer(rx, read(os.path.join(d, g))):
                defined[kind].add(m.group(1))
    dangling = []
    for base, _dirs, files in os.walk(d):
        for fn in files:
            if not fn.endswith((".md", ".html")): continue
            p = os.path.join(base, fn)
            text = read(p)
            for i, ln in enumerate(text.splitlines(), 1):
                for kind, rx in REF_RES.items():
                    for m in rx.finditer(ln):
                        tok = m.group(1)
                        if defined[kind] and tok not in defined[kind]:
                            dangling.append({"id": tok, "kind": kind,
                                             "where": f"{os.path.relpath(p, d)}:{i}"})
    # de-dup
    seen, uniq = set(), []
    for x in dangling:
        k = (x["id"], x["where"])
        if k not in seen: seen.add(k); uniq.append(x)
    out = {"defined_counts": {k: len(v) for k, v in defined.items()}, "dangling": uniq}
    if as_json: print(json.dumps(out, ensure_ascii=False, indent=2)); return 0
    if not uniq:
        print("Dangling references: none found (mechanical pass — still do the semantic review).")
        return 0
    print("## Dangling references (mechanical pass)\n| ID | Kind | Where |\n| --- | --- | --- |")
    for x in uniq[:200]:
        print(f"| {x['id']} | {x['kind']} | {x['where']} |")
    return 0

# ---------------------------------------------------------------- main
def main(argv):
    ap = argparse.ArgumentParser(prog="clarify_tools.py")
    ap.add_argument("cmd", choices=["status", "answers", "integrity"])
    ap.add_argument("src", nargs="?", help="answers: answer-sheet file or '-' for stdin")
    ap.add_argument("--dir", default="clarify-output")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--by", default="user")
    ap.add_argument("--source", default="answer sheet")
    a = ap.parse_args(argv)
    if a.cmd == "status":    return cmd_status(a.dir, a.json)
    if a.cmd == "answers":
        if not a.src: ap.error("answers requires a file path or '-'")
        return cmd_answers(a.dir, a.src, a.json, a.by, a.source)
    if a.cmd == "integrity": return cmd_integrity(a.dir, a.json)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
