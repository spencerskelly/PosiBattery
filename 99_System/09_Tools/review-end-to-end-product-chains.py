#!/usr/bin/env python3
"""Step 27 end-to-end product chain audit.

Governed Step 27 review entry point.

Systematically audits the six governed BMID/PosiGuard requirement chains in
both directions. Known architecture/customer-discovery gaps are explicit and
do not authorize substitute semantic links.
"""
from pathlib import Path
from collections import defaultdict, Counter
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"end-to-end-product-chain-audit.md"
DISP=ROOT/"80_Decisions and Planning"/"Semantic Linking Review Dispositions 0.1.yaml"

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
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; texts[rel]=t; bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

def links(p,field):
    out=[]
    for raw in vals(notes[p].get(field)):
        q=resolve(target(raw))
        if q: out.append(q)
    return out

def has(p,field,q):
    return q in links(p,field)

specs=[
  {
    "requirement":"BMID - Provide Battery Identity to Compatible Charger",
    "product":"PosiCharge BMID",
    "use_case":"Charge a BMID-Equipped Battery Using Battery Information",
    "need":"Integrate the Battery with Truck and Charger Controls",
    "satisfier":"Identify Battery to Charger",
    "satisfier_type":"Function",
    "implementation":"Battery Identification and Charger Communication Software Design",
    "implementation_relation":"realizedBy",
    "known_gap":None,
    "architecture":"PosiCharge BMID Product Assembly Local Model",
  },
  {
    "requirement":"BMID - Provide Supported Battery Condition Information to Charger",
    "product":"PosiCharge BMID",
    "use_case":"Charge a BMID-Equipped Battery Using Battery Information",
    "need":"Charge Each Battery Correctly for Its Chemistry and Condition",
    "satisfier":"Report Battery Temperature to Charger",
    "satisfier_type":"Function",
    "implementation":"Electrolyte-Immersed Temperature Sensor",
    "implementation_relation":"realizedBy",
    "known_gap":None,
    "architecture":"PosiCharge BMID Product Assembly Local Model",
  },
  {
    "requirement":"BMID - Retain Battery-Specific Usage History",
    "product":"PosiCharge BMID",
    "use_case":"Review BMID Battery History and Exceptions",
    "need":"Document Battery Care for Warranty Compliance",
    "satisfier":"Log Battery Events and Usage",
    "satisfier_type":"Function",
    "implementation":"Data Handling Design",
    "implementation_relation":"dependsOn",
    "known_gap":None,
    "architecture":None,
  },
  {
    "requirement":"BMID - Preserve Battery Association",
    "product":"PosiCharge BMID",
    "use_case":"Inspect Battery Condition Through a BMID",
    "need":"Prevent Battery Abuse and Premature Replacement",
    "satisfier":None,
    "satisfier_type":None,
    "implementation":None,
    "implementation_relation":None,
    "known_gap":"requirement_satisfaction",
    "gap_code":"EXC-ARCH-UNRESOLVED",
    "gap_owner":"BMID product/system architecture",
    "gap_reason":"No existing Function, Design, Object, or Result demonstrates preservation of identity/history association with the physical battery.",
    "architecture":None,
  },
  {
    "requirement":"PosiGuard - Support Lead-Acid and Lithium Battery Fleets",
    "product":"PosiCharge PosiGuard",
    "use_case":"Integrate a BMID with Charger Vehicle and Fleet Systems",
    "need":"Integrate the Battery with Truck and Charger Controls",
    "satisfier":"PosiCharge PosiGuard",
    "satisfier_type":"Object",
    "implementation":None,
    "implementation_relation":None,
    "known_gap":None,
    "intentional_pattern":"object_satisfaction",
    "pattern_reason":"Application/chemistry coverage is a product-level capability. Nearby sensing/communication Functions do not individually prove this Requirement.",
    "architecture":None,
  },
  {
    "requirement":"PosiGuard - Support Local Service Configuration",
    "product":"PosiCharge PosiGuard",
    "use_case":"Configure and Service a Supported BMID",
    "need":None,
    "satisfier":"Configure Device from Mobile App or PC",
    "satisfier_type":"Function",
    "implementation":"Mobile App Interface",
    "implementation_relation":"realizedBy",
    "known_gap":"upstream_customer_need",
    "gap_code":"EXC-EVIDENCE-PENDING",
    "gap_owner":"Product requirements / customer discovery",
    "gap_reason":"Step 85 found no existing Customer Need that maps cleanly enough to the service/configuration Use Case; customer-side need evidence is still required.",
    "architecture":None,
  },
]

