#!/usr/bin/env python3
"""Step 15 Function ownership and decomposition review.

Reviews every Function for product performers, generic/goal decomposition,
specialization, inverse synchronization, and explicit behavior-context entry.
Ordering/triggering is inventoried but not required here; Step 17 owns actual
sequence/state semantics.
"""
# Governed Step 15 review entry point
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"function-ownership-decomposition-review.md"

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

funcs={p:d for p,d in notes.items() if d.get("type")=="Function"}
objects={p:d for p,d in notes.items() if d.get("type")=="Object"}
counts=Counter(); findings=[]; generic=[]; specific=[]

# incoming relationship index from model notes
incoming=defaultdict(list)
for p,d in notes.items():
    for field in ("performs","hasChild","supertypeOf","realizedBy","satisfiedBy","precedes","triggers"):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if q: incoming[q].append((field,p))

for p,d in sorted(funcs.items()):
    counts["functions"]+=1
    tags=set(str(x) for x in vals(d.get("tags")))
    is_generic=("goal-function" in tags or "general-function" in tags)
    if is_generic:
        generic.append(p); counts["generic_or_goal_functions"]+=1
    else:
        specific.append(p); counts["specific_functions"]+=1

    performers=[resolve(target(x)) for x in vals(d.get("performedBy")) if resolve(target(x))]
    childof=[resolve(target(x)) for x in vals(d.get("childOf")) if resolve(target(x))]
    haschild=[resolve(target(x)) for x in vals(d.get("hasChild")) if resolve(target(x))]
    subtype=[resolve(target(x)) for x in vals(d.get("subtypeOf")) if resolve(target(x))]
    supertype=[resolve(target(x)) for x in vals(d.get("supertypeOf")) if resolve(target(x))]
    realized=[resolve(target(x)) for x in vals(d.get("realizes")) if resolve(target(x))]
    satisfies=[resolve(target(x)) for x in vals(d.get("satisfies")) if resolve(target(x))]
    precedes=[resolve(target(x)) for x in vals(d.get("precedes")) if resolve(target(x))]
    follows=[resolve(target(x)) for x in vals(d.get("follows")) if resolve(target(x))]
    triggered=[resolve(target(x)) for x in vals(d.get("triggeredBy")) if resolve(target(x))]
    triggers=[resolve(target(x)) for x in vals(d.get("triggers")) if resolve(target(x))]

    if performers: counts["functions_with_performer"]+=1
    if childof or haschild: counts["functions_with_decomposition"]+=1
    if subtype or supertype: counts["functions_with_specialization"]+=1
    if realized: counts["functions_with_use_case_realization"]+=1
    if satisfies: counts["functions_with_requirement_satisfaction"]+=1
    if precedes or follows: counts["functions_with_sequence"]+=1
    if triggered or triggers: counts["functions_with_trigger_semantics"]+=1

    # Specific functions should have at least one actual Object performer.
    if not is_generic and not performers:
        findings.append((p,"specific-function-no-performer","Specific Function has no performedBy Object."))

    # Generic/goal functions intentionally roll up behavior. They should have
    # decomposition or specialization context, not be disconnected taxonomy labels.
    if is_generic and not (childof or haschild or subtype or supertype):
        findings.append((p,"generic-function-no-structure","Generic/goal Function has no child/parent or specialization structure."))

    # Validate performer target type and reciprocal Object.performs.
    for q in performers:
        if q not in objects:
            findings.append((p,"performer-type",f"{Path(q).stem} is not an Object."))
            continue
        inv={resolve(target(x)) for x in vals(notes[q].get("performs")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"performer-inverse",f"{Path(q).stem} lacks reciprocal performs."))

    # Validate child decomposition reciprocity and Function endpoint types.
    for q in childof:
        if q not in funcs:
            findings.append((p,"childOf-type",f"{Path(q).stem} is not a Function."))
            continue
        inv={resolve(target(x)) for x in vals(notes[q].get("hasChild")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"childOf-inverse",f"{Path(q).stem} lacks reciprocal hasChild."))
    for q in haschild:
        if q not in funcs:
            findings.append((p,"hasChild-type",f"{Path(q).stem} is not a Function."))
            continue
        inv={resolve(target(x)) for x in vals(notes[q].get("childOf")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"hasChild-inverse",f"{Path(q).stem} lacks reciprocal childOf."))

    # Validate specialization reciprocity among Functions.
    for q in subtype:
        if q not in funcs:
            findings.append((p,"subtypeOf-type",f"{Path(q).stem} is not a Function."))
            continue
        inv={resolve(target(x)) for x in vals(notes[q].get("supertypeOf")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"subtypeOf-inverse",f"{Path(q).stem} lacks reciprocal supertypeOf."))
    for q in supertype:
        if q not in funcs:
            findings.append((p,"supertypeOf-type",f"{Path(q).stem} is not a Function."))
            continue
        inv={resolve(target(x)) for x in vals(notes[q].get("subtypeOf")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"supertypeOf-inverse",f"{Path(q).stem} lacks reciprocal subtypeOf."))

# Active BMID ownership check.
bmid=resolve("PosiCharge BMID")
active=[]
if bmid:
    for raw in vals(notes[bmid].get("performs")):
        q=resolve(target(raw))
        if q in funcs: active.append(q)
counts["active_bmid_functions"]=len(active)
for p in active:
    performers={resolve(target(x)) for x in vals(notes[p].get("performedBy")) if resolve(target(x))}
    if bmid not in performers:
        findings.append((p,"active-bmid-performer-inverse","PosiCharge BMID performs Function but Function lacks performedBy inverse."))
counts["active_bmid_functions_with_performer_inverse"]=sum(
    1 for p in active if bmid in {resolve(target(x)) for x in vals(notes[p].get("performedBy")) if resolve(target(x))}
)

# A sequence/trigger link is valid only if inverse exists and target class fits.
for p,d in funcs.items():
    for fld,invfld in (("precedes","follows"),("follows","precedes"),("triggeredBy","triggers"),("triggers","triggeredBy")):
        for raw in vals(d.get(fld)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,"unresolved-behavior-link",f"{fld}: {raw}"))
                continue
            if fld in {"precedes","follows"} and notes[q].get("type")!="Function":
                findings.append((p,"sequence-type",f"{fld} target {Path(q).stem} is not Function."))
            inv={resolve(target(x)) for x in vals(notes[q].get(invfld)) if resolve(target(x))}
            if p not in inv:
                findings.append((p,"behavior-inverse",f"{fld} {Path(q).stem} lacks reciprocal {invfld}."))

print("function ownership and decomposition review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Function Ownership and Decomposition Review","",
"Step 15 whole-vault review of Function performers, generic/goal decomposition, specialization, product context, and any existing ordering/trigger links.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- Specific product Functions should identify one or more Object performers when evidence states who performs the behavior.",
"- Goal/general Functions are reusable behavior taxonomy and may intentionally have no direct product performer; they must instead have meaningful decomposition or specialization context.",
"- hasChild/childOf is behavioral decomposition/ownership; subtypeOf/supertypeOf is behavioral specialization. They are not interchangeable.",
"- performs/performedBy is product behavior ownership/use and is validated bidirectionally.",
"- realizedBy/realizes and satisfies/satisfiedBy provide downstream behavioral traceability but do not replace performer ownership for a specific Function.",
"- precedes/follows and triggeredBy/triggers are not required merely to make a Function connected. Step 17 reviews actual behavioral sequencing/state semantics.",
"- No Function hierarchy, sequence, trigger, or performer relationship is invented by this review.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("FUNCTION OWNERSHIP AND DECOMPOSITION REVIEW PASSED")
