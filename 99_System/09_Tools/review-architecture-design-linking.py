#!/usr/bin/env python3
"""Step 10 architecture-to-design semantic-linking review.

Reviews all Design notes plus architecture/product Objects for implementation
and context relationships: hasDesign/designOf, realizedBy/realizes,
appliesTo/applies, satisfies/satisfiedBy, and supported dependsOn/dependencyOf.
Report-only; unresolved choices are recorded rather than filled.
"""
# Step 10 governed review entry point
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"architecture-design-linking-review.md"

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
texts={}
bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    text=p.read_text(encoding="utf-8",errors="replace")
    d=fm(text)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; texts[rel]=text; bybase[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

designs={p:d for p,d in notes.items() if d.get("type")=="Design"}
objects={p:d for p,d in notes.items() if d.get("type")=="Object"}
functions={p:d for p,d in notes.items() if d.get("type")=="Function"}

incoming=defaultdict(list)
for p,d in notes.items():
    for field in ("hasDesign","designOf","realizedBy","realizes","appliesTo","applies","satisfies","satisfiedBy","dependsOn","dependencyOf","performs","performedBy"):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if q: incoming[q].append((field,p))

counts=Counter()
findings=[]
unresolved=[]
active_bmid_functions=[]
bmid_path=resolve("PosiCharge BMID")

# Current active-engineering function set = functions explicitly performed by BMID.
if bmid_path:
    for raw in vals(notes[bmid_path].get("performs")):
        q=resolve(target(raw))
        if q and q in functions:
            active_bmid_functions.append(q)

# Design inventory.
for p,d in sorted(designs.items()):
    counts["designs"]+=1
    abstract=bool(d.get("abstract",False))
    counts["abstract_designs" if abstract else "specific_designs"]+=1

    ownership=bool(vals(d.get("designOf"))) or any(f=="hasDesign" for f,_ in incoming[p])
    realizes=bool(vals(d.get("realizes"))) or any(f=="realizedBy" for f,_ in incoming[p])
    applies=bool(vals(d.get("appliesTo"))) or any(f=="applies" for f,_ in incoming[p])
    satisfies=bool(vals(d.get("satisfies"))) or any(f=="satisfiedBy" for f,_ in incoming[p])
    dependency=bool(vals(d.get("dependsOn")) or vals(d.get("dependencyOf"))) or any(f in {"dependsOn","dependencyOf"} for f,_ in incoming[p])

    if ownership: counts["designs_with_ownership_context"]+=1
    if realizes: counts["designs_with_realization_context"]+=1
    if applies: counts["designs_with_applicability_context"]+=1
    if satisfies: counts["designs_with_satisfaction_context"]+=1
    if dependency: counts["designs_with_dependency_context"]+=1
    if ownership or realizes or applies or satisfies or dependency:
        counts["designs_with_any_implementation_context"]+=1
    else:
        counts["designs_without_any_implementation_context"]+=1
        # Generic abstract Design roots are allowed to exist primarily as taxonomy.
        if not abstract:
            findings.append((p,"specific-design-context-gap","Specific Design has no ownership, realization, applicability, satisfaction, or dependency context."))

# Verify Object<->Design reciprocal ownership wherever asserted.
for p,d in objects.items():
    for raw in vals(d.get("hasDesign")):
        q=resolve(target(raw))
        if not q or q not in designs: continue
        backs={resolve(target(x)) for x in vals(notes[q].get("designOf"))}
        if p not in backs:
            findings.append((p,"hasDesign-inverse",f"hasDesign {Path(q).stem} lacks reciprocal designOf."))
for p,d in designs.items():
    for raw in vals(d.get("designOf")):
        q=resolve(target(raw))
        if not q or q not in objects: continue
        backs={resolve(target(x)) for x in vals(notes[q].get("hasDesign"))}
        if p not in backs:
            findings.append((p,"designOf-inverse",f"designOf {Path(q).stem} lacks reciprocal hasDesign."))

# Review active BMID function implementation choices.
for p in sorted(active_bmid_functions):
    d=functions[p]
    direct_realized=[resolve(target(x)) for x in vals(d.get("realizedBy"))]
    direct_realized=[x for x in direct_realized if x in designs]
    deps=[resolve(target(x)) for x in vals(d.get("dependsOn"))]
    deps=[x for x in deps if x in designs]
    if direct_realized:
        counts["active_bmid_functions_with_direct_design_realization"]+=1
    elif deps:
        counts["active_bmid_functions_with_design_dependency_only"]+=1
    else:
        counts["active_bmid_functions_with_no_design_path"]+=1
        unresolved.append((p,"EXC-ARCH-UNRESOLVED","No supported Design realization/dependency is currently modeled."))

# Check realizedBy/realizes symmetry for Function->Design and Design->Function.
for p,d in functions.items():
    for raw in vals(d.get("realizedBy")):
        q=resolve(target(raw))
        if not q or q not in designs: continue
        backs={resolve(target(x)) for x in vals(notes[q].get("realizes"))}
        if p not in backs:
            findings.append((p,"realizedBy-inverse",f"realizedBy {Path(q).stem} lacks reciprocal realizes."))
for p,d in designs.items():
    for raw in vals(d.get("realizes")):
        q=resolve(target(raw))
        if not q or q not in functions: continue
        backs={resolve(target(x)) for x in vals(notes[q].get("realizedBy"))}
        if p not in backs:
            findings.append((p,"realizes-inverse",f"realizes {Path(q).stem} lacks reciprocal realizedBy."))

# Active BMID Object design entry.
if bmid_path:
    bmid_designs=[resolve(target(x)) for x in vals(notes[bmid_path].get("hasDesign"))]
    bmid_designs=[x for x in bmid_designs if x in designs]
    counts["bmid_object_owned_designs"]+=len(bmid_designs)
    if not bmid_designs:
        findings.append((bmid_path,"active-object-design-gap","Active BMID Object has no hasDesign entry."))

print("architecture to design linking review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  active BMID functions reviewed: {len(active_bmid_functions)}")
print(f"  unresolved architecture choices: {len(unresolved)}")
for p,code,msg in unresolved:
    print(f"  UNRESOLVED {code}: {p}: {msg}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings:
    print(f"  FINDING {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=[
"# Architecture-to-Design Linking Review","",
"Step 10 review of Design ownership, realization, applicability, satisfaction, dependency context, and active BMID architecture choices.","",
"## Summary","",
"| Metric | Count |","|---|---:|",
]
for k,v in sorted(counts.items()):
    lines.append(f"| {k} | {v} |")
lines += [
f"| active BMID functions reviewed | {len(active_bmid_functions)} |",
f"| unresolved architecture choices | {len(unresolved)} |",
f"| findings | {len(findings)} |","",
"## Unresolved architecture choices","",
"| Function | Exception | Reason |","|---|---|---|"
]
if unresolved:
    for p,code,msg in unresolved:
        lines.append(f"| {p} | {code} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings:
        lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- hasDesign/designOf expresses design ownership/context, not merely similarity.",
"- realizedBy/realizes is reserved for direct implementation of Function/Use Case behavior by a Design.",
"- dependsOn/dependencyOf is an enabling dependency and must not be promoted to realization merely to close a traceability gap.",
"- appliesTo/applies scopes a Design/Requirement/Info claim; absence is not automatically a defect when ownership/realization already supplies context.",
"- Specific Designs without any implementation/context relationship are review findings; abstract/general Design families may legitimately exist primarily as reusable taxonomy.",
"- Active BMID Functions with no supported Design path are recorded as EXC-ARCH-UNRESOLVED rather than linked to a nearby Design by inference.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings:
    raise SystemExit(2)
print("ARCHITECTURE DESIGN LINKING REVIEW PASSED WITH EXPLICIT UNRESOLVED CHOICES" if unresolved else "ARCHITECTURE DESIGN LINKING REVIEW PASSED")
