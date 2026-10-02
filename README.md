# PosiBattery

PosiBattery is an MDSE working vault for industrial battery systems, beginning with material-handling equipment (MHE/forklift) and electric ground support equipment (eGSE/GSE), with adjacent battery markets used to find transferable technology and product concepts.

## Start here

- [[Battery Installed Devices/README_Battery Installed Devices|Battery Installed Devices]] — market reference for devices physically installed on or integrated into a battery.
- Current modeling authority for new work is the MDSE 0.8 pre-release contract carried from `Test_Vault_`: Ruleset 1.23, element schema 1.17, relationship schema 1.35, and Local Model schema 0.2.
- The `261001` repository was reviewed as 2026-10-01 architecture evidence, but the current `Test_Vault_` rules govern where they differ.

## Architecture transition status

This vault started from the older Ruleset 1.18 base and still contains legacy empty navigation/system scaffolding such as Thing, Interface, Context, and Transition folders. Those legacy artifacts are not authority for new model content on this branch.

The current contract changes the core model in several important ways:

- reusable engineering entities are **Objects**, not Things;
- interfaces are **Ports**, not Interface elements;
- contextual uses of reusable definitions are **Local Model occurrences** owned by the containing Object;
- local connections and flows belong to the assembly context that forms them;
- folders are navigation only;
- deployment in forklift, GSE, or another application is context, not a reason to duplicate the reusable commercial product definition.

See [[99_System/10_Docs/PosiBattery Architecture Alignment - 2026-10-02]] for the transition record.
