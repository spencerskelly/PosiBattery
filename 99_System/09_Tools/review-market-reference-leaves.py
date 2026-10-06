#!/usr/bin/env python3
"""Step 24 market/reference catalog leaf review.

Classifies concrete product notes with no direct engineering-entry relationships
as legitimate reference leaves only when identity, market attribution, and
provenance remain sound. It also detects accidental active-engineering use so
sparse catalog content is not incorrectly exempted.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"market-reference-leaf-review.md"
DISP=ROOT/"80_Decisions and Planning"/"Semantic Linking Review Dispositions 0.1.yaml"

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

notes={}; texts={}; bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; texts[rel]=t
    bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

# Relationship fields needed to detect incoming contextual reuse.
REL=ROOT/"99_System"/"03_Schemas"/"relationships.yaml"
rel=yaml.safe_load(REL.read_text(encoding="utf-8")) or {}
fields=set()
for rec in rel.get("paired",[])+rel.get("temporaryPairs",[]):
    fields.update(x for x in (rec.get("forward"),rec.get("inverse")) if x)
for rec in rel.get("symmetric",[])+rel.get("oneWay",[]):
    if rec.get("field"): fields.add(rec["field"])

incoming=defaultdict(list)
outgoing=defaultdict(list)
for p,d in notes.items():
    for field in fields:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q: continue
            outgoing[p].append((field,q))
            incoming[q].append((field,p))
    m=re.search(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->",texts[p])
    if m:
        for name in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1)):
            q=resolve(name.strip())
            if q:
                outgoing[p].append(("localModelDefinition",q))
                incoming[q].append(("localModelDefinition",p))

products={p:d for p,d in notes.items() if p.startswith("10_Products/") and d.get("type")=="Object"}
concrete={p:d for p,d in products.items() if d.get("abstract") is not True}
abstract={p:d for p,d in products.items() if d.get("abstract") is True}

entry_fields={"performs","hasDesign","applies","appliesTo","satisfies","satisfiedBy","hasPort","hasPart","hasState"}
market_fields={"madeBy","offeredBy","poweredBy","rebrandOf","offeredWith","integratesWith"}
baseline_identity_fields={"subtypeOf","supertypeOf","madeBy","offeredBy","describedBy","supportedBy","contradictedBy"}
active_incoming_fields={
    "participants","verifies","satisfies","appliesTo","hasPart","hasDesign",
    "performs","localModelDefinition"
}

counts=Counter(); findings=[]; rows=[]
thin=[]

for p,d in sorted(concrete.items()):
    counts["concrete_products"]+=1
    entries=sorted(f for f in entry_fields if vals(d.get(f)))
    if entries:
        counts["concrete_products_with_engineering_entry"]+=1
        continue

    thin.append(p)
    counts["thin_reference_candidates"]+=1

    family=bool(vals(d.get("subtypeOf")))
    market=bool(vals(d.get("madeBy")) or vals(d.get("offeredBy")))
    evidence=bool(re.search(r"https?://",texts[p],re.I) or vals(d.get("describedBy")) or vals(d.get("supportedBy")))
    if family: counts["thin_with_family_identity"]+=1
    if market: counts["thin_with_market_attribution"]+=1
    if evidence: counts["thin_with_provenance_signal"]+=1

    if not family:
        findings.append((p,"reference-leaf-no-family","Concrete reference leaf lacks subtypeOf family/category identity."))
    if not market:
        findings.append((p,"reference-leaf-no-market-attribution","Concrete reference leaf lacks madeBy/offeredBy context."))
    if not evidence:
        findings.append((p,"reference-leaf-no-provenance","Concrete reference leaf lacks direct URL or governed describedBy/supportedBy provenance."))

    active_consumers=[]
    for field,src in incoming[p]:
        if field in active_incoming_fields:
            active_consumers.append((field,src))
    if active_consumers:
        counts["thin_with_active_consumer_signal"]+=1
        findings.append((p,"reference-leaf-active-consumer",
                         "; ".join(f"{field} from {src}" for field,src in active_consumers[:8])))

    extra=[]
    for field,q in outgoing[p]+incoming[p]:
        if field not in baseline_identity_fields and field not in {"subtypeOf","supertypeOf"}:
            extra.append((field,q))

    if extra:
        counts["thin_reused_in_market_or_reference_context"]+=1
        cls="reused_reference_leaf"
    else:
        counts["thin_intentionally_sparse"]+=1
        cls="intentionally_sparse_reference_leaf"

    present_fields={field for field,_ in outgoing[p]} | {field for field,_ in incoming[p]}
    object_dims={
        "upstream":{"subtypeOf","supertypeOf","partOf","hasPart","offeredBy","madeBy","poweredBy","suppliedBy","rebrandOf","applies","drivenBy","describedBy","supportedBy"},
        "downstream":{"hasPart","hasPort","performs","hasDesign","hasState","satisfies"},
        "ownership_use":{"partOf","hasPart","performs","hasDesign","participants","localModelDefinition"},
        "evidence":{"describedBy","supportedBy","contradictedBy"},
    }
    missing_dims=[dim for dim,alts in object_dims.items() if not (present_fields & alts)]
    rows.append((p,cls,len(extra),family,market,evidence,missing_dims))

counts["abstract_product_definitions"]=len(abstract)
counts["product_objects"]=len(products)

# Step 24 formal review classifications are stored only for the thin leaf set.
disp=yaml.safe_load(DISP.read_text(encoding="utf-8")) or {}
records=disp.get("records") or {}
reviewed_thin=0
bad_registry=[]
for p in thin:
    rec=records.get(p)
    if not rec:
        continue
    reviewed_thin+=1
    if rec.get("classification")!="reference_content":
        bad_registry.append((p,rec.get("classification")))
counts["thin_with_reference_content_registry_classification"]=reviewed_thin
for p,cls in bad_registry:
    findings.append((p,"reference-leaf-registry-classification",f"Expected reference_content, found {cls!r}."))

print("market reference leaf review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,cls,n,fam,mkt,ev,missing in rows:
    print(f"  LEAF {cls}: {p} extra_context={n} family={fam} market={mkt} evidence={ev} missing={','.join(missing) or 'none'}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Market / Reference Catalog Leaf Review","",
"Step 24 classifies concrete product notes that intentionally stop before downstream engineering detail.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Reference leaves","",
"| Path | Classification | Extra contextual relationships | Family identity | Market attribution | Provenance | Missing Step 2 dimensions |",
"|---|---|---:|---|---|---|---|"]
for p,cls,n,fam,mkt,ev,missing in rows:
    lines.append(f"| {p} | {cls} | {n} | {fam} | {mkt} | {ev} | {', '.join(missing) or 'none'} |")
if not rows: lines.append("| _None_ | | | | | | |")

lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")

lines += ["","## Interpretation","",
"- A reference leaf is not an orphan. It must still retain product-family identity, market attribution, and appropriate provenance.",
"- Downstream Function/Design/Requirement/Verification links are intentionally absent for comparison/catalog products until engineering adopts them.",
"- A leaf may still be reused in market context through offeredWith, integratesWith, rebrand, technology provenance, or other non-engineering relationships.",
"- A one-way active-engineering consumer such as Use Case participants, Verification targeting, or Local Model definition use disqualifies an Object from automatic reference-leaf treatment and becomes a finding.",
"- EXC-REFERENCE-LEAF is the controlled semantic-linking explanation for absent engineering-chain dimensions on these reviewed notes.",
"- Step 25 remains responsible for true whole-vault orphans; Step 24 does not add artificial links merely to improve connectivity.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("MARKET REFERENCE LEAF REVIEW PASSED")
