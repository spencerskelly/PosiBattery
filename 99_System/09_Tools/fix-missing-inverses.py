#!/usr/bin/env python3
"""Add the missing inverse relationship to target notes.

Runs check-relationships.py, reads its `missing_inverse` findings, and writes the
expected inverse field onto each target note's frontmatter.

Skips (and reports) any edge whose forward link is also flagged `endpoint_incompatible`:
those links point at the wrong kind of note, so the forward link needs a human decision
and adding an inverse would only cement the mistake.

Usage (from repo root):
  python 99_System/09_Tools/fix-missing-inverses.py            # dry run
  python 99_System/09_Tools/fix-missing-inverses.py --apply    # write changes
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "99_System" / "09_Tools" / "check-relationships.py"

MISSING = re.compile(r"ERROR \[missing_inverse\] (.+?\.md): (\w+): (.+?\.md) expected (\w+)\s*$")
ENDPOINT = re.compile(r"ERROR \[endpoint_incompatible\] (.+?\.md): (\w+): .* target=(.+?\.md)\s*$")


def run_checker() -> list[str]:
    proc = subprocess.run([sys.executable, str(CHECKER)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode == 2:
        sys.exit(proc.stderr or "checker could not run (is PyYAML installed?)")
    return proc.stdout.splitlines()


def link_for(source_rel: str, stems: dict[str, list[str]]) -> str:
    stem = source_rel[:-3]
    name = Path(stem).name
    return f"[[{name}]]" if len(stems[name]) == 1 else f"[[{stem}]]"


def split_frontmatter(text: str):
    nl = "\r\n" if "\r\n" in text else "\n"
    if not text.startswith("---" + nl):
        return None
    end = text.find(nl + "---", 3 + len(nl))
    if end < 0:
        return None
    return nl, text[: end + len(nl)], text[end + len(nl):]  # head incl. trailing newline, rest starts at closing ---


def add_link(head: str, nl: str, field: str, link: str):
    """Return (new_head, status). Head is frontmatter text up to (not including) the closing '---'."""
    item = f'  - "{link}"'
    lines = head.split(nl)  # last element is '' because head ends with nl
    key = re.compile(rf"^{re.escape(field)}:\s*(.*)$")
    for i, line in enumerate(lines):
        m = key.match(line)
        if not m:
            continue
        if m.group(1).strip() not in ("", "|", ">"):
            return head, "inline-value"  # scalar / flow list: leave for a human
        j = i + 1
        last = i
        while j < len(lines) and (lines[j].startswith("  - ") or lines[j].startswith("- ")):
            last = j
            j += 1
        if any(link in l for l in lines[i + 1 : last + 1]):
            return head, "already-present"
        lines.insert(last + 1, item)
        return nl.join(lines), "appended"
    # field absent: insert before closing marker (end of head)
    insert_at = len(lines) - 1 if lines and lines[-1] == "" else len(lines)
    lines[insert_at:insert_at] = [f"{field}:", item]
    return nl.join(lines), "added-field"


def main() -> int:
    apply = "--apply" in sys.argv
    out = run_checker()

    incompatible = {m.groups() for l in out if (m := ENDPOINT.search(l))}
    incompatible = {(s, f, t) for s, f, t in incompatible}

    todo: dict[tuple[str, str], list[str]] = defaultdict(list)  # (target, inverse) -> [source,...]
    skipped = []
    for l in out:
        m = MISSING.search(l)
        if not m:
            continue
        src, field, tgt, inv = m.groups()
        if (src, field, tgt) in incompatible:
            skipped.append((src, field, tgt, inv))
            continue
        if src not in todo[(tgt, inv)]:
            todo[(tgt, inv)].append(src)

    stems: dict[str, list[str]] = defaultdict(list)
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        stems[p.stem].append(p.relative_to(ROOT).as_posix())

    stats = defaultdict(int)
    manual = []
    for (tgt, inv), sources in sorted(todo.items()):
        path = ROOT / tgt
        text = path.read_bytes().decode("utf-8")  # bytes: keep CRLF intact
        parts = split_frontmatter(text)
        if not parts:
            manual.append((tgt, inv, "no frontmatter"))
            continue
        nl, head, rest = parts
        for src in sources:
            head, status = add_link(head, nl, inv, link_for(src, stems))
            stats[status] += 1
            if status == "inline-value":
                manual.append((tgt, inv, "field is not a block list; add " + link_for(src, stems) + " by hand"))
        if apply:
            path.write_bytes((head + rest).encode("utf-8"))

    total = sum(len(v) for v in todo.values())
    print(f"{'APPLIED' if apply else 'DRY RUN'}: {total} inverse links across {len(todo)} (note, field) pairs")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
    print(f"skipped (forward link has wrong endpoint types, fix the forward link): {len(skipped)}")
    for s in skipped[:10]:
        print(f"  {s[0]} --{s[1]}--> {s[2]}")
    if len(skipped) > 10:
        print(f"  ... {len(skipped) - 10} more")
    for m in manual:
        print(f"  MANUAL: {m[0]}: {m[1]}: {m[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
