#!/usr/bin/env python3
"""Step 19 validation execution relationship review.

Reviews Procedure, Setup, Plan, Result, and Step notes and inventories the
governed relationships that connect reusable Verification intent to execution
capability, campaign selection, ordered activity, and result evidence.

This is report-only. It does not require execution artifacts to exist before
controlled method/campaign/execution evidence is available.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"validation-execution-relationship-review.md"

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
    notes[rel]=d
    bodies[rel]=t
    bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

counts=Counter(); findings=[]; review_prompts=[]; rows=[]

execution_types=("Procedure","Setup","Plan","Result","Step")
for typ in ("Verification",)+execution_types:
    counts[f"type_{typ}"]=sum(1 for d in notes.values() if d.get("type")==typ)

paired={
    "childOf":"hasChild","hasChild":"childOf",
    "includedIn":"includes","includes":"includedIn",
    "dependsOn":"dependencyOf","dependencyOf":"dependsOn",
    "drivenBy":"drives","drives":"drivenBy",
    "verifies":"verifiedBy","verifiedBy":"verifies",
    "satisfies":"satisfiedBy","satisfiedBy":"satisfies",
    "supports":"supportedBy","supportedBy":"supports",
    "contradicts":"contradictedBy","contradictedBy":"contradicts",
    "describedBy":"describes","describes":"describedBy",
    "givesRiseTo":"arisesIn","arisesIn":"givesRiseTo",
}

canonical_fields={
    "Procedure": {"givesRiseTo","arisesIn","childOf","includedIn","dependsOn","hasChild","includes","dependencyOf"},
    "Setup": {"givesRiseTo","arisesIn","dependencyOf","includedIn","childOf","hasChild","includes","dependsOn"},
    "Plan": {"drivenBy","dependsOn","includedIn","childOf","includes","drives","applies"},
    "Result": {"includedIn","childOf","dependsOn","describedBy","verifies","satisfies","supports","contradicts"},
    "Step": {"childOf","includedIn","follows","precedes","hasChild","includes","dependsOn"},
}

# Validate relationships actually present on execution artifacts. Relationship
# endpoint permissibility itself is also covered by the vault-wide relationship audit.
for p,d in sorted(notes.items()):
    typ=str(d.get("type"))
    if typ not in execution_types: continue

    present=0
    for field in canonical_fields[typ]:
        for raw in vals(d.get(field)):
            present+=1
            q=resolve(target(raw))
            if not q:
                findings.append((p,"unresolved-execution-link",f"{field}: {raw}"))
                continue
            qtyp=str(notes[q].get("type"))
            rows.append((typ,p,field,qtyp,q))
            counts[f"{typ}_{field}_assertions"]+=1

            invfield=paired.get(field)
            if invfield:
                inv={resolve(target(x)) for x in vals(notes[q].get(invfield)) if resolve(target(x))}
                if p not in inv:
                    findings.append((p,"execution-link-inverse",f"{field} {Path(q).stem} lacks reciprocal {invfield}."))

    if present:
        counts[f"{typ}_with_execution_context"]+=1
    else:
        counts[f"{typ}_without_execution_context"]+=1

    # Semantic review prompts, not hard failures, for sparse library/raw items.
    if typ=="Procedure":
        child_types=[]
        for raw in vals(d.get("hasChild")):
            q=resolve(target(raw))
            if q: child_types.append(str(notes[q].get("type")))
        if child_types and any(x not in {"Step","Procedure"} for x in child_types):
            review_prompts.append((p,"procedure-child-review",f"hasChild target types: {sorted(set(child_types))}"))
    elif typ=="Plan":
        member_types=[]
        for raw in vals(d.get("includes")):
            q=resolve(target(raw))
            if q: member_types.append(str(notes[q].get("type")))
        canonical={"Verification","Procedure","Setup","Result"}
        noncanonical=sorted(set(member_types)-canonical)
        if noncanonical:
            review_prompts.append((p,"plan-membership-review",f"noncanonical included types: {noncanonical}"))
    elif typ=="Result":
        evidence=sum(len(vals(d.get(f))) for f in ("verifies","satisfies","supports","contradicts"))
        if evidence:
            counts["results_with_evidence_target"]+=1
        else:
            review_prompts.append((p,"result-no-evidence-target","Raw/unreviewed Result may be acceptable; reviewed Result should identify what it verifies/supports/contradicts/satisfies."))

# Inventory the canonical bridge pattern when present.
for p,d in sorted(notes.items()):
    if d.get("type")=="Plan":
        members=[]
        for raw in vals(d.get("includes")):
            q=resolve(target(raw))
            if q: members.append(str(notes[q].get("type")))
        for typ in ("Verification","Procedure","Setup","Result"):
            if typ in members: counts[f"plans_including_{typ}"]+=1

for p,d in sorted(notes.items()):
    if d.get("type")=="Procedure":
        for raw in vals(d.get("dependsOn")):
            q=resolve(target(raw))
            if q and notes[q].get("type")=="Setup":
                counts["procedure_to_setup_dependencies"]+=1
        for raw in vals(d.get("hasChild")):
            q=resolve(target(raw))
            if q and notes[q].get("type")=="Step":
                counts["procedure_to_step_children"]+=1

for p,d in sorted(notes.items()):
    if d.get("type")=="Result":
        for raw in vals(d.get("includedIn")):
            q=resolve(target(raw))
            if q and notes[q].get("type")=="Plan":
                counts["results_in_plan"]+=1
        for raw in vals(d.get("dependsOn")):
            q=resolve(target(raw))
            if q and notes[q].get("type") in {"Procedure","Setup"}:
                counts["result_execution_dependencies"]+=1

# Confirm the six current BMID Verification intents remain explicitly
# pre-execution rather than silently claiming test execution.
verifications=[p for p,d in notes.items() if d.get("type")=="Verification"]
preexecution_markers=0
for p in verifications:
    body=bodies[p]
    if ("No approved Procedure" in body and "Setup" in body and "Result" in body):
        preexecution_markers+=1
counts["verification_notes_with_explicit_preexecution_statement"]=preexecution_markers

print("validation execution relationship review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
print(f"  review_prompts: {len(review_prompts)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,k,msg in review_prompts: print(f"  REVIEW {k}: {p}: {msg}")
for typ,p,field,qtyp,q in rows:
    print(f"  LINK {typ} {Path(p).stem} --{field}--> {qtyp} {Path(q).stem}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Validation Execution Relationship Review","",
"Step 19 whole-vault review of Procedure, Setup, Plan, Result, and Step execution semantics.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |",f"| review_prompts | {len(review_prompts)} |",
"","## Existing execution relationships","",
"| Source type | Source | Relationship | Target type | Target |","|---|---|---|---|---|"]
if rows:
    for typ,p,field,qtyp,q in rows:
        lines.append(f"| {typ} | {p} | {field} | {qtyp} | {q} |")
else:
    lines.append("| _None_ | | | | |")

lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")

lines += ["","## Review prompts","",
"| Path | Kind | Detail |","|---|---|---|"]
if review_prompts:
    for p,k,msg in review_prompts: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")

lines += ["","## Canonical execution pattern","",
"- Verification defines reusable verification intent and continues to point at the engineering target with verifies.",
"- Plan selects campaign content. When a concrete campaign exists, Plan.includes is the preferred membership bridge for selected Verification, Procedure, Setup, and Result records.",
"- Procedure defines the ordered method. Procedure.hasChild may own Steps, and Procedure.dependsOn may identify required Setup or other prerequisites.",
"- Setup defines reusable execution capability/configuration. It is normally discovered through dependencyOf from the Procedure/Plan/Verification context that requires it.",
"- Result records execution evidence. Result should retain campaign/execution context through includedIn/childOf/dependsOn as supported and use verifies/supports/contradicts/satisfies for the engineering claim it evidences.",
"- The current vocabulary has no dedicated resultOf/executes relationship. Do not invent one during semantic-link closure; use Plan membership, dependencies, and Result evidence links unless a later schema decision explicitly adds a stronger term.",
"- Result is not a substitute for Verification intent, and Procedure/Setup/Plan are not substitutes for Verification intent.",
"- Absence of Procedure, Setup, Plan, Result, and Step is correct when no controlled method, campaign selection, or executed evidence exists.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("VALIDATION EXECUTION RELATIONSHIP REVIEW PASSED")
