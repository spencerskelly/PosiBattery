#!/usr/bin/env python3
"""Step 25 true-orphan semantic review.

Governed Step 25 review entry point.

A graph-isolated note is acceptable only when every Step-2 expectation
dimension has a reviewed intentional/non-applicable disposition. Unresolved
exceptions do not close an orphan.
"""
from pathlib import Path
from collections import defaultdict
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REL=ROOT/"99_System"/"03_Schemas"/"relationships.yaml"
RULES=ROOT/"99_System"/"09_Tools"/"semantic-linking-report-rules.yaml"
DISP=ROOT/"80_Decisions and Planning"/"Semantic Linking Review Dispositions 0.1.yaml"
REPORT=ROOT/"true-orphan-review.md"

def load(p): return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
def fm(t):
    if not t.startswith("---\n"): return {}
    e=t.find("\n---",4)
    if e<0:return {}
    try:return yaml.safe_load(t[4:e]) or {}
    except Exception:return {}
def vals(v):
    if v is None:return []
    return v if isinstance(v,list) else [v]
def target(v):
    if not isinstance(v,str):return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

rel=load(REL); rules=load(RULES); disp=load(DISP)
fields=set()
for rec in rel.get("paired",[])+rel.get("temporaryPairs",[]):
    fields.update(x for x in (rec.get("forward"),rec.get("inverse")) if x)
for rec in rel.get("symmetric",[])+rel.get("oneWay",[]):
    if rec.get("field"): fields.add(rec["field"])

notes={}; texts={}; bybase=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts: continue
    t=p.read_text(encoding="utf-8",errors="replace"); d=fm(t)
    if not isinstance(d,dict) or not d.get("type"): continue
    relp=p.relative_to(ROOT).as_posix()
    notes[relp]=d; texts[relp]=t; bybase[p.stem].append(relp)

def resolve(name):
    if not name:return None
    if "/" in name:
        ms=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else: ms=bybase.get(Path(name).name,[])
    return ms[0] if len(ms)==1 else None

incoming=defaultdict(list); outgoing=defaultdict(list)
for p,d in notes.items():
    for field in fields:
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if q:
                outgoing[p].append((field,q)); incoming[q].append((field,p))
    m=re.search(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->",texts[p])
    if m:
        for name in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1)):
            q=resolve(name.strip())
            if q:
                outgoing[p].append(("localModelDefinition",q)); incoming[q].append(("localModelDefinition",p))

orphans=sorted(p for p in notes if not outgoing[p] and not incoming[p])
matrix=rules.get("dimensions") or {}
records=disp.get("records") or {}
allowed_classes=set(disp.get("allowed_completeness_classes") or [])
allowed_codes=set(disp.get("allowed_exception_codes") or [])
unresolved_codes={"EXC-ARCH-UNRESOLVED","EXC-IMPORT-HOLDING","EXC-EVIDENCE-PENDING"}

explained=[]; unexplained=[]; details=[]
for p in orphans:
    typ=str(notes[p].get("type") or "")
    dims=sorted((matrix.get(typ) or {}).keys())
    rec=records.get(p)
    reasons=[]
    ok=isinstance(rec,dict) and rec.get("classification") in allowed_classes
    if not ok: reasons.append("missing/invalid reviewed classification")
    gaps=(rec.get("gaps") or {}) if isinstance(rec,dict) else {}
    if not isinstance(gaps,dict):
        gaps={}; ok=False; reasons.append("gaps is not a mapping")
    for dim in dims:
        g=gaps.get(dim)
        if not isinstance(g,dict):
            ok=False; reasons.append(f"{dim}: no reviewed disposition"); continue
        state=g.get("disposition"); code=g.get("exception")
        if state not in {"intentionally_absent","not_applicable"}:
            ok=False; reasons.append(f"{dim}: disposition {state!r} does not close orphan")
        if code not in allowed_codes:
            ok=False; reasons.append(f"{dim}: invalid exception {code!r}")
        elif code in unresolved_codes:
            ok=False; reasons.append(f"{dim}: unresolved exception {code}")
    if ok: explained.append(p)
    else: unexplained.append(p)
    details.append((p,typ,(rec or {}).get("classification") if isinstance(rec,dict) else None,dims,reasons))

print("true orphan review")
print(f"  raw isolated model elements: {len(orphans)}")
print(f"  explained isolated model elements: {len(explained)}")
print(f"  unexplained isolated model elements: {len(unexplained)}")
for p in explained: print(f"  EXPLAINED: {p}")
for p in unexplained: print(f"  UNEXPLAINED: {p}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# True Orphan Review","",
"Step 25 distinguishes raw graph isolation from unexplained semantic orphaning.","",
"## Summary","",
f"- Raw isolated model elements: **{len(orphans)}**",
f"- Explained isolated model elements: **{len(explained)}**",
f"- Unexplained isolated model elements: **{len(unexplained)}**","",
"| Path | Type | Classification | Step-2 dimensions | Result |",
"|---|---|---|---|---|"]
for p,typ,cls,dims,reasons in details:
    result="explained intentional exception" if not reasons else "; ".join(reasons)
    lines.append(f"| {p} | {typ} | {cls or ''} | {', '.join(dims)} | {result} |")
if not details: lines.append("| _None_ | | | | |")
lines += ["","## Rule","",
"- A raw graph-isolated note is not automatically a defect.",
"- Every isolated note is reviewed individually.",
"- If a valid semantic relationship is supported, add it rather than using an exception.",
"- If the note is intentionally non-semantic framing/reference content, every applicable Step-2 dimension must have a controlled intentional/non-applicable disposition.",
"- Unresolved exception codes never count as orphan closure.",
"- EXC-FRAMING is appropriate only when the body clearly functions as framing/navigation rather than as an engineering decision node.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if unexplained: raise SystemExit(2)
print("TRUE ORPHAN REVIEW PASSED")