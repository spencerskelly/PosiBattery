#!/usr/bin/env python3
"""Step 11 Use Case participation and need-link review.

Reviews every Use Case for participant validity, Actor/Organization need
semantics, scenario membership/option links, realization, and requirement-driving
links. Customer Needs are subtype/tagged Use Cases whose participants represent
people/orgs who hold the need; the governed hasNeed/needOf pair is preferred for
that semantic statement.
"""
# Governed Step 11 review entry point
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"use-case-participation-need-review.md"

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
bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; bybase[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

usecases={p:d for p,d in notes.items() if d.get("type")=="Use Case"}
counts=Counter(); findings=[]; upgrade_pairs=[]
for p,d in sorted(usecases.items()):
    counts["use_cases"]+=1
    tags=set(str(x) for x in vals(d.get("tags")))
    subtype=str(d.get("subtype") or "")
    is_need=("customer-need" in tags or subtype=="why" or p.startswith("50_Customer Needs/"))
    is_oper=("operational-use-case" in tags or subtype=="what")
    is_context=(not is_need and not is_oper)
    counts["customer_needs" if is_need else "operational_use_cases" if is_oper else "context_use_cases"]+=1

    participants=[]
    for raw in vals(d.get("participants")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-participant",str(raw)))
            continue
        participants.append(q)
        if notes[q].get("type") not in {"Actor","Organization","Object","Function","Port","Document"}:
            findings.append((p,"invalid-participant-type",f"{Path(q).stem}: {notes[q].get('type')}"))
    if participants: counts["use_cases_with_participants"]+=1
    else: findings.append((p,"missing-participants","No participants are modeled."))

    if is_need:
        actor_org=[q for q in participants if notes[q].get("type") in {"Actor","Organization"}]
        if actor_org: counts["needs_with_actor_or_org_participant"]+=1
        else: findings.append((p,"need-without-holder","Customer Need has no Actor/Organization participant."))

        needof={resolve(target(x)) for x in vals(d.get("needOf")) if resolve(target(x))}
        for q in actor_org:
            hasneed={resolve(target(x)) for x in vals(notes[q].get("hasNeed")) if resolve(target(x))}
            if q not in needof or p not in hasneed:
                upgrade_pairs.append((q,p))
        if needof: counts["needs_with_governed_needOf"]+=1

        if vals(d.get("realizedBy")): counts["needs_with_realizedBy"]+=1
        else: findings.append((p,"need-without-capability","Customer Need has no realizedBy capability/function."))

    if is_oper:
        if vals(d.get("realizedBy")): counts["operational_with_realizedBy"]+=1
        else: findings.append((p,"operational-without-realization","Operational Use Case has no realizedBy Function/Design."))
        if vals(d.get("drives")): counts["operational_with_drives"]+=1
        if any(notes[q].get("type") in {"Actor","Organization"} for q in participants):
            counts["operational_with_actor_or_org_participant"]+=1
        else:
            findings.append((p,"operational-without-human-org","Operational Use Case has no Actor/Organization participant."))

    if vals(d.get("includes")) or vals(d.get("includedIn")):
        counts["use_cases_with_include_membership"]+=1
    if vals(d.get("optionOf")) or vals(d.get("hasOption")):
        counts["use_cases_with_option_semantics"]+=1

print("use case participation and need linking review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  governed actor/org need pairs missing or unsynchronized: {len(upgrade_pairs)}")
for actor,need in upgrade_pairs:
    print(f"  NEED_PAIR_GAP {actor} -> {need}")
print(f"  findings excluding need-pair upgrade: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Use Case Participation and Need-Link Review","",
"Step 11 whole-vault review of Use Case participants, customer-need holders, operational realization, and scenario links.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| governed Actor/Organization need pairs missing or unsynchronized | {len(upgrade_pairs)} |",
f"| other findings | {len(findings)} |","",
"## Missing governed need pairs","",
"| Actor/Organization | Customer Need |","|---|---|"]
if upgrade_pairs:
    for a,n in upgrade_pairs: lines.append(f"| {a} | {n} |")
else: lines.append("| _None_ | |")
lines += ["","## Other findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- participants states who/what participates in a Use Case; it does not replace the semantic statement that an Actor or Organization has a Customer Need.",
"- For Customer Needs, Actor/Organization participants should also be represented by the governed hasNeed/needOf pair when the note explicitly says that role has the problem.",
"- Operational Use Cases should normally have an Actor/Organization participant and a realizedBy Function/Design when the behavior boundary is mature.",
"- Customer Need realizedBy links express the capability/functions that address the need; they are distinct from need ownership.",
"- Includes/optionOf are required only when scenario membership/option semantics actually exist; their absence is not itself a defect.",
"- External actor behavior stays in Use Cases; product-controlled behavior stays in Functions.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings:
    raise SystemExit(2)
print("USE CASE REVIEW PASSED WITH NEED-LINK UPGRADE QUEUE" if upgrade_pairs else "USE CASE REVIEW PASSED")
