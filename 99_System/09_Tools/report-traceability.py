#!/usr/bin/env python3
"""Report orphan and weak-traceability quality findings for PosiBattery.

This is intentionally report-only. It uses the governed relationship schema to
build a semantic graph, then highlights isolated elements and missing high-value
traceability patterns. It does not assert that every finding is a defect.
"""
from __future__ import annotations
from pathlib import Path
from collections import Counter, defaultdict
import re

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required")

ROOT=Path(__file__).resolve().parents[2]
REL_PATH=ROOT/"99_System"/"03_Schemas"/"relationships.yaml"
REPORT=ROOT/"traceability-quality-report.md"

def load_yaml(path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def frontmatter(text):
    if not text.startswith("---\n"): return {}
    end=text.find("\n---",4)
    if end<0: return {}
    try: return yaml.safe_load(text[4:end]) or {}
    except Exception: return {}

def vals(v):
    if v is None: return []
    return v if isinstance(v,list) else [v]

def link_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

rel_schema=load_yaml(REL_PATH)
relationship_fields=set()
for rec in rel_schema.get("paired",[])+rel_schema.get("temporaryPairs",[]):
    if rec.get("forward"): relationship_fields.add(rec["forward"])
    if rec.get("inverse"): relationship_fields.add(rec["inverse"])
for rec in rel_schema.get("symmetric",[])+rel_schema.get("oneWay",[]):
    if rec.get("field"): relationship_fields.add(rec["field"])

notes={}
texts={}
basename=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    rel=p.relative_to(ROOT).as_posix()
    text=p.read_text(encoding="utf-8",errors="replace")
    data=frontmatter(text)
    if not isinstance(data,dict) or not data.get("type"): continue
    notes[rel]=data
    texts[rel]=text
    basename[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        matches=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        matches=basename.get(Path(name).name,[])
    return matches[0] if len(matches)==1 else None

incoming=defaultdict(list)
outgoing=defaultdict(list)
for source,data in notes.items():
    for field in relationship_fields:
        if field not in data: continue
        for raw in vals(data.get(field)):
            target=link_target(raw)
            target_path=resolve(target)
            if not target_path: continue
            outgoing[source].append((field,target_path))
            incoming[target_path].append((field,source))

    # Governed Local Model definition references are contextual uses of reusable
    # definitions. Count them as semantic connectivity for orphan detection,
    # while keeping them separate from note-level relationship expectations.
    text=texts[source]
    m=re.search(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->",text)
    if m:
        for target in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1)):
            target_path=resolve(target.strip())
            if not target_path: continue
            outgoing[source].append(("localModelDefinition",target_path))
            incoming[target_path].append(("localModelDefinition",source))

orphans=[]
for path in notes:
    if not outgoing[path] and not incoming[path]:
        orphans.append(path)

# High-value expectations are deliberately broad and review-oriented.
# Each entry is a set of alternative relationships; one present relationship
# satisfies that traceability signal.
expectations={
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
    "Verification":[
        ("verification target", {"verifies"}),
    ],
    "Use Case":[
        ("participation or realization", {"participants","realizedBy","drives","hasNeed","needOf","arisesIn","givesRiseTo"}),
    ],
    "Object":[
        ("architecture/behavior/business context", {"supertypeOf","subtypeOf","partOf","hasPart","performs","hasDesign","madeBy","offeredBy","applies","describedBy"}),
    ],
    "Document":[
        ("subject/evidence trace", {"describes","supports","references","referencedBy"}),
    ],
}

weak=[]
by_type=Counter()
by_signal=Counter()
for path,data in notes.items():
    typ=str(data.get("type") or "")
    fields={f for f,_ in outgoing[path]} | {f for f,_ in incoming[path]}
    for label,alternatives in expectations.get(typ,[]):
        if not (fields & alternatives):
            weak.append((path,typ,label,sorted(alternatives)))
            by_type[typ]+=1
            by_signal[(typ,label)]+=1

# Product-development focus subset: high-value chain classes.
focus_types={"Use Case","Requirement","Function","Design","Verification"}
focus_notes=[p for p,d in notes.items() if str(d.get("type")) in focus_types]
focus_orphans=[p for p in orphans if p in focus_notes]
focus_weak=[x for x in weak if x[1] in focus_types]

summary={
    "model_notes":len(notes),
    "semantic_relationship_assertions":sum(len(v) for v in outgoing.values()),
    "isolated_model_elements":len(orphans),
    "product_development_focus_notes":len(focus_notes),
    "isolated_focus_elements":len(focus_orphans),
    "weak_traceability_findings":len(weak),
    "focus_weak_traceability_findings":len(focus_weak),
}

lines=[
"# PosiBattery Orphan and Traceability Quality Report","",
"Report-only quality scan generated by `99_System/09_Tools/report-traceability.py`. Findings are review prompts, not automatic failures.","",
"## Summary","",
"| Check | Count |","|---|---:|",
]
for k,v in summary.items(): lines.append(f"| {k.replace('_',' ')} | {v} |")

lines += ["","## Isolated model elements","",
"An isolated element has no resolved governed relationship assertion either incoming or outgoing. Body wikilinks and plain-text citations do not count as semantic model relationships.","",
"| Path | Type |","|---|---|"]
for path in orphans[:400]:
    lines.append(f"| {path} | {notes[path].get('type','')} |")
if len(orphans)>400: lines.append(f"| … | {len(orphans)-400} additional isolated elements omitted |")

lines += ["","## Weak high-value traceability","",
"These checks ask whether selected element classes have at least one relationship from each high-value alternative set. Missing a signal means 'review this element', not 'the model is wrong'.","",
"| Path | Type | Missing signal | Acceptable alternatives |","|---|---|---|---|"]
for path,typ,label,alts in weak[:500]:
    lines.append(f"| {path} | {typ} | {label} | {', '.join(alts)} |")
if len(weak)>500: lines.append(f"| … |  | {len(weak)-500} additional findings omitted |  |")

lines += ["","## Findings by type","",
"| Type | Weak-traceability findings |","|---|---:|"]
for typ,count in sorted(by_type.items()):
    lines.append(f"| {typ} | {count} |")

lines += ["","## Interpretation","",
"- Folder placement, body links, and source URLs do not substitute for governed semantic relationships.",
"- Generic market-reference leaves may legitimately remain weakly connected; prioritize product-development chain classes before broad catalog cleanup.",
"- Do not invent relationships merely to reduce this report. Add links only when meaning and evidence support them.",
"- The report is intended to help choose high-value curation work and does not alter lifecycle status or block the build.",
""]
REPORT.write_text("\n".join(lines),encoding="utf-8")
print("orphan and traceability quality reporting")
for k,v in summary.items(): print(f"  {k.replace('_',' ')}: {v}")
for typ,count in sorted(by_type.items()): print(f"  weak {typ}: {count}")
for (typ,label),count in sorted(by_signal.items()): print(f"  missing signal {typ} / {label}: {count}")
for path in orphans: print(f"  isolated: {path}")
print(f"  report: {REPORT.relative_to(ROOT)}")
print("TRACEABILITY REPORT GENERATED (REPORT-ONLY)")
