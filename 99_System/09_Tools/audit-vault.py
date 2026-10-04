#!/usr/bin/env python3
from __future__ import annotations
import re, sys, json
from pathlib import Path
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    print("PyYAML is required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
SYSTEM = ROOT / "99_System"
SCHEMAS = SYSTEM / "03_Schemas"
REPORT = ROOT / "audit-report.md"

EXCLUDE_PREFIXES = (".obsidian/", "99_System/")
MODEL_CLASSES = set()
REL = {}

def load_yaml(path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)

element_schema = load_yaml(SCHEMAS / "element-types.yaml") or {}
rel_schema = load_yaml(SCHEMAS / "relationships.yaml") or {}

# tolerate schema shape changes
for k,v in element_schema.items():
    if isinstance(v, dict) and ("idPrefix" in v or "prefix" in v or "template" in v):
        MODEL_CLASSES.add(k)
for container_key in ("types","elementTypes","classes"):
    container = element_schema.get(container_key)
    if isinstance(container, dict):
        MODEL_CLASSES.update(container.keys())

# Build relationship field -> inverse map by scanning dicts recursively.
def walk_rel(obj):
    if isinstance(obj, dict):
        field = obj.get("field") or obj.get("name") or obj.get("relationship")
        inv = obj.get("inverse") or obj.get("inverseField")
        if isinstance(field,str):
            REL[field] = inv if isinstance(inv,str) else None
        for v in obj.values(): walk_rel(v)
    elif isinstance(obj, list):
        for v in obj: walk_rel(v)
walk_rel(rel_schema)

def frontmatter(text):
    if not text.startswith("---\n"):
        return None, None
    end = text.find("\n---",4)
    if end < 0:
        return None, "unterminated"
    raw = text[4:end]
    try:
        data = yaml.safe_load(raw) or {}
        return data, None
    except Exception as e:
        return None, str(e)

md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
notes = {}
model_notes = {}
parse_errors = []
no_fm = []
for p in md_files:
    relp = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding="utf-8", errors="replace")
    fm, err = frontmatter(text)
    notes[relp] = {"path":p,"text":text,"fm":fm}
    if err: parse_errors.append((relp,err))
    if fm is None:
        no_fm.append(relp)
        continue
    if isinstance(fm,dict) and fm.get("type"):
        model_notes[relp] = fm

ids=defaultdict(list); uids=defaultdict(list)
bad_id=[]; bad_uid=[]; missing=[]; deprecated=[]
for path,fm in model_notes.items():
    i=str(fm.get("id","")).strip()
    u=str(fm.get("uid","")).strip()
    if i: ids[i].append(path)
    if u: uids[u].append(path)
    if not re.fullmatch(r"[A-Z]+-\d{5}",i): bad_id.append((path,i or "<missing>"))
    if not re.fullmatch(r"\d{17}[a-z-]{13}",u): bad_uid.append((path,u or "<missing>"))
    for req in ("type","subtype","id","uid","status","tags"):
        if req not in fm: missing.append((path,req))
    for old in ("kind","instanceOf","control","boundary"):
        if old in fm: deprecated.append((path,old,fm.get(old)))

dup_ids={k:v for k,v in ids.items() if len(v)>1}
dup_uids={k:v for k,v in uids.items() if len(v)>1}

# Wikilink resolution approximation using Obsidian basename/path behavior.
basename=defaultdict(list)
stempath={}
for path in notes:
    stem=path[:-3] if path.endswith(".md") else path
    stempath[stem]=path
    basename[Path(stem).name].append(path)

broken=[]; ambiguous=[]
link_re=re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
for source,n in notes.items():
    for m in link_re.finditer(n["text"]):
        target=m.group(1).strip().removesuffix(".md")
        if not target or "://" in target: continue
        if "/" in target:
            matches=[p for s,p in stempath.items() if s==target or s.endswith("/"+target)]
        else:
            matches=basename.get(target,[])
        if len(matches)==0: broken.append((source,target))
        elif len(matches)>1: ambiguous.append((source,target,matches))

# Relationship target and inverse check.
rel_missing=[]; inverse_missing=[]
def values(v):
    if v is None: return []
    if isinstance(v,list): return v
    return [v]
def link_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None
def resolve(target):
    if "/" in target:
        ms=[p for s,p in stempath.items() if s==target or s.endswith("/"+target)]
    else: ms=basename.get(target,[])
    return ms[0] if len(ms)==1 else None

