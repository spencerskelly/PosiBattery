# PosiBattery Architecture Alignment — 2026-10-02

## Purpose

Record the architecture basis used before adding battery-market reference content.

## Authority reviewed

Current authority comes from `spencerskelly/Test_Vault_`:

- `99_System/10_Docs/00 - Current State.md`
- `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`
- `99_System/03_Schemas/element-types.yaml` 1.17
- `99_System/03_Schemas/relationships.yaml` 1.35
- `99_System/03_Schemas/local-model.yaml` 0.2
- `99_System/02_AI/AI_INSTRUCTIONS.md`

The 2026-10-01 import-model repository `spencerskelly/261001` was also reviewed. Current Test_Vault_ governance explicitly treats it as reference-only, so it is useful for architecture history and navigation ideas but does not override the current schema.

## Consequence for PosiBattery

PosiBattery was created from the September Ruleset 1.18 base. Its legacy system files used Thing, Interface, Context, Transition, `instanceOf`, `control`, and `boundary`. Those are not used for new content in this branch.

This branch overlays the current schemas, AI instructions, Spencer author identity, Ruleset 1.23, and the current Object/Info templates needed by this first market-reference slice. It intentionally does **not** delete all legacy scaffold or claim that the complete runtime base migration is finished.

## Modeling rule for the market reference

A commercial battery-mounted or battery-integrated device is modeled once as a reusable **Object** definition.

Application statements such as “installed on this forklift battery” or “used in this GSE battery pack” are contextual uses. When we model a specific battery/product architecture, those uses belong in the owning Object's **Local Model** as occurrences. We do not create duplicate product definitions for each application.

Generic device families may be abstract Objects and commercial products may be true reusable specializations of those families through `subtypeOf`.

Ports, Item Flows, Functions, Requirements, and deeper product structure are added only when evidence or an engineering question justifies them. The first market pass should not invent interfaces or behavior that vendor evidence does not establish.

## Research evidence rule

For “market today” claims:

1. prefer current manufacturer/product pages and current manuals or data sheets;
2. record the evidence date;
3. distinguish current, obsolete, and unclear market status;
4. preserve unknowns rather than infer missing specifications;
5. record battery-adjacent products separately from products physically installed on or integrated into the battery.
