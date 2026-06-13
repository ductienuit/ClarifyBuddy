#!/usr/bin/env python3
"""Clarify deterministic helpers (stdlib-only).

Usage:
  python clarify_tools.py status    [--dir clarify-output] [--json]
  python clarify_tools.py answers   <answer-sheet-file|-> [--dir clarify-output] [--json] [--by WHO] [--source LABEL]
  python clarify_tools.py integrity [--dir clarify-output] [--json]
  python clarify_tools.py manifest  [--dir clarify-output] [--json]

These are AIDS for the Clarify engines, not replacements: the engine prompts stay
the source of rules. If Python is unavailable in the environment, the engines
perform the same steps manually — never fail a command because this script can't
run. Output defaults to compact markdown (paste-ready); --json for machines.
"""
import argparse, datetime, json, os, re, sys

# ---------------------------------------------------------------- shared
ARTIFACTS = [  # (filename-or-glob, produced-by, description)
    ("prd-draft.md|brd-draft.md", "/clarify:from-idea", "draft (PRD/BRD)"),
    ("elicitation-pack.md", "/clarify:from-idea", "questions grouped by owner"),
    ("edge-case-matrix.md", "/clarify:from-idea or from-spec", "edge cases"),
    ("error-handling.md", "/clarify:from-idea or from-spec", "error/message map"),
    ("model-suggestions.md", "/clarify:from-idea or from-spec", "flows/diagrams/state"),
    ("audit-report.md", "/clarify:audit or from-spec", "score + findings"),
    ("stories.md", "/clarify:from-spec", "stories + AC"),
    ("test-scenarios.md", "/clarify:from-spec", "test scenarios"),
    ("api-data-impact.md", "/clarify:from-spec", "API/data impact"),
    ("traceability-matrix.md", "/clarify:from-spec", "traceability"),
    ("decision-log.md", "/clarify:improve answers", "decision audit trail"),
    ("change-impact.md", "/clarify:improve change-request", "CR impact analysis"),
    ("final-brd.md|final-prd.md", "/clarify:finalize", "final sign-off doc"),
    ("wireframes.html", "/clarify:finalize", "low-fi HTML wireframes"),
    ("review-pack/index.html", "/clarify:export", "visual review pack"),
]
ID_RE = re.compile(r"\*\*([AQSV]\d+)\*\*")

def read(p):
    try:
        with open(p, encoding="utf-8") as f: return f.read()
    except OSError: return ""

def find_draft(d):
    for n in ("brd-draft.md", "prd-draft.md"):
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
        for key in ("Role", "Target standard", "Domain", "Language"):
            m = re.search(r"-\s*%s:\s*(.+)" % re.escape(key), body)
            if m: profile[key] = m.group(1).strip()
    # outstanding A/Q/S/V = ids in draft minus ids already in decision-log
    draft_text = read(draft) if draft else ""
    ids = sorted(set(ID_RE.findall(draft_text)), key=lambda s: (s[0], int(s[1:])))
    decided = set(re.findall(r"\|\s*([AQSV]\d+|CR-\d+)\s*\|", read(os.path.join(d, "decision-log.md"))))
    outstanding = [i for i in ids if i not in decided]
    archived = sorted(n for n in (os.listdir(d) if os.path.isdir(d) else [])
                      if re.match(r"final-(brd|prd)\.v\d+.*\.md$", n))
    out = {"dir": d, "artifacts": rows, "profile": profile,
           "outstanding_ids": outstanding, "decided_count": len(decided),
           "archived_versions": archived}
    if as_json: print(json.dumps(out, ensure_ascii=False, indent=2)); return 0
    if not os.path.isdir(d) or not any(r["exists"] for r in rows):
        print(f"No Clarify artifacts found in `{d}`. Start with `/clarify:from-idea` "
              "(new idea) or `/clarify:from-spec` (existing document).")
        return 0
    print("| Artifact | Exists | Produced by |\n| --- | --- | --- |")
    for r in rows:
        print(f"| {r['desc']} | {'yes' if r['exists'] else 'NO'} | {r['produced_by']} |")
    if profile:
        print("\nDocument Profile: " + "; ".join(f"{k}: {v}" for k, v in profile.items()))
    print(f"\nOutstanding A/Q/S/V ({len(outstanding)}): " + (", ".join(outstanding) or "none"))
    if archived: print("Archived final versions: " + ", ".join(archived))
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
    # append to decision log (skip skips and 'keep')
    applied = [x for x in decisions if not (x["decision"] in ("keep", "skip"))]
    log = os.path.join(d, "decision-log.md")
    os.makedirs(d, exist_ok=True)
    if not os.path.exists(log):
        with open(log, "w", encoding="utf-8") as f:
            f.write("<!-- Generated by Clarify improve answers. Append-only — never rewrite past rows. -->\n\n"
                    "# Decision Log\n\n"
                    "| # | Date | Item | Decision | Decided by | Source | Sections affected |\n"
                    "| --- | --- | --- | --- | --- | --- | --- |\n")
    existing = read(log)
    n = len(re.findall(r"(?m)^\|\s*\d+\s*\|", existing))
    today = datetime.date.today().isoformat()
    with open(log, "a", encoding="utf-8") as f:
        for x in applied:
            n += 1
            f.write(f"| {n} | {today} | {x['item']} | {x['decision']} | {by} | {source_label} | <fill> |\n")
    out = {"decisions": decisions, "logged": len(applied), "warnings": warnings, "log": log}
    print(json.dumps(out, ensure_ascii=False, indent=2) if as_json else
          f"Parsed {len(decisions)} decisions; appended {len(applied)} to {log}."
          + (f" Warnings: {len(warnings)} (" + "; ".join(warnings[:5]) + ")" if warnings else "")
          + "\nNow APPLY the decisions to the draft per the improve workflow, and fill 'Sections affected'.")
    return 0

