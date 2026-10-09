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

The completed 100-step architecture-improvement record and detailed completion evidence are in:

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

Existing exceptions do not create competing root taxonomies. The 100-step architecture-improvement roadmap is complete; current quality state, known review items, and recommended next engineering work are controlled by `99_System/10_Docs/PosiBattery Runtime Handoff State.md`.

Folder authority here determines where knowledge is organized for navigation. It does not create engineering semantics; element types, governed properties, relationships, evidence provenance, and Local Model records remain authoritative for meaning.

## Current project capture and validation (2026-10-08)

The known PosiBattery project chats have been reconciled against repository artifacts in `80_Decisions and Planning/PosiBattery Project Chat to GitHub Traceability Audit 2026-10-08.md`. See also `80_Decisions and Planning/PosiBattery GitHub Capture and Reconciliation Audit 2026-10-08.md` and `99_System/10_Docs/PosiBattery Runtime Handoff State.md`.

The 100-step architecture and 28-step semantic-linking programs were completed and validated on their **historical October 5** snapshots. Later October 6 implementation edits are committed but have **current relationship-integrity failures** (256 missing inverse assertions and 75 incompatible endpoints on the audited model commit). Track recovery in [GitHub issue #2](https://github.com/spencerskelly/PosiBattery/issues/2); systematic Function-realization review coverage is tracked separately in [issue #3](https://github.com/spencerskelly/PosiBattery/issues/3). Do not claim the current branch is a passing/golden baseline before both blocking workflows pass on one revision. Local unpushed changes cannot be certified by a remote audit.

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
