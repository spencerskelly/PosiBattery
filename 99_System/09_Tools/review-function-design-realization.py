#!/usr/bin/env python3
"""Step 16 Function-to-Design realization review.

Reviews all Function realizedBy->Design and Function dependsOn->Design claims,
checks inverse synchronization and semantic overlap, and validates the active
BMID decisions against the governed Step 89 record. Report-only.
"""
# Governed Step 16 review entry point
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"function-design-realization-review.md"
BMID_TRACE=ROOT/"80_Decisions and Planning"/"BMID Function Design Traceability Step 89 0.1.yaml"

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
designs={p:d for p,d in notes.items() if d.get("type")=="Design"}
counts=Counter(); findings=[]; realization_rows=[]; dependency_rows=[]

for p,d in sorted(funcs.items()):
    counts["functions"]+=1
    realized=[]
    deps=[]
    for raw in vals(d.get("realizedBy")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-realizedBy",str(raw)))
            continue
        typ=notes[q].get("type")
        if typ=="Design":
            realized.append(q)
            counts["function_to_design_realization_assertions"]+=1
            inv={resolve(target(x)) for x in vals(notes[q].get("realizes")) if resolve(target(x))}
            if p not in inv:
                findings.append((p,"realization-inverse",f"{Path(q).stem} lacks reciprocal realizes."))
        elif typ=="Function":
            counts["function_to_function_realizedBy_assertions"]+=1
        else:
            findings.append((p,"invalid-realizedBy-target",f"{Path(q).stem}: {typ}"))

    for raw in vals(d.get("dependsOn")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-dependsOn",str(raw)))
            continue
        typ=notes[q].get("type")
        if typ=="Design":
            deps.append(q)
            counts["function_to_design_dependency_assertions"]+=1
            inv={resolve(target(x)) for x in vals(notes[q].get("dependencyOf")) if resolve(target(x))}
            if p not in inv:
                findings.append((p,"dependency-inverse",f"{Path(q).stem} lacks reciprocal dependencyOf."))
        else:
            counts[f"function_dependency_target_{typ or 'unknown'}"]+=1

    if realized:
        counts["functions_with_design_realization"]+=1
    if deps:
        counts["functions_with_design_dependency"]+=1

    overlap=set(realized)&set(deps)
    for q in sorted(overlap):
        findings.append((p,"realization-dependency-overlap",f"{Path(q).stem} is both realizedBy and dependsOn; relationship meaning must be disambiguated."))

    for q in realized:
        realization_rows.append((p,q))
    for q in deps:
        dependency_rows.append((p,q))

# Reverse-side validation for Design relationships back to Functions.
for q,d in sorted(designs.items()):
    for raw in vals(d.get("realizes")):
        p=resolve(target(raw))
        if not p:
            findings.append((q,"unresolved-realizes",str(raw)))
            continue
        if p not in funcs:
            continue
        fwd={resolve(target(x)) for x in vals(notes[p].get("realizedBy")) if resolve(target(x))}
        if q not in fwd:
            findings.append((q,"realizes-inverse",f"{Path(p).stem} lacks reciprocal realizedBy."))
    for raw in vals(d.get("dependencyOf")):
        p=resolve(target(raw))
        if not p:
            findings.append((q,"unresolved-dependencyOf",str(raw)))
            continue
        if p not in funcs:
            continue
        fwd={resolve(target(x)) for x in vals(notes[p].get("dependsOn")) if resolve(target(x))}
        if q not in fwd:
            findings.append((q,"dependencyOf-inverse",f"{Path(p).stem} lacks reciprocal dependsOn."))

# Validate governed BMID decision record exactly; do not infer additional mapping.
trace=yaml.safe_load(BMID_TRACE.read_text(encoding="utf-8")) or {}
expected_direct={}
for rec in trace.get("direct_realization_links",[]):
    if not isinstance(rec,dict): continue
    expected_direct[str(rec.get("function"))]=set(str(x) for x in vals(rec.get("realizedBy")))
expected_deps={}
for rec in trace.get("existing_design_dependencies",[]):
    if not isinstance(rec,dict): continue
    expected_deps[str(rec.get("function"))]=set(str(x) for x in vals(rec.get("dependsOn")))
gap_names={str(rec.get("function")) for rec in trace.get("open_design_gaps",[]) if isinstance(rec,dict)}

for name,targets in expected_direct.items():
    p=resolve(name)
    if not p or p not in funcs:
        findings.append((str(BMID_TRACE.relative_to(ROOT)),"missing-function",name)); continue
    actual={Path(q).stem for q in [resolve(target(x)) for x in vals(notes[p].get("realizedBy"))] if q in designs}
    if actual!=targets:
        findings.append((p,"bmid-direct-realization-drift",f"expected {sorted(targets)}, found {sorted(actual)}"))
    else:
        counts["bmid_approved_direct_realizations"]+=len(targets)

for name,targets in expected_deps.items():
    p=resolve(name)
    if not p or p not in funcs:
        findings.append((str(BMID_TRACE.relative_to(ROOT)),"missing-function",name)); continue
    actual={Path(q).stem for q in [resolve(target(x)) for x in vals(notes[p].get("dependsOn"))] if q in designs}
    if not targets.issubset(actual):
        findings.append((p,"bmid-design-dependency-drift",f"expected at least {sorted(targets)}, found {sorted(actual)}"))
    else:
        counts["bmid_approved_design_dependencies"]+=len(targets)

for name in sorted(gap_names):
    p=resolve(name)
    if not p or p not in funcs:
        findings.append((str(BMID_TRACE.relative_to(ROOT)),"missing-gap-function",name)); continue
    realized={resolve(target(x)) for x in vals(notes[p].get("realizedBy")) if resolve(target(x)) in designs}
    deps={resolve(target(x)) for x in vals(notes[p].get("dependsOn")) if resolve(target(x)) in designs}
    if realized or deps:
        findings.append((p,"bmid-open-gap-drift","Step 89 marks this unresolved but a Design path is now present."))
    else:
        counts["bmid_explicit_unresolved_design_gaps"]+=1

print("function to design realization review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,q in realization_rows: print(f"  REALIZATION {Path(p).stem} -> {Path(q).stem}")
for p,q in dependency_rows: print(f"  DEPENDENCY {Path(p).stem} -> {Path(q).stem}")
for name in sorted(gap_names): print(f"  EXPLICIT_GAP {name}: EXC-ARCH-UNRESOLVED")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Function-to-Design Realization Review","",
"Step 16 whole-vault review of direct Function→Design implementation and enabling Function→Design dependencies.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Direct realizations","",
"| Function | Design |","|---|---|"]
if realization_rows:
    for p,q in realization_rows: lines.append(f"| {p} | {q} |")
else: lines.append("| _None_ | |")
lines += ["","## Design dependencies","",
"| Function | Design |","|---|---|"]
if dependency_rows:
    for p,q in dependency_rows: lines.append(f"| {p} | {q} |")
else: lines.append("| _None_ | |")
lines += ["","## Explicit BMID design gaps","",
"| Function | Disposition |","|---|---|"]
for name in sorted(gap_names): lines.append(f"| {name} | EXC-ARCH-UNRESOLVED |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- realizedBy/realizes means a Design directly implements the Function; use it only when the implementation claim is specific and defensible.",
"- dependsOn/dependencyOf means a Design enables or is required by the Function without claiming that the Design itself realizes the full behavior.",
"- The same Function/Design pair should not simultaneously carry realizedBy and dependsOn unless a reviewed semantic reason explicitly justifies both.",
"- Function→Function realizedBy remains legal under the schema but is outside the Function→Design focus of this step.",
"- The three Step 89 BMID gaps remain explicit. No Design is created or substituted merely to reduce traceability findings.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("FUNCTION DESIGN REALIZATION REVIEW PASSED WITH EXPLICIT BMID GAPS" if gap_names else "FUNCTION DESIGN REALIZATION REVIEW PASSED")
