# PosiBattery MDSE Vault

PosiBattery is an engineering vault running the lean MDSE **0.8.1** runtime.

Runtime:
- Workbench 0.1.17
- Bootstrap 0.3.1
- relationships 1.36
- element-types 1.18
- Local Model 0.2
- Modeling Ruleset 1.23

For AI tools or anyone rebuilding/reorganizing the vault, the authoritative filesystem guidance is:

`99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`

PosiBattery-specific organization and migration guidance is in:

`99_System/10_Docs/PosiBattery Model Organization and Handoff.md`

The active incremental architecture-improvement sequence is controlled by:

`80_Decisions and Planning/PosiBattery Architecture Improvement Plan.md`

The authoritative current runtime handoff is in:

`99_System/10_Docs/PosiBattery Runtime Handoff State.md`

Runtime modeling rules are in:

`99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`

AI authoring rules are in:

`99_System/02_AI/AI_INSTRUCTIONS.md`

The vault intentionally does not contain the methodology workspace's Current State, release manifest, Translator Definition, Decision Log, EA evidence, archives, or Workbench design notes. The engineering vault is a runtime artifact, not a copy of the methodology workspace.

## Authoritative PosiBattery vault architecture

The numbered domain structure is the authoritative vault-level information architecture for PosiBattery. New stable content and future migrations should use these domains:

- [[README_Products|10 Products]]
- [[README_Product Architecture|20 Product Architecture]]
- [[README_Product Capabilities|30 Product Capabilities]]
- [[README_Use and Operations|40 Use and Operations]]
- [[README_Customer Needs|50 Customer Needs]]
- [[README_Stakeholders and Ecosystem|60 Stakeholders and Ecosystem]]
- [[README_Research and Evidence|70 Research and Evidence]]
- [[README_Decisions and Planning|80 Decisions and Planning]]
- [[README_Definitions and Reusable Reference|90 Definitions and Reusable Reference]]
- [[README_System|99 System]]

Existing exceptions do not create competing root taxonomies. Several areas inside these domains are still transitional or pending migration review. In particular, mixed-content folders and the remaining underscore-prefixed research roots are being reconciled through `80_Decisions and Planning/PosiBattery Architecture Improvement Plan.md`.

Folder authority here determines where knowledge is organized for navigation. It does not create engineering semantics; element types, governed properties, relationships, evidence provenance, and Local Model records remain authoritative for meaning.

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
