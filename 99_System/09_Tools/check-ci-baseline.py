#!/usr/bin/env python3
"""Read-only PosiBattery exact-main-SHA GitHub Actions status. Requires authenticated gh.
Exit 0: core CI green; 1: incomplete/failed; 2: unavailable evidence.
"""
import json
import shutil
import subprocess
import sys

REPO = "spencerskelly/PosiBattery"
REQUIRED = ("MDSE Vault Audit", "Semantic Linking Completion Gate")

def run(*args, json_output=True):
    p = subprocess.run(["gh", *args], capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or str(p.returncode))
    return json.loads(p.stdout) if json_output else p.stdout.strip()

def main():
    if not shutil.which("gh"):
        print("BLOCKED: Install/authenticate GitHub CLI: gh auth login")
        return 2
    try:
        head = run("api", f"repos/{REPO}/branches/main", "--jq", ".commit.sha", json_output=False)
        runs = run("run", "list", "-R", REPO, "--branch", "main", "--limit", "100",
                   "--json", "databaseId,name,headSha,status,conclusion,createdAt,url")
    except Exception as e:
        print(f"BLOCKED: GitHub access unavailable: {e}")
        return 2
    if len(head) != 40:
        print("BLOCKED: unexpected branch SHA:", head)
        return 2
    print(f"Repository: {REPO}\nExact main SHA: {head}")
    failed = False
    for name in REQUIRED:
        hits = sorted((r for r in runs if r.get("name") == name and r.get("headSha") == head),
                      key=lambda r: r.get("createdAt", ""), reverse=True)
        if not hits:
            print(f"UNVERIFIED: {name} — missing exact-SHA run among 100 recent")
            failed = True
            continue
        r = hits[0]
        print(f"{name}: {r.get('status')}/{r.get('conclusion')} — {r.get('url')}")
        failed |= r.get("status") != "completed" or r.get("conclusion") != "success"
    for n in (2, 3, 5):
        try:
            issue = run("issue", "view", str(n), "-R", REPO,
                        "--json", "number,title,state,closedAt,updatedAt")
            print(f"Issue #{n}: {issue.get('state')} — {issue.get('title')}")
        except Exception as e:
            print(f"Issue #{n}: unverified ({e})")
    print("RESULT:", "INCOMPLETE/FAILED — inspect reported runs" if failed else
          "CORE CI GREEN on exact main SHA; local runtime still unverified")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
