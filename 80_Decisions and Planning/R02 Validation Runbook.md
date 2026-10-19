# R02 One-command Validation Runbook

**Purpose:** Replace repeated GitHub connector status checks with one reproducible read-only execution and a durable, inspectable SHA-specific report. This document is instructions, not validation evidence.

## One command

On a Mac, Windows (Python environment) or Linux machine with GitHub CLI installed and authenticated, from a current local clone:

```bash
git pull --ff-only origin main
python3 99_System/09_Tools/check-ci-baseline.py
```

On Windows, use `py -3` instead of `python3` when appropriate. The helper checks the actual GitHub `main` branch SHA through the API, queries Actions runs, and reports the state of issues #2, #3 and #5. It changes no repository files. GitHub CLI setup: `gh auth login` (once); check via `gh auth status`.

**Return codes:** 0 = both core Actions workflows completed successfully for the exact current `main` SHA; 1 = a workflow is absent, pending or failed; 2 = GitHub CLI/network/auth unavailable. A code 0 is **CI evidence only**, not proof that local Obsidian bootstrap or Workbench has been tested.

The two required workflows are `MDSE Vault Audit` and `Semantic Linking Completion Gate`. The second currently contains the three issue #5 checks (weak traceability priority, end-to-end product chain, high-value evidence). Only trust the checks for the same exact SHA. R02 baseline instructions must not infer success from an empty legacy commit-status response.

## If the report is incomplete

Open the reported workflow URL or browse [Actions](https://github.com/spencerskelly/PosiBattery/actions). If jobs are pending, rerun the command after the job completes. If a workflow is not present for the SHA, use GitHub Actions' `Run workflow` control for the corresponding workflow on `main`; then rerun the helper. If it fails, inspect step-level reports and artifacts and record exact failure rather than editing model links to suppress diagnostics.

For issue status: `gh issue view 2 -R spencerskelly/PosiBattery --json state,closedAt,title` (repeat for 3 and 5).

## Separate local runtime acceptance

A completely verified release additionally requires a clean checkout and execution of the precise commands in:
- `.github/workflows/mdse-vault-audit.yml`
- `.github/workflows/semantic-linking-completion-gate.yml`

These use Ubuntu 24.04, Python 3.12 + PyYAML, and Node 22 for the semantic gate. Workbench/Obsidian startup requires an interactive clean-vault test and is not proven by green CI.

## Working rule

- Use one R02 checkpoint per *changed finding or real test run*, not one per attempt to read the same inaccessible Actions interface.
- Do not repeatedly commit ChatReview just to say Actions remain inaccessible.
- Preserve one tested SHA, run URLs, conclusions, failing steps and dispositions in ChatReview.md. After release baseline, update the Runtime Handoff.
- Public third-party / marked-confidential PDF risks are R01 and remain urgent, owner-controlled, independent of R02.
