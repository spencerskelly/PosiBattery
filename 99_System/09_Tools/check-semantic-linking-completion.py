#!/usr/bin/env python3
"""Final semantic-linking completion acceptance check.

Consumes the traceability report generated in the same workflow and enforces
the program-level conditions that must be zero. Accepted named engineering
gaps are validated separately by the Step 26 and Step 27 validators.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/"traceability-quality-report.md"

if not REPORT.exists():
    raise SystemExit("traceability-quality-report.md not found; run report-traceability.py first")

text=REPORT.read_text(encoding="utf-8")
required_zero=[
    "unexplained isolated model elements",
    "applicable unexplained findings",
    "disposition registry errors",
]

values={}
for key in required_zero:
    m=re.search(rf"\|\s*{re.escape(key)}\s*\|\s*(\d+)\s*\|",text,re.I)
    if not m:
        raise SystemExit(f"Could not read required completion metric: {key}")
    values[key]=int(m.group(1))

print("semantic linking completion acceptance")
for key,value in values.items():
    print(f"  {key}: {value}")

bad={k:v for k,v in values.items() if v!=0}
if bad:
    for key,value in bad.items():
        print(f"  FAIL {key}: {value}")
    raise SystemExit(2)

print("SEMANTIC LINKING COMPLETION ACCEPTANCE PASSED")
