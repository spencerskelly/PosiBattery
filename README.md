# PosiBattery MDSE Vault

PosiBattery is an engineering vault running the lean MDSE **0.8.0** runtime.

Runtime schemas:
- relationships 1.35
- element-types 1.17
- Local Model 0.2
- Modeling Ruleset 1.23

For AI tools or anyone rebuilding/reorganizing the vault, the authoritative filesystem guidance is:

`99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`

Runtime modeling rules are in:

`99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`

AI authoring rules are in:

`99_System/02_AI/AI_INSTRUCTIONS.md`

The vault intentionally does not contain the methodology workspace's Current State, release manifest, Translator Definition, Decision Log, EA evidence, archives, or Workbench design notes. The engineering vault is a runtime artifact, not a copy of the methodology workspace.

## Current model areas

The present PosiBattery content includes:

- Customer Actors
- Customer Needs
- Definitions
- Organizations
- Performance Metrics
- Product Designs
- Product Functions
- Products
- Research
- Source Documents
- Downloads

These folders support navigation only. They do not create engineering semantics; relationships and schemas do that.

## Opening the vault

1. Clone the repository and open the folder as a vault in Obsidian 1.13.0 or later.
2. When Obsidian asks, choose **Trust author and enable plugins**.
   Every plugin is already in the vault, pinned and configured; do not install or update plugins yourself.
3. MDSE Bootstrap asks once for your name and registers your author code, creating your note in
   `99_System/04_People`. Commit and sync with Git afterwards so others see it.
4. The status bar shows **MDSE: release OK** when the vault matches the controlled release.
   Click it to see the check; run **MDSE Bootstrap: Show release check** at any time.
5. Create notes with **Templater: Create new note from template** using templates in `99_System/05_Templates`.

## For the release owner

Before sharing a clean base, initialize `.vault.yaml` once with `Initialize-Vault.sh` or `Initialize-Vault.ps1`.
Initialization changes the vault UID/name and preserves `mdse_release`.
