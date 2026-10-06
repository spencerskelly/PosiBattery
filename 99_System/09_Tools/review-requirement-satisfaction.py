#!/usr/bin/env python3
"""Step 14 Requirement satisfaction review.

Reviews every active Requirement for at least one valid satisfaction path from
Function, Design, Object, or Result. Known gaps are preserved explicitly rather
than closed with semantically weak links.
"""
# Governed Step 14 review entry point
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"requirement-satisfaction-review.md"

def fm(text):
    if not text.startswith("---\n"): return {}
    e=text.find("\n---",4)
    if e<0:return {}
    try:return yaml.safe_load(text[4:e]) or {}
    except Exception:return {}

def vals(v):
    if v is None:return []
    return v if isinstance(v,list) else [v]

def target(v):
    if not isinstance(v,str):return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

notes={}; bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else: ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

reqs={p:d for p,d in notes.items() if d.get("type")=="Requirement"}
allowed={"Function","Design","Object","Result"}
counts=Counter(); findings=[]; unresolved=[]; rows=[]

for p,d in sorted(reqs.items()):
    counts["requirements"]+=1
    satisfiers=[]
    for raw in vals(d.get("satisfiedBy")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-satisfier",str(raw)))
            continue
        typ=notes[q].get("type")
        if typ not in allowed:
            findings.append((p,"invalid-satisfier-type",f"{Path(q).stem}: {typ}"))
            continue
        satisfiers.append(q)
        counts[f"satisfier_type_{typ}"]+=1

        inv={resolve(target(x)) for x in vals(notes[q].get("satisfies")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"missing-satisfies-inverse",f"{Path(q).stem} lacks reciprocal satisfies."))

    if satisfiers:
        counts["requirements_with_satisfaction"]+=1
    else:
        if Path(p).stem=="BMID - Preserve Battery Association":
            unresolved.append((p,"EXC-ARCH-UNRESOLVED","No Function/Design/Object/Result yet demonstrates the required battery-association preservation without inferring an implementation mechanism."))
            counts["requirements_with_explicit_gap"]+=1
        else:
            findings.append((p,"missing-satisfaction","No valid satisfiedBy path and no approved explicit gap."))

    rows.append((p,satisfiers))

print("requirement satisfaction review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  explicit unresolved satisfaction gaps: {len(unresolved)}")
for p,code,msg in unresolved: print(f"  UNRESOLVED {code}: {p}: {msg}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,sats in rows:
    print(f"  SATISFACTION {Path(p).stem}: {', '.join(Path(x).stem for x in sats) if sats else '(gap)'}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Requirement Satisfaction Review","",
"Step 14 review of every governed Requirement for a valid satisfaction path through Function, Design, Object, or Result.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| explicit unresolved satisfaction gaps | {len(unresolved)} |",f"| findings | {len(findings)} |","","## Satisfaction map","",
"| Requirement | Satisfied by |","|---|---|"]
for p,sats in rows:
    lines.append(f"| {p} | {'<br>'.join(Path(x).stem for x in sats) if sats else '_Explicit gap_'} |")
lines += ["","## Explicit unresolved gaps","",
"| Requirement | Exception | Reason |","|---|---|---|"]
if unresolved:
    for p,code,msg in unresolved: lines.append(f"| {p} | {code} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- Function satisfaction is preferred when a Function directly fulfills the Requirement behavior.",
"- Design or Object satisfaction is valid when the Requirement is fulfilled by an implementation/product property rather than one discrete Function.",
"- Result satisfaction is reserved for an executed evidence/result element that itself demonstrates fulfillment under the schema.",
"- appliesTo is scope, not satisfaction.",
"- A Verification verifies a Requirement; it does not satisfy it.",
"- BMID Preserve Battery Association remains explicitly unresolved because the current model does not yet define a defensible implementation/satisfaction mechanism.",
"- PosiGuard lead-acid/lithium support is satisfied by the PosiCharge PosiGuard Object because the Requirement is an application/product-coverage obligation and the product note explicitly establishes that support.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("REQUIREMENT SATISFACTION REVIEW PASSED WITH EXPLICIT GAP" if unresolved else "REQUIREMENT SATISFACTION REVIEW PASSED")
