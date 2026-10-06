#!/usr/bin/env python3
"""Step 18 Verification coverage review.

Governed Step 18 review entry point.

Reviews every Verification intent, validates verifies/verifiedBy synchronization,
checks active Requirement coverage, and distinguishes requirement-level
verification intent from Function/Design implementation detail and from
Procedure/Setup/Plan/Result execution artifacts. Report-only.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"verification-coverage-review.md"

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
    d=fm(p.read_text(encoding="utf-8",errors="replace"))
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d
    bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

counts=Counter(); findings=[]; verification_rows=[]; requirement_rows=[]
valid_targets={"Requirement","Function","Design","Info"}

verifications={p:d for p,d in notes.items() if d.get("type")=="Verification"}
requirements={p:d for p,d in notes.items() if d.get("type")=="Requirement"}
functions={p:d for p,d in notes.items() if d.get("type")=="Function"}
designs={p:d for p,d in notes.items() if d.get("type")=="Design"}

for typ in ("Verification","Requirement","Function","Design","Procedure","Setup","Plan","Result"):
    counts[f"type_{typ}"]=sum(1 for d in notes.values() if d.get("type")==typ)

# Active Requirements: product-scoped requirements in the current model.
active_requirements={}
for p,d in requirements.items():
    tags={str(x) for x in vals(d.get("tags"))}
    if vals(d.get("appliesTo")) or "product-requirement" in tags:
        active_requirements[p]=d
counts["active_requirements"]=len(active_requirements)

# Validate every Verification intent and inverse synchronization.
for p,d in sorted(verifications.items()):
    raw_targets=vals(d.get("verifies"))
    if not raw_targets:
        findings.append((p,"verification-no-target","Active Verification intent has no verifies target."))
        continue
    valid_count=0
    for raw in raw_targets:
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-verifies",str(raw)))
            continue
        qtyp=str(notes[q].get("type"))
        if qtyp not in valid_targets:
            findings.append((p,"invalid-verifies-target",f"{Path(q).stem}: {qtyp}"))
            continue
        valid_count+=1
        counts[f"verification_targets_{qtyp}"]+=1
        inverse={resolve(target(x)) for x in vals(notes[q].get("verifiedBy")) if resolve(target(x))}
        if p not in inverse:
            findings.append((p,"verification-inverse",f"{Path(q).stem} lacks reciprocal verifiedBy."))
        verification_rows.append((p,q,qtyp))
    if valid_count:
        counts["verifications_with_valid_target"]+=1

# Validate reverse-side verifiedBy claims for all supported target classes.
for q,d in sorted(notes.items()):
    if d.get("type") not in valid_targets: continue
    for raw in vals(d.get("verifiedBy")):
        p=resolve(target(raw))
        if not p:
            findings.append((q,"unresolved-verifiedBy",str(raw)))
            continue
        if p not in verifications:
            findings.append((q,"verifiedBy-not-verification",f"{Path(p).stem}: {notes[p].get('type')}"))
            continue
        fwd={resolve(target(x)) for x in vals(notes[p].get("verifies")) if resolve(target(x))}
        if q not in fwd:
            findings.append((q,"verifiedBy-inverse",f"{Path(p).stem} lacks reciprocal verifies."))

# Active Requirement coverage is mandatory. Verification intent may exist even
# when implementation/satisfaction remains unresolved.
verified_active=set()
for q,d in sorted(active_requirements.items()):
    direct=[]
    for raw in vals(d.get("verifiedBy")):
        p=resolve(target(raw))
        if p in verifications:
            direct.append(p)
    if direct:
        verified_active.add(q)
        counts["active_requirements_with_verification_intent"]+=1
    else:
        findings.append((q,"active-requirement-no-verification","Product-scoped Requirement has no Verification intent."))

    sats=[]
    for raw in vals(d.get("satisfiedBy")):
        p=resolve(target(raw))
        if p: sats.append(p)
    if sats:
        counts["active_requirements_with_satisfier"]+=1
    else:
        counts["active_requirements_without_satisfier"]+=1

    requirement_rows.append((q,direct,sats))

# Function/Design verification relevance:
# If a Function/Design is a satisfier of a verified Requirement, the requirement
# Verification provides outcome-level verification coverage. Do not require a
# duplicate direct Verification unless independent implementation criteria exist.
mediated_functions=set(); mediated_designs=set()
for q in verified_active:
    for raw in vals(notes[q].get("satisfiedBy")):
        p=resolve(target(raw))
        if not p: continue
        if p in functions:
            mediated_functions.add(p)
        elif p in designs:
            mediated_designs.add(p)

# Designs that directly realize a requirement-satisfying Function are part of the
# same verified chain, but are not asserted to be design-verified unless a
# Verification explicitly targets them.
for p in list(mediated_functions):
    for raw in vals(notes[p].get("realizedBy")):
        q=resolve(target(raw))
        if q in designs:
            mediated_designs.add(q)

counts["functions_with_requirement_mediated_verification"]=len(mediated_functions)
counts["designs_with_requirement_mediated_verification"]=len(mediated_designs)
counts["functions_with_direct_verification"]=sum(1 for p,d in functions.items() if vals(d.get("verifiedBy")))
counts["designs_with_direct_verification"]=sum(1 for p,d in designs.items() if vals(d.get("verifiedBy")))

# Execution artifacts are distinct from reusable Verification intent. Inventory
# them here; Step 19 owns their execution relationships.
execution_types={"Procedure","Setup","Plan","Result"}
execution={typ:[p for p,d in notes.items() if d.get("type")==typ] for typ in execution_types}
counts["execution_artifacts_total"]=sum(len(v) for v in execution.values())

print("verification coverage review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,q,qtyp in verification_rows:
    print(f"  VERIFIES {Path(p).stem} -> {qtyp} {Path(q).stem}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Verification Coverage Review","",
"Step 18 whole-vault review of Verification intent and active Requirement coverage.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Verification targets","",
"| Verification | Target type | Target |","|---|---|---|"]
if verification_rows:
    for p,q,qtyp in verification_rows:
        lines.append(f"| {p} | {qtyp} | {q} |")
else:
    lines.append("| _None_ | | |")

lines += ["","## Active Requirement coverage","",
"| Requirement | Verification intent | Satisfaction disposition |","|---|---|---|"]
for q,direct,sats in requirement_rows:
    v=", ".join(Path(x).stem for x in direct) if direct else "_Missing_"
    s=", ".join(Path(x).stem for x in sats) if sats else "_Implementation/satisfaction unresolved_"
    lines.append(f"| {q} | {v} | {s} |")

lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")

lines += ["","## Interpretation","",
"- Verification is reusable verification intent. Procedure, Setup, Plan, and Result are execution artifacts and do not replace Verification intent.",
"- Every active product-scoped Requirement must have a Verification disposition; the current model uses explicit Verification notes.",
"- A Verification may legitimately exist before a Requirement has an approved satisfier or implementation. Verification intent states what must eventually be demonstrated, not how it is implemented.",
"- Functions and Designs do not require duplicate direct Verification merely because they participate in a verified Requirement chain. Add direct verification only when independent behavior- or implementation-specific acceptance criteria exist.",
"- Requirement-mediated coverage is outcome-level traceability; it must not be misread as proof that a particular Design implementation has already been executed or passed.",
"- Step 19 owns Procedure/Setup/Plan/Result execution relationships. This step does not invent them.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("VERIFICATION COVERAGE REVIEW PASSED")
