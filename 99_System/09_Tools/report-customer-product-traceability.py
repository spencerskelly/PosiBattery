#!/usr/bin/env python3
"""Report customer-to-product traceability for PosiBattery (report-only).

Regenerates the counts used by "Product to Customer Need Map" so the map can be
rebuilt from the vault links instead of by hand (see C269: the earlier
generator was not in the repository).

Chain: Actor --hasNeed--> Use Case (why) --realizedBy--> Function / Design
       --performedBy / designOf--> product (Object under 10_Products).

Routes per product (a product counts as reached through F, D, O or S):
  F  product performs a Function that a why Use Case is realizedBy.
  D  product has a Design that realizes, or is a dependency of, a Function on
     route F's list, or that a why Use Case is realizedBy directly.
  O  product is offeredWith a product reached by F (map rule since round 40).
  S  product satisfies a why Use Case directly (stated benefit, no modeled
     Function); weaker than F and reported separately.
  I  product inherits route F or D from a generalization (an ancestor through
     subtypeOf performs the Function or has the Design); owner rule 2026-10-17.
Abstract notes (abstract: true) are counted apart; per the owner (2026-10-17)
generic products are traced through their specializations.

Writes customer-product-traceability-report.md at the vault root (untracked;
delete before committing, like the other generated reports). Always exits 0.
"""
from __future__ import annotations
from pathlib import Path
from collections import defaultdict
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required")

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "customer-product-traceability-report.md"
LINK = re.compile(r"\[\[([^\]|#]+)")
FIELDS = ["hasNeed", "needOf", "participants", "realizedBy", "realizes", "performs",
          "performedBy", "hasDesign", "designOf", "dependencyOf", "dependsOn",
          "subtypeOf", "supertypeOf", "offeredWith", "satisfies", "satisfiedBy",
          "arisesIn", "givesRiseTo"]


def load():
    notes = {}
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith((".git", "99_System", ".obsidian")):
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        try:
            fm = yaml.safe_load(text[3:end]) or {}
        except Exception:
            continue
        rec = {"path": rel, "type": fm.get("type"), "subtype": fm.get("subtype"),
               "abstract": bool(fm.get("abstract"))}
        for k in FIELDS:
            v = fm.get(k) or []
            if isinstance(v, str):
                v = [v]
            rec[k] = [m.group(1).strip() for x in v for m in [LINK.match(str(x))] if m]
        notes[p.stem] = rec
    return notes


def main():
    G = load()
    ty = lambda n: G[n]["type"] if n in G else None
    prods = sorted(n for n in G if ty(n) == "Object" and G[n]["path"].startswith("10_Products/")
                   and not n.startswith("README"))
    concrete = [p for p in prods if not G[p]["abstract"]]
    why = [u for u in G if ty(u) == "Use Case" and G[u]["subtype"] == "why"]
    uc_actor = {u for u in why if any(ty(a) == "Actor" for a in G[u]["needOf"] + G[u]["participants"])}
    f_need = defaultdict(set)
    d_need = defaultdict(set)
    for u in uc_actor:
        for x in G[u]["realizedBy"]:
            if ty(x) == "Function":
                f_need[x].add(u)
            elif ty(x) == "Design":
                d_need[x].add(u)
    for d in [n for n in G if ty(n) == "Design"]:
        for f in G[d]["realizes"] + G[d]["dependencyOf"]:
            d_need[d] |= f_need.get(f, set())
    for f in list(f_need):
        for d in G[f]["realizedBy"] + G[f]["dependsOn"]:
            if ty(d) == "Design":
                d_need[d] |= f_need[f]
    route = {}
    needs = defaultdict(set)
    for p in prods:
        F = set().union(*[f_need.get(f, set()) for f in G[p]["performs"]])
        D = set().union(*[d_need.get(d, set()) for d in G[p]["hasDesign"]])
        S = {u for u in G[p]["satisfies"] if u in uc_actor}
        route[p] = {"F": F, "D": D, "S": S}
        needs[p] = F | D | S
    for p in prods:
        O = set()
        for o in G[p]["offeredWith"]:
            if o in route:
                O |= route[o]["F"]
        route[p]["O"] = O
        needs[p] |= O
    def ancestors(n, seen=None):
        seen = set() if seen is None else seen
        for a in G[n]["subtypeOf"]:
            if a in G and a not in seen:
                seen.add(a)
                ancestors(a, seen)
        return seen
    for p in prods:
        I = set()
        for a in ancestors(p):
            if a in route:
                I |= route[a]["F"] | route[a]["D"]
        route[p]["I"] = I
    for p in prods:
        needs[p] |= route[p]["I"]
    reached = [p for p in concrete if needs[p]]
    by = {k: [p for p in concrete if route[p][k]] for k in "FDOSI"}
    first = {"F": 0, "D": 0, "O": 0, "S": 0, "I": 0}
    for p in reached:
        for k in "FDOSI":
            if route[p][k]:
                first[k] += 1
                break
    missing = [p for p in concrete if not needs[p]]
    gen = [p for p in prods if G[p]["abstract"]]

    def kids(n, seen=None):
        seen = set() if seen is None else seen
        for c in G[n]["supertypeOf"]:
            if c in G and c not in seen:
                seen.add(c)
                kids(c, seen)
        return seen
    gen_traced = [p for p in gen if any(needs.get(k) for k in kids(p))]
    lines = ["# Customer to Product Traceability Report", "",
             f"- Concrete products: {len(concrete)}; reached: {len(reached)} "
             f"(first route F {first['F']}, D {first['D']}, O {first['O']}, S {first['S']}, I {first['I']}); "
             f"no route: {len(missing)}",
             f"- Products with each route (overlapping): F {len(by['F'])}, D {len(by['D'])}, "
             f"O {len(by['O'])}, S {len(by['S'])}, I {len(by['I'])}",
             f"- Abstract (generic) notes: {len(gen)}; traced through a specialization: {len(gen_traced)}",
             f"- Why Use Cases linked to an Actor: {len(uc_actor)} of {len(why)}", "",
             "## No route", ""]
    groups = defaultdict(list)
    for p in missing:
        groups["/".join(G[p]["path"].split("/")[1:-1])].append(p)
    for g in sorted(groups):
        lines.append(f"- **{g}** ({len(groups[g])}): " + ", ".join(f"[[{p}]]" for p in groups[g]))
    lines += ["", "## Generic notes with no traced specialization", ""]
    lines += [f"- [[{p}]]" for p in gen if p not in gen_traced]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:7]))
    print(f"report: {REPORT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
