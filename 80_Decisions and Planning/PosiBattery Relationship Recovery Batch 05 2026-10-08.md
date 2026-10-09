# PosiBattery Relationship Recovery — Batch 05 (2026-10-08)

## Controlled repair
- **Review branch:** `recovery/relationship-invariants-batch-01`, [draft PR #4](https://github.com/spencerskelly/PosiBattery/pull/4). **Main is unchanged.**
- **Starting commit:** `1505cbc3d36bf78e6a50ca133a2223935fa7f2f1`; independently verified baseline: **160** relationship diagnostics = 18 `endpoint_incompatible` + 142 `missing_inverse`, as recorded in [[PosiBattery Relationship Recovery Batch 04 2026-10-08]].
- **Purpose:** eliminate product-to-product misuse of `hasDesign` and correct the already evidenced reciprocal Crown watering-supply compatibility links. `hasDesign` may target **Design**, not another **Object**.

## Changes and evidence

| Source Object | Old field → new field | Linked product Object | Evidence for semantics |
| --- | --- | --- | --- |
| [[Midac Aquamatic Watering System]] | `hasDesign` → `offeredWith` | [[Midac PzS Traction Battery]] | The battery already lists Aquamatic under `offeredWith`; dealer identifies it as an optional accessory |
| [[Exide Automatic Watering System and Level Sensor]] | `hasDesign` → `offeredWith` | [[Exide MARATHON Battery]] | The battery already lists the watering kit under `offeredWith`; GNB product overview documents available watering accessories |
| [[Crown V-Force Single Point Watering System]] | `hasDesign` → `integratesWith` | [[Philadelphia Scientific Water Injector System]] | Crown parts listing names Philly Scientific Injector as a compatible water supply for V-Force float kits |
| [[PosiCharge PosiConnect]] | `hasDesign` → `offeredWith` | [[PosiCharge PosiGuard]] | PosiGuard already lists PosiConnect under `offeredWith`; app and public product notes establish supported BMID management |
| [[Stryten inCOMMAND]] | `hasDesign` → `offeredWith` | [[Stryten M-Series Li610 Battery]] | Li610 already lists inCOMMAND under `offeredWith`; Stryten source says Li610 integrates with inCOMMAND |
| [[Philadelphia Scientific Water Injector System]] | `hasPart` → `integratesWith` | [[Crown V-Force Single Point Watering System]] | Reciprocal companion to Crown kit's documented compatibility; independent finished products are not parts of each other |
| [[Philadelphia Scientific Stealth Watering System]] | `hasPart` → `integratesWith` | [[Crown V-Force Single Point Watering System]] | Crown already lists Stealth under `integratesWith`, and the cited Crown parts listing confirms supported water supply |

The last two repairs intentionally preserve Philadelphia Scientific products' *actual* component links (e.g. watering manifold, shutoff valves) and remove only erroneous **entire commercial product** containment. The Crown note retains `integratesWith: [[Philadelphia Scientific Stealth Watering System]]` and gains `[[Philadelphia Scientific Water Injector System]]`. No model IDs, UIDs, sources, explanatory bodies, legitimate Design allocations, or unrelated relationships were changed.

## Batch 05 predicted gate delta (not a CI assertion)

Baseline log patterns:
- Five product `hasDesign: Object -> Object` endpoint violations.
- Five `missing_inverse` demands for inappropriate `designOf`.
- Four legitimate opposite-end `offeredWith` links lacking source-side symmetric mirrors.
- Injector `hasPart` to Crown plus Crown's preexisting `integratesWith` to Stealth each cause a missing inverse; Stealth's `hasPart` Crown also causes a missing inverse.

**Expected reduction: 17 relationship errors** (5 incompatible endpoints + 12 missing inverses), targeting **143** (13 endpoint + 130 inverse) if no other model state changes. Independently verify actual log counts for both MDSE Vault Audit and Semantic Linking Completion Gate at the same new modeling commit before claiming success. Full-vault validation will still fail with remaining defects.

## Handoff

1. Verify the five `Object.hasDesign -> Object` endpoint violations are gone, and no new `integratesWith` / `offeredWith` mirror defects appeared. Preserve full source fidelity.
2. Continue with other 13 cross-class endpoints: `Function.realizedBy` to Object/Document, `Design.designOf` and same-class hierarchy links, Design `realizes` Object and the remote-control accessory `hasPart` Function.
3. Synchronize valid missing inverses only **after** their corresponding endpoint semantics are sound.
4. Track separate evidence and traceability failures under [issue #5](https://github.com/spencerskelly/PosiBattery/issues/5); relationship validation is [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2). Keep PR #4 draft and do not advance `main` while blockers remain.
