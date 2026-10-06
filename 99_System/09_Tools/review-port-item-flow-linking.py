#!/usr/bin/env python3
"""Step 9 Port and Item Flow semantic-linking review.

Reviews every first-class Port and Item Flow note and their Local Model
occurrences. Contextual connections/flow roles count as interface semantics;
the review does not manufacture definition-level interfaces/hasFlow links.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"port-item-flow-linking-review.md"

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

def block_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[(?:[^#\]|]+)?#\^([^\]|]+)",v.strip())
    return m.group(1).strip() if m else None

notes={}
texts={}
bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    text=p.read_text(encoding="utf-8",errors="replace")
    d=fm(text)
    if not isinstance(d,dict) or not d.get("type"): continue
    rel=p.relative_to(ROOT).as_posix()
    notes[rel]=d; texts[rel]=text; bybase[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

ports={p:d for p,d in notes.items() if d.get("type")=="Port"}
flows={p:d for p,d in notes.items() if d.get("type")=="Item Flow"}
findings=[]
counts=Counter()

# Definition-level semantic evidence.
for p,d in ports.items():
    counts["ports"]+=1
    owner=bool(vals(d.get("portOf"))) or any(
        p in [resolve(target(x)) for x in vals(nd.get("hasPort"))]
        for nd in notes.values()
    )
    iface=bool(vals(d.get("interfaces")) or vals(d.get("exposes")) or vals(d.get("exposedBy")))
    data=bool(vals(d.get("hasFlow")) or vals(d.get("transmits")) or vals(d.get("receives")) or vals(d.get("exchanges")))
    if owner: counts["ports_with_note_level_owner"]+=1
    if iface: counts["ports_with_note_level_interface_semantics"]+=1
    if data: counts["ports_with_note_level_flow_semantics"]+=1

for p,d in flows.items():
    counts["item_flows"]+=1
    owner=bool(vals(d.get("flowOf")))
    usage=False
    for q,qd in ports.items():
        for fld in ("hasFlow","transmits","receives","exchanges"):
            if p in [resolve(target(x)) for x in vals(qd.get(fld))]:
                usage=True
    if owner: counts["item_flows_with_note_level_owner"]+=1
    if usage: counts["item_flows_with_note_level_port_use"]+=1

# Parse Local Model enough to connect endpoint definitions -> connections -> flows.
START=re.compile(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->")
endpoint_occ=defaultdict(list)  # definition path -> [(owner, token, part)]
flow_occ=defaultdict(list)      # definition path -> [(owner, token, conn, roleA, roleB)]
connections=[]

for owner,text in texts.items():
    m=START.search(text)
    if not m: continue
    body=m.group(1)
    lines=body.splitlines()
    section=None
    current=None
    records=[]
    parent_conn=None
    for line in lines:
        sm=re.match(r"^###\s+(Part Occurrences|Local Interfaces|Connections)\s*$",line)
        if sm:
            section=sm.group(1); current=None; continue
        hm=re.match(r"^(#{4,5})\s+(.+?)\s*$",line)
        if hm:
            level=len(hm.group(1))
            if level==5:
                kind="flow"
            elif section=="Part Occurrences":
                kind="part"
            elif section=="Local Interfaces":
                kind="endpoint"
            elif section=="Connections":
                kind="connection"
            else:
                kind=None
            current={"kind":kind,"heading":hm.group(2),"fields":{},"token":None,"parent_conn":parent_conn}
            records.append(current)
            continue
        if current:
            f=re.match(r"^-\s+([A-Za-z][A-Za-z0-9]*):\s*(.*?)\s*$",line)
            if f:
                current["fields"][f.group(1)]=f.group(2); continue
            b=re.match(r"^\^((?:part|ep|conn|flow)-[0-9]{17}[a-z-]{13})\s*$",line)
            if b:
                current["token"]=b.group(1)
                if current["kind"]=="connection": parent_conn=current["token"]
                if current["kind"]=="flow": current["parent_conn"]=parent_conn

    bytoken={r["token"]:r for r in records if r.get("token")}
    for r in records:
        kind=r.get("kind"); fields=r.get("fields",{}); tok=r.get("token")
        if kind=="endpoint":
            dp=resolve(target(fields.get("definition")))
            if dp:
                endpoint_occ[dp].append((owner,tok,block_target(fields.get("part"))))
        elif kind=="connection":
            a=block_target(fields.get("endpointA")); b=block_target(fields.get("endpointB"))
            connections.append((owner,tok,a,b,bytoken))
        elif kind=="flow":
            dp=resolve(target(fields.get("definition")))
            if dp:
                flow_occ[dp].append((owner,tok,r.get("parent_conn"),fields.get("endpointA"),fields.get("endpointB")))

# Index which endpoint occurrence tokens participate in connections.
connected_eps=defaultdict(int)
for owner,ctok,a,b,bytoken in connections:
    if a: connected_eps[(owner,a)]+=1
    if b: connected_eps[(owner,b)]+=1

for p,d in sorted(ports.items()):
    occs=endpoint_occ.get(p,[])
    counts["port_endpoint_occurrences"]+=len(occs)
    if occs: counts["ports_with_local_model_use"]+=1
    else:
        # A Port with no note-level semantics and no local occurrence is a true dead end.
        direct=bool(vals(d.get("portOf")) or vals(d.get("interfaces")) or vals(d.get("exposes")) or
                    vals(d.get("exposedBy")) or vals(d.get("hasFlow")) or vals(d.get("transmits")) or
                    vals(d.get("receives")) or vals(d.get("exchanges")))
        if not direct:
            findings.append((p,"port-semantic-dead-end","Port has neither governed note-level interaction/ownership semantics nor Local Model occurrence use."))
    for owner,tok,part in occs:
        if connected_eps[(owner,tok)]==0:
            findings.append((p,"unused-endpoint-occurrence",f"{tok} in {owner} is not connected."))
    # Flat occurrence connections are sufficient interface meaning; no exposes required.
    if vals(d.get("exposes")) or vals(d.get("exposedBy")):
        counts["ports_with_exposure_semantics"]+=1

for p,d in sorted(flows.items()):
    occs=flow_occ.get(p,[])
    counts["flow_occurrences"]+=len(occs)
    if occs: counts["item_flows_with_local_model_use"]+=1
    else:
        direct=False
        if vals(d.get("flowOf")): direct=True
        for q,qd in ports.items():
            if any(p==resolve(target(x)) for fld in ("hasFlow","transmits","receives","exchanges") for x in vals(qd.get(fld))):
                direct=True
        if not direct:
            findings.append((p,"item-flow-semantic-dead-end","Item Flow has neither governed Port relationship nor Local Model flow occurrence."))
    for owner,tok,conn,a,b in occs:
        if not conn:
            findings.append((p,"flow-without-connection",f"{tok} in {owner} has no parent connection."))
        if (a,b) not in {("transmit","receive"),("receive","transmit"),("exchange","exchange")}:
            findings.append((p,"flow-role-semantic-gap",f"{tok} in {owner} roles are {a}/{b}; review direction semantics."))

# Every Local Model connection should have endpoint definitions that resolve to Ports.
for owner,ctok,a,b,bytoken in connections:
    for label,tok in (("A",a),("B",b)):
        r=bytoken.get(tok)
        if not r:
            findings.append((owner,"connection-endpoint-missing",f"{ctok} endpoint {label} cannot be found."))
            continue
        dp=resolve(target(r.get("fields",{}).get("definition")))
        if not dp or dp not in ports:
            findings.append((owner,"connection-endpoint-port-gap",f"{ctok} endpoint {label} does not resolve to a Port definition."))

print("port and item flow linking review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  local connections: {len(connections)}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,occs in sorted(endpoint_occ.items()):
    if p in ports: print(f"  PORT_WHERE_USED {p}: {len(occs)} endpoint occurrence(s)")
for p,occs in sorted(flow_occ.items()):
    if p in flows: print(f"  FLOW_WHERE_USED {p}: {len(occs)} flow occurrence(s)")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=[
"# Port and Item Flow Linking Review","",
"Step 9 whole-vault review of first-class Ports and Item Flows, including ownership, interaction/exposure, data-direction semantics, and Local Model occurrence use.","",
"## Summary","",
"| Metric | Count |","|---|---:|",
]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| local connections | {len(connections)} |",f"| findings | {len(findings)} |","","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Port where-used","",
"| Port | Endpoint occurrences |","|---|---:|"]
for p,occs in sorted(endpoint_occ.items()):
    if p in ports: lines.append(f"| {p} | {len(occs)} |")
lines += ["","## Item Flow where-used","",
"| Item Flow | Flow occurrences |","|---|---:|"]
for p,occs in sorted(flow_occ.items()):
    if p in flows: lines.append(f"| {p} | {len(occs)} |")
lines += ["","## Interpretation","",
"- A Local Model endpoint occurrence connected to another endpoint is valid contextual interface semantics; a duplicate definition-level interfaces relationship is not required.",
"- Exposure relationships are needed only when an outer/boundary Port exposes an inner Port. The current flat BMID integration model has no such hierarchy, so no exposes/exposedBy link is expected.",
"- Local Model flow occurrences provide contextual transmits/receives direction. Duplicating those roles as definition-level Port transmits/receives relationships would incorrectly globalize context-specific direction.",
"- hasFlow/flowOf is definition-level ownership, not a requirement for a reusable Item Flow whose authoritative use is contextual under a Local Model connection.",
"- Semantic dead ends are reported only when neither valid note-level semantics nor occurrence use exists.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("PORT AND ITEM FLOW LINKING REVIEW PASSED")
