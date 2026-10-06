#!/usr/bin/env python3
"""Step 21 high-value evidence-bearing note review.

Governed Step 21 review entry point.

Prioritizes evidence curation for the active BMID engineering chain rather than
bulk-linking every URL-bearing market/reference note. Validates curated source
Document relationships and direct source support for the highest-value active
Requirements, satisfying Functions, and directly realizing Designs.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"high-value-evidence-review.md"

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

notes={}; bodies={}; bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; bodies[rel]=t
    bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

source_docs={p:d for p,d in notes.items()
             if d.get("type")=="Document" and "source-document" in {str(x) for x in vals(d.get("tags"))}}
counts=Counter(); findings=[]; rows=[]

# Global evidence-signal inventory remains a queue, not a defect count.
signal_re=re.compile(r"https?://|(?:^|\n)\s*(?:[-*]\s*)?\*{0,2}(?:Source|Sources|Evidence)\b",re.I)
evidence_signal=[p for p,t in bodies.items() if signal_re.search(t)]
counts["evidence_signal_notes"]=len(evidence_signal)

def source_links(p,field):
    out=[]
    for raw in vals(notes[p].get(field)):
        q=resolve(target(raw))
        if q in source_docs: out.append(q)
    return out

def all_links(p,field):
    return [q for raw in vals(notes[p].get(field)) if (q:=resolve(target(raw)))]

# Validate all source Document describes/supports/contradicts relationships and inverse sync.
for p,d in sorted(source_docs.items()):
    counts["curated_source_documents"]+=1
    for field,invfield in (("describes","describedBy"),("supports","supportedBy"),("contradicts","contradictedBy")):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,f"unresolved-{field}",str(raw))); continue
            inv=set(all_links(q,invfield))
            if p not in inv:
                findings.append((p,f"{field}-inverse",f"{Path(q).stem} lacks {invfield}."))
            counts[f"source_document_{field}_assertions"]+=1
            rows.append((p,field,q,notes[q].get("type")))

# Active requirements are current product-scoped Requirements.
active_req={p:d for p,d in notes.items()
            if d.get("type")=="Requirement" and (vals(d.get("appliesTo")) or "product-requirement" in {str(x) for x in vals(d.get("tags"))})}
counts["active_requirements"]=len(active_req)

# The battery-association requirement is an internally derived semantic-integrity
# obligation. It has rationale and Verification intent, but current external
# evidence does not establish a lifecycle implementation; direct source support
# is therefore not required in this step.
association_name="BMID - Preserve Battery Association"
association=resolve(association_name)

high_value_req=[]
for p,d in sorted(active_req.items()):
    src=source_links(p,"supportedBy")
    verified=all_links(p,"verifiedBy")
    if verified: counts["active_requirements_with_verification_evidence_path"]+=1
    else: findings.append((p,"requirement-no-verification-evidence-path","Active Requirement lacks verifiedBy."))

    if p==association:
        counts["active_requirements_internal_semantic_basis"]+=1
        continue
    high_value_req.append(p)
    if src:
        counts["high_value_requirements_with_curated_source_support"]+=1
    else:
        findings.append((p,"high-value-requirement-no-curated-source","Expected direct curated source support."))

# Requirement satisfiers that are Functions are the highest-value behavior evidence targets.
sat_functions=set()
for p in active_req:
    for q in all_links(p,"satisfiedBy"):
        if notes[q].get("type")=="Function": sat_functions.add(q)
counts["requirement_satisfying_functions"]=len(sat_functions)
for p in sorted(sat_functions):
    if source_links(p,"supportedBy"):
        counts["satisfying_functions_with_curated_source_support"]+=1
    else:
        findings.append((p,"satisfying-function-no-curated-source","Active Requirement-satisfying Function lacks direct curated source support."))

# Directly realizing Designs for those Functions are high-value implementation claims.
realizing_designs=set()
for p in sat_functions:
    for q in all_links(p,"realizedBy"):
        if notes[q].get("type")=="Design": realizing_designs.add(q)
counts["direct_realizing_designs"]=len(realizing_designs)
for p in sorted(realizing_designs):
    if source_links(p,"supportedBy"):
        counts["realizing_designs_with_curated_source_support"]+=1
    else:
        findings.append((p,"realizing-design-no-curated-source","Direct active Function realization lacks curated source support."))

# Product scope Objects should have source-document subject traceability where
# the active requirement depends on a public product claim.
scope_objects=set()
for p in active_req:
    for q in all_links(p,"appliesTo"):
        if notes[q].get("type")=="Object": scope_objects.add(q)
counts["active_requirement_scope_objects"]=len(scope_objects)
for p in sorted(scope_objects):
    if source_links(p,"describedBy"):
        counts["active_scope_objects_with_curated_source_description"]+=1
    else:
        findings.append((p,"active-scope-object-no-source-document","Active product scope lacks a curated Source Document description."))

# PosiConnect is a selected supporting product in the active service chain.
posiconnect=resolve("PosiCharge PosiConnect")
if posiconnect:
    counts["selected_supporting_products"]=1
    if source_links(posiconnect,"describedBy"):
        counts["selected_supporting_products_with_curated_source_description"]=1
    else:
        findings.append((posiconnect,"supporting-product-no-source-document","Selected supporting product lacks curated Source Document description."))

# Explicitly preserve verification execution distinction.
verifications=[p for p,d in notes.items() if d.get("type")=="Verification"]
results=[p for p,d in notes.items() if d.get("type")=="Result"]
counts["verification_intents"]=len(verifications)
counts["executed_results"]=len(results)

# Report the broad queue without failing sparse reference content.
curated_target_notes=set()
for p,d in notes.items():
    for field in ("supportedBy","describedBy","contradictedBy"):
        if source_links(p,field): curated_target_notes.add(p)
counts["notes_with_curated_source_document_relationship"]=len(curated_target_notes)
counts["evidence_signal_notes_not_directly_curated"]=sum(1 for p in evidence_signal if p not in curated_target_notes and p not in source_docs)

print("high-value evidence review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,field,q,qtyp in rows: print(f"  EVIDENCE {Path(p).stem} --{field}--> {qtyp} {Path(q).stem}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# High-Value Evidence Review","",
"Step 21 prioritizes active engineering evidence while deliberately leaving low-value market/reference URL content sparse.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Curated source relationships","",
"| Source Document | Relationship | Target type | Target |","|---|---|---|---|"]
for p,field,q,qtyp in rows:
    lines.append(f"| {p} | {field} | {qtyp} | {q} |")
if not rows: lines.append("| _None_ | | | |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Review policy","",
"- Curate evidence first where it affects active Requirements, their satisfiers, direct Designs, architecture/product scope, validation intent, supplier/product selections, or another real engineering decision.",
"- Do not create semantic links merely because a reference note contains a URL.",
"- Product/competitor source pages support only the claims actually stated by those sources; feature similarity is not evidence for a different product.",
"- The BMID battery-association Requirement remains an internally derived semantic-integrity obligation with Verification intent and an unresolved implementation path. Current public source evidence does not establish the lifecycle mechanism, so Step 21 does not force a direct source-support assertion.",
"- Verification intent remains distinct from executed evidence. With zero Result notes, no test-pass evidence is claimed.",
"- Remaining evidence-signal notes are a curation queue. Reference-content sparsity is acceptable unless a later engineering decision materially relies on one of those claims.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("HIGH-VALUE EVIDENCE REVIEW PASSED")
