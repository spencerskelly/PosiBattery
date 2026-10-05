#!/usr/bin/env python3
"""Step 6 product identity/family semantic-linking review.

Report-only. Reviews all model Objects in 10_Products for product identity,
specialization/family structure, maker/offering context, and engineering entry
points. It does not invent product relationships.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
PRODUCTS=ROOT/"10_Products"
REPORT=ROOT/"product-linking-review.md"

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
for p in PRODUCTS.rglob("*.md"):
    d=fm(p.read_text(encoding="utf-8",errors="replace"))
    if d.get("type")!="Object": continue
    notes[p.relative_to(ROOT).as_posix()]=d

bybase=defaultdict(list)
for p in notes: bybase[Path(p).stem].append(p)
def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else: ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

incoming=defaultdict(list)
for p,d in notes.items():
    for field in ("subtypeOf","supertypeOf"):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if q: incoming[q].append((field,p))

counts=Counter()
findings=[]
thin=[]
classes={}
entry_fields={"performs","hasDesign","applies","appliesTo","satisfies","satisfiedBy","hasPort","hasPart","hasState"}

for p,d in sorted(notes.items()):
    abstract=bool(d.get("abstract",False))
    pc=d.get("productClass")
    sub=[target(x) for x in vals(d.get("subtypeOf")) if target(x)]
    sup=[target(x) for x in vals(d.get("supertypeOf")) if target(x)]
    maker=[target(x) for x in vals(d.get("madeBy")) if target(x)]
    offer=[target(x) for x in vals(d.get("offeredBy")) if target(x)]
    entries=sorted(f for f in entry_fields if vals(d.get(f)))
    counts["objects"]+=1
    counts["abstract" if abstract else "concrete"]+=1
    if pc: counts[f"productClass:{pc}"]+=1

    # Current-use completeness classification for Step 6.
    active = (Path(p).stem=="PosiCharge BMID")
    if active:
        cls="active_engineering"
    elif abstract:
        cls="engineering_support"
    else:
        cls="reference_content"
    classes[p]=cls
    counts[f"class:{cls}"]+=1

    if abstract and not (sub or sup):
        findings.append((p,"family-isolated","Abstract product/category has neither subtypeOf nor supertypeOf."))
    if not abstract and not sub:
        findings.append((p,"concrete-no-family","Concrete product offering has no subtypeOf family/category link."))

    if pc=="product-family":
        if not abstract: findings.append((p,"productClass-mismatch","product-family is expected to be abstract in the current pattern."))
        if not sup: findings.append((p,"product-family-no-members","Explicit product-family has no supertypeOf members."))
    if pc=="product-variant" and not sub:
        findings.append((p,"variant-no-family","Explicit product-variant has no subtypeOf family."))
    if pc=="product-category" and not abstract:
        findings.append((p,"productClass-mismatch","product-category is expected to be abstract in the current pattern."))

    # A concrete commercial offering normally has a maker or offering organization.
    tags=set(str(x) for x in vals(d.get("tags")))
    if not abstract and "commercial-product" in tags and not (maker or offer):
        findings.append((p,"commercial-no-org","Commercial product has neither madeBy nor offeredBy."))

    # Active product family must have an engineering entry into behavior/design and
    # product requirement/context traceability.
    if active:
        if not (d.get("performs") or d.get("hasDesign")):
            findings.append((p,"active-no-behavior-design","Active product family has no performs/hasDesign entry point."))
        if not (d.get("applies") or d.get("satisfies") or d.get("satisfiedBy")):
            findings.append((p,"active-no-requirement-context","Active product family has no requirement/context entry path."))

    if not abstract and not entries:
        thin.append(p)

# Check exact specialization reciprocity inside Products.
for p,d in notes.items():
    for raw in vals(d.get("subtypeOf")):
        name=target(raw); q=resolve(name)
        if not q: continue
        backs={target(x) for x in vals(notes[q].get("supertypeOf"))}
        if Path(p).stem not in backs:
            findings.append((p,"specialization-inverse",f"subtypeOf {name} lacks reciprocal supertypeOf."))
    for raw in vals(d.get("supertypeOf")):
        name=target(raw); q=resolve(name)
        if not q: continue
        backs={target(x) for x in vals(notes[q].get("subtypeOf"))}
        if Path(p).stem not in backs:
            findings.append((p,"specialization-inverse",f"supertypeOf {name} lacks reciprocal subtypeOf."))

print("product identity and family linking review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
print(f"  thin concrete reference offerings: {len(thin)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p in thin: print(f"  THIN_REFERENCE: {p}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=[
"# Product Identity and Family Linking Review","",
"Step 6 report-only whole-domain review of Object notes under `10_Products`. Product/category structure is reviewed independently from later architecture/behavior detail passes.","",
"## Summary","",
"| Metric | Count |","|---|---:|",
]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [
f"| blocking/review findings | {len(findings)} |",
f"| concrete reference offerings with no direct engineering entry field | {len(thin)} |","",
"## Findings","",
"| Path | Kind | Detail |","|---|---|---|",
]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Thin reference offerings","",
"Concrete reference offerings without direct performs/hasDesign/applies/satisfies/structure entry fields are not automatically defects. They remain valid reference leaves if identity, family, organization/evidence context are sound; later product-development adoption promotes them to a stricter standard.","",
"| Path |","|---|"]
for p in thin[:500]: lines.append(f"| {p} |")
if not thin: lines.append("| _None_ |")
lines += ["","## Classification used for Step 6","",
"- `PosiCharge BMID`: active_engineering because it is the current end-to-end product-development family with Requirement/Function/Design/Verification context.",
"- Abstract product/category Objects: engineering_support unless later product-development use promotes them.",
"- Concrete catalog offerings: reference_content unless later active use promotes them.",
"- This classification is based on current engineering use, not folder placement alone. The folder only defines the review scope.",
"",
"## Interpretation","",
"- A valid product identity should have a defensible family/specialization path unless it is a deliberate root.",
"- Commercial offerings should normally identify a maker/offering organization when the vault claims they are commercial products.",
"- Thin reference leaves do not need artificial behavior/design links.",
"- Active product families do need a meaningful entry into behavior/design and requirement/context.",
"- All existing specialization assertions remain subject to the separate relationship validator.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings:
    raise SystemExit(2)
print("PRODUCT LINKING REVIEW PASSED")
