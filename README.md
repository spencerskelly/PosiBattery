# MDSE Base Vault

Lean runtime base for MDSE release **0.8.0**.

Runtime schemas:
- relationships 1.35
- element-types 1.17
- Local Model 0.2

This vault intentionally does not contain the methodology workspace's Current State,
release manifest, Translator Definition, Decision Log, EA evidence, archives, or
Workbench design notes. Runtime rules are in
`99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` and the schemas under
`99_System/03_Schemas`.

## Opening the vault

1. Clone the vault repository and open the folder as a vault in Obsidian 1.13.0 or later.
2. When Obsidian asks, choose **Trust author and enable plugins** (turns off Restricted mode).
   Every plugin is already in the vault, pinned and configured; do not install or update plugins yourself.
3. MDSE Bootstrap asks once for your name and registers your author code, creating your note in
   `99_System/04_People`. Commit and sync with Git afterwards so others see it.
4. The status bar shows **MDSE: release OK** when the vault matches the controlled release.
   Click it to see the check; run **MDSE Bootstrap: Show release check** at any time.
5. Create notes with **Templater: Create new note from template** (templates in `99_System/05_Templates`).

## For the release owner

Before sharing, initialize `.vault.yaml` once with `Initialize-Vault.sh` or `Initialize-Vault.ps1`.
Initialization changes the vault UID/name and preserves `mdse_release`.
