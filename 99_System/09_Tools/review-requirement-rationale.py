#!/usr/bin/env python3
"""Step 12 Requirement upstream-rationale review.

Reviews every governed Requirement for a defensible upstream reason to exist.
Accepted rationale paths are governed semantic relationships such as drivenBy,
derivedFrom, refinedBy/childOf, references, plus appliesTo as scope/context.
This step does not infer new requirements or source claims.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"requirement-upstream-rationale-review.md"

def fm(text):
    if not text.startswith("---\n"): return {}
    e=text.find("\n---",4)
    if e<0: return {}
    try: return yaml.safe_load(text[4:e]) or {}
    except Exception: return {}

def vals(v):
    if v is None: return []
    return v if isinstance(v,list) else [v]

def target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

notes={}
bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; bybase[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

reqs={p:d for p,d in notes.items() if d.get("type")=="Requirement"}
counts=Counter(); findings=[]; rows=[]

for p,d in sorted(reqs.items()):
    counts["requirements"]+=1
    rationale=[]
    for field in ("drivenBy","derivedFrom","refinedBy","childOf","references"):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,"unresolved-upstream",field,str(raw)))
                continue
            rationale.append((field,q,notes[q].get("type"),notes[q].get("subtype")))
            counts[f"rationale_{field}"]+=1

    scope=[]
    for raw in vals(d.get("appliesTo")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-scope","appliesTo",str(raw)))
            continue
        scope.append(q)
        counts["scope_appliesTo"]+=1

    if not rationale:
        findings.append((p,"missing-upstream-rationale","", "No governed upstream rationale relationship."))
    else:
        counts["requirements_with_upstream_rationale"]+=1

    if not scope:
        findings.append((p,"missing-scope","", "No appliesTo scope is modeled."))
    else:
        counts["requirements_with_scope"]+=1

    # Rationale quality: an active product requirement should normally be driven
    # by a Use Case/need, or derived/refined/referenced from another formal source.
    valid=False
    for field,q,typ,sub in rationale:
        if field=="drivenBy" and typ=="Use Case":
            valid=True
            if sub=="why": counts["rationale_customer_need"]+=1
            elif sub=="what": counts["rationale_operational_use_case"]+=1
            else: counts["rationale_other_use_case_context"]+=1
        elif field in {"derivedFrom","refinedBy","childOf"} and typ=="Requirement":
            valid=True; counts["rationale_requirement_hierarchy"]+=1
        elif field=="references" and typ in {"Requirement","Document"}:
            valid=True; counts["rationale_formal_reference"]+=1

    if valid: counts["requirements_with_defensible_rationale_path"]+=1
    else: findings.append((p,"weak-rationale-type","", "Upstream links exist but none form an approved rationale path."))

    rows.append((p,rationale,scope))

print("requirement upstream rationale review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,fld,msg in findings: print(f"  FINDING {k}: {p}: {fld} {msg}")
for p,rationale,scope in rows:
    rs="; ".join(f"{f}->{Path(q).stem} [{typ}/{sub or '-'}]" for f,q,typ,sub in rationale)
    ss=", ".join(Path(q).stem for q in scope)
    print(f"  REQUIREMENT {Path(p).stem}: rationale={rs}; scope={ss}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Requirement Upstream Rationale Review","",
"Step 12 review of every governed Requirement for why it exists and where it applies.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Requirement rationale paths","",
"| Requirement | Upstream rationale | Scope |","|---|---|---|"]
for p,rationale,scope in rows:
    rs="<br>".join(f"{f} → {Path(q).stem} ({typ}{' / '+str(sub) if sub else ''})" for f,q,typ,sub in rationale)
    ss="<br>".join(Path(q).stem for q in scope)
    lines.append(f"| {p} | {rs} | {ss} |")
lines += ["","## Findings","",
"| Path | Kind | Field | Detail |","|---|---|---|---|"]
if findings:
    for p,k,fld,msg in findings: lines.append(f"| {p} | {k} | {fld} | {msg} |")
else: lines.append("| _None_ | | | |")
lines += ["","## Interpretation","",
"- drivenBy from a Customer Need or operational Use Case is a valid rationale path for an active product Requirement.",
"- appliesTo establishes explicit engineering scope but does not by itself explain why a Requirement exists.",
"- derivedFrom/refinedBy/childOf are valid Requirement-hierarchy rationale paths when such hierarchy exists.",
"- references to a formal Requirement or Document may provide source rationale when the relationship is semantically correct.",
"- Body prose or folder placement may explain context to a human but does not replace governed upstream rationale.",
"- No new upstream relationship is added unless existing model content supports the exact semantic claim.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("REQUIREMENT UPSTREAM RATIONALE REVIEW PASSED")
