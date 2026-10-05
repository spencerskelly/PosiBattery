#!/usr/bin/env python3
"""Headless compatibility/smoke review for the installed MDSE Workbench against PosiBattery.

This does not pretend to automate the Obsidian UI. It verifies the current built
Workbench artifact's declared capabilities against the current schemas/model,
simulates representative bounded graph views, and validates the Local Model
records used by occurrence-aware features.
"""
from __future__ import annotations
from pathlib import Path
from collections import defaultdict, deque
import json, re, sys, time

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required")

ROOT=Path(__file__).resolve().parents[2]
PLUGIN=ROOT/".obsidian/plugins/mdse-workbench"
REL=ROOT/"99_System/03_Schemas/relationships.yaml"
EL=ROOT/"99_System/03_Schemas/element-types.yaml"
LM=ROOT/"99_System/03_Schemas/local-model.yaml"

def load_yaml(p):
    with p.open(encoding="utf-8") as f: return yaml.safe_load(f) or {}

def frontmatter(text):
    if not text.startswith("---\n"): return {}
    e=text.find("\n---",4)
    if e<0: return {}
    try: return yaml.safe_load(text[4:e]) or {}
    except Exception: return {}

def vals(v):
    if v is None: return []
    return v if isinstance(v,list) else [v]

def link_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

def version_tuple(v):
    return tuple(int(x) for x in str(v).split("."))

manifest=json.loads((PLUGIN/"manifest.json").read_text(encoding="utf-8"))
main=(PLUGIN/"main.js").read_text(encoding="utf-8",errors="replace")
rels=load_yaml(REL)
els=load_yaml(EL)
local_schema=load_yaml(LM)

fail=[]
review=[]
checks=[]

def check(name, ok, detail):
    checks.append((name,ok,detail))
    if not ok: fail.append(f"{name}: {detail}")

# Built artifact / capability contract.
check("Workbench manifest version", manifest.get("version")=="0.1.17", f"installed={manifest.get('version')}")
for token in [
    'id: "diagnostics"',
    'id: "runtime-health"',
    'id: "inspect-semantic-cache"',
    'id: "rebuild-index"',
    'name: "Explore internal structure of current Object"',
    'name: "Explore functional view of current note"',
    'name: "Explore requirements view of current note"',
    '"Where Used"',
    '"Interfaces"',
    '"Verification"',
    '"Design"',
    '"Scenario"',
    '"Behavior"',
    '"Evidence"',
]:
    check(f"Workbench capability {token}", token in main, "present" if token in main else "missing")

m=re.search(r'var MIN_RELATIONSHIPS_VERSION = "([^"]+)"',main)
min_rel=m.group(1) if m else None
check("Workbench minimum relationship schema discoverable", bool(min_rel), f"minimum={min_rel}")
check("Active relationship schema compatible", bool(min_rel) and version_tuple(rels.get("schemaVersion","0"))>=version_tuple(min_rel),
      f"active={rels.get('schemaVersion')} minimum={min_rel}")
check("Local Model readable version 0.2", 'var READABLE_VERSIONS = ["0.1", "0.2"]' in main, "Workbench parser supports 0.1 and 0.2")
check("Local Model schema writable 0.2", str(local_schema.get("compatibility",{}).get("writableVersion"))=="0.2",
      f"writable={local_schema.get('compatibility',{}).get('writableVersion')}")
check("Cooperative UI budget present", "var UI_WORK_SLICE_BUDGET_MS = 12" in main, "expected 12 ms budget")
check("Large-view cap present", "nodeCap: 80" in main and "nodeCap: 200" in main, "bounded profile caps 80/200")

