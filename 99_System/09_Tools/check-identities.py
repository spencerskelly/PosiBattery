#!/usr/bin/env python3
"""Complete MDSE identity validation for PosiBattery.

Checks:
- current IDs: format, uniqueness, and type-prefix compatibility where type is present;
- note UIDs: 30-character format, uniqueness, and registered author code;
- former IDs: format, uniqueness/reservation, and no collision with any current ID;
- Local Model identities: governed prefix/token format, globally unique token namespace,
  no collision with note UIDs, and registered author code.

Run from the vault root:
    python 99_System/09_Tools/check-identities.py
Exit code 1 means an identity invariant is violated.
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
SCHEMA = ROOT / "99_System" / "03_Schemas" / "element-types.yaml"
AUTHORS = ROOT / "99_System" / "03_Schemas" / "authors.yaml"
PEOPLE = ROOT / "99_System" / "04_People"

ID_RE = re.compile(r"^[A-Z][A-Z0-9]*-\d{5}$")
UID_RE = re.compile(r"^\d{17}[a-z-]{13}$")
LOCAL_RE = re.compile(r"^\^(part|ep|conn|flow)-(\d{17}[a-z-]{13})\s*$")
FORMER_LINE_RE = re.compile(r"^\s*[-*]\s*([A-Z][A-Z0-9]*-\d{5})\b")
LOCAL_PREFIXES = {"part", "ep", "conn", "flow"}


def read_yaml(path: Path):
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


schema = read_yaml(SCHEMA)
prefix_by_type = {}
for rec in schema.get("classes", []):
    if isinstance(rec, dict) and rec.get("name") and rec.get("prefix"):
        prefix_by_type[str(rec["name"])] = str(rec["prefix"])

known_author_codes = set()
authors = read_yaml(AUTHORS)
for rec in authors.get("ai_authors", []):
    if isinstance(rec, dict) and rec.get("code"):
        known_author_codes.add(str(rec["code"]))
unmapped = authors.get("unmapped")
if isinstance(unmapped, dict) and unmapped.get("code"):
    known_author_codes.add(str(unmapped["code"]))

for p in PEOPLE.glob("*.md"):
    fm = frontmatter(p.read_text(encoding="utf-8", errors="replace"))
    code = fm.get("code")
    if code:
        known_author_codes.add(str(code))
    for old in fm.get("previousCodes") or []:
        known_author_codes.add(str(old))

current_ids = defaultdict(list)
former_ids = defaultdict(list)
uids = defaultdict(list)
local_tokens = defaultdict(list)
problems = []

markdown_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
identity_notes = 0

for p in markdown_files:
    rel = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(text)
    current_id = str(fm.get("id", "") or "").strip()
    uid = str(fm.get("uid", "") or "").strip()
    typ = str(fm.get("type", "") or "").strip()

    if current_id or uid:
        identity_notes += 1

    if current_id:
        current_ids[current_id].append(rel)
        if not ID_RE.fullmatch(current_id):
            problems.append(("invalid current ID format", rel, current_id))
        expected = prefix_by_type.get(typ)
        if expected and not current_id.startswith(expected + "-"):
            problems.append(("ID/type prefix mismatch", rel, f"{current_id} expected {expected}- for {typ}"))

    if uid:
        uids[uid].append(rel)
        if not UID_RE.fullmatch(uid):
            problems.append(("invalid UID format", rel, uid))
        else:
            code = uid[17:]
            if code not in known_author_codes:
                problems.append(("unregistered UID author code", rel, code))

    # Current contract reserves former IDs found in the controlled body section.
    lines = text.splitlines()
    in_former = False
    for line in lines:
        if re.fullmatch(r"##\s+Former ids\s*", line, flags=re.I):
            in_former = True
            continue
        if in_former and line.startswith("## "):
            in_former = False
        if in_former:
            m = FORMER_LINE_RE.match(line)
            if m:
                former_ids[m.group(1)].append(rel)

    # Also honor legacy/frontmatter formerIds if encountered.
    raw_former = fm.get("formerIds") or []
    if isinstance(raw_former, str):
        raw_former = [raw_former]
    if isinstance(raw_former, list):
        for x in raw_former:
            x = str(x).strip()
            if x:
                former_ids[x].append(rel)

    for line in lines:
        m = LOCAL_RE.fullmatch(line.strip())
        if not m:
            continue
        kind, token = m.groups()
        local_id = f"{kind}-{token}"
        local_tokens[token].append((rel, local_id))
        if token[17:] not in known_author_codes:
            problems.append(("unregistered Local Model author code", rel, f"{local_id}: {token[17:]}"))

for ident, paths in current_ids.items():
    if len(paths) > 1:
        problems.append(("duplicate current ID", ident, ", ".join(paths)))

for uid, paths in uids.items():
    if len(paths) > 1:
        problems.append(("duplicate note UID", uid, ", ".join(paths)))

for ident, paths in former_ids.items():
    if not ID_RE.fullmatch(ident):
        problems.append(("invalid former ID format", ident, ", ".join(paths)))
    if len(paths) > 1:
        problems.append(("duplicate former ID reservation", ident, ", ".join(paths)))
    if ident in current_ids:
        problems.append(("former ID reused as current ID", ident, f"former: {paths}; current: {current_ids[ident]}"))

for token, records in local_tokens.items():
    if len(records) > 1:
        problems.append(("duplicate Local Model token", token, str(records)))
    if token in uids:
        problems.append(("Local Model token collides with note UID", token, f"local: {records}; note: {uids[token]}"))

print("identity validation")
print(f"  markdown files scanned: {len(markdown_files)}")
print(f"  notes with identity fields: {identity_notes}")
print(f"  current IDs: {len(current_ids)}")
print(f"  note UIDs: {len(uids)}")
print(f"  former ID reservations: {len(former_ids)}")
print(f"  Local Model records: {sum(len(v) for v in local_tokens.values())}")
print(f"  Local Model identity tokens: {len(local_tokens)}")
print(f"  registered author codes: {len(known_author_codes)}")
print(f"  findings: {len(problems)}")

for kind, key, detail in problems:
    print(f"  ERROR [{kind}] {key}: {detail}")

if problems:
    sys.exit(1)

print("IDENTITY VALIDATION PASSED")
