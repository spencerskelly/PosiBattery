#!/usr/bin/env python3
"""Step 8 Local Model context and occurrence-use review.

Validates every governed Local Model region against local-model.yaml 0.2
semantics relevant to linking completeness. Report-only; no model mutation.
"""
from pathlib import Path
from collections import Counter, defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
SCHEMA=ROOT/"99_System/03_Schemas/local-model.yaml"
REPORT=ROOT/"local-model-linking-review.md"
TOKEN_RE=re.compile(r"^(part|ep|conn|flow)-(\d{17}[a-z-]{13})$")
START_RE=re.compile(r"<!--\s*MDSE:LOCAL-MODEL START(?:\s+schema=(\S+?))?\s*-->")
END_RE=re.compile(r"<!--\s*MDSE:LOCAL-MODEL END\s*-->")

def fm(text):
    if not text.startswith("---\n"): return {}
    e=text.find("\n---",4)
    if e<0: return {}
    try: return yaml.safe_load(text[4:e]) or {}
    except Exception: return {}

def vals(v):
    if v is None: return []
    return v if isinstance(v,list) else [v]

def note_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

def block_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[(?:[^#\]|]+)?#\^([^\]|]+)",v.strip())
    return m.group(1).strip() if m else None

schema=yaml.safe_load(SCHEMA.read_text(encoding="utf-8")) or {}
readable=set(str(x) for x in schema.get("compatibility",{}).get("readableVersions",[]))
writable=str(schema.get("compatibility",{}).get("writableVersion",""))

notes={}
texts={}
bybase=defaultdict(list)
uids=set()
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts: continue
    text=p.read_text(encoding="utf-8",errors="replace")
    d=fm(text)
    rel=p.relative_to(ROOT).as_posix()
    if isinstance(d,dict) and d.get("type"):
        notes[rel]=d
        texts[rel]=text
        bybase[p.stem].append(rel)
        if d.get("uid"): uids.add(str(d.get("uid")))

def resolve(name):
    if not name: return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

def descendants(root):
    # subtypeOf is authored child -> parent; derive concrete descendants transitively.
    children=defaultdict(set)
    for p,d in notes.items():
        for raw in vals(d.get("subtypeOf")):
            q=resolve(note_target(raw))
            if q: children[q].add(p)
    seen=set(); stack=list(children.get(root,set()))
    while stack:
        p=stack.pop()
        if p in seen: continue
        seen.add(p)
        stack.extend(children.get(p,set()))
    return sorted(p for p in seen if not bool(notes.get(p,{}).get("abstract",False)))

findings=[]
counts=Counter()
all_tokens=set()
definition_uses=defaultdict(list)
regions=[]

# Simple parser tailored to canonical local-model Markdown records.
for owner,text in sorted(texts.items()):
    starts=list(START_RE.finditer(text)); ends=list(END_RE.finditer(text))
    if not starts and not ends: continue
    counts["owners_with_local_model"]+=1
    if len(starts)!=1 or len(ends)!=1 or starts[0].start()>ends[0].start():
        findings.append((owner,"marker-structure","Local Model must contain exactly one ordered start/end marker pair."))
        continue
    version=starts[0].group(1)
    counts[f"schema_{version}"]+=1
    if version not in readable:
        findings.append((owner,"schema-version",f"Schema {version} is not readable under local-model.yaml."))
    if version!=writable:
        findings.append((owner,"noncanonical-writer-version",f"Current canonical writer version is {writable}; found {version}."))
    body=text[starts[0].end():ends[0].start()]
    records=[]
    current=None
    current_kind=None
    current_heading=None
    current_parent_conn=None

    lines=body.splitlines()
    for i,line in enumerate(lines):
        hm=re.match(r"^(#{4,5})\s+(.+?)\s*$",line)
        if hm:
            level=len(hm.group(1)); heading=hm.group(2).strip()
            if current and current.get("token") is None:
                findings.append((owner,"missing-local-id",f"Record '{current_heading}' has no native block ID."))
            # h5 is flow nested under most recent h4 connection
            if level==5:
                current_kind="flow"
            else:
                # infer by active section above
                prefix="\n".join(lines[:i])
                sec_matches=list(re.finditer(r"(?m)^###\s+(Part Occurrences|Local Interfaces|Connections)\s*$",prefix))
                sec=sec_matches[-1].group(1) if sec_matches else None
                current_kind={"Part Occurrences":"part","Local Interfaces":"endpoint","Connections":"connection"}.get(sec)
                if current_kind=="connection": current_parent_conn=None
            current={"kind":current_kind,"heading":heading,"fields":{},"token":None,"parent_connection":current_parent_conn}
            records.append(current)
            current_heading=heading
            continue
        if current:
            fm_field=re.match(r"^-\s+([A-Za-z][A-Za-z0-9]*):\s*(.*?)\s*$",line)
            if fm_field:
                current["fields"][fm_field.group(1)]=fm_field.group(2)
                continue
            bm=re.match(r"^\^((?:part|ep|conn|flow)-[0-9]{17}[a-z-]{13})\s*$",line)
            if bm:
                current["token"]=bm.group(1)
                if current["kind"]=="connection": current_parent_conn=current["token"]
                if current["kind"]=="flow": current["parent_connection"]=current_parent_conn

    if current and current.get("token") is None:
        findings.append((owner,"missing-local-id",f"Record '{current_heading}' has no native block ID."))

    bytoken={r.get("token"):r for r in records if r.get("token")}
    regions.append((owner,version,records))
    counts["local_records"]+=len(records)

    # identity/global uniqueness
    for r in records:
        tok=r.get("token")
        if not tok: continue
        if not TOKEN_RE.match(tok):
            findings.append((owner,"token-format",f"{tok} does not match governed local ID format."))
        bare=tok.split("-",1)[1]
        if bare in uids:
            findings.append((owner,"uid-collision",f"{tok} collides with a note UID."))
        if tok in all_tokens:
            findings.append((owner,"duplicate-token",f"{tok} is not globally unique."))
        all_tokens.add(tok)
        counts[f"kind_{r.get('kind')}"]+=1

    for r in records:
        kind=r.get("kind"); fields=r.get("fields",{}); tok=r.get("token")
        defn=resolve(note_target(fields.get("definition"))) if fields.get("definition") else None

        if kind=="part":
            if not defn:
                findings.append((owner,"part-definition",f"{tok} has unresolved/missing Object definition."))
            elif notes[defn].get("type")!="Object":
                findings.append((owner,"part-definition-type",f"{tok} definition is {notes[defn].get('type')}, expected Object."))
            else:
                definition_uses[defn].append((owner,tok,kind))
                usage=fields.get("usage","standard").strip()
                if usage not in {"standard","variant","option"}:
                    findings.append((owner,"part-usage",f"{tok} has invalid usage {usage}."))
                if usage=="standard" and bool(notes[defn].get("abstract",False)):
                    findings.append((owner,"abstract-standard",f"{tok} uses abstract definition {Path(defn).stem} as standard."))
                if usage in {"variant","option"}:
                    cands=descendants(defn)
                    if not cands:
                        findings.append((owner,"variant-no-candidates",f"{tok} {usage} family {Path(defn).stem} has no concrete candidate."))
                    counts["variant_or_option_candidate_total"]+=len(cands)
            if "usage" in fields: counts[f"usage_{fields['usage'].strip()}"]+=1
            else: counts["usage_standard_implicit"]+=1

        elif kind=="endpoint":
            if not defn:
                findings.append((owner,"endpoint-definition",f"{tok} has unresolved/missing Port definition."))
            elif notes[defn].get("type")!="Port":
                findings.append((owner,"endpoint-definition-type",f"{tok} definition is {notes[defn].get('type')}, expected Port."))
            else:
                definition_uses[defn].append((owner,tok,kind))
                usage=fields.get("usage","standard").strip()
                if usage not in {"standard","variant","option"}:
                    findings.append((owner,"endpoint-usage",f"{tok} has invalid usage {usage}."))
                if usage=="standard" and bool(notes[defn].get("abstract",False)):
                    findings.append((owner,"abstract-standard",f"{tok} uses abstract Port {Path(defn).stem} as standard."))
                if usage in {"variant","option"} and not descendants(defn):
                    findings.append((owner,"variant-no-candidates",f"{tok} {usage} Port family has no concrete candidate."))
            part=block_target(fields.get("part")); parent=block_target(fields.get("parent"))
            if part and parent:
                findings.append((owner,"endpoint-owner","Endpoint cannot have both part and parent."))
            if part:
                if part not in bytoken or bytoken[part].get("kind")!="part":
                    findings.append((owner,"endpoint-part-ref",f"{tok} references missing/non-part {part}."))
            if parent:
                if parent not in bytoken or bytoken[parent].get("kind")!="endpoint":
                    findings.append((owner,"endpoint-parent-ref",f"{tok} references missing/non-endpoint {parent}."))
            for fld in ("exposes","equals"):
                if fields.get(fld):
                    bt=block_target(fields[fld])
                    if bt and (bt not in bytoken or bytoken[bt].get("kind")!="endpoint"):
                        findings.append((owner,f"endpoint-{fld}-ref",f"{tok} {fld} references missing/non-endpoint {bt}."))
                    if fld=="equals": findings.append((owner,"temporary-equals",f"{tok} retains temporary equals semantics."))
            if "usage" in fields: counts[f"usage_{fields['usage'].strip()}"]+=1
            else: counts["usage_standard_implicit"]+=1

        elif kind=="connection":
            if "usage" in fields:
                findings.append((owner,"connection-usage",f"{tok} must not carry usage."))
            a=block_target(fields.get("endpointA")); b=block_target(fields.get("endpointB"))
            for label,bt in (("endpointA",a),("endpointB",b)):
                if not bt or bt not in bytoken or bytoken[bt].get("kind")!="endpoint":
                    findings.append((owner,"connection-endpoint",f"{tok} {label} does not resolve to an endpoint."))
            if a and b and a==b:
                findings.append((owner,"connection-self",f"{tok} connects an endpoint to itself."))

        elif kind=="flow":
            if "usage" in fields:
                findings.append((owner,"flow-usage",f"{tok} must not carry usage."))
            if not r.get("parent_connection") or r["parent_connection"] not in bytoken:
                findings.append((owner,"flow-parent",f"{tok} is not nested under a valid connection."))
            if not defn:
                findings.append((owner,"flow-definition",f"{tok} has unresolved/missing Item Flow definition."))
            elif notes[defn].get("type")!="Item Flow":
                findings.append((owner,"flow-definition-type",f"{tok} definition is {notes[defn].get('type')}, expected Item Flow."))
            else:
                definition_uses[defn].append((owner,tok,kind))
            roles={fields.get("endpointA"),fields.get("endpointB")}
            allowed={"transmit","receive","exchange","unspecified"}
            if not fields.get("endpointA") in allowed or not fields.get("endpointB") in allowed:
                findings.append((owner,"flow-role",f"{tok} has invalid endpoint role."))
            if fields.get("endpointA")=="transmit" and fields.get("endpointB")!="receive":
                findings.append((owner,"flow-direction",f"{tok} transmit on A should pair with receive on B for this directed flow."))
            if fields.get("endpointB")=="transmit" and fields.get("endpointA")!="receive":
                findings.append((owner,"flow-direction",f"{tok} transmit on B should pair with receive on A for this directed flow."))

    # contextual topology must not be duplicated as note-level composition on owner.
    owner_fm=notes.get(owner,{})
    owner_parts={resolve(note_target(x)) for x in vals(owner_fm.get("hasPart")) if resolve(note_target(x))}
    local_part_defs={resolve(note_target(r["fields"].get("definition"))) for r in records if r.get("kind")=="part" and r["fields"].get("definition")}
    overlap=sorted(x for x in owner_parts & local_part_defs if x)
    if overlap:
        findings.append((owner,"composition-duplication","Local part definitions also persisted as owner hasPart: "+", ".join(Path(x).stem for x in overlap)))

# where-used completeness for every reusable definition actually used in Local Model
counts["unique_definitions_used"]=len(definition_uses)
for defn,uses in definition_uses.items():
    if not uses:
        findings.append((defn,"where-used","Definition occurrence use was not indexed."))

print("local model context and occurrence-use review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  local regions: {len(regions)}")
print(f"  unique local tokens: {len(all_tokens)}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for defn,uses in sorted(definition_uses.items()):
    print(f"  WHERE_USED {defn}: {len(uses)} occurrence(s)")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=[
"# Local Model Context and Occurrence-Use Review","",
"Step 8 review of every governed Local Model owner, occurrence, endpoint, connection, flow, definition reference, usage mode, and where-used path.","",
"## Summary","",
"| Metric | Count |","|---|---:|",
]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| local regions | {len(regions)} |",f"| unique local tokens | {len(all_tokens)} |",f"| findings | {len(findings)} |","","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else: lines.append("| _None_ | | |")
lines += ["","## Definition where-used coverage","",
"| Reusable definition | Local occurrences |","|---|---:|"]
for defn,uses in sorted(definition_uses.items()):
    lines.append(f"| {defn} | {len(uses)} |")
lines += ["","## Interpretation","",
"- Local Model occurrence links provide contextual where-used coverage for reusable Object, Port, and Item Flow definitions.",
"- Part and endpoint usage semantics are checked against standard/variant/option rules; connections and flows may not carry usage.",
"- A variant/option family must resolve to at least one concrete subtype candidate.",
"- Connections must resolve exactly two endpoint references; flows must be nested under a connection and use valid endpoint roles.",
"- Contextual part occurrences must not be duplicated as note-level hasPart solely to make the graph look connected.",
"- No physical connector, protocol, internal electronics, or BOM detail is inferred by this review.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("LOCAL MODEL LINKING REVIEW PASSED")
