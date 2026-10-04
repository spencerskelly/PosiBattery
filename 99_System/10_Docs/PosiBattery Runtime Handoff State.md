# PosiBattery Runtime Handoff State

## Current controlled state

- Repository: `spencerskelly/PosiBattery`
- Branch: `main`
- Vault name: `PosiBattery`
- Vault UID: `20261004152953762skellyspencer`
- MDSE release: `0.8.0`
- Modeling Ruleset: `1.23`
- Workbench: `0.1.17`
- Bootstrap: `0.3.1`
- relationships schema: `1.35`
- element-types schema: `1.17`
- Local Model schema: `0.2`

## Handoff readiness

The vault now has:

- initialized vault identity;
- current v0.8 runtime schemas;
- current AI instructions;
- explicit filesystem contract;
- current verified Workbench candidate;
- matching Bootstrap candidate;
- matching controlled plugin lock;
- PosiBattery-specific model-organization guidance;
- Git history preserving the changes.

## Important interpretation

The existing root content folders are established PosiBattery knowledge areas and remain valid.

The newer numbered Product folders are the preferred navigation pattern for future stable product-model work, but existing notes should not be bulk-moved simply for visual consistency.

## Next tool startup sequence

Read:

1. `AGENTS.md`
2. `99_System/02_AI/AI_INSTRUCTIONS.md`
3. `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`
4. `99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`
5. `99_System/10_Docs/PosiBattery Model Organization and Handoff.md`

Then run the MDSE Bootstrap release check and Workbench diagnostics inside Obsidian before large edits.

## Known limitation

Workbench 0.1.17 is the last verified candidate from the WB-106 disposable acceptance repository, not a separately promoted final Workbench release. It passed the automated test suite, 60k semantic-cache smoke test, and production build through performance/stability Step 24.

Treat any later Workbench build as newer only when its controlled artifact and plugin lock have both been intentionally promoted.
