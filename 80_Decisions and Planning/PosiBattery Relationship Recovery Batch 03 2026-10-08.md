# PosiBattery Relationship Recovery — Batch 03 (2026-10-08)

## Recovery boundary

This third bounded repair continues [draft PR #4](https://github.com/spencerskelly/PosiBattery/pull/4) under [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2) and follows [[PosiBattery Relationship Recovery Batch 02 2026-10-08]].

**Incoming validated branch model SHA:** `525eff644ed4a492df84f0b3ea98a8b25bf2f010`. **Incoming relationship findings:** 56 `endpoint_incompatible` + 218 `missing_inverse` = 274. Both primary relationship gates failed; all four supporting core checks passed.

**Last Batch 03 modeling commit:** `464e2c2f34bee195be07342d1a4ab1337200c0c6`.

## Governed semantic correction

`relationships.yaml` 1.36 defines the paired relationship:

- `Use Case.realizedBy -> Function` (authored from a Use Case to a Function);
- `Function.realizes -> Use Case` (the synchronized inverse);
- `Function.realizedBy -> Design` is separately valid for a Function's implementation design.

The previous generated modeling work incorrectly appended existing Customer Need/operational Use Case references to `Function.realizedBy`, alongside legitimate Design targets. That caused endpoint type violations and inverse mismatch findings. **In each of the 21 cases below, the target Use Case was independently fetched and verified to already carry the exact `realizedBy: [[Function]]` assertion.** No new requirement, Use Case, or customer evidence relationship was inferred.

For each source Function, move the single Use Case link from `realizedBy:` to `realizes:`. Preserve all real Design targets in `realizedBy`, all preexisting other `realizes` links, source evidence, IDs, UIDs, status, and note body. The Use Case note needs no edit; its forward assertion is already correct.

| Function note corrected | Existing Use Case reciprocal |
| --- | --- |
| [[Manage Chargers Remotely]] | [[Monitor and Manage Chargers and Batteries Across Sites]] |
| [[Diagnose Vehicle Remotely]] | [[Find and Fix Vehicle Faults Without Downtime]] |
| [[Report Truck Telemetry]] | [[Find and Fix Vehicle Faults Without Downtime]] |
| [[Protect Battery from Deep Discharge]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[Communicate with Charger]] | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Lock Out Vehicle After Impact]] | [[Protect Aircraft and Ground Crew During Ground Operations]] |
| [[Record Images of Load Handling]] | [[Review an Impact Event and Decide Whether to Return the Vehicle to Service]] |
| [[Compensate Charge for Battery Temperature]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] |
| [[Control Operator Access]] | [[Authenticate and Complete Pre-Shift Authorization]] |
| [[Predict Battery Replacement Timing]] | [[Prevent Battery Abuse and Premature Replacement]] |
| [[Water Battery Cells]] | [[Keep Trucks Working Without Battery Maintenance Labor]] |
| [[Transmit Battery Data Wirelessly]] | [[Integrate a BMID with Charger Vehicle and Fleet Systems]] |
| [[Command Vehicle Operating Limits over CAN]] | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Enforce Pre-Shift Checklist]] | [[Authenticate and Complete Pre-Shift Authorization]] |
| [[Upload Battery Data to Cloud Portal]] | [[Review Battery Care and Warranty Compliance]] |
| [[Track Equalization]] | [[Review Battery Care and Warranty Compliance]] |
| [[Adapt Charge to Battery Condition]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] |
| [[Communicate Battery State over CAN]] | [[Integrate the Battery with Truck and Charger Controls]] |
| [[Calculate Battery Abuse Cycles]] | [[Review Battery Care and Warranty Compliance]] |
| [[Charge Under BMS Control]] | [[Charge Each Battery Correctly for Its Chemistry and Condition]] |
| [[Control Charger from Remote Panel]] | [[Monitor and Manage Chargers and Batteries Across Sites]] |

## Validation

The incoming relationship validation log reported **21 endpoint incompatibilities** for `Function.realizedBy -> Use Case`. The existing opposite-end `Use Case.realizedBy -> Function` assertions also lacked the correct `Function.realizes` inverse, and the wrongly directed `Function.realizedBy` field requested an invalid `Use Case.realizes` inverse. If all 21 corrected pairs were the only change:

| Diagnostic | Before | Expected after |
| --- | ---: | ---: |
| `endpoint_incompatible` | 56 | 35 |
| `missing_inverse` | 218 | 176 |
| **Total** | **274** | **211** |

**Important:** the figures above are a *validation prediction*, not a CI result. Confirm actual findings using both MDSE Vault Audit and Semantic Linking Completion Gate on the same SHA. The source notes were edited individually and each change asserts no new product evidence; the final audit is needed to ensure no unexpected side effects. The general and PR-only gates in [issue #5](https://github.com/spencerskelly/PosiBattery/issues/5) also remain separate acceptance dimensions.

## Handoff / next corrective patterns

When CI confirms this category's closure, classify the remaining endpoint defects before adding inverses:

1. `Object.hasPart -> Info (Organization)`: physical composition is invalid. Inspect existing maker/seller fields, and only use the appropriate `madeBy`/`offeredBy` with verified semantics.
2. `Object.hasDesign -> Object (product)`: a product-to-product relation requires evidence and correct compatible predicate (`offeredWith`, `rebrandOf`, `integratesWith` where allowed); do not convert automatically.
3. `Function.realizedBy -> Object/Document` and cross-type `Design.designOf/subtypeOf/realizes`: independently inspect intended hierarchy, product performance and evidence support.
4. One remaining `Object.hasPart -> Function` on a remote-control kit may be another `performs/Function.performedBy` inverse, subject to checking the existing Function note first.
5. Synchronize inverse relationships only after all invalid endpoint semantics are repaired; retain historical commitment and review decisions.

Do **not** merge PR #4 or close issue #2 while full relationship checks fail. The recovery branch preserves the engineering work for human review.