findings=[]; repairs=[]; intentional=[]; unresolved=[]; rows=[]
counts=Counter()

def fail(req,stage,msg):
    findings.append((req,stage,msg))

def require_pair(a,af,b,bf,req,stage):
    if not has(a,af,b): fail(req,stage,f"{Path(a).stem} lacks {af} -> {Path(b).stem}")
    if not has(b,bf,a): fail(req,stage,f"{Path(b).stem} lacks {bf} -> {Path(a).stem}")

for spec in specs:
    req=resolve(spec["requirement"]); product=resolve(spec["product"]); uc=resolve(spec["use_case"])
    if not req: fail(spec["requirement"],"identity","Requirement not found"); continue
    counts["chains"]+=1
    if not product: fail(spec["requirement"],"scope","Product not found"); continue
    if not uc: fail(spec["requirement"],"use_case","Use Case not found"); continue

    # Product scope and reciprocal applicability.
    require_pair(req,"appliesTo",product,"applies",spec["requirement"],"scope")

    # Need -> Use Case -> Requirement, or explicit upstream discovery gap.
    need=None
    if spec["need"]:
        need=resolve(spec["need"])
        if not need:
            fail(spec["requirement"],"need","Customer Need not found")
        else:
            require_pair(need,"arisesIn",uc,"givesRiseTo",spec["requirement"],"need_use_case")
            counts["chains_with_need_use_case"]+=1
    else:
        unresolved.append({
            "requirement":spec["requirement"],"stage":"Need -> Use Case",
            "code":spec["gap_code"],"owner":spec["gap_owner"],"reason":spec["gap_reason"]
        })
        counts["accepted_unresolved_upstream_need"]+=1

    require_pair(uc,"drives",req,"drivenBy",spec["requirement"],"use_case_requirement")

    # Requirement satisfaction.
    satisfier=None
    if spec["satisfier"]:
        satisfier=resolve(spec["satisfier"])
        if not satisfier:
            fail(spec["requirement"],"satisfaction","Satisfier not found")
        else:
            if notes[satisfier].get("type")!=spec["satisfier_type"]:
                fail(spec["requirement"],"satisfaction",f"Satisfier type is {notes[satisfier].get('type')}, expected {spec['satisfier_type']}")
            require_pair(req,"satisfiedBy",satisfier,"satisfies",spec["requirement"],"satisfaction")
            counts[f"chains_with_{spec['satisfier_type'].lower()}_satisfaction"]+=1

            if spec["satisfier_type"]=="Function":
                # Performer/product context must match the scoped product.
                require_pair(satisfier,"performedBy",product,"performs",spec["requirement"],"function_product_context")
            elif spec["satisfier_type"]=="Object":
                if satisfier!=product:
                    fail(spec["requirement"],"object_satisfaction","Object satisfier is not the scoped product")
                intentional.append({
                    "requirement":spec["requirement"],
                    "stage":"Requirement -> Function",
                    "classification":"intentional semantic alternate",
                    "reason":spec.get("pattern_reason","Product Object directly satisfies the Requirement.")
                })
                counts["intentional_object_satisfaction_patterns"]+=1
    else:
        unresolved.append({
            "requirement":spec["requirement"],"stage":"Requirement satisfaction",
            "code":spec["gap_code"],"owner":spec["gap_owner"],"reason":spec["gap_reason"]
        })
        counts["accepted_unresolved_satisfaction"]+=1

    # Function -> Design implementation, dependency, or explicit gap.
    impl=None
    if satisfier and spec["satisfier_type"]=="Function":
        if spec["implementation"]:
            impl=resolve(spec["implementation"])
            if not impl:
                fail(spec["requirement"],"implementation","Design not found")
            else:
                relation=spec["implementation_relation"]
                inverse="realizes" if relation=="realizedBy" else "dependencyOf"
                require_pair(satisfier,relation,impl,inverse,spec["requirement"],"function_design")
                counts[f"chains_with_design_{relation}"]+=1
        elif spec.get("known_gap")=="function_implementation":
            unresolved.append({
                "requirement":spec["requirement"],"stage":"Function -> Design/Architecture",
                "code":spec["gap_code"],"owner":spec["gap_owner"],"reason":spec["gap_reason"]
            })
            counts["accepted_unresolved_function_implementation"]+=1
        else:
            fail(spec["requirement"],"implementation","Function satisfier has neither governed implementation path nor explicit gap")

    # Optional contextual Local Model architecture correspondence.
    if spec.get("architecture"):
        arch=resolve(spec["architecture"])
        if not arch:
            fail(spec["requirement"],"architecture","Architecture context note not found")
        else:
            require_pair(arch,"describes",product,"describedBy",spec["requirement"],"architecture_product_context")
            if "MDSE:LOCAL-MODEL START" not in texts[arch]:
                fail(spec["requirement"],"architecture","Architecture note lacks Local Model block")
            else:
                counts["chains_with_local_model_context"]+=1

    # Verification intent is requirement-level and reciprocal.
    verifs=links(req,"verifiedBy")
    if len(verifs)!=1:
        fail(spec["requirement"],"verification",f"Expected exactly one verifiedBy target, found {len(verifs)}")
        verification=None
    else:
        verification=verifs[0]
        if notes[verification].get("type")!="Verification":
            fail(spec["requirement"],"verification",f"verifiedBy target type is {notes[verification].get('type')}")
        require_pair(verification,"verifies",req,"verifiedBy",spec["requirement"],"verification_inverse")
        counts["chains_with_verification_intent"]+=1

    # Backward audit summary is implicit in all pair checks above.
    rows.append({
        "requirement":spec["requirement"],
        "need":spec["need"] or "UNRESOLVED",
        "use_case":spec["use_case"],
        "satisfier":spec["satisfier"] or "UNRESOLVED",
        "implementation":spec["implementation"] or (
            "OBJECT SATISFIER" if spec.get("intentional_pattern")=="object_satisfaction" else "UNRESOLVED"
        ),
        "architecture":spec.get("architecture") or "not separately modeled/required",
        "verification":Path(verification).stem if verification else "INVALID",
    })

