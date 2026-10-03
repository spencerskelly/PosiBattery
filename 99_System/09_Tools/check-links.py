#!/usr/bin/env python3
"""Check every web address cited in the vault's model notes.

Usage:   python3 99_System/09_Tools/check-links.py            # test all addresses, write Research/Link Check Report.md
         python3 99_System/09_Tools/check-links.py --list     # only list and classify addresses (no network)
Needs only the Python standard library. Run it from the vault root on a machine with internet access.
A result is OK when the server answers 200 and, for a file address, returns a document type (not an HTML page).
It flags: HTTP errors, redirects that land on a home page, and 'file' addresses that return HTML.
"""
import re, sys, glob, os, urllib.request, urllib.parse, urllib.error, collections, datetime
ROOT = os.getcwd()
FOLDERS = ["Battery Products", "Research", "Product Functions", "Product Designs", "Organizations", "Performance Metrics", "Source Documents"]
URLRE = re.compile(r"https?://[^\s<>)\]|]+")
LANDSEG = {"products", "product", "batteries-and-chargers", "applications", "solutions", "trak", "company", "about", "motive-power", "motive-power-solutions"}
def classify(u):
    p = urllib.parse.urlparse(u); path = p.path or "/"; segs = [s for s in path.split("/") if s]
    if re.search(r"\.(pdf|docx?|xlsx?|zip)(\?|$)", u.lower()) or ("/downloads/" in u.lower() and "/~/" in u.lower()): return "file"
    if (not segs and not p.query) or (len(segs) == 1 and re.fullmatch(r"[a-z]{2}(-[a-z]{2})?", segs[0])) or (segs and segs[-1].lower() in LANDSEG and not p.query): return "home-or-landing"
    return "page"
usage = collections.defaultdict(set)
for d in FOLDERS:
    for f in glob.glob(os.path.join(d, "**", "*.md"), recursive=True):
        for u in URLRE.findall(open(f, encoding="utf-8").read()): usage[u.rstrip(".,;")].add(os.path.basename(f)[:-3])
urls = sorted(usage)
if "--list" in sys.argv:
    for u in urls: print(classify(u), u)
    print(len(urls), "addresses"); sys.exit(0)
def check(u):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (link-check)"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            ct = (r.headers.get("Content-Type") or "").lower(); final = r.geturl(); code = r.status
    except urllib.error.HTTPError as e: return "HTTP %s" % e.code, "", ""
    except Exception as e: return "ERROR %s" % type(e).__name__, "", ""
    flags = []
    if classify(u) == "file" and "pdf" not in ct and "octet" not in ct and "msword" not in ct and "officedocument" not in ct and "zip" not in ct: flags.append("file address returned " + ct.split(";")[0])
    fp = urllib.parse.urlparse(final)
    if classify(final) == "home-or-landing" and classify(u) != "home-or-landing": flags.append("redirected to a home or landing page: " + final)
    return ("OK" if not flags else "CHECK"), ct.split(";")[0], "; ".join(flags)
rows = []
for i, u in enumerate(urls, 1):
    status, ct, note = check(u); rows.append((status, u, ct, note, sorted(usage[u])))
    print(i, len(urls), status, u)
bad = [r for r in rows if r[0] != "OK"]
out = ["# Link Check Report", "", "Generated " + datetime.date.today().isoformat() + " by check-links.py. " + str(len(rows)) + " addresses; " + str(len(bad)) + " need attention.", "", "| Status | Address | Content type | Note | Used in |", "|---|---|---|---|---|"]
for s, u, ct, n, used in sorted(rows, key=lambda r: (r[0] == "OK", r[0])): out.append("| %s | <%s> | %s | %s | %s |" % (s, u, ct, n, ", ".join("[[%s]]" % x for x in used[:5])))
open(os.path.join("Research", "Link Check Report.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("Wrote Research/Link Check Report.md")
