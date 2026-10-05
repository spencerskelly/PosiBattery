#!/usr/bin/env python3
"""Complete governed relationship validation for PosiBattery.

Validates instantiated model notes against relationships.yaml:
- relationship field names are controlled;
- relationship targets resolve uniquely to model notes;
- endpoint classes satisfy from/to/sameClass/excludePairs rules;
- paired and symmetric inverse fields are persisted;
- provisional and temporary relationship terms are reported;
- link-bearing unknown frontmatter fields are rejected as uncontrolled relationship-like fields.

Exit code 1 means a relationship invariant is violated.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "99_System" / "03_Schemas"
REL_PATH = SCHEMAS / "relationships.yaml"
ELEMENT_PATH = SCHEMAS / "element-types.yaml"

WIKILINK_RE = re.compile(r"^\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]$")


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(text[4:end]) or {}
    except Exception:
        return {}


def values(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def link_target(v):
    if not isinstance(v, str):
        return None
    m = WIKILINK_RE.match(v.strip())
    return m.group(1).strip().removesuffix(".md") if m else None


rel_schema = load_yaml(REL_PATH)
element_schema = load_yaml(ELEMENT_PATH)

common_fields = set(element_schema.get("commonProperties") or [])
common_fields.update(x.get("name") for x in element_schema.get("optionalProperties", []) if isinstance(x, dict) and x.get("name"))
common_fields.update(element_schema.get("translatedOnlyProperties") or [])
for props in (element_schema.get("classOptionalProperties") or {}).values():
    for rec in props or []:
        if isinstance(rec, dict) and rec.get("name"):
            common_fields.add(rec["name"])

rules = {}
inverse = {}
provisional = set()
temporary = set()
symmetric = set()
one_way = set()

for rec in rel_schema.get("paired", []):
    f, inv = rec.get("forward"), rec.get("inverse")
    if f:
        rules[f] = rec
        inverse[f] = inv
        if rec.get("provisional"):
            provisional.add(f)
        if rec.get("temporary"):
            temporary.add(f)
    if inv:
        inv_rule = dict(rec)
        inv_rule["from"], inv_rule["to"] = rec.get("to"), rec.get("from")
        if rec.get("excludePairs"):
            inv_rule["excludePairs"] = [[b, a] for a, b in rec["excludePairs"]]
        rules[inv] = inv_rule
        inverse[inv] = f
        if rec.get("provisional"):
            provisional.add(inv)
        if rec.get("temporary"):
            temporary.add(inv)

for rec in rel_schema.get("temporaryPairs", []):
    f, inv = rec.get("forward"), rec.get("inverse")
    if f:
        rules[f] = rec
        inverse[f] = inv
        temporary.add(f)
    if inv:
        inv_rule = dict(rec)
        inv_rule["from"], inv_rule["to"] = rec.get("to"), rec.get("from")
        rules[inv] = inv_rule
        inverse[inv] = f
        temporary.add(inv)

for rec in rel_schema.get("symmetric", []):
    f = rec.get("field")
    if f:
        rules[f] = rec
        inverse[f] = f
        symmetric.add(f)
        if rec.get("temporary"):
            temporary.add(f)

for rec in rel_schema.get("oneWay", []):
    f = rec.get("field")
    if f:
        rules[f] = rec
        inverse[f] = None
        one_way.add(f)

relationship_fields = set(rules)

# Explicit retired vocabulary that must not reappear as relationship assertions.
# These names are retained only as historical/modeling terminology elsewhere.
deprecated_relationship_fields = {
    "instanceOf",
    "usedIn",
    "uses",
    "satisfy",
    "verify",
    "realize",
    "implementedBy",
    "implements",
    "relatedTo",
}

notes = {}
basename = defaultdict(list)
stempath = {}
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    rel = p.relative_to(ROOT).as_posix()
    if rel.startswith("99_System/"):
        continue
    fm = frontmatter(p.read_text(encoding="utf-8", errors="replace"))
    if not isinstance(fm, dict) or not fm.get("type"):
        continue
    notes[rel] = fm
    stem = rel[:-3]
    basename[Path(stem).name].append(rel)
    stempath[stem] = rel


def resolve(target: str):
    if "/" in target:
        matches = [p for stem, p in stempath.items() if stem == target or stem.endswith("/" + target)]
    else:
        matches = basename.get(target, [])
    return matches


def class_allowed(rule, source_type, target_type):
    if rule.get("sameClass") and source_type != target_type:
        return False, "sameClass"
    src = rule.get("from")
    dst = rule.get("to")
    if src not in (None, "any") and source_type not in (src if isinstance(src, list) else [src]):
        return False, "from"
    if dst not in (None, "any") and target_type not in (dst if isinstance(dst, list) else [dst]):
        return False, "to"
    for pair in rule.get("excludePairs") or []:
        if list(pair) == [source_type, target_type]:
            return False, "excludePairs"
    return True, ""


def contains_link(v):
    return any(link_target(x) is not None for x in values(v))


findings = []
counts = defaultdict(int)
relationship_assertions = 0

# Index all assertions first for inverse tests.
assertions = defaultdict(list)
for source, fm in notes.items():
    for field in relationship_fields:
        if field not in fm:
            continue
        for raw in values(fm.get(field)):
            target = link_target(raw)
            if target:
                assertions[(source, field)].append(target)

for source, fm in notes.items():
    source_type = str(fm.get("type") or "")

    # Controlled-name enforcement for relationship-like YAML fields.
    for field, val in fm.items():
        if field in relationship_fields or field in common_fields:
            continue
        if field in deprecated_relationship_fields and contains_link(val):
            findings.append(("deprecated_relationship_field", source, field, "replace with governed vocabulary"))
            counts["deprecated_relationship_fields"] += 1
        elif contains_link(val):
            findings.append(("uncontrolled_relationship_field", source, field, str(val)))
            counts["uncontrolled_relationship_fields"] += 1

    for field in relationship_fields:
        if field not in fm:
            continue
        for raw in values(fm.get(field)):
            target = link_target(raw)
            if not target:
                # Relationship fields are link-valued under this contract.
                findings.append(("non_link_relationship_value", source, field, str(raw)))
                counts["non_link_relationship_values"] += 1
                continue

            relationship_assertions += 1
            matches = resolve(target)
            if len(matches) == 0:
                findings.append(("unresolved_relationship_target", source, field, target))
                counts["unresolved_targets"] += 1
                continue
            if len(matches) > 1:
                findings.append(("ambiguous_relationship_target", source, field, f"{target} -> {matches}"))
                counts["ambiguous_targets"] += 1
                continue

            target_path = matches[0]
            target_type = str(notes[target_path].get("type") or "")
            ok, reason = class_allowed(rules[field], source_type, target_type)
            if not ok:
                findings.append(("endpoint_incompatible", source, field, f"{source_type} -> {target_type} ({reason}) target={target_path}"))
                counts["endpoint_incompatible"] += 1

            inv = inverse.get(field)
            if inv:
                source_stem = Path(source[:-3]).name
                source_full = source[:-3]
                backs = assertions.get((target_path, inv), [])
                if not any(x == source_stem or x == source_full or x.endswith("/" + source_stem) for x in backs):
                    findings.append(("missing_inverse", source, field, f"{target_path} expected {inv}"))
                    counts["missing_inverses"] += 1

            if field in provisional:
                findings.append(("provisional_relationship", source, field, target_path))
                counts["provisional_relationships"] += 1

            if field in temporary:
                findings.append(("temporary_relationship", source, field, target_path))
                counts["temporary_relationships"] += 1

print("relationship validation")
print(f"  model notes: {len(notes)}")
print(f"  governed relationship fields: {len(relationship_fields)}")
print(f"  relationship assertions: {relationship_assertions}")
for key in [
    "uncontrolled_relationship_fields",
    "deprecated_relationship_fields",
    "non_link_relationship_values",
    "unresolved_targets",
    "ambiguous_targets",
    "endpoint_incompatible",
    "missing_inverses",
    "provisional_relationships",
    "temporary_relationships",
]:
    print(f"  {key.replace('_', ' ')}: {counts[key]}")
print(f"  findings: {len(findings)}")

for kind, source, field, detail in findings:
    print(f"  ERROR [{kind}] {source}: {field}: {detail}")

if findings:
    sys.exit(1)

print("RELATIONSHIP VALIDATION PASSED")
