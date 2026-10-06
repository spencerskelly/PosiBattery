#!/usr/bin/env python3
"""Step 20 curated Source Document relationship and provenance review.

Reviews every governed Document note (currently the eight curated Source
Documents), validates describes/describedBy and evidence relationships, and
checks structured provenance migration without inventing unknown access dates.
"""
from pathlib import Path
from collections import Counter, defaultdict
from urllib.parse import urlparse
import re, yaml

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"curated-source-document-review.md"
SOURCE_DIR=ROOT/"70_Research and Evidence"/"Source Documents"

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
    d=fm(p.read_text(encoding="utf-8",errors="replace"))
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

documents={p:d for p,d in notes.items() if d.get("type")=="Document"}
source_docs={p:d for p,d in documents.items() if "source-document" in {str(x) for x in vals(d.get("tags"))}}
counts=Counter(); findings=[]; rows=[]

counts["governed_documents"]=len(documents)
counts["curated_source_documents"]=len(source_docs)
if len(documents)!=len(source_docs):
    for p in sorted(set(documents)-set(source_docs)):
        findings.append((p,"document-outside-curated-source-set","Governed Document lacks source-document tag; review scope/classification."))

allowed_source_classes={"web-page","datasheet","brochure","manual","standard","article","database","other"}

for p,d in sorted(source_docs.items()):
    counts["source_documents_reviewed"]+=1

    sc=d.get("sourceClass")
    su=d.get("sourceUrl")
    sr=d.get("sourceRevision")
    acc=d.get("accessed")

    if sc:
        counts["with_sourceClass"]+=1
        if sc not in allowed_source_classes:
            findings.append((p,"invalid-sourceClass",str(sc)))
    else:
        findings.append((p,"missing-sourceClass","Curated Source Document has known source class but no structured sourceClass."))

    if su:
        counts["with_sourceUrl"]+=1
        try:
            u=urlparse(str(su))
            if u.scheme not in {"http","https"} or not u.netloc:
                raise ValueError()
        except Exception:
            findings.append((p,"invalid-sourceUrl",str(su)))
    else:
        findings.append((p,"missing-sourceUrl","Curated Source Document has a known original web address but no structured sourceUrl."))

    if sr: counts["with_sourceRevision"]+=1
    if acc: counts["with_accessed"]+=1

    desc=[]
    for raw in vals(d.get("describes")):
        q=resolve(target(raw))
        if not q:
            findings.append((p,"unresolved-describes",str(raw)))
            continue
        desc.append(q)
        inv={resolve(target(x)) for x in vals(notes[q].get("describedBy")) if resolve(target(x))}
        if p not in inv:
            findings.append((p,"describes-inverse",f"{Path(q).stem} lacks reciprocal describedBy."))
        rows.append((p,"describes",q,notes[q].get("type")))
        counts[f"describes_target_{notes[q].get('type')}"]+=1

    if not desc:
        findings.append((p,"source-document-no-subject","Curated Source Document has no governed describes target."))
    else:
        counts["with_describes"]+=1

    for field in ("supports","contradicts"):
        for raw in vals(d.get(field)):
            q=resolve(target(raw))
            if not q:
                findings.append((p,f"unresolved-{field}",str(raw)))
                continue
            invfield="supportedBy" if field=="supports" else "contradictedBy"
            inv={resolve(target(x)) for x in vals(notes[q].get(invfield)) if resolve(target(x))}
            if p not in inv:
                findings.append((p,f"{field}-inverse",f"{Path(q).stem} lacks reciprocal {invfield}."))
            rows.append((p,field,q,notes[q].get("type")))
            counts[f"{field}_assertions"]+=1

# Requirements may cite Documents via references; validate any such reverse evidence.
for p,d in notes.items():
    if d.get("type")!="Requirement": continue
    for raw in vals(d.get("references")):
        q=resolve(target(raw))
        if q in source_docs:
            counts["requirement_references_to_source_documents"]+=1
            inv={resolve(target(x)) for x in vals(notes[q].get("referencedBy")) if resolve(target(x))}
            if p not in inv:
                findings.append((p,"references-inverse",f"{Path(q).stem} lacks reciprocal referencedBy."))

print("curated source document review")
for k,v in sorted(counts.items()): print(f"  {k}: {v}")
print(f"  findings: {len(findings)}")
for p,k,msg in findings: print(f"  FINDING {k}: {p}: {msg}")
for p,field,q,qtyp in rows: print(f"  LINK {Path(p).stem} --{field}--> {qtyp} {Path(q).stem}")
print(f"  report: {REPORT.relative_to(ROOT)}")

lines=["# Curated Source Document Review","",
"Step 20 whole-vault review of governed Document evidence relationships and structured provenance.","",
"## Summary","",
"| Metric | Count |","|---|---:|"]
for k,v in sorted(counts.items()): lines.append(f"| {k} | {v} |")
lines += [f"| findings | {len(findings)} |","","## Evidence relationships","",
"| Document | Relationship | Target type | Target |","|---|---|---|---|"]
if rows:
    for p,field,q,qtyp in rows: lines.append(f"| {p} | {field} | {qtyp} | {q} |")
else:
    lines.append("| _None_ | | | |")
lines += ["","## Findings","",
"| Path | Kind | Detail |","|---|---|---|"]
if findings:
    for p,k,msg in findings: lines.append(f"| {p} | {k} | {msg} |")
else:
    lines.append("| _None_ | | |")
lines += ["","## Interpretation","",
"- All governed Document notes are currently curated Source Documents.",
"- describes/describedBy is appropriate for identifying the product or organization whose published facts the source defines or documents.",
"- supports/contradicts should be added only when the Document is being used as evidence for a specific engineering claim. It is not required merely because a source contains facts about a reference product.",
"- These eight documents primarily describe competitor/reference products and their organizations. Their evidence should not be projected onto active BMID Requirements, Functions, or Designs simply because similar behavior exists.",
"- sourceClass and sourceUrl are migrated when known. sourceRevision is optional and is migrated only when the source itself supplies a useful document code/date.",
"- accessed remains absent where the original web access/download date is not recorded. Local-copy review date is not silently substituted for original source access date.",
"- references is reserved for a Requirement citing a Document/Requirement; no such relationship should be invented unless the Requirement actually depends on that source.",
]
REPORT.write_text("\n".join(lines),encoding="utf-8")
if findings: raise SystemExit(2)
print("CURATED SOURCE DOCUMENT REVIEW PASSED")