# Cross-chain expected unresolved decisions.
expected_unresolved={
    ("BMID - Preserve Battery Association","Requirement satisfaction","EXC-ARCH-UNRESOLVED"),
    ("PosiGuard - Support Local Service Configuration","Need -> Use Case","EXC-EVIDENCE-PENDING"),
}
actual_unresolved={(x["requirement"],x["stage"],x["code"]) for x in unresolved}
if actual_unresolved!=expected_unresolved:
    findings.append(("Step 27","unresolved_set",f"Expected {sorted(expected_unresolved)}, found {sorted(actual_unresolved)}"))

# The remaining Step-89 architecture gaps are active supporting-function gaps, not
# requirement-satisfaction-chain breaks. Preserve them as supplemental unresolved
# architecture decisions in the report.
supplemental=[
]
counts["supplemental_active_architecture_gaps"]=len(supplemental)

# Need records remain hypotheses until customer-side validation exists.
need_hypotheses=0
for row in rows:
    if row["need"]=="UNRESOLVED": continue
    p=resolve(row["need"])
    tags={str(x) for x in vals(notes[p].get("tags"))}
    if "need-hypothesis" in tags:
        need_hypotheses+=1
counts["chain_need_records_still_hypotheses"]=need_hypotheses

# Formal active-chain registry classifications.
disp=yaml.safe_load(DISP.read_text(encoding="utf-8")) or {}
records=disp.get("records") or {}
registry_findings=[]
active_chain_paths=set()
for spec in specs:
    for name in [spec["requirement"],spec["product"],spec["use_case"],spec.get("need"),spec.get("satisfier"),spec.get("implementation"),spec.get("architecture")]:
        p=resolve(name) if name else None
        if p: active_chain_paths.add(p)
    req=resolve(spec["requirement"])
    if req:
        active_chain_paths.update(links(req,"verifiedBy"))
# Include all source needs attached to the five governed product Use Cases, not
# only the representative Need selected for each requirement-centered chain.
for spec in specs:
    uc=resolve(spec["use_case"])
    if uc:
        active_chain_paths.update(q for q in links(uc,"givesRiseTo") if notes[q].get("type")=="Use Case" and notes[q].get("subtype")=="why")