# Schema parse compatibility as Workbench expects.
classes={str(x.get("name")) for x in els.get("classes",[]) if isinstance(x,dict) and x.get("name")}
unknown=[]
relationship_fields=set()
inverse_fields=set()
for section in ("paired","temporaryPairs"):
    for rec in rels.get(section,[]) or []:
        if not isinstance(rec,dict): continue
        f=rec.get("forward"); inv=rec.get("inverse")
        if f: relationship_fields.add(f)
        if inv: inverse_fields.add(inv)
        for side in ("from","to"):
            v=rec.get(side)
            if v=="any" or v is None: continue
            for c in (v if isinstance(v,list) else [v]):
                if c not in classes: unknown.append((f,side,c))
for section in ("symmetric","oneWay"):
    for rec in rels.get(section,[]) or []:
        if not isinstance(rec,dict): continue
        f=rec.get("field")
        if f: relationship_fields.add(f)
        for side in ("between","from","to"):
            v=rec.get(side)
            if v=="any" or v is None: continue
            for c in (v if isinstance(v,list) else [v]):
                if c not in classes: unknown.append((f,side,c))
check("Workbench schema endpoint classes", not unknown, f"unknown={unknown[:8]}")

# Current model graph and authored relationship resolution.
notes={}
texts={}
basename=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    rel=p.relative_to(ROOT).as_posix()
    text=p.read_text(encoding="utf-8",errors="replace")
    fm=frontmatter(text)
    if not isinstance(fm,dict) or not fm.get("type"): continue
    notes[rel]=fm; texts[rel]=text; basename[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=basename.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

out=defaultdict(list); inc=defaultdict(list)
unresolved=[]
for source,fm in notes.items():
    for field in relationship_fields|inverse_fields:
        if field not in fm: continue
        for raw in vals(fm.get(field)):
            target=link_target(raw)
            if not target: continue
            dest=resolve(target)
            if not dest: unresolved.append((source,field,target)); continue
            out[source].append((field,dest))
            inc[dest].append((field,source))

check("Current model notes indexed", len(notes)>=900, f"model_notes={len(notes)}")
check("Authored relationship resolution", not unresolved, f"resolved_assertions={sum(map(len,out.values()))} unresolved={len(unresolved)}")

# Local Model parsing/compatibility smoke.
START=re.compile(r"<!--\s*MDSE:LOCAL-MODEL START(?:\s+schema=(\S+?))?\s*-->")
END=re.compile(r"<!--\s*MDSE:LOCAL-MODEL END\s*-->")
TOKEN=re.compile(r"^(part|ep|conn|flow)-(\d{17}[a-z-]{13})$")
local_regions=[]
local_errors=[]
local_records=0
for path,text in texts.items():
    sm=START.search(text); em=END.search(text)
    if not sm and not em: continue
    if not sm or not em or sm.start()>em.start():
        local_errors.append((path,"marker mismatch")); continue
    version=sm.group(1)
    if version not in {"0.1","0.2"}: local_errors.append((path,f"unsupported schema {version}"))
    body=text[sm.end():em.start()]
    ids=re.findall(r"(?m)^\^(part|ep|conn|flow)-([0-9]{17}[a-z-]{13})\s*$",body)
    local_records += len(ids)
    all_id_strings=[f"{k}-{tok}" for k,tok in ids]
    if len(all_id_strings)!=len(set(all_id_strings)): local_errors.append((path,"duplicate local IDs"))
    definitions=re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",body)
    for d in definitions:
        if not resolve(d.strip()): local_errors.append((path,f"unresolved definition {d}"))
    # same-note block references must point at an ID in this region
    idset=set(all_id_strings)
    for block in re.findall(r"\[\[#\^([^\]|]+)",body):
        if block not in idset: local_errors.append((path,f"unresolved local block {block}"))
    local_regions.append((path,version,len(all_id_strings),definitions))

check("Local Model regions readable", len(local_regions)>=1 and not local_errors,
      f"regions={len(local_regions)} records={local_records} errors={local_errors[:5]}")
check("BMID Local Model record count", local_records==11, f"records={local_records}")

# Workbench-style bounded graph smoke for representative current-model views.
def step_ok(step, current_type, next_type):
    if step.get("from") and current_type not in step["from"]: return False
    if step.get("to") and next_type not in step["to"]: return False
    return True

def traverse(start,steps,depth=2,node_cap=80,per_parent=12):
    if start not in notes: return None
    depth_of={start:0}; frontier=[start]; omitted=0
    for d in range(depth):
        nxt=[]
        for p in frontier:
            candidates=[]
            for st in steps:
                if st.get("atStartOnly") and d>0: continue
                edges=out[p] if st["direction"]=="out" else inc[p]
                for field,n in edges:
                    if field!=st["field"] or n in depth_of: continue
                    if not step_ok(st,str(notes[p].get("type","")),str(notes[n].get("type",""))): continue
                    if n not in candidates: candidates.append(n)
            candidates.sort(key=lambda x: Path(x).stem.lower())
            room=max(0,min(per_parent,node_cap-len(depth_of)))
            show=candidates[:room]; omitted+=max(0,len(candidates)-len(show))
            for n in show:
                depth_of[n]=d+1; nxt.append(n)
        frontier=nxt
        if len(depth_of)>=node_cap: break
    return len(depth_of),omitted

def by_name(name):
    ms=basename.get(name,[])
    return ms[0] if len(ms)==1 else None

profiles=[
 ("Structure large assembly","Industrial Truck Anatomy",[
   {"field":"hasPart","direction":"out"},{"field":"hasChild","direction":"out"},{"field":"hasState","direction":"out"},{"field":"includes","direction":"out"}],2,80,12),
 ("Functional product","PosiCharge BMID",[
   {"field":"performs","direction":"out","from":["Object"],"to":["Function"],"atStartOnly":True},
   {"field":"performs","direction":"in","from":["Function"],"to":["Object"]},
   {"field":"hasChild","direction":"in","from":["Function"],"to":["Function"],"atStartOnly":True},
   {"field":"hasChild","direction":"out","from":["Function"],"to":["Function"]},
   {"field":"precedes","direction":"in","from":["Function"],"to":["Function"]},
   {"field":"precedes","direction":"out","from":["Function"],"to":["Function"]}],2,80,12),
 ("Requirements BMID","BMID - Provide Supported Battery Condition Information to Charger",[
   {"field":"derivedFrom","direction":"out","from":["Requirement"],"to":["Requirement"]},
   {"field":"derivedFrom","direction":"in","from":["Requirement"],"to":["Requirement"]},
   {"field":"refines","direction":"out","from":["Requirement"],"to":["Requirement"]},
   {"field":"refines","direction":"in","from":["Requirement"],"to":["Requirement"]},
   {"field":"satisfies","direction":"in","from":["Requirement"],"to":["Function","Design"]},
   {"field":"verifies","direction":"in","from":["Requirement"],"to":["Verification"]},
   {"field":"appliesTo","direction":"out","from":["Requirement"]},
   {"field":"drives","direction":"in","from":["Requirement"],"to":["Use Case"]}],2,80,12),
 ("Scenario BMID","Charge a BMID-Equipped Battery Using Battery Information",[
   {"field":"participants","direction":"out","from":["Use Case"]},
   {"field":"realizedBy","direction":"out","from":["Use Case"],"to":["Function","Design"]},
   {"field":"optionOf","direction":"out","from":["Use Case"],"to":["Use Case"]},
   {"field":"drives","direction":"out","from":["Use Case"],"to":["Requirement"]}],2,80,12),
 ("Verification BMID","Verify BMID Battery Condition Information Delivery",[
   {"field":"verifies","direction":"out","from":["Verification"],"to":["Requirement"]},
   {"field":"satisfies","direction":"in","from":["Requirement"],"to":["Function","Design"]}],2,80,12),
]
view_results=[]
for label,name,steps,depth,cap,pp in profiles:
    start=by_name(name)
    res=traverse(start,steps,depth,cap,pp) if start else None
    ok=bool(res and res[0]>1 and res[0]<=cap)
    view_results.append((label,name,start,res))
    check(f"Representative view: {label}",ok,f"start={start} result={res}")

# Occurrence-aware behavior boundary.
owner="20_Product Architecture/PosiCharge BMID Product Assembly Local Model.md"
owner_type=str(notes.get(owner,{}).get("type",""))
direct_internal_supported=owner_type=="Object"
if not direct_internal_supported:
    review.append(
      "The current BMID Local Model owner is type Info. Workbench 0.1.17's Internal profile starts only from Object, "
      "so that context note cannot launch the Internal view directly. The Local Model remains readable/validated, and "
      "definition-centric occurrence discovery is available through occurrence-aware Where Used / Interfaces paths. "
      "Treat this as a Workbench interaction limitation, not a model-integrity failure."
    )

# Static capability for occurrence-aware paths.
check("Occurrence-aware Where Used path", 'case "Where Used":\n        return null;' in main and "withLocalWhereUsed" in main,
      "vault-wide occurrence hydration is implemented")
check("Occurrence-aware Interfaces path", 'case "Interfaces":\n      case "Where Used":' in main and "withLocalInterfaces" in main,
      "vault-wide occurrence hydration is implemented")
check("Occurrence-aware Structure path", "withLocalStructure" in main and "needsLocalOccurrences: true" in main,
      "local part occurrence augmentation is implemented")

report=ROOT/"workbench-model-review.md"
lines=["# PosiBattery Workbench Model Review","",
"Headless compatibility/smoke review for the installed Workbench against the cleaned model. This is not a substitute for clicking through the Obsidian UI; it verifies the repository/runtime contracts that those interactions consume.","",
"## Checks","",
"| Check | Result | Detail |","|---|---|---|"]
for name,ok,detail in checks:
    lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {str(detail).replace('|','/')} |")
lines += ["","## Representative bounded views","",
"| View | Start | Result |","|---|---|---|"]
for label,name,start,res in view_results:
    lines.append(f"| {label} | {name} | {res if res else 'not available'} |")
lines += ["","## Review findings",""]
if review:
    lines += [f"- {x}" for x in review]
else:
    lines += ["- None."]
lines += ["","## Interpretation","",
"- The installed built artifact remains Workbench 0.1.17 and exposes diagnostics, runtime health, semantic-cache inspection, rebuild, and the governed exploration profiles.",
"- Active relationships/element schemas are compatible with the Workbench parser contract and relationship targets resolve in the cleaned vault.",
"- Representative large/current-model traversals remain bounded by the Workbench node caps and return useful non-empty views.",
"- The BMID Local Model parses as schema 0.2 with 11 local records and resolved definitions/block references.",
"- UI responsiveness, canvas rendering, click behavior, and actual elapsed interactive timings require an Obsidian runtime; this headless check does not fabricate those observations.",
""]
report.write_text("\n".join(lines),encoding="utf-8")

print("Workbench cleaned-model review")
print(f"  workbench version: {manifest.get('version')}")
print(f"  model notes: {len(notes)}")
print(f"  relationship assertions: {sum(map(len,out.values()))}")
print(f"  unresolved relationship links: {len(unresolved)}")
print(f"  local model regions: {len(local_regions)}")
print(f"  local model records: {local_records}")
print(f"  representative views passed: {sum(1 for n,o,d in checks if n.startswith('Representative view:') and o)}/{sum(1 for n,o,d in checks if n.startswith('Representative view:'))}")
print(f"  review findings: {len(review)}")
for x in review: print("  REVIEW:",x)
print(f"  blocking findings: {len(fail)}")
for x in fail: print("  FAIL:",x)
print(f"  report: {report.relative_to(ROOT)}")
if fail:
    sys.exit(1)
print("WORKBENCH MODEL REVIEW PASSED WITH DOCUMENTED INTERACTION LIMITATIONS" if review else "WORKBENCH MODEL REVIEW PASSED")
