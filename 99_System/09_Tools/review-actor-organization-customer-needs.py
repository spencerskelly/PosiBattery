#!/usr/bin/env python3
"""Step 22 Actor, Organization, and Customer Need semantic review.

Governed Step 22 review entry point.

Validates Actor-to-Need ownership, Customer Need participation, legacy
organization identity treatment, and governed business relationships.
Report-only: no identity/type migration is implied.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"actor-organization-customer-need-review.md"
ORG_DIR_PREFIX="60_Stakeholders and Ecosystem/Organizations/"

ROLE_NAMES={
    "Accessory Maker","Battery Maker","Brand Owner","Charger Maker",
    "Dealer or Distributor","Monitor Maker","Software Vendor","Truck OEM",
}
NON_IDENTITY_ORG_FOLDER={
    "Business Relationship Ledger","Business Relationship Vocabulary",
    "Industrial Battery Supply and Private-Label Relationships",
    "Offerings by Organization",
    "Products Offered or Promoted with Industrial Batteries",
}

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
    notes[rel]=d; bodies[rel]=t
    bybase[p.stem].append(rel)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

counts=Counter(); findings=[]

actors={p:d for p,d in notes.items() if d.get("type")=="Actor"}
customer_needs={p:d for p,d in notes.items()
                if d.get("type")=="Use Case"
                and (d.get("subtype")=="why" or "customer-need" in {str(x) for x in vals(d.get("tags"))})}

typed_orgs={p:d for p,d in notes.items() if d.get("type")=="Organization"}
legacy_org_like={}
role_notes={}
org_folder_other={}
for p,d in notes.items():
    if not p.startswith(ORG_DIR_PREFIX): continue
    tags={str(x) for x in vals(d.get("tags"))}
    stem=Path(p).stem
    if stem in ROLE_NAMES or "business-role" in tags:
        role_notes[p]=d
    elif stem in NON_IDENTITY_ORG_FOLDER:
        org_folder_other[p]=d
    elif d.get("type")=="Organization" or (d.get("type")=="Info" and "organization" in tags):
        legacy_org_like[p]=d
    else:
        org_folder_other[p]=d

org_identities=dict(typed_orgs)
org_identities.update(legacy_org_like)

counts["actors"]=len(actors)
counts["customer_needs"]=len(customer_needs)
counts["typed_organizations"]=len(typed_orgs)
counts["legacy_info_organization_identities"]=sum(1 for p in legacy_org_like if notes[p].get("type")=="Info")
counts["organization_identities_total"]=len(org_identities)
counts["business_role_notes"]=len(role_notes)
counts["organization_folder_nonidentity_notes"]=len(org_folder_other)

for p,d in sorted({**actors,**org_identities}.items()):
    for raw in vals(d.get("hasNeed")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-hasNeed",str(raw))); continue
        if q not in customer_needs:
            findings.append((p,"hasNeed-non-customer-need",f"{Path(q).stem}: {notes[q].get('type')}/{notes[q].get('subtype')}")); continue
        inverse=set(resolve(target(x)) for x in vals(notes[q].get("needOf")))
        if p not in inverse:
            findings.append((p,"hasNeed-inverse",f"{Path(q).stem} lacks needOf back to {Path(p).stem}."))
        if p in actors: counts["actor_need_pairs"]+=1
        else: counts["organization_need_pairs"]+=1

for q,d in sorted(customer_needs.items()):
    holders=[]
    participants=set(resolve(target(x)) for x in vals(d.get("participants")))
    for raw in vals(d.get("needOf")):
        p=resolve(target(raw))
        if not p:
            findings.append((q,"unresolved-needOf",str(raw))); continue
        if p not in actors and p not in org_identities:
            findings.append((q,"needOf-invalid-holder",f"{Path(p).stem}: {notes[p].get('type')}")); continue
        holders.append(p)
        if q not in set(resolve(target(x)) for x in vals(notes[p].get("hasNeed"))):
            findings.append((q,"needOf-inverse",f"{Path(p).stem} lacks hasNeed back to {Path(q).stem}."))
        if p not in participants:
            findings.append((q,"need-holder-not-participant",f"{Path(p).stem} owns need but is absent from participants."))
    if holders:
        counts["customer_needs_with_holder"]+=1
    else:
        findings.append((q,"customer-need-no-holder","Customer Need has no Actor/Organization need owner."))
    if vals(d.get("realizedBy")):
        counts["customer_needs_with_realizedBy"]+=1
    else:
        findings.append((q,"customer-need-no-realization","Customer Need lacks realizedBy."))

for p,d in sorted(actors.items()):
    hn=vals(d.get("hasNeed"))
    if hn:
        counts["actors_with_needs"]+=1
    elif vals(d.get("supertypeOf")):
        counts["generic_actors_without_direct_needs"]+=1
    else:
        findings.append((p,"actor-no-need-context","Actor has neither hasNeed nor specialization context."))
    forbidden=set(d).intersection({
        "makes","offers","supplierOf","distributedBy","subsidiaryOf","parentOf",
        "partnerOf","integratesWith","madeBy","offeredBy"
    })
    if forbidden:
        findings.append((p,"actor-business-structure-link",f"Actor carries organization/product business fields: {sorted(forbidden)}"))

paired=[
 ("playsRole","rolePlayedBy"),("makes","madeBy"),("offers","offeredBy"),
 ("supplierOf","suppliedBy"),("distributedBy","distributorOf"),
 ("subsidiaryOf","parentOf"),("successorOf","predecessorOf"),
 ("privateLabelFor","privateLabelledBy"),("poweredBy","powers"),
]
symmetric=["partnerOf","integratesWith"]
business_assertions=0

def resolved_set(p,field):
    return set(q for raw in vals(notes[p].get(field)) if (q:=resolve(target(raw))))

for p,d in sorted(notes.items()):
    for field,inv in paired:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,"unresolved-business-link",f"{field}: {raw}")); continue
            business_assertions+=1
            counts[f"assertions_{field}"]+=1
            if p not in resolved_set(q,inv):
                findings.append((p,"business-inverse",f"{field} -> {Path(q).stem} lacks {inv}."))

            if field=="playsRole":
                if p not in org_identities or q not in role_notes:
                    findings.append((p,"playsRole-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))
            elif field in {"makes","offers"}:
                if p not in org_identities or notes[q].get("type")!="Object":
                    findings.append((p,f"{field}-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))
            elif field in {"supplierOf","distributedBy","subsidiaryOf","successorOf","privateLabelFor"}:
                if p not in org_identities or q not in org_identities:
                    findings.append((p,f"{field}-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))
            elif field=="poweredBy":
                if notes[p].get("type")!="Object" or q not in org_identities:
                    findings.append((p,"poweredBy-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))

    for field in symmetric:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,"unresolved-business-link",f"{field}: {raw}")); continue
            business_assertions+=1
            counts[f"assertions_{field}"]+=1
            if p not in resolved_set(q,field):
                findings.append((p,"business-symmetric-mirror",f"{field} -> {Path(q).stem} lacks mirror."))
            if field=="partnerOf" and (p not in org_identities or q not in org_identities):
                findings.append((p,"partnerOf-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))
            if field=="integratesWith":
                allowed=lambda x: x in org_identities or notes[x].get("type")=="Object"
                if not allowed(p) or not allowed(q):
                    findings.append((p,"integratesWith-endpoint",f"{Path(p).stem} -> {Path(q).stem}"))

counts["business_relationship_assertions_reviewed"]=business_assertions

vocab=next((p for p in notes if Path(p).stem=="Business Relationship Vocabulary"),None)
ledger=next((p for p in notes if Path(p).stem=="Business Relationship Ledger"),None)
if vocab:
    body=bodies[vocab]
    if "relationships.yaml 1.35 has no organization relationships" in body or "**Status:** provisional" in body:
        findings.append((vocab,"stale-business-governance","Live vocabulary still describes governed business predicates as provisional."))
    else:
        counts["business_vocabulary_governance_aligned"]=1
if ledger:
    if "Ledger of every provisional business link" in bodies[ledger]:
        findings.append((ledger,"stale-business-ledger","Live ledger still calls all business links provisional."))
    else:
        counts["business_ledger_governance_aligned"]=1

print("actor organization customer need review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Actor, Organization, and Customer Need Review","",
"Step 22 review of stakeholder need ownership and the governed business-relationship network.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- Customer Need is represented as Use Case subtype why; hasNeed/needOf identifies who holds the need, while participants remains scenario participation.",
"- The generic Vehicle Operator Actor may remain without direct hasNeed when its specialized Forklift Operator and GSE Operator roles carry the specific need ownership.",
"- No customer organization is invented merely because customer Actors exist. Actor roles and institutional Organizations are distinct concepts.",
"- Existing organization identities remain legacy Info notes where already established. relationships.yaml 1.36 explicitly supports those legacy organization endpoints; mass type migration is not required for semantic completeness.",
"- Business relationships such as makes, offers, supplierOf, distributedBy, subsidiaryOf, partnerOf, integratesWith, and playsRole are governed relationship semantics and must retain synchronized inverses or mirrors.",
"- playsRole is for durable organization identity in the market. Supplier, channel, partner, integration, and competition context must not be flattened into permanent global roles.",
"- madeBy and offeredBy remain distinct: maker identity is not inferred from brand or channel availability.",
"- poweredBy is technology provenance and does not assert physical manufacture.",
"- Customer and business context does not substitute for product architecture: organization-to-product commercial links do not imply hasPart, hasDesign, performs, or other engineering structure.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("ACTOR ORGANIZATION CUSTOMER NEED REVIEW PASSED")
