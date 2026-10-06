#!/usr/bin/env python3
"""Report semantic-linking quality findings for PosiBattery.

Report-only. Relationship integrity is enforced separately by check-relationships.py.
This reporter consumes the approved Step 2/3/4 linking contract through
semantic-linking-report-rules.yaml plus the reviewed disposition registry.
"""
from __future__ import annotations
from pathlib import Path
from collections import Counter, defaultdict
import re

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required")

ROOT=Path(__file__).resolve().parents[2]
REL_PATH=ROOT/"99_System"/"03_Schemas"/"relationships.yaml"
RULES_PATH=ROOT/"99_System"/"09_Tools"/"semantic-linking-report-rules.yaml"
DISP_PATH=ROOT/"80_Decisions and Planning"/"Semantic Linking Review Dispositions 0.1.yaml"
REPORT=ROOT/"traceability-quality-report.md"

def load_yaml(path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def frontmatter(text):
    if not text.startswith("---\n"): return {}
    end=text.find("\n---",4)
    if end<0: return {}
    try: return yaml.safe_load(text[4:end]) or {}
    except Exception: return {}

def vals(v):
    if v is None: return []
    return v if isinstance(v,list) else [v]

def link_target(v):
    if not isinstance(v,str): return None
    m=re.match(r"\[\[([^\]|#]+)",v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None

rel_schema=load_yaml(REL_PATH)
rules=load_yaml(RULES_PATH)
disp_doc=load_yaml(DISP_PATH)

relationship_fields=set()
for rec in rel_schema.get("paired",[])+rel_schema.get("temporaryPairs",[]):
    if rec.get("forward"): relationship_fields.add(rec["forward"])
    if rec.get("inverse"): relationship_fields.add(rec["inverse"])
for rec in rel_schema.get("symmetric",[])+rel_schema.get("oneWay",[]):
    if rec.get("field"): relationship_fields.add(rec["field"])

notes={}
texts={}
basename=defaultdict(list)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts or "99_System" in p.parts:
        continue
    rel=p.relative_to(ROOT).as_posix()
    text=p.read_text(encoding="utf-8",errors="replace")
    data=frontmatter(text)
    if not isinstance(data,dict) or not data.get("type"):
        continue
    notes[rel]=data
    texts[rel]=text
    basename[p.stem].append(rel)

def resolve(name):
    if not name: return None
    if "/" in name:
        matches=[p for p in notes if p[:-3]==name or p[:-3].endswith("/"+name)]
    else:
        matches=basename.get(Path(name).name,[])
    return matches[0] if len(matches)==1 else None

incoming=defaultdict(list)
outgoing=defaultdict(list)
for source,data in notes.items():
    for field in relationship_fields:
        if field not in data: continue
        for raw in vals(data.get(field)):
            target=link_target(raw)
            target_path=resolve(target)
            if not target_path: continue
            outgoing[source].append((field,target_path))
            incoming[target_path].append((field,source))

    # Local Model definition references count only as contextual where-used/use.
    text=texts[source]
    m=re.search(r"<!--\s*MDSE:LOCAL-MODEL START[^>]*-->([\s\S]*?)<!--\s*MDSE:LOCAL-MODEL END\s*-->",text)
    if m:
        for target in re.findall(r"(?m)^- definition:\s*\[\[([^\]|#]+)",m.group(1)):
            target_path=resolve(target.strip())
            if not target_path: continue
            outgoing[source].append(("localModelDefinition",target_path))
            incoming[target_path].append(("localModelDefinition",source))

orphans=[p for p in notes if not outgoing[p] and not incoming[p]]

# ---------------------------------------------------------------------------
# Legacy Step-97-compatible metrics, retained only for baseline comparability.
# ---------------------------------------------------------------------------
legacy_expectations={
    "Requirement":[
        ("upstream rationale", {"drivenBy","derivedFrom","refinedBy","references","appliesTo"}),
        ("satisfaction path", {"satisfiedBy"}),
        ("verification path", {"verifiedBy"}),
    ],
    "Function":[
        ("performer/product context", {"performedBy"}),
        ("intent or implementation trace", {"satisfies","realizes","realizedBy","drivenBy"}),
    ],
    "Design":[
        ("design ownership/context", {"designOf","appliesTo"}),
        ("behavior/requirement trace", {"realizes","satisfies","verifiedBy"}),
    ],
    "Verification":[("verification target", {"verifies"})],
    "Use Case":[("participation or realization", {"participants","realizedBy","drives","hasNeed","needOf","arisesIn","givesRiseTo"})],
    "Object":[("architecture/behavior/business context", {"supertypeOf","subtypeOf","partOf","hasPart","performs","hasDesign","madeBy","offeredBy","applies","describedBy"})],
    "Document":[("subject/evidence trace", {"describes","supports","references","referencedBy"})],
}
legacy_weak=[]
legacy_by_type=Counter()
legacy_by_signal=Counter()
for path,data in notes.items():
    typ=str(data.get("type") or "")
    fields={f for f,_ in outgoing[path]} | {f for f,_ in incoming[path]}
    for label,alternatives in legacy_expectations.get(typ,[]):
        if not fields & alternatives:
            legacy_weak.append((path,typ,label,sorted(alternatives)))
            legacy_by_type[typ]+=1
            legacy_by_signal[(typ,label)]+=1

legacy_focus_types=set(rules.get("legacy_focus_types") or ["Use Case","Requirement","Function","Design","Verification"])
focus_notes=[p for p,d in notes.items() if str(d.get("type")) in legacy_focus_types]
focus_orphans=[p for p in orphans if p in focus_notes]
legacy_focus_weak=[x for x in legacy_weak if x[1] in legacy_focus_types]

# ---------------------------------------------------------------------------
# Step 2 matrix-driven dimensional findings.
# ---------------------------------------------------------------------------
matrix=rules.get("dimensions") or {}
raw_dimension_findings=[]
raw_by_type=Counter()
raw_by_dimension=Counter()
for path,data in notes.items():
    typ=str(data.get("type") or "")
    fields={f for f,_ in outgoing[path]} | {f for f,_ in incoming[path]}
    for dim, alternatives in (matrix.get(typ) or {}).items():
        alts=set(alternatives or [])
        if alts and not (fields & alts):
            raw_dimension_findings.append((path,typ,dim,sorted(alts)))
            raw_by_type[typ]+=1
            raw_by_dimension[(typ,dim)]+=1

# ---------------------------------------------------------------------------
# Step 3/4 reviewed classification and exception dispositions.
# Nothing is silently inferred as final classification: Steps 6-27 populate the
# registry as notes are reviewed.
# ---------------------------------------------------------------------------
records=disp_doc.get("records") or {}
allowed_classes=set(disp_doc.get("allowed_completeness_classes") or [])
allowed_dispositions=set(disp_doc.get("allowed_dispositions") or [])
allowed_codes=set(disp_doc.get("allowed_exception_codes") or [])
unresolved_codes={"EXC-ARCH-UNRESOLVED","EXC-IMPORT-HOLDING","EXC-EVIDENCE-PENDING"}
strict_dims=rules.get("strict_active_dimensions") or {}

registry_errors=[]
reviewed_paths=set()
class_counts=Counter()
exception_counts=Counter()
disposition_counts=Counter()
applicable_findings=[]
explained_findings=[]
unresolved_findings=[]

raw_lookup=defaultdict(dict)
for path,typ,dim,alts in raw_dimension_findings:
    raw_lookup[path][dim]=(typ,alts)

for path,rec in records.items():
    if path not in notes:
        registry_errors.append(f"unknown note path: {path}")
        continue
    if not isinstance(rec,dict):
        registry_errors.append(f"{path}: record must be a mapping")
        continue
    cls=rec.get("classification")
    if cls not in allowed_classes:
        registry_errors.append(f"{path}: invalid or missing classification {cls!r}")
        continue
    reviewed_paths.add(path)
    class_counts[cls]+=1

    gaps=rec.get("gaps") or {}
    if not isinstance(gaps,dict):
        registry_errors.append(f"{path}: gaps must be a mapping")
        gaps={}

    # Determine dimensions that matter under the reviewed completeness class.
    typ=str(notes[path].get("type") or "")
    if cls=="active_engineering":
        required=set(strict_dims.get(typ) or [])
    elif cls=="engineering_support":
        required={d for d in ("ownership_use","evidence") if d in (matrix.get(typ) or {})}
    else:
        required=set()

    for dim in sorted(required):
        if dim not in raw_lookup.get(path,{}):
            continue  # linked by the semantic graph
        disposition_rec=gaps.get(dim)
        if not isinstance(disposition_rec,dict):
            applicable_findings.append((path,typ,cls,dim,"unreviewed",None))
            continue
        state=disposition_rec.get("disposition")
        code=disposition_rec.get("exception")
        if state not in allowed_dispositions:
            registry_errors.append(f"{path}/{dim}: invalid disposition {state!r}")
            applicable_findings.append((path,typ,cls,dim,"invalid",code))
            continue
        if state=="linked":
            # Reporter says it is actually unlinked, so a manual linked override is inconsistent.
            registry_errors.append(f"{path}/{dim}: registry says linked but graph has no qualifying link")
            applicable_findings.append((path,typ,cls,dim,"inconsistent",code))
            continue
        if code not in allowed_codes:
            registry_errors.append(f"{path}/{dim}: missing/invalid exception code {code!r}")
            applicable_findings.append((path,typ,cls,dim,state,code))
            continue
        disposition_counts[state]+=1
        exception_counts[code]+=1
        explained_findings.append((path,typ,cls,dim,state,code))
        if state=="unresolved" or code in unresolved_codes:
            unresolved_findings.append((path,typ,cls,dim,state,code))

unreviewed_notes=sorted(set(notes)-reviewed_paths)

# Step 25: distinguish raw graph isolation from unexplained isolation.
# A deliberately non-semantic framing/reference note may remain graph-isolated
# only when every Step-2 dimension has a reviewed, non-unresolved exception.
explained_orphans=[]
unexplained_orphans=[]
for path in orphans:
    typ=str(notes[path].get("type") or "")
    dims=set((matrix.get(typ) or {}).keys())
    rec=records.get(path)
    ok=isinstance(rec,dict) and rec.get("classification") in allowed_classes
    gaps=(rec.get("gaps") or {}) if isinstance(rec,dict) else {}
    if not isinstance(gaps,dict):
        ok=False
        gaps={}
    for dim in dims:
        g=gaps.get(dim)
        if not isinstance(g,dict):
            ok=False
            break
        state=g.get("disposition")
        code=g.get("exception")
        if state not in {"intentionally_absent","not_applicable"} or code not in allowed_codes or code in unresolved_codes:
            ok=False
            break
    if ok:
        explained_orphans.append(path)
    else:
        unexplained_orphans.append(path)

summary={
    "model_notes":len(notes),
    "semantic_relationship_assertions":sum(len(v) for v in outgoing.values()),
    "isolated_model_elements":len(orphans),
    "explained_isolated_model_elements":len(explained_orphans),
    "unexplained_isolated_model_elements":len(unexplained_orphans),
    "legacy_product_development_focus_notes":len(focus_notes),
    "legacy_isolated_focus_elements":len(focus_orphans),
    "legacy_weak_traceability_findings":len(legacy_weak),
    "legacy_focus_weak_traceability_findings":len(legacy_focus_weak),
    "matrix_dimension_findings":len(raw_dimension_findings),
    "reviewed_completeness_classifications":len(reviewed_paths),
    "unreviewed_completeness_classifications":len(unreviewed_notes),
    "applicable_unexplained_findings":len(applicable_findings),
    "explained_exception_findings":len(explained_findings),
    "unresolved_exception_findings":len(unresolved_findings),
    "disposition_registry_errors":len(registry_errors),
}

lines=[
"# PosiBattery Semantic Linking Quality Report","",
"Report-only quality scan generated by `99_System/09_Tools/report-traceability.py`. Relationship integrity is validated separately; this report evaluates semantic completeness and review dispositions.","",
"## Summary","",
"| Check | Count |","|---|---:|",
]
for k,v in summary.items():
    lines.append(f"| {k.replace('_',' ')} | {v} |")

lines += ["","## Contract","",
"- Step 2 expectation dimensions are loaded from `99_System/09_Tools/semantic-linking-report-rules.yaml`; they are no longer hard-coded as the primary completeness contract.",
"- Step 3 completeness classes and Step 4 exception codes are consumed through `Semantic Linking Review Dispositions 0.1.yaml`.",
"- Notes are not silently assigned a final completeness class. Steps 6–27 populate reviewed classifications/dispositions.",
"- Local Model definition use counts as contextual ownership/use for reusable definitions.",
"- Findings remain report-only during the semantic-linking program.",
""]

lines += ["## Isolated model elements","",
"| Path | Type | Review state |","|---|---|---|"]
for path in orphans[:400]:
    state="explained intentional exception" if path in explained_orphans else "UNEXPLAINED"
    lines.append(f"| {path} | {notes[path].get('type','')} | {state} |")
if not orphans:
    lines.append("| _None_ | | |")

lines += ["","## Matrix-driven raw dimension findings","",
"These are unfiltered Step 2 expectation gaps before Step 3 classification and Step 4 exception review. They are a review queue, not defect counts.","",
"| Path | Type | Missing dimension | Qualifying relationships |","|---|---|---|---|"]
for path,typ,dim,alts in raw_dimension_findings[:600]:
    lines.append(f"| {path} | {typ} | {dim} | {', '.join(alts)} |")
if len(raw_dimension_findings)>600:
    lines.append(f"| … | | {len(raw_dimension_findings)-600} additional raw findings omitted | |")

lines += ["","## Reviewed applicable unexplained findings","",
"| Path | Type | Completeness class | Dimension | State |","|---|---|---|---|---|"]
for row in applicable_findings[:400]:
    path,typ,cls,dim,state,code=row
    lines.append(f"| {path} | {typ} | {cls} | {dim} | {state} |")
if not applicable_findings:
    lines.append("| _None yet_ | | | | |")

lines += ["","## Reviewed exceptions","",
"| Path | Type | Completeness class | Dimension | Disposition | Exception |","|---|---|---|---|---|---|"]
for path,typ,cls,dim,state,code in explained_findings[:400]:
    lines.append(f"| {path} | {typ} | {cls} | {dim} | {state} | {code} |")
if not explained_findings:
    lines.append("| _None yet_ | | | | | |")

lines += ["","## Legacy Step-97 comparison","",
"These metrics are retained only so progress can be compared with the frozen Step 1 baseline. New review work should use the matrix-driven dimensions and reviewed completeness classes above.","",
"| Type | Legacy weak findings |","|---|---:|"]
for typ,count in sorted(legacy_by_type.items()):
    lines.append(f"| {typ} | {count} |")

lines += ["","## Matrix findings by type","",
"| Type | Raw dimension findings |","|---|---:|"]
for typ,count in sorted(raw_by_type.items()):
    lines.append(f"| {typ} | {count} |")

lines += ["","## Registry validation",""]
if registry_errors:
    lines += [f"- {x}" for x in registry_errors[:200]]
else:
    lines += ["- No disposition-registry errors."]

lines += ["","## Interpretation","",
"- A raw matrix finding is not automatically a defect; the note must first receive its Step 3 completeness classification.",
"- Active-engineering findings become completion obligations unless a Step 4 controlled exception legitimately applies.",
"- Reference/catalog leaves may remain sparse; do not manufacture relationships to reduce counts.",
"- Unresolved exceptions stay visible and are not equivalent to repaired links.",
"- Folder placement and ordinary body links do not satisfy semantic-linking expectations.",
""]

REPORT.write_text("\n".join(lines),encoding="utf-8")

print("semantic linking quality reporting")
for k,v in summary.items():
    print(f"  {k.replace('_',' ')}: {v}")
for typ,count in sorted(legacy_by_type.items()):
    print(f"  legacy weak {typ}: {count}")
for typ,count in sorted(raw_by_type.items()):
    print(f"  matrix raw {typ}: {count}")
for path in explained_orphans:
    print(f"  isolated explained: {path}")
for path in unexplained_orphans:
    print(f"  isolated unexplained: {path}")
for err in registry_errors:
    print(f"  registry error: {err}")
print(f"  report: {REPORT.relative_to(ROOT)}")
print("SEMANTIC LINKING REPORT GENERATED (REPORT-ONLY)")
