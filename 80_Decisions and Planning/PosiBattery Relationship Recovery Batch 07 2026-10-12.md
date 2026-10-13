# PosiBattery Relationship Recovery — Batch 07 (2026-10-12)

## Controlled repair
- **Branch:** `main`. **Starting commit:** `3d294f15`.
- **Rule (user decision, 2026-10-12):** direct realization is prioritized over dependency. Where a Function is `realizedBy` a Design, a `dependsOn` to the same Design is redundant and is removed.
- **Trigger:** `review-function-design-realization.py` could not run before (it crashed on an empty `open_design_gaps:` key; fixed in `3d294f15`). Once it ran it reported 44 `realization-dependency-overlap` findings and 2 `bmid-direct-realization-drift` findings.

## Changes and evidence

For each pair below the Function already carries `realizedBy` to the Design, so no connection between the two was lost. The matching `dependencyOf` entry on the Design was removed with it to keep inverses synchronized. 86 files changed, 88 lines deleted, 0 added.

| Function | Design | Entries removed |
| --- | --- | --- |
| [[Accumulate Amp-Hours]] | [[Current Integration Amp-Hour Accumulation]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Adapt Charge to Battery Condition]] | [[Adaptive Charge Profile Control Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Alert on Abnormal Condition]] | [[Abnormal Condition Alert Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Alert on Low Electrolyte Level]] | [[Low Electrolyte Alert Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Calculate Battery Abuse Cycles]] | [[Battery Abuse Cycle Analytics]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Charge Under BMS Control]] | [[BMS-Directed Charge Control Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Circulate Electrolyte]] | [[Air Injection Electrolyte Circulation]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Circulate Electrolyte]] | [[Forced Electrolyte Circulation]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Command Vehicle Operating Limits over CAN]] | [[CAN Vehicle Operating Limit Command]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Communicate Battery State over CAN]] | [[CAN Battery State Communication Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Communicate with Charger]] | [[Battery-Charger Data Communication Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Compensate Charge for Battery Temperature]] | [[Temperature-Compensated Charge Control Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Complete Missed Equalization Automatically]] | [[Missed Equalization Recovery Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Configure Device from Mobile App or PC]] | [[Device Configuration and Service Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Control Charger from Remote Panel]] | [[Wired Remote Charger Control Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Control Operator Access]] | [[Operator Access Authorization Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Desulfate Battery During Charge]] | [[Lead-Acid Desulfation Charge Control Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Detect Battery Weight]] | [[Battery Weight Determination Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Detect Cell Failure]] | [[Cell Failure Diagnostic Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Detect Voltage Imbalance]] | [[Voltage Imbalance Detection Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Diagnose Vehicle Remotely]] | [[Remote Vehicle Diagnostics Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Display Battery Status to Operator]] | [[Vehicle Operator Display Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Display Truck Status to Operator]] | [[Vehicle Operator Display Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Enforce Pre-Shift Checklist]] | [[Pre-Shift Checklist Enforcement Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Estimate Remaining Run Time]] | [[Remaining Runtime Estimation Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Estimate State of Health]] | [[Usage-History State of Health Analytics]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Export Battery Data to PC]] | [[PC Battery Data Export Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Indicate Battery Status Locally]] | [[Warning and Display Device Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Indicate Charger Status Locally]] | [[Local Charger Status Indication]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Lock Out Vehicle After Impact]] | [[Impact-Triggered Vehicle Lockout Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Log Battery Events and Usage]] | [[Battery Event and Usage Logging Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Manage Chargers Remotely]] | [[Remote Charger Management Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Measure Battery Temperature]] | [[Battery Temperature Measurement Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Measure Electrolyte Specific Gravity]] | [[In-Cell Specific Gravity Probe]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Predict Battery Replacement Timing]] | [[Battery Replacement Timing Prediction Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Protect Battery from Deep Discharge]] | [[Deep Discharge Protection Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Record Images of Load Handling]] | [[Load-Handling Image Capture Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Report Battery Temperature to Charger]] | [[Battery Temperature Reporting to Charger]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Report Truck Telemetry]] | [[Truck Telemetry Reporting Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Sense Electrolyte Level]] | [[Electrolyte Level Sensing Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Track Equalization]] | [[Equalization Event Tracking Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Transmit Battery Data Wirelessly]] | [[Wireless Battery Data Communication Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Upload Battery Data to Cloud Portal]] | [[Cloud Battery Data Upload Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |
| [[Water Battery Cells]] | [[Battery Cell Watering Design]] | `dependsOn` on the Function; `dependencyOf` on the Design |

## Step 89 record updated (conflict kept visible)

`BMID Function Design Traceability Step 89 0.1.yaml` named [[Electrolyte-Immersed Temperature Sensor]] and [[Mobile App Interface]] as direct realizing Designs. It now names [[Battery Temperature Reporting to Charger]] and [[Device Configuration and Service Design]], with a `revision_note` on each keeping the earlier statement. The two former Designs were reclassified from `active_engineering` to `reference_content` in the dispositions registry, since nothing governed names them as active any more.

## Two overstated containment links removed (market reference leaves)

| Source note | Removed entry | Target | Valid link retained (evidence) |
| --- | --- | --- | --- |
| [[TLD Aircraft Safety Docking]] | `hasPart` | [[TLD NBL-E Belt Loader]] | `offeredWith` in both directions; the belt loader is the host vehicle the docking system is offered with, not a component of it |
| [[TLD NBL-E Belt Loader]] | `partOf` | [[TLD Aircraft Safety Docking]] | same |
| [[Fronius Selectiva 4.0]] | `hasPart` | [[Fronius Charge & Connect]] | `offeredWith` in both directions; the Fronius flyer (T1, cited in the note) says chargers "connect to" Charge & Connect, which is integration, not containment |
| [[Fronius Charge & Connect]] | `partOf` | [[Fronius Selectiva 4.0]] | same |

Same reasoning as Batch 05: independent commercial products are not parts of each other. Four lines deleted, none added. `review-market-reference-leaves.py` findings 4 → 0 with the existing registry entries, which were correct once the links were removed.

## Local verification
Relationship, identity, vault audit, completion acceptance, weak-traceability, end-to-end chain, function-design realization and architecture-design review scripts pass. No script called by the 28 workflows fails locally when run in report-then-check order.

## Handoff
1. Update README and Runtime Handoff State with the new baseline; keep the 256 missing-inverse and 75 incompatible-endpoint numbers visible as the conflict record.