for source,fm in model_notes.items():
    for field,inv in REL.items():
        if field not in fm: continue
        for raw in values(fm[field]):
            t=link_target(raw)
            if not t: continue
            target_path=resolve(t)
            if not target_path:
                rel_missing.append((source,field,t))
                continue
            if inv:
                tfm=notes[target_path]["fm"]
                if isinstance(tfm,dict):
                    back=[]
                    for rv in values(tfm.get(inv)):
                        bt=link_target(rv)
                        if bt: back.append(bt)
                    src_stem=Path(source[:-3]).name
                    src_full=source[:-3]
                    if src_stem not in back and src_full not in back and not any(x.endswith("/"+src_stem) for x in back):
                        inverse_missing.append((source,field,target_path,inv))

# top-level navigation coverage
root_dirs=[p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(".") and p.name!="99_System"]
nav={}
for d in root_dirs:
    names={p.name for p in d.iterdir() if p.is_file()}
    expected={
        f"README_{d.name}.md",
        f"BASE_local_{d.name}.base",
        f"BASE_all_{d.name}.base",
        f"CANVAS_{d.name}.canvas",
    }
    nav[d.name]=sorted(expected-names)

# path lengths
long_paths=[]
for p in ROOT.rglob("*"):
    if p.is_file():
        rp=p.relative_to(ROOT).as_posix()
        if len(rp)>212: long_paths.append((len(rp),rp))
long_paths.sort(reverse=True)

by_type=Counter(str(fm.get("type")) for fm in model_notes.values())
by_status=Counter(str(fm.get("status")) for fm in model_notes.values())

def list_rows(items, headers, maxn=100):
    if not items: return "_None._\n"
    rows=["| "+" | ".join(headers)+" |","|"+"|".join(["---"]*len(headers))+"|"]
    for item in list(items)[:maxn]:
        if not isinstance(item,(list,tuple)): item=(item,)
        rows.append("| "+" | ".join(str(x).replace("|","\\|").replace("\n"," ") for x in item)+" |")
    if len(items)>maxn: rows.append(f"| … | {len(items)-maxn} more not shown |" + " |"*(len(headers)-2))
    return "\n".join(rows)+"\n"

lines=[]
lines += ["# PosiBattery Integrity Audit","","Generated by `99_System/09_Tools/audit-vault.py`.","","## Summary",""]
summary=[
("Markdown files",len(md_files)),("Model notes",len(model_notes)),("Frontmatter parse errors",len(parse_errors)),
("Duplicate IDs",len(dup_ids)),("Duplicate UIDs",len(dup_uids)),("Malformed/missing IDs",len(bad_id)),
("Malformed/missing UIDs",len(bad_uid)),("Missing governed core properties",len(missing)),
("Deprecated properties",len(deprecated)),("Broken wikilinks",len(broken)),("Ambiguous wikilinks",len(ambiguous)),
("Unresolved relationship targets",len(rel_missing)),("Missing relationship inverses",len(inverse_missing)),
("Paths over 212 chars",len(long_paths))]
lines += ["| Check | Count |","|---|---:|"]+[f"| {a} | {b} |" for a,b in summary]
lines += ["","## Model notes by type","", "| Type | Count |","|---|---:|"]+[f"| {k} | {v} |" for k,v in sorted(by_type.items())]
lines += ["","## Model notes by status","", "| Status | Count |","|---|---:|"]+[f"| {k} | {v} |" for k,v in sorted(by_status.items())]

sections=[
("Frontmatter parse errors",parse_errors,["Path","Error"]),
("Duplicate IDs",[(k,", ".join(v)) for k,v in dup_ids.items()],["ID","Paths"]),
("Duplicate UIDs",[(k,", ".join(v)) for k,v in dup_uids.items()],["UID","Paths"]),
("Malformed or missing IDs",bad_id,["Path","ID"]),
("Malformed or missing UIDs",bad_uid,["Path","UID"]),
("Missing governed core properties",missing,["Path","Property"]),
("Deprecated properties",deprecated,["Path","Property","Value"]),
("Broken wikilinks",broken,["Source","Target"]),
("Ambiguous wikilinks",[(a,b,", ".join(c)) for a,b,c in ambiguous],["Source","Target","Matches"]),
("Unresolved relationship targets",rel_missing,["Source","Relationship","Target"]),
("Missing relationship inverses",inverse_missing,["Source","Relationship","Target","Expected inverse"]),
("Paths over 212 characters",long_paths,["Length","Path"]),
]
for title,data,headers in sections:
    lines += ["",f"## {title}","",list_rows(data,headers,200)]

lines += ["","## Top-level navigation coverage","", "| Folder | Missing standard artifacts |","|---|---|"]
for k,v in sorted(nav.items()):
    lines.append(f"| {k} | {', '.join(v) if v else 'Complete'} |")

lines += ["","## Interpretation","","This report detects structural inconsistencies. It does not automatically decide semantic reclassification, duplicate-concept merges, or whether a relationship should exist. Those remain engineering/model-review decisions.",""]

REPORT.write_text("\n".join(lines),encoding="utf-8")
print("\n".join(lines))
