#!/usr/bin/env python3
"""Step 13 Requirement applicability review.

Reviews every Requirement appliesTo/applies pair for explicit engineering scope,
reciprocity, target identity, and family-vs-variant scope consistency.
Report-only: product-family scope is not expanded onto child offerings unless
the model has evidence that each child inherits/satisfies the obligation.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"requirement-applicability-review.md"

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
counts=Counter(); findings=[]; rows=[]

for p,d in sorted(reqs.items()):
    counts["requirements"]+=1
    tags=set(str(x) for x in vals(d.get("tags")))
    scopes=[]
    for raw in vals(d.get("appliesTo")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-appliesTo",str(raw)))
            continue
        scopes.append(q)
        qd=notes[q]
        counts["appliesTo_assertions"]+=1
        if qd.get("type")!="Object":
            findings.append((p,"non-object-scope",f"{Path(q).stem} is {qd.get('type')}, expected product/context Object for current product requirements."))
        inv={resolve(target(x)) for x in vals(qd.get("applies")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"missing-applies-inverse",f"{Path(q).stem} lacks reciprocal applies."))
    if not scopes:
        findings.append((p,"missing-applicability","Requirement has no explicit appliesTo scope."))
    else:
        counts["requirements_with_explicit_scope"]+=1

    family_tag="family-level" in tags
    variant_tag="variant-specific" in tags
    if family_tag and variant_tag:
        findings.append((p,"scope-tag-conflict","Requirement is tagged both family-level and variant-specific."))

    for q in scopes:
        qd=notes[q]
        pc=str(qd.get("productClass") or "")
        abstract=bool(qd.get("abstract",False))
        if family_tag:
            counts["family_level_requirements"]+=1
            if not (pc=="product-family" or abstract):
                findings.append((p,"family-scope-target",f"family-level Requirement targets non-family/non-abstract Object {Path(q).stem}."))
        if variant_tag:
            counts["variant_specific_requirements"]+=1
            if pc=="product-family" or abstract:
                findings.append((p,"variant-scope-target",f"variant-specific Requirement targets family/abstract Object {Path(q).stem}."))
        rows.append((p,q,pc,abstract,family_tag,variant_tag))

# Detect stray inverse applies on product Objects that point to Requirements which
# do not reciprocate.
for q,qd in notes.items():
    if qd.get("type")!="Object": continue
    for raw in vals(qd.get("applies")):
        p=resolve(target(raw))
        if not p or p not in reqs: continue
        forward={resolve(target(x)) for x in vals(reqs[p].get("appliesTo")) if resolve(target(x))}
        if q not in forward:
            findings.append((q,"stray-applies-inverse",f"applies {Path(p).stem} lacks reciprocal appliesTo."))

# Family-level requirement scope should remain on the family definition. Do not
# require duplication to descendants because that would imply child applicability
# or compliance not established by evidence.
family_targets=[q for _,q,pc,abstract,fam,var in rows if fam]
counts["unique_family_scope_targets"]=len(set(family_targets))
variant_targets=[q for _,q,pc,abstract,fam,var in rows if var]
counts["unique_variant_scope_targets"]=len(set(variant_targets))

print("requirement applicability review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,q,pc,abstract,fam,var in rows:
    scope_kind="family-level" if fam else "variant-specific" if var else "unclassified"
    print(f"  APPLICABILITY {Path(p).stem} -> {Path(q).stem}: {scope_kind}, productClass={pc or '-'}, abstract={abstract}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Requirement Applicability Review","",
"Step 13 review of every Requirement's explicit scope and reciprocal product applicability.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Applicability map","",
"| Requirement | appliesTo | Requirement scope | Target productClass | Target abstract |","|---|---|---|---|---|"]
for p,q,pc,abstract,fam,var in rows:
    sk="family-level" if fam else "variant-specific" if var else "unclassified"
    lines.append(f"| {p} | {q} | {sk} | {pc or ''} | {abstract} |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- appliesTo/applies is the authoritative applicability relationship; folder placement and prose alone do not establish product scope.",
"- Family-level Requirements target the reusable product-family Object. They are not duplicated onto every child product because doing so would assert child applicability/compliance that may not yet be evidenced.",
"- Variant-specific Requirements target the specific offering/variant that owns the obligation.",
"- Product specialization and Requirement applicability are separate semantics. subtypeOf does not automatically copy Requirements to a child.",
"- If a family Requirement later gains exceptions or variant refinements, represent those with explicit Requirement/model semantics rather than relying on inherited folder structure.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("REQUIREMENT APPLICABILITY REVIEW PASSED")
