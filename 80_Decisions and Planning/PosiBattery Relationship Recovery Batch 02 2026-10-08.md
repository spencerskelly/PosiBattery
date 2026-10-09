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

## Actual CI acceptance result — model revision `5ebb7867`

**Verified on 2026-10-08**, using two independent GitHub Actions logs for the model revision immediately following all 13 corrected Object notes:

| Gate | Run | Actual result |
| --- | --- | --- |
| MDSE Vault Audit | [37888709553](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709553) | **FAIL**, but reduced to **56 endpoint_incompatible + 218 missing_inverse = 274** |
| Semantic Linking Completion Gate | [37888709591](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709591) | **FAIL**, identical **274** diagnostic split |
| Workbench Model Review | [37888709637](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709637) | PASS |
| True Orphan Review | [37888709585](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709585) | PASS |
| Local Model Review | [37888709546](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709546) | PASS |
| Port Flow Review | [37888709658](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709658) | PASS |

The observed delta is exactly **39** fewer diagnostics: 13 endpoint errors + 26 missing inverse errors, confirming the predicted effect and preserving four passing core checks. The original `main` baseline of 331 is now **57 above the recovery branch model's 274** across both batches. The final documentation-only SHA should receive a separate GitHub Actions run; the model semantics are unchanged by this evidence write.

**Additional PR-triggered checks identified independently of the two primary gates**:

- [Weak Traceability Priority Review 37888709539](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709539): **FAIL**, including disposition registry and weak-evidence classification findings.
- [End-to-End Product Chain Audit 37888709551](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709551): **FAIL**; specifically, two Function↔Design pairs lack bidirectional realization assertions (`Report Battery Temperature to Charger` ↔ `Electrolyte-Immersed Temperature Sensor`, `Configure Device from Mobile App or PC` ↔ `Mobile App Interface`).
- [High-Value Evidence Review 37888709578](https://github.com/spencerskelly/PosiBattery/actions/runs/37888709578): **FAIL**, including missing direct curated source support on active Function/Design chains.

These additional failures must be triaged as **separate validation dimensions** rather than interpreted as a reason to restore invalid `partOf` or blindly insert inverses. The above failures are observations on revision `5ebb7867`; this batch did not modify the cited Function/Design/evidence files. Whether those checks already failed before the recovery PR must be established from comparable run data before attributing regressions.

**Acceptance decision:** **PASS for the bounded 13-note diagnostic-delta test**; **FAIL for full-vault stability and merge readiness**.

---

## Handoff / next batch

After CI confirms this delta, the known `Object.partOf -> Function` class should be exhausted. Next classify other `endpoint_incompatible` errors by meaning **before** adding inverses: misuse of `Function.realizedBy` toward Customer Needs/Use Cases, product Objects and Source Documents; `Object.hasPart` toward Organization/Info; `Object.hasDesign` toward product Objects; and Design `subtypeOf` or `designOf` to wrong element classes. Many apparent `missing_inverse` entries are generated symptoms of these bad predicates. Preserve the original user's engineering claims, evidence and provenance while selecting the correct relationship type.

**Do not** merge PR #4 or mark issue #2 complete while global relationship validation fails. Continue to preserve IDs/UIDs, evidence and original note bodies. Future batches should prefer a single multi-file commit to reduce GitHub Actions noise.