for p in sorted(active_chain_paths):
    rec=records.get(p)
    if not isinstance(rec,dict) or rec.get("classification")!="active_engineering":
        registry_findings.append((p,"classification","Expected active_engineering."))

service_uc=resolve("Configure and Service a Supported BMID")
if service_uc:
    rec=records.get(service_uc) or {}
    g=(rec.get("gaps") or {}).get("upstream")
    if not isinstance(g,dict) or g.get("disposition")!="unresolved" or g.get("exception")!="EXC-EVIDENCE-PENDING":
        registry_findings.append((service_uc,"upstream_gap","Expected unresolved / EXC-EVIDENCE-PENDING."))

counts["active_chain_registry_elements"]=len(active_chain_paths)
counts["active_chain_registry_findings"]=len(registry_findings)
for p,kind,msg in registry_findings:
    findings.append(("Step 27 registry",kind,f"{p}: {msg}"))

print("end to end product chain audit")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  repaired_breaks: {len(repairs)}")
print(f"  intentional_alternates: {len(intentional)}")
print(f"  accepted_unresolved_chain_breaks: {len(unresolved)}")
print(f"  findings: {len(findings)}")
for x in unresolved:
    print(f"  UNRESOLVED {x['requirement']} | {x['stage']} | {x['code']} | owner={x['owner']} | {x['reason']}")
for x in intentional:
    print(f"  INTENTIONAL {x['requirement']} | {x['stage']} | {x['reason']}")
for req,stage,msg in findings:
    print(f"  FINDING {req} | {stage} | {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# End-to-End Product Chain Audit","",
"Step 27 systematically audits every governed BMID/PosiGuard Requirement chain forward and backward.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [
f"| repaired_breaks | {len(repairs)} |",
f"| intentional_alternates | {len(intentional)} |",
f"| accepted_unresolved_chain_breaks | {len(unresolved)} |",
f"| findings | {len(findings)} |",
"",
"## Requirement-centered chains","",
"| Requirement | Customer Need | Use Case | Satisfier | Design / implementation | Architecture context | Verification |",
"|---|---|---|---|---|---|---|"]
for row in rows:
    lines.append("| " + " | ".join(str(row[k]) for k in ["requirement","need","use_case","satisfier","implementation","architecture","verification"]) + " |")

lines += ["","## Accepted unresolved chain breaks","",
"| Requirement | Stage | Exception | Owner | Reason |","|---|---|---|---|---|"]
if unresolved:
    for x in unresolved:
        lines.append(f"| {x['requirement']} | {x['stage']} | {x['code']} | {x['owner']} | {x['reason']} |")
else: lines.append("| _None_ | | | | |")

lines += ["","## Intentional semantic alternates","",
"| Requirement | Stage | Reason |","|---|---|---|"]
if intentional:
    for x in intentional:
        lines.append(f"| {x['requirement']} | {x['stage']} | {x['reason']} |")
else: lines.append("| _None_ | | |")

lines += ["","## Supplemental active architecture gaps","",
"| Element | Stage | Exception | Owner | Reason |","|---|---|---|---|---|"]
for x in supplemental:
    lines.append(f"| {x['element']} | {x['stage']} | {x['code']} | {x['owner']} | {x['reason']} |")

lines += ["","## Findings","",
"| Requirement | Stage | Finding |","|---|---|---|"]
if findings:
    for req,stage,msg in findings: lines.append(f"| {req} | {stage} | {msg} |")
else: lines.append("| _None_ | | |")

lines += ["","## Audit rules","",
"- Forward and backward relationship checks are equally required; every governed pair used in a chain must be synchronized.",
"- A Customer Need may remain a hypothesis; that is an evidence-quality limitation, not a broken semantic relationship.",
"- Product-level application coverage may be satisfied directly by an Object when a Function would overstate the semantics.",
"- dependsOn/dependencyOf is accepted for enabling Design implementation where realizedBy/realizes would overstate direct realization.",
"- Local Model architecture is contextual unless a governed definition-to-occurrence/relationship explicitly exists; no sensor wiring, service topology, or protocol is invented.",
"- Verification intent closes the modeled chain at the requirement level. No executed Result is claimed.",
"- Accepted unresolved breaks require an exception code, responsible workstream, and reason; they remain visible for Step 28.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("END TO END PRODUCT CHAIN AUDIT PASSED")
