# PosiBattery Relationship Recovery — Batch 02 (2026-10-08)

## Context

This is the second bounded repair under [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2), continuing [draft PR #4](https://github.com/spencerskelly/PosiBattery/pull/4) on `recovery/relationship-invariants-batch-01`, building on [[PosiBattery Relationship Recovery Batch 01 2026-10-08]]. This file records the repair, verification inputs and handoff. The `main` model remains the approval boundary.

**Incoming verified branch baseline:** `b0860ccc8ce1901d3e4e9f1fc141579a50c4c276`, with 313 relationship errors: 69 endpoint incompatibilities and 244 missing inverses. The preceding main baseline had 331 errors (75+256).

## Invariant and correction

Per `99_System/03_Schemas/relationships.yaml` 1.36:

- `partOf/hasPart`: Object-to-Object physical or logical composition; **never** an Object part of a Function.
- `performs/performedBy`: Object-to-Function behavior realization.

For every row below, the implementation Object carried `partOf: [[Function]]` but an empty `performs:`. The corresponding Function note already contained `performedBy: [[Object]]`, establishing the existing implementation claim. Therefore, move exactly the Function link from `partOf` to `performs`; keep all product-to-Object `partOf` links, existing `hasDesign`/component/dependency relations, model identity and evidence unchanged.

| Object edited | Function already containing reciprocal `performedBy` |
| --- | --- |
| [[Charger Remote Management Agent]] | [[Manage Chargers Remotely]] |
| [[Missed Equalization Recovery Firmware]] | [[Complete Missed Equalization Automatically]] |
| [[Device Configuration and Service Firmware]] | [[Configure Device from Mobile App or PC]] |
| [[PC Battery Data Retrieval Software]] | [[Export Battery Data to PC]] |
| [[Load-Handling Image Capture Logic]] | [[Record Images of Load Handling]] |
| [[Temperature Compensation Charge Control Firmware]] | [[Compensate Charge for Battery Temperature]] |
| [[CAN Battery State Communication Firmware]] | [[Communicate Battery State over CAN]] |
| [[Remote Vehicle Diagnostic Service]] | [[Diagnose Vehicle Remotely]] |
| [[BMS-Directed Charge Control Firmware]] | [[Charge Under BMS Control]] |
| [[Battery Data Export Firmware]] | [[Export Battery Data to PC]] |
| [[Load-Handling Camera Assembly]] | [[Record Images of Load Handling]] |
| [[Vehicle Diagnostic Data Acquisition Logic]] | [[Diagnose Vehicle Remotely]] |
| [[Electrolyte Air Circulation Assembly]] | [[Circulate Electrolyte]] |

## Expected quality improvement and validation gate

On the incoming branch audit logs, 13 endpoint violations were `partOf: Object -> Function`. For each corrected Object, the logs also showed two related inverse defects: false `hasPart` expected on the Function and missing `performs` expected from an existing `performedBy` link. Therefore, the **predicted** delta for this batch is 39 errors:

| Category | Before batch 02 | Expected after batch 02 |
| --- | ---: | ---: |
| `endpoint_incompatible` | 69 | 56 |
| `missing_inverse` | 244 | 218 |
| **Total** | **313** | **274** |

These are expectations, not a pass claim. The actual result must be confirmed from MDSE Vault Audit **and** Semantic Linking Completion Gate on the same final branch commit. Check that all thirteen edited note names disappear from relationship error reports; check Workbench, True Orphan, Local Model and Port Flow separately. The target count does not imply the remaining defects are acceptable.

## Handoff / next batch

After CI confirms this delta, the known `Object.partOf -> Function` class should be exhausted. Next classify other `endpoint_incompatible` errors by meaning **before** adding inverses: misuse of `Function.realizedBy` toward Customer Needs/Use Cases, product Objects and Source Documents; `Object.hasPart` toward Organization/Info; `Object.hasDesign` toward product Objects; and Design `subtypeOf` or `designOf` to wrong element classes. Many apparent `missing_inverse` entries are generated symptoms of these bad predicates. Preserve the original user's engineering claims, evidence and provenance while selecting the correct relationship type.

**Do not** merge PR #4 or mark issue #2 complete while global relationship validation fails. Continue to preserve IDs/UIDs, evidence and original note bodies. Future batches should prefer a single multi-file commit to reduce GitHub Actions noise.
