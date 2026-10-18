#!/usr/bin/env python3
"""Validate productCategory and category facet properties on 10_Products Objects.

Checks, against classOptionalProperties.Object in element-types.yaml:
- productCategory is one of the declared values;
- a category facet appears only on notes whose productCategory is in the facet's category list;
- facet value types (number, list[number], enum, list[enum]) and enum membership;
- <quantity>Min is not greater than <quantity>Max;
- company is a link to a note tagged organization, and equals the first madeBy link where madeBy exists;
- declared property names do not collide with relationships.yaml fields.

Run from the vault root:
    python 99_System/09_Tools/check-product-facets.py
Exit code 1 means a facet invariant is violated.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "99_System" / "03_Schemas" / "element-types.yaml"
PRODUCTS = ROOT / "10_Products"


def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
props = {p["name"]: p for p in schema["classOptionalProperties"]["Object"]}
categories = props["productCategory"]["allowed"]
facets = {n: p for n, p in props.items() if p.get("category")}

findings = []
REL = ROOT / "99_System" / "03_Schemas" / "relationships.yaml"
rel_fields = set()


def collect(node):
    if isinstance(node, dict):
        for key, val in node.items():
            if key in ("forward", "inverse", "field") and isinstance(val, str):
                rel_fields.add(val)
            collect(val)
    elif isinstance(node, list):
        for item in node:
            collect(item)


collect(yaml.safe_load(REL.read_text(encoding="utf-8")))
for name in sorted(set(props) & rel_fields):
    findings.append(("99_System/03_Schemas/element-types.yaml", f"property {name} collides with a relationship field"))
ORGS = set()
for _p in ROOT.rglob("*.md"):
    if ".obsidian" in _p.parts:
        continue
    _fm = frontmatter(_p)
    if _fm and "organization" in (_fm.get("tags") or []):
        ORGS.add(_p.stem)
checked = with_facets = with_company = 0
import re as _re
def _target(v):
    m = _re.fullmatch(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", v) if isinstance(v, str) else None
    return m.group(1).strip() if m else None
for path in sorted(PRODUCTS.rglob("*.md")):
    fm = frontmatter(path)
    if not fm or fm.get("type") != "Object":
        continue
    checked += 1
    rel = path.relative_to(ROOT).as_posix()
    cat = fm.get("productCategory")
    if cat is not None and cat not in categories:
        findings.append((rel, f"productCategory {cat!r} not declared"))
    if "company" in fm:
        with_company += 1
        tgt = _target(fm["company"])
        if tgt is None or tgt not in ORGS:
            findings.append((rel, f"company {fm['company']!r} is not a link to an organization note"))
        elif fm.get("madeBy"):
            first = _target(fm["madeBy"][0])
            if first != tgt:
                findings.append((rel, f"company {tgt!r} differs from first madeBy {first!r}"))
    present = [k for k in facets if k in fm]
    if present:
        with_facets += 1
    for k in present:
        spec, v = facets[k], fm[k]
        if cat not in spec["category"]:
            findings.append((rel, f"{k} not valid for productCategory {cat!r}"))
        kind = spec["value"]
        if kind == "number" and not is_number(v):
            findings.append((rel, f"{k} must be a number, got {v!r}"))
        elif kind == "list[number]" and not (isinstance(v, list) and v and all(is_number(x) for x in v)):
            findings.append((rel, f"{k} must be a non-empty list of numbers, got {v!r}"))
        elif kind == "enum" and v not in spec.get("allowed", []):
            findings.append((rel, f"{k} value {v!r} not allowed"))
        elif kind == "list[enum]" and not (isinstance(v, list) and v and all(x in spec.get("allowed", []) for x in v)):
            findings.append((rel, f"{k} values {v!r} not allowed"))
        elif kind == "boolean" and not isinstance(v, bool):
            findings.append((rel, f"{k} must be true or false, got {v!r}"))
    for k in present:
        if k.endswith("Min"):
            mx = k[:-3] + "Max"
            if mx in fm and is_number(fm[k]) and is_number(fm[mx]) and fm[k] > fm[mx]:
                findings.append((rel, f"{k} {fm[k]} is greater than {mx} {fm[mx]}"))

print(f"  product Objects checked: {checked}")
print(f"  with facet properties: {with_facets}")
print(f"  with company: {with_company}")
print(f"  declared categories: {len(categories)}; declared facets: {len(facets)}")
print(f"  findings: {len(findings)}")
for rel, msg in findings[:50]:
    print(f"  - {rel}: {msg}")
print("PRODUCT FACET VALIDATION " + ("FAILED" if findings else "PASSED"))
sys.exit(1 if findings else 0)
