#!/usr/bin/env python3
"""check-names.py - enforce the PosiBattery naming rule: no two notes share a name.
Checks (run from the vault root): duplicate file names (case-insensitive) outside 99_System, aliases that equal another note's name,
aliases used by more than one note, and duplicate aliases inside one note. On a collision, rename one note with an identifier after the
name in parentheses (the brand or the application), for example 'Battery Tracker (Hyster)'. Exit code 1 if any problem is found."""
import os, re, sys, glob, collections
SKIP = (".git/", ".obsidian/", "99_System/")
names = collections.defaultdict(list); aliases = collections.defaultdict(list); problems = []
for f in glob.glob("**/*", recursive=True):
    if not os.path.isfile(f) or f.startswith(SKIP): continue
    base, ext = os.path.splitext(os.path.basename(f))
    if ext not in (".md", ".canvas", ".base"): continue
    if base.startswith(("README_", "BASE_", "CANVAS_")): continue
    names[base.lower()].append(f)
    if ext == ".md":
        t = open(f, encoding="utf-8").read(); m = re.search(r"## Aliases\n\n(.*?)\n\n## Former", t, re.S); seen = []
        for a in ([x[2:].strip() for x in m.group(1).split("\n") if x.startswith("- ")] if m else []):
            if a.lower() in seen: problems.append(f"duplicate alias in {base}: {a}")
            seen.append(a.lower()); aliases[a.lower()].append(base)
for n, fs in names.items():
    if len(fs) > 1: problems.append(f"same note name: {n}: {fs}")
for a, bs in aliases.items():
    if len(set(bs)) > 1: problems.append(f"alias used by several notes: '{a}': {sorted(set(bs))}")
    if a in names and a not in [b.lower() for b in bs]: problems.append(f"alias equals another note's name: '{a}' ({sorted(set(bs))}) vs {names[a]}")
print("name check:", "PASSED" if not problems else f"{len(problems)} problem(s)"); [print(" ", p) for p in problems]
sys.exit(1 if problems else 0)
