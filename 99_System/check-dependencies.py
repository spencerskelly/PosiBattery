#!/usr/bin/env python3
"""Check function dependencies against product links (report-only by default).

For each row of Research/Function Design Dependencies.md, list products that perform the function
but have no hasDesign link to the design (or to a design under the class). With --strict, exit 1
when a row marked strong has such a gap and its Gap handling column says 'unreviewed'.
"""
import re, sys, glob, os, collections
try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
notes = {}
for pat in ("Products/**/*.md", "Product Functions/*.md", "Product Designs/*.md"):
    for f in glob.glob(os.path.join(ROOT, pat), recursive=True):
        t = open(f, encoding="utf-8").read(); m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
        if m:
            try: fm = yaml.safe_load(m.group(1)) or {}
            except Exception: continue
            notes[os.path.basename(f)[:-3]] = fm
def links(fm, k):
    out = []
    for x in fm.get(k) or []:
        m = re.search(r"\[\[([^\]|#]+)", str(x)); out.append(m.group(1) if m else str(x).strip())
    return out
def anc(x, seen=None):
    seen = seen if seen is not None else set()
    for y in links(notes.get(x, {}), "subtypeOf"):
        if y not in seen: seen.add(y); anc(y, seen)
    return seen
prods = {n: fm for n, fm in notes.items() if fm.get("type") == "Object" and not fm.get("abstract")}
reg = open(os.path.join(ROOT, "Research", "Function Design Dependencies.md"), encoding="utf-8").read().split("**Withdrawn")[0]
bad = []; total = 0
print("Function | design or class | strength | products lacking it | handling")
for line in reg.split("\n"):
    if not line.startswith("| [["): continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    if len(c) < 6: continue
    f = re.sub(r"[\[\]]", "", c[0]); strength, handling = c[3], c[4]
    for d in re.findall(r"\[\[([^\]]+)\]\]", c[1]):
        ps = [p for p, fm in prods.items() if f in links(fm, "performs")]
        miss = [p for p in ps if not (d in links(prods[p], "hasDesign") or any(d in anc(x) for x in links(prods[p], "hasDesign")))]
        total += 1
        if ps and miss:
            print(f"{f} | {d} | {strength} | {len(miss)} of {len(ps)} | {handling}")
            if strength == "strong" and handling.strip() in ("", "unreviewed"): bad.append((f, d))
print(f"\n{total} dependency pairs checked; {len(bad)} strong pairs with an unreviewed gap")
if "--strict" in sys.argv and bad:
    for f, d in bad: print("UNREVIEWED:", f, "->", d)
    sys.exit(1)