# ---------------------------------------------------------------- integrity
DEF_PATTERNS = {  # id-kind -> (defining file globs, definition regex)
    "BR": (["brd-draft.md", "prd-draft.md", "final-brd.md", "final-prd.md"], r"\|\s*(BR-?\d+)\s*\|"),
    "F":  (["model-suggestions.md", "final-brd.md", "final-prd.md"], r"\|\s*(F\d+)\s*\|"),
    "S":  (["review-pack/screens/screen-inventory.md"], r"\|\s*(S\d+)\s*\|"),
    "CODE": (["error-handling.md"], r"\|\s*([A-Z][A-Z0-9]+_[A-Z0-9_]*\d+)\s*\|"),
}
REF_RES = {
    "BR": re.compile(r"\b(BR-?\d+)\b"),
    "F": re.compile(r"\b(F\d{2,})\b"),
    "CODE": re.compile(r"\b([A-Z][A-Z0-9]{1,}_[A-Z0-9_]*\d+)\b"),
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

# ---------------------------------------------------------------- manifest
def cmd_manifest(d, as_json):
    rp = os.path.join(d, "review-pack")
    mpath = os.path.join(rp, "manifest.json")
    try:
        manifest = json.loads(read(mpath)) if os.path.exists(mpath) else {}
    except json.JSONDecodeError:
        manifest = {}
    entries = []
    for base, _dirs, files in os.walk(rp):
        for fn in files:
            if fn == "manifest.json": continue
            rel = os.path.relpath(os.path.join(base, fn), d).replace(os.sep, "/")
            ext = os.path.splitext(fn)[1]
            rendered = ext in (".svg", ".png", ".html", ".pdf")
            entries.append({"path": rel, "render_status": "rendered" if rendered else "source-only"})
    # keep prior descriptive fields where paths match
    prior = {e.get("path"): e for e in manifest.get("artifacts", []) if isinstance(e, dict)}
    for e in entries:
        if e["path"] in prior:
            merged = dict(prior[e["path"]]); merged.update(e); e.clear(); e.update(merged)
    manifest.setdefault("generated_by", "clarify:export")
    manifest["artifacts"] = entries
    os.makedirs(rp, exist_ok=True)
    with open(mpath, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    msg = {"manifest": mpath, "artifact_count": len(entries)}
    print(json.dumps(msg, indent=2) if as_json else
          f"manifest.json updated: {len(entries)} artifacts verified on disk.")
    return 0

# ---------------------------------------------------------------- main
def main(argv):
    ap = argparse.ArgumentParser(prog="clarify_tools.py")
    ap.add_argument("cmd", choices=["status", "answers", "integrity", "manifest"])
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
    if a.cmd == "manifest":  return cmd_manifest(a.dir, a.json)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
