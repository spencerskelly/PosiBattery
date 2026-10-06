#!/usr/bin/env python3
"""Step 23 product-to-market ecosystem relationship review.

Validates product attribution, commercial offering/channel links, technology
provenance, rebrands, integrations, and offered-together context. Missing
market attribution is reported for review; sparse catalog leaves are resolved
in Step 24 rather than force-linked here.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"product-market-ecosystem-review.md"

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
    t=p.read_text(encoding="utf-8",errors="replace")
    d=fm(t)
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

def links(p,field):
    out=[]
    for raw in vals(notes[p].get(field)):
        q=resolve(target(raw))
        if q: out.append(q)
    return out

product_notes={p:d for p,d in notes.items()
               if p.startswith("10_Products/") and d.get("type")=="Object"}
concrete={p:d for p,d in product_notes.items() if d.get("abstract") is not True}
abstract={p:d for p,d in product_notes.items() if d.get("abstract") is True}

orgs={p:d for p,d in notes.items()
      if d.get("type")=="Organization"
      or (d.get("type")=="Info" and "organization" in {str(x) for x in vals(d.get("tags"))}
          and "business-role" not in {str(x) for x in vals(d.get("tags"))})}

counts=Counter(); findings=[]; prompts=[]; rows=[]
counts["product_objects"]=len(product_notes)
counts["concrete_product_objects"]=len(concrete)
counts["abstract_product_objects"]=len(abstract)

paired=[
 ("madeBy","makes"),("offeredBy","offers"),("poweredBy","powers"),
 ("rebrandOf","rebrandedAs"),
]
symmetric=["offeredWith","integratesWith"]

for p,d in sorted(product_notes.items()):
    if links(p,"madeBy"): counts["products_with_madeBy"]+=1
    if links(p,"offeredBy"): counts["products_with_offeredBy"]+=1
    if links(p,"poweredBy"): counts["products_with_poweredBy"]+=1
    if links(p,"rebrandOf"): counts["products_with_rebrandOf"]+=1
    if links(p,"offeredWith"): counts["products_with_offeredWith"]+=1
    if links(p,"integratesWith"): counts["products_with_integratesWith"]+=1

    if p in concrete and not (links(p,"madeBy") or links(p,"offeredBy")):
        counts["concrete_products_without_maker_or_offerer"]+=1
        prompts.append((p,"market-attribution-review","Concrete product has neither madeBy nor offeredBy; Step 24 should decide whether it is an intentional sparse reference leaf or needs evidence-backed attribution."))

    for field,inv in paired:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,f"unresolved-{field}",str(raw))); continue
            if p not in set(links(q,inv)):
                findings.append((p,f"{field}-inverse",f"{Path(q).stem} lacks reciprocal {inv}."))
            rows.append((p,field,q,notes[q].get("type")))
            counts[f"{field}_assertions"]+=1

            if field in {"madeBy","offeredBy","poweredBy"} and q not in orgs:
                findings.append((p,f"{field}-endpoint",f"{Path(q).stem} is not an Organization/legacy organization identity."))
            if field=="rebrandOf" and notes[q].get("type")!="Object":
                findings.append((p,"rebrandOf-endpoint",f"{Path(q).stem} is not Object."))

    for field in symmetric:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,f"unresolved-{field}",str(raw))); continue
            if p not in set(links(q,field)):
                findings.append((p,f"{field}-mirror",f"{Path(q).stem} lacks mirrored {field}."))
            rows.append((p,field,q,notes[q].get("type")))
            counts[f"{field}_assertions"]+=1
            if field=="offeredWith" and notes[q].get("type")!="Object":
                findings.append((p,"offeredWith-endpoint",f"{Path(q).stem} is not Object."))
            if field=="integratesWith" and notes[q].get("type") not in {"Object","Info","Organization"}:
                findings.append((p,"integratesWith-endpoint",f"{Path(q).stem} has unsupported type {notes[q].get('type')}."))

# Organization-side supply/channel/private-label relationships materially place
# products in market context even when they do not point directly at a product.
for p,d in sorted(orgs.items()):
    for field,inv in [
        ("supplierOf","suppliedBy"),("distributedBy","distributorOf"),
        ("privateLabelFor","privateLabelledBy"),("partnerOf","partnerOf")
    ]:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,f"unresolved-{field}",str(raw))); continue
            if q not in orgs:
                findings.append((p,f"{field}-endpoint",f"{Path(q).stem} is not an organization identity.")); continue
            if p not in set(links(q,inv)):
                findings.append((p,f"{field}-inverse",f"{Path(q).stem} lacks reciprocal/mirror {inv}."))
            counts[f"organization_{field}_assertions"]+=1

# Customer/environment context: count, but do not require, strong behavior routes.
customer_needs={p for p,d in notes.items()
                if d.get("type")=="Use Case"
                and (d.get("subtype")=="why" or "customer-need" in {str(x) for x in vals(d.get("tags"))})}
need_functions=set()
for q in customer_needs:
    for x in links(q,"realizedBy"):
        if notes[x].get("type")=="Function": need_functions.add(x)

for p,d in concrete.items():
    performed=set(links(p,"performs"))
    if performed & need_functions:
        counts["concrete_products_with_direct_customer_need_behavior_route"]+=1
    option_route=False
    for q in links(p,"offeredWith"):
        if set(links(q,"performs")) & need_functions:
            option_route=True; break
    if option_route:
        counts["concrete_products_with_offeredWith_customer_need_route"]+=1

# Distinctions worth continuously protecting.
for p,d in concrete.items():
    makers=set(links(p,"madeBy"))
    offerers=set(links(p,"offeredBy"))
    if makers and offerers and makers != offerers:
        counts["products_distinguishing_maker_and_offerer"]+=1
    if links(p,"poweredBy") and not makers:
        counts["poweredBy_without_manufacturer_claim"]+=1

print("product market ecosystem review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
print(f"  review_prompts: {len(prompts)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,k,msg in prompts: print(f"  REVIEW {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Product-to-Market Ecosystem Review","",
"Step 23 reviews commercial/ecosystem semantics without treating them as product architecture.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |",f"| review_prompts | {len(prompts)} |",
"","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Step 24 attribution queue","",
"| Path | Kind | Detail |","|---|---|---|"]
if prompts:
    for p,k,msg in prompts: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Semantic boundaries","",
"- madeBy/makes identifies maker/manufacturer identity; offeredBy/offers identifies commercial/channel availability and must not be promoted to maker identity without evidence.",
"- poweredBy/powers records a named technology/platform source and does not prove physical manufacturing.",
"- rebrandOf/rebrandedAs is a commercial identity relationship between real products and is not copyOf or subtypeOf.",
"- offeredWith is market/configuration/bundle context. It does not mean hasPart and does not imply the option is present on every unit.",
"- integratesWith is compatibility/integration context and does not by itself imply interfaces, composition, or implementation ownership.",
"- supplierOf/distributedBy/privateLabelFor/partnerOf describe organization ecosystem context and remain distinct from product architecture.",
"- Customer-need routes through performs are stronger than routes through offeredWith; option context must remain visibly weaker.",
"- Missing maker/offerer attribution on a concrete catalog note is not auto-fixed. Step 24 will classify legitimate sparse reference leaves versus accidental gaps.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("PRODUCT MARKET ECOSYSTEM REVIEW PASSED")
