#!/usr/bin/env python3
"""Step 17 behavioral sequencing and state-link review.

Reviews State, State Machine, Functional Flow, Function, and Design notes for
governed sequencing, triggering, ownership, and initial/final-state semantics.
Report-only: absence of sequence/state modeling is not treated as a defect.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"behavioral-sequencing-state-review.md"

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
    notes[rel]=d; bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

counts=Counter(); findings=[]; rows=[]
types=Counter(str(d.get("type")) for d in notes.values())
for typ in ("Function","Design","State","State Machine","Functional Flow","Item Flow","Object"):
    counts[f"type_{typ.replace(' ','_')}"]=types.get(typ,0)

sequence_types={"Function","Design","State","Functional Flow"}
triggered_types={"Function","Design","State"}
trigger_source_types={"Function","Design","State","Item Flow"}

def resolved_values(p,d,field):
    out=[]
    for raw in vals(d.get(field)):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-link",f"{field}: {raw}"))
        else:
            out.append(q)
    return out

# Sequence and trigger review across all notes.
for p,d in sorted(notes.items()):
    typ=str(d.get("type"))
    for field,inv in (("precedes","follows"),("follows","precedes")):
        qs=resolved_values(p,d,field)
        if qs:
            counts[f"{field}_assertions"]+=len(qs)
            counts["notes_with_sequence"]+=1
        for q in qs:
            qtyp=str(notes[q].get("type"))
            if typ not in sequence_types or qtyp!=typ:
                findings.append((p,"sequence-endpoint-type",
                    f"{field} {Path(q).stem}: expected same compatible behavior class; found {typ} -> {qtyp}."))
            invset={resolve(target(x)) for x in vals(notes[q].get(inv)) if resolve(target(x))}
            if p not in invset:
                findings.append((p,"sequence-inverse",f"{field} {Path(q).stem} lacks reciprocal {inv}."))
            rows.append((field,p,q))

    for field,inv in (("triggeredBy","triggers"),("triggers","triggeredBy")):
        qs=resolved_values(p,d,field)
        if qs:
            counts[f"{field}_assertions"]+=len(qs)
            counts["notes_with_trigger_semantics"]+=1
        for q in qs:
            qtyp=str(notes[q].get("type"))
            if field=="triggeredBy":
                if typ not in triggered_types or qtyp not in trigger_source_types:
                    findings.append((p,"trigger-endpoint-type",
                        f"triggeredBy {Path(q).stem}: invalid {typ} <- {qtyp}."))
            else:
                if typ not in trigger_source_types or qtyp not in triggered_types:
                    findings.append((p,"trigger-endpoint-type",
                        f"triggers {Path(q).stem}: invalid {typ} -> {qtyp}."))
            invset={resolve(target(x)) for x in vals(notes[q].get(inv)) if resolve(target(x))}
            if p not in invset:
                findings.append((p,"trigger-inverse",f"{field} {Path(q).stem} lacks reciprocal {inv}."))
            rows.append((field,p,q))

# State-machine ownership and start/end semantics.
states={p:d for p,d in notes.items() if d.get("type")=="State"}
sms={p:d for p,d in notes.items() if d.get("type")=="State Machine"}
objects={p:d for p,d in notes.items() if d.get("type")=="Object"}

for p,d in sorted(states.items()):
    owners=resolved_values(p,d,"stateOf")
    if owners: counts["states_with_owner"]+=1
    if not owners:
        findings.append((p,"state-no-owner","State has no stateOf owner."))
    for q in owners:
        if notes[q].get("type") not in {"Object","State Machine"}:
            findings.append((p,"state-owner-type",f"{Path(q).stem} is not Object or State Machine."))
        inv={resolve(target(x)) for x in vals(notes[q].get("hasState")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"state-owner-inverse",f"{Path(q).stem} lacks reciprocal hasState."))

for p,d in sorted(sms.items()):
    owners=resolved_values(p,d,"stateOf")
    if owners: counts["state_machines_with_owner"]+=1
    if not owners:
        findings.append((p,"state-machine-no-owner","State Machine has no stateOf Object owner."))
    for q in owners:
        if q not in objects:
            findings.append((p,"state-machine-owner-type",f"{Path(q).stem} is not an Object."))
        inv={resolve(target(x)) for x in vals(notes[q].get("hasState")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"state-machine-owner-inverse",f"{Path(q).stem} lacks reciprocal hasState."))

    contained=resolved_values(p,d,"hasState")
    initials=resolved_values(p,d,"initialState")
    finals=resolved_values(p,d,"finalState")
    counts["state_machine_hasState_assertions"]+=len(contained)
    counts["initialState_assertions"]+=len(initials)
    counts["finalState_assertions"]+=len(finals)
    if contained: counts["state_machines_with_states"]+=1
    if initials: counts["state_machines_with_initial_state"]+=1
    if finals: counts["state_machines_with_final_state"]+=1
    for q in contained:
        if q not in states:
            findings.append((p,"hasState-type",f"{Path(q).stem} is not a State."))
        inv={resolve(target(x)) for x in vals(notes[q].get("stateOf")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"hasState-inverse",f"{Path(q).stem} lacks reciprocal stateOf."))
    contained_set=set(contained)
    for field,qs in (("initialState",initials),("finalState",finals)):
        for q in qs:
            if q not in states:
                findings.append((p,"state-boundary-type",f"{field} target {Path(q).stem} is not a State."))
            if contained_set and q not in contained_set:
                findings.append((p,"state-boundary-membership",f"{field} target {Path(q).stem} is not in hasState."))

# Functional Flow participation is inventoried; sequencing is optional unless modeled.
flows={p:d for p,d in notes.items() if d.get("type")=="Functional Flow"}
for p,d in sorted(flows.items()):
    context=sum(len(vals(d.get(f))) for f in ("childOf","hasChild","includedIn","includes","dependsOn","precedes","follows","describedBy","supportedBy"))
    if context: counts["functional_flows_with_context"]+=1

print("behavioral sequencing and state review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for fld,p,q in rows: print(f"  LINK {fld}: {Path(p).stem} -> {Path(q).stem}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Behavioral Sequencing and State Review","",
"Step 17 whole-vault review of sequencing, triggering, State, State Machine, and Functional Flow semantics.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Existing behavior links","",
"| Relationship | Source | Target |","|---|---|---|"]
if rows:
    for fld,p,q in rows: lines.append(f"| {fld} | {p} | {q} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- Sequence and trigger relationships encode actual behavior; they are never required merely to increase connectivity.",
"- precedes/follows must describe ordered behavior and remain inverse-synchronized.",
"- triggeredBy/triggers is element-level trigger semantics. Transition-level guard/trigger/effect text remains source evidence on the preceding state where applicable.",
"- State ownership uses stateOf/hasState. State Machine initialState/finalState point to States and are one-way.",
"- Functional Flow elements may remain absent or sparse until the model contains supported flow semantics.",
"- A vault with no first-class State, State Machine, Functional Flow, precedes/follows, or triggeredBy/triggers assertions is valid when no such behavior has yet been modeled.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("BEHAVIORAL SEQUENCING AND STATE REVIEW PASSED")
