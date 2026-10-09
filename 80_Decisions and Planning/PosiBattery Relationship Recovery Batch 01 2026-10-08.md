# PosiBattery Relationship Recovery — Batch 01 (2026-10-08)

## Authority and purpose

This is the first bounded engineering repair of [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2), using a pull-request branch. The authoritative model is the Obsidian notes and the governed `relationships.yaml` 1.36 contract, with `main` kept unchanged until review and merge.

**Baseline:** `main` commit `7fbe3034b138cec55ef8a9e152f761b62d1cb67b`. The MDSE Vault Audit / Semantic Linking Completion Gate on that baseline fail with **331** relationship diagnostics: **75** `endpoint_incompatible` and **256** `missing_inverse`. Workbench, True Orphan, Local Model and Port Flow reviews passed on that baseline.

## Modeling rule

- `partOf` is the inverse of `hasPart` and has legal endpoints **Object -> Object** only.
- `performs` is a forward **Object -> Function** relationship, inverse `performedBy` on the Function.
- In each of the six cases below, an implementation Object incorrectly asserted `partOf: [[Function]]` and had an empty `performs:` field. The matching Function already named that Object as `performedBy`.
- Correct each Object by moving the Function link from `partOf` to `performs`. **Retain** its valid `partOf` links to product Objects, `hasPart` links to components, Design links, IDs, UIDs, evidence, and note body.

| Implementation Object | Function | Semantics |
| --- | --- | --- |
| [[Wired Remote Charger Control Assembly]] | [[Control Charger from Remote Panel]] | Implements remote panel control, is not a physical part of a Function. |
| [[Remote Charger Management Service]] | [[Manage Chargers Remotely]] | Hosted service performs remote management. |
| [[Pre-Shift Checklist Enforcement Logic]] | [[Enforce Pre-Shift Checklist]] | Software performs operator inspection gate. |
| [[Automatic Watering Control Logic]] | [[Water Battery Cells]] | Control logic performs charger-supervised watering. |
| [[Load-Handling Image Storage]] | [[Record Images of Load Handling]] | Implementation storage contributes to image-recording behavior, as already designated by inverse Function relation. |
| [[Adaptive Charge Profile Control Firmware]] | [[Adapt Charge to Battery Condition]] | Firmware performs adaptive charge-profile logic. |

## Pre-change diagnostics and expected recovery

GitHub Actions baseline logs contained **exactly 18** diagnostics mentioning the six Object names:
- 6 endpoint violations due to `partOf: Object -> Function`.
- 6 missing `hasPart` inverses on Function targets, which are deliberately not created because that would be false composition.
- 6 missing `performs` inverses of existing `performedBy` Function links, resolved by adding the correct forward link.

**Expected after these six edits:** `313` remaining errors (`69` endpoint incompatible and `244` missing inverse) *if all other model state is unchanged*. This is a test expectation, not a claim that validation has passed. Confirm from CI logs tied to the branch SHA. If actual counts differ, inspect before extending the repair.

## Validation and restrictions

1. Verify all six changed Object YAML headers with no `partOf: [[Function]]`, `performs: [[Function]]`, and preserved product `partOf` links; verify all six Function `performedBy` links already exist.
2. Compare GitHub Actions relationship diagnostics to baseline by **category and file/target**, not only by total count.
3. Ensure unrelated identity, traceability, Local Model, Port/Item Flow, and Workbench reviews remain passing.
4. Do not create a false `hasPart` on Functions, nor infer additional physical product implementations from the generic design.
5. Keep this batch as a reviewable PR; do **not** mark issue #2 or the vault golden while the global relationship gates fail.

## Handoff

Once this batch's delta is confirmed, continue with the next semantically clear category of invalid Object-to-Function composition. Separately classify invalid `hasPart` Object-to-Info (manufacturer / Organization) and invalid `hasDesign` Object-to-Object (commercial product) relationships. Correct endpoint misuse **before** blindly propagating inverses. Use a stable batch log and record a new CI SHA each time.

The function-by-function realization completeness effort remains in [issue #3](https://github.com/spencerskelly/PosiBattery/issues/3) and is not closed by these relationship repairs.
