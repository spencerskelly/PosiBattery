#!/usr/bin/env python3
"""Step 7 product-architecture ownership/composition review.

Reviews reusable Object architecture under 20_Product Architecture, plus the
BMID Local Model boundary, to distinguish definition-level structure from
contextual occurrence structure. Report-only; does not invent relationships.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
ARCH=ROOT/"20_Product Architecture"
REPORT=ROOT/"product-architecture-linking-review.md"

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
texts={}
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d
    texts[rel]=t

bybase=defaultdict(list)
for p in notes: bybase[Path(p).stem].append(p)
def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else: ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

arch_objects={p:d for p,d in notes.items() if p.startswith("20_Product Architecture/") and d.get("type")=="Object"}
findings=[]
counts=Counter()
local_uses=defaultdict(list)

# Gather governed Local Model definition uses vault-wide.
lm_re=re.compile(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->")
for src,text in texts.items():
    m=lm_re.search(text)
    if not m: continue
    for name in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1)):
        q=resolve(name.strip())
        if q: local_uses[q].append(src)

for p,d in sorted(arch_objects.items()):
    counts["architecture_objects"]+=1
    abstract=bool(d.get("abstract",False))
    counts["abstract" if abstract else "concrete"]+=1
    hp=[resolve(target(x)) for x in vals(d.get("hasPart")) if resolve(target(x))]
    po=[resolve(target(x)) for x in vals(d.get("partOf")) if resolve(target(x))]
    hport=[resolve(target(x)) for x in vals(d.get("hasPort")) if resolve(target(x))]
    hdesign=[resolve(target(x)) for x in vals(d.get("hasDesign")) if resolve(target(x))]
    sub=[resolve(target(x)) for x in vals(d.get("subtypeOf")) if resolve(target(x))]
    sup=[resolve(target(x)) for x in vals(d.get("supertypeOf")) if resolve(target(x))]
    if hp: counts["objects_with_hasPart"]+=1
    if po: counts["objects_with_partOf"]+=1
    if hport: counts["objects_with_hasPort"]+=1
    if hdesign: counts["objects_with_hasDesign"]+=1
    if sub or sup: counts["objects_with_specialization"]+=1
    if local_uses.get(p): counts["objects_used_by_local_model"]+=1

    # Every definition-level hasPart must reciprocate with partOf.
    for q in hp:
        backs={resolve(target(x)) for x in vals(notes.get(q,{}).get("partOf")) if resolve(target(x))}
        if p not in backs:
            findings.append((p,"missing-part-inverse",f"hasPart {q} lacks reciprocal partOf"))
    for q in po:
        backs={resolve(target(x)) for x in vals(notes.get(q,{}).get("hasPart")) if resolve(target(x))}
        if p not in backs:
            findings.append((p,"missing-whole-inverse",f"partOf {q} lacks reciprocal hasPart"))

    # Reusable anatomy part should have an owner unless it is an assembly root.
    is_anatomy_part=("truck-part" in vals(d.get("tags")) or "gse-part" in vals(d.get("tags")))
    if is_anatomy_part and not d.get("hasPart") and not po:
        findings.append((p,"architecture-owner-gap","Reusable anatomy part has no partOf owner."))

    # Root assemblies should have useful composition.
    if Path(p).stem in {"Industrial Truck Anatomy","GSE Vehicle Anatomy"} and not hp:
        findings.append((p,"assembly-empty","Architecture root has no definition-level parts."))

    # Local Model definitions should not be duplicated as hasPart solely because
    # they occur in contextual topology. Flag only exact overlap.
    for src in local_uses.get(p,[]):
        src_d=notes.get(src,{})
        src_hp={resolve(target(x)) for x in vals(src_d.get("hasPart")) if resolve(target(x))}
        if p in src_hp:
            findings.append((p,"local-model-duplication",f"Definition is both a Local Model occurrence in {src} and direct hasPart of that context."))

# Review the BMID Local Model integration context explicitly.
lm_path="20_Product Architecture/PosiCharge BMID Product Assembly Local Model.md"
lm_text=texts.get(lm_path,"")
lm_defs=[]
if lm_text:
    m=lm_re.search(lm_text)
    if m:
        lm_defs=[resolve(x.strip()) for x in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1))]
        lm_defs=[x for x in lm_defs if x]
counts["bmid_local_model_definition_uses"]=len(lm_defs)
counts["bmid_local_model_unique_definitions"]=len(set(lm_defs))

# BMID context must describe the product, not claim contextual battery/charger as parts.
lm_d=notes.get(lm_path,{})
if target(next(iter(vals(lm_d.get("describes"))),None))!="PosiCharge BMID":
    findings.append((lm_path,"context-owner-gap","BMID Local Model context does not describe PosiCharge BMID."))
if vals(lm_d.get("hasPart")):
    findings.append((lm_path,"context-hasPart","BMID Local Model context should use occurrences, not hasPart composition."))

expected_context={"PosiCharge BMID","Industrial Traction Battery","Industrial Battery Charger","iBMID - Battery Interaction","iBMID - Charger Communication","BMID Battery Sensing Data","BMID Charger Battery Information"}
actual_names={Path(p).stem for p in set(lm_defs)}
missing=sorted(expected_context-actual_names)
if missing:
    findings.append((lm_path,"local-model-definition-gap","Missing expected reusable definitions: "+", ".join(missing)))

print("product architecture ownership and composition review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=[
"# Product Architecture Ownership and Composition Review","",
"Step 7 report-only review of reusable architecture Objects and the BMID contextual Local Model boundary.","",
"## Summary","",
"| Metric | Count |","|---|---:|",
]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- Industrial Truck Anatomy and GSE Vehicle Anatomy are reusable definition-level assemblies. Their constituent reusable subsystem Objects use hasPart/partOf.",
"- Context-specific BMID integration topology belongs in Local Model records. Battery and charger occurrences are external context and must not become BMID hasPart children.",
"- Local Model definition use is valid where-used context and is deliberately distinct from reusable composition.",
"- hasPort and hasDesign are not required on every reusable architecture Object; add them only where the architecture actually defines an interface or design ownership claim.",
"- No relationship should be added merely because an Object lacks one of the optional architecture relationship dimensions.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("PRODUCT ARCHITECTURE LINKING REVIEW PASSED")
