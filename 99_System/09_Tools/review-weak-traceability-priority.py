#!/usr/bin/env python3
"""Step 26 weak-traceability priority review.

Governed Step 26 review entry point.

Classifies the legacy weak-traceability queue by current engineering use, with
strict attention to active BMID/PosiGuard Designs, Functions, and Requirements.
Reference/support content is counted separately and is not force-linked.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
RULES=ROOT/"99_System"/"09_Tools"/"semantic-linking-report-rules.yaml"
DISP=ROOT/"80_Decisions and Planning"/"Semantic Linking Review Dispositions 0.1.yaml"
REL=ROOT/"99_System"/"03_Schemas"/"relationships.yaml"
REPORT=ROOT/"weak-traceability-priority-review.md"

def load(p): return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
def fm(t):
    if not t.startswith("---\n"): return {}
    e=t.find("\n---",4)
    if e<0:return {}
    try:return yaml.safe_load(t[4:e]) or {}
    except Exception:return {}
def vals(v):
    if v is None:return []
    return v if isinstance(v,list) else [v]
def target(v):
    if not isinstance(v,str):return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

notes={}; texts={}; bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace"); d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    relp=p.relative_to(ROOT).as_posix()
    notes[relp]=d; texts[relp]=t; bybase[p.stem].append(relp)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else: ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

rel=load(REL)
fields=set()
for rec in rel.get("paired",[])+rel.get("temporaryPairs",[]):
    fields.update(x for x in (rec.get("forward"),rec.get("inverse")) if x)
for rec in rel.get("symmetric",[])+rel.get("oneWay",[]):
    if rec.get("field"): fields.add(rec["field"])

incoming=defaultdict(list); outgoing=defaultdict(list)
for p,d in notes.items():
    for field in fields:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if q:
                outgoing[p].append((field,q)); incoming[q].append((field,p))

def linkset(p, field=None):
    xs=outgoing[p] if field is None else [(f,q) for f,q in outgoing[p] if f==field]
    return {q for f,q in xs}

# Legacy Step-97 signals retained for baseline comparison.
legacy_expectations={
    "Requirement":[
        ("upstream rationale", {"drivenBy","derivedFrom","refinedBy","references","appliesTo"}),
        ("satisfaction path", {"satisfiedBy"}),
        ("verification path", {"verifiedBy"}),
    ],
    "Function":[
        ("performer/product context", {"performedBy"}),
        ("intent or implementation trace", {"satisfies","realizes","realizedBy","drivenBy"}),
    ],
    "Design":[
        ("design ownership/context", {"designOf","appliesTo"}),
        ("behavior/requirement trace", {"realizes","satisfies","verifiedBy"}),
    ],
}
legacy=[]
for p,d in notes.items():
    typ=str(d.get("type") or "")
    relfields={f for f,_ in outgoing[p]} | {f for f,_ in incoming[p]}
    for label,alts in legacy_expectations.get(typ,[]):
        if not (relfields & alts):
            legacy.append((p,typ,label,alts))

# Active engineering anchors follow the explicit BMID Step-88/89 product-model
# decisions rather than every market feature mapped onto PosiGuard.
active_req={p for p,d in notes.items()
            if d.get("type")=="Requirement"
            and (vals(d.get("appliesTo")) or "product-requirement" in {str(x) for x in vals(d.get("tags"))})}

STEP89=ROOT/"80_Decisions and Planning"/"BMID Function Design Traceability Step 89 0.1.yaml"
step89=load(STEP89)
active_functions=set()
active_designs=set()
for row in step89.get("direct_realization_links") or []:
    fp=resolve(str(row.get("function") or ""))
    if fp: active_functions.add(fp)
    for name in row.get("realizedBy") or []:
        dp=resolve(str(name))
        if dp: active_designs.add(dp)
for row in step89.get("existing_design_dependencies") or []:
    fp=resolve(str(row.get("function") or ""))
    if fp: active_functions.add(fp)
    for name in row.get("dependsOn") or []:
        dp=resolve(str(name))
        if dp: active_designs.add(dp)
for row in step89.get("open_design_gaps") or []:
    fp=resolve(str(row.get("function") or ""))
    if fp: active_functions.add(fp)

active_by_type={"Design":active_designs,"Function":active_functions,"Requirement":active_req}

# Current-use classification for weak notes outside the active set.
def classify_weak(p,typ):
    if p in active_by_type.get(typ,set()):
        return "active_engineering"
    d=notes[p]
    tags={str(x) for x in vals(d.get("tags"))}
    if typ=="Function":
        performers={q for f,q in incoming[p] if f=="performs" and notes[q].get("type")=="Object"}
        if "general-function" in tags or not performers or vals(d.get("supertypeOf")) or vals(d.get("hasChild")):
            return "engineering_support"
        return "reference_content"
    if typ=="Design":
        owners={q for f,q in incoming[p] if f=="hasDesign" and notes[q].get("type")=="Object"}
        active_dependency=any(q in active_functions for f,q in outgoing[p] if f=="dependencyOf")
        if "general-design" in tags or active_dependency or not owners or vals(d.get("supertypeOf")) or vals(d.get("hasChild")):
            return "engineering_support"
        return "reference_content"
    if typ=="Requirement":
        return "active_engineering"
    return "reference_content"

weak_notes=defaultdict(list)
for p,typ,label,alts in legacy:
    weak_notes[p].append(label)

counts=Counter()
for p,labels in weak_notes.items():
    typ=notes[p].get("type")
    cls=classify_weak(p,typ)
    counts[f"weak_notes_{typ}"]+=1
    counts[f"weak_notes_class_{cls}"]+=1
    counts["legacy_weak_findings"]+=len(labels)
    if cls=="active_engineering":
        counts["active_weak_notes"]+=1
        counts["active_weak_findings"]+=len(labels)

# Strict Step-2 active dimensions.
rules=load(RULES); matrix=rules.get("dimensions") or {}; strict=rules.get("strict_active_dimensions") or {}
active_dimension_gaps=[]
for typ,paths in active_by_type.items():
    for p in sorted(paths):
        relfields={f for f,_ in outgoing[p]} | {f for f,_ in incoming[p]}
        for dim in strict.get(typ,[]):
            alts=set((matrix.get(typ) or {}).get(dim) or [])
            if alts and not (relfields & alts):
                active_dimension_gaps.append((p,typ,dim,sorted(alts)))

# Named active unresolved decisions are carried from the authoritative earlier
# reviews even when the coarse matrix has another qualifying relationship.
named_active_unresolved=[]
for row in step89.get("open_design_gaps") or []:
    fp=resolve(str(row.get("function") or ""))
    if fp:
        named_active_unresolved.append((fp,"Function","implementation","EXC-ARCH-UNRESOLVED"))
preserve=resolve("BMID - Preserve Battery Association")
if preserve:
    named_active_unresolved.append((preserve,"Requirement","satisfaction","EXC-ARCH-UNRESOLVED"))

def expected_exception(p,typ,dim):
    return None

records=(load(DISP).get("records") or {})
active_registry_findings=[]
active_unresolved=list(named_active_unresolved)
for p,typ,dim,alts in active_dimension_gaps:
    exp=expected_exception(p,typ,dim)
    rec=records.get(p)
    if not isinstance(rec,dict) or rec.get("classification")!="active_engineering":
        active_registry_findings.append((p,typ,dim,"missing active_engineering classification"))
        continue
    g=(rec.get("gaps") or {}).get(dim)
    if exp:
        state,code=exp
        if not isinstance(g,dict) or g.get("disposition")!=state or g.get("exception")!=code:
            active_registry_findings.append((p,typ,dim,f"expected {state}/{code}"))
    else:
        active_registry_findings.append((p,typ,dim,"unexplained active dimension gap"))

for typ,paths in active_by_type.items():
    for p in paths:
        rec=records.get(p)
        if not isinstance(rec,dict) or rec.get("classification")!="active_engineering":
            if not any(x[0]==p for x in active_registry_findings):
                active_registry_findings.append((p,typ,"classification","missing active_engineering classification"))

# Every legacy weak note is now formally classified. Lower-value support/reference
# notes receive controlled dispositions only for matrix dimensions that remain
# missing after the Step-26 specialization/dependency rule alignment.
weak_registry_findings=[]
for p,labels in sorted(weak_notes.items()):
    typ=str(notes[p].get("type") or "")
    expected_cls=classify_weak(p,typ)
    rec=records.get(p)
    if not isinstance(rec,dict) or rec.get("classification")!=expected_cls:
        weak_registry_findings.append((p,"classification",f"expected {expected_cls}"))
        continue
    relfields={f for f,_ in outgoing[p]} | {f for f,_ in incoming[p]}
    missing=[]
    for dim,alts in (matrix.get(typ) or {}).items():
        if alts and not (relfields & set(alts)):
            missing.append(dim)
    gaps=rec.get("gaps") or {}
    if expected_cls=="engineering_support":
        for dim in missing:
            if dim!="evidence":
                continue
            g=gaps.get(dim)
            if not isinstance(g,dict) or g.get("disposition")!="not_applicable" or g.get("exception")!="EXC-NOT-APPLICABLE":
                weak_registry_findings.append((p,dim,"expected not_applicable / EXC-NOT-APPLICABLE"))
    elif expected_cls=="reference_content":
        for dim in missing:
            g=gaps.get(dim)
            if dim=="evidence":
                if not isinstance(g,dict) or g.get("disposition")!="not_applicable" or g.get("exception")!="EXC-NOT-APPLICABLE":
                    weak_registry_findings.append((p,dim,"expected not_applicable / EXC-NOT-APPLICABLE"))
            elif dim in {"upstream","downstream","ownership_use"}:
                if not isinstance(g,dict) or g.get("disposition")!="intentionally_absent" or g.get("exception")!="EXC-REFERENCE-LEAF":
                    weak_registry_findings.append((p,dim,"expected intentionally_absent / EXC-REFERENCE-LEAF"))

print("weak traceability priority review")
print(f"  legacy weak findings: {len(legacy)}")
print(f"  weak notes: {len(weak_notes)}")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
for typ,paths in active_by_type.items(): print(f"  active {typ}: {len(paths)}")
print(f"  active strict dimension gaps: {len(active_dimension_gaps)}")
print(f"  active unresolved accepted gaps: {len(active_unresolved)}")
print(f"  active registry/unexplained findings: {len(active_registry_findings)}")
print(f"  weak queue registry findings: {len(weak_registry_findings)}")
for p,typ,dim,msg in active_registry_findings:
    print(f"  ACTIVE_FINDING {typ} {dim}: {p}: {msg}")
for p,dim,msg in weak_registry_findings:
    print(f"  WEAK_REGISTRY_FINDING {dim}: {p}: {msg}")
for p,typ,dim,code in active_unresolved:
    print(f"  ACTIVE_UNRESOLVED {typ} {dim}: {p}: {code}")
for p,labels in sorted(weak_notes.items()):
    typ=notes[p].get("type"); cls=classify_weak(p,typ)
    relfields={f for f,_ in outgoing[p]} | {f for f,_ in incoming[p]}
    missing=[]
    for dim,alts in (matrix.get(typ) or {}).items():
        if alts and not (relfields & set(alts)):
            missing.append(dim)
    print(f"  WEAK {cls} {typ}: {p}: {', '.join(labels)} | matrix_missing={','.join(missing) or 'none'}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Weak Traceability Priority Review","",
"Step 26 reviews the legacy weak-traceability queue by current engineering priority. Legacy counts are retained for comparability; completion is judged by active-engineering unexplained gaps.","",
"## Summary","",
f"- Legacy weak findings: **{len(legacy)}**",
f"- Unique weak notes: **{len(weak_notes)}**",
f"- Active strict Step-2 dimension gaps: **{len(active_dimension_gaps)}**",
f"- Active accepted unresolved gaps: **{len(active_unresolved)}**",
f"- Active registry/unexplained findings: **{len(active_registry_findings)}**",
f"- Weak-queue registry findings: **{len(weak_registry_findings)}**","",
"## Active engineering set","",
f"- Designs: **{len(active_designs)}**",
f"- Functions: **{len(active_functions)}**",
f"- Requirements: **{len(active_req)}**","",
"## Active registry/unexplained findings","",
"| Path | Type | Dimension | Finding |","|---|---|---|---|"]
if active_registry_findings:
    for p,typ,dim,msg in active_registry_findings:
        lines.append(f"| {p} | {typ} | {dim} | {msg} |")
else: lines.append("| _None_ | | | |")
lines += ["","## Active unresolved exceptions","",
"| Path | Type | Dimension | Exception |","|---|---|---|---|"]
if active_unresolved:
    for p,typ,dim,code in active_unresolved:
        lines.append(f"| {p} | {typ} | {dim} | {code} |")
else: lines.append("| _None_ | | | |")
lines += ["","## Legacy weak notes by current-use class","",
"| Path | Type | Class | Legacy weak dimensions |","|---|---|---|---|"]
for p,labels in sorted(weak_notes.items()):
    typ=notes[p].get("type"); cls=classify_weak(p,typ)
    lines.append(f"| {p} | {typ} | {cls} | {', '.join(labels)} |")
lines += ["","## Interpretation","",
"- Legacy weak findings are compatibility metrics, not the final completeness contract.",
"- Active BMID/PosiGuard engineering is evaluated against Step-2 strict dimensions and reviewed Step-4 dispositions.",
"- The battery-association satisfaction gap and the three known BMID Function implementation gaps remain explicit EXC-ARCH-UNRESOLVED items; they are visible unresolved engineering decisions, not unexplained omissions.",
"- Reusable generic Functions/Designs may be engineering_support; competitor/catalog implementations may be reference_content.",
"- Lower-value reference/support weak findings do not justify invented realization, satisfaction, verification, or ownership links.",
"- Step 26 succeeds when active engineering has zero unexplained gaps; accepted named unresolved decisions remain visible for the final handoff.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if active_registry_findings or weak_registry_findings: raise SystemExit(2)
print("WEAK TRACEABILITY PRIORITY REVIEW PASSED")
