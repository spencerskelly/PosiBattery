# PosiBattery Relationship Recovery — Batch 06 (2026-10-12)

## Controlled repair
- **Branch:** `main` (single-branch repository since the 2026-10-12 consolidation).
- **Starting commit:** `2e5f2497`; baseline: **26** relationship findings (13 `endpoint_incompatible` pairs plus their missing inverses), carried from [[PosiBattery Relationship Recovery Batch 05 2026-10-08]] (which recorded 13 endpoint + 130 inverse errors before later batches and the consolidation).
- **Purpose:** remove wrong-endpoint relationship entries. In 11 of the 13 pairs the note already carried the *valid* link to the same target, so the invalid entry was a duplicate and is removed rather than retyped. No target was left unlinked.

## Changes and evidence

| Source note | Removed entry (field → target) | Valid link retained (evidence the relationship is still modeled) |
| --- | --- | --- |
| [[Crown V-HFM3 Wired Remote Control Kit]] | `hasPart` → [[Control Charger from Remote Panel]] (Object hasPart Function is not allowed) | `performs` / `performedBy` |
| [[Battery Cell Watering Design]] | `designOf` → [[Water Battery Cells]] (Design designOf Function is not allowed) | `realizes` / `realizedBy`; `dependencyOf` / `dependsOn` |
| [[Cloud Portal Integration]] | `supertypeOf` → [[Document - PosiCharge PosiGuard Product Page]] (cross-class) | `supportedBy` / `supports` |
| [[Battery Identification and Charger Communication Software Design]] | `subtypeOf` → [[Document - PosiCharge BMID FAQ]] (cross-class) | `supportedBy` / `supports` |
| [[Forced Electrolyte Circulation]] | `realizes` → [[Midac EUW Electrolyte Circulation System]] (Design realizes Object is not allowed) | `designOf` / `hasDesign` |
| [[Battery-Charger Data Communication Design]] | `supertypeOf` → [[Communicate with Charger]] (cross-class) | `realizes` / `realizedBy`; `dependencyOf` / `dependsOn` |
| [[Export Battery Data to PC]] | `realizedBy` → [[Power Designers PowerTrac SP+]] (Function realizedBy Object is not allowed) | `performedBy` / `performs` |
| [[Log Battery Events and Usage]] | `realizedBy` → [[Document - PosiCharge BMID FAQ]] | `supportedBy` / `supports` |
| [[Complete Missed Equalization Automatically]] | `realizedBy` → [[Power Designers REVOLUTION X]] | `performedBy` / `performs` |
| [[Desulfate Battery During Charge]] | `realizedBy` → [[Desulfation Charge Control Firmware]] | `performedBy` / `performs` |
| [[Circulate Electrolyte]] | `realizedBy` → [[HOPPECKE trak uplift air Battery]] | `performedBy` / `performs` |

Each edit deletes exactly one frontmatter list item. Zero lines were added. No `id`, `uid`, `status`, source, body text or other relationship was changed.

## Open decision: two Design → Design `designOf` pairs (not changed)

| Source Design | Entry | Target Design |
| --- | --- | --- |
| [[Direct Temperature Input Charge Compensation]] | `designOf` | [[Battery Temperature Measurement Design]] |
| [[Communicated Battery Temperature Charge Compensation]] | `designOf` | [[Battery Temperature Reporting to Charger]] |

`designOf` must target an Object or Document, so both are invalid. Proposed fix (awaiting confirmation): retype to `dependsOn`, with `dependencyOf` on each target Design. Evidence: the Communicated note's body states it "reuses [[Battery Temperature Reporting to Charger]]"; the Measurement design already carries `dependencyOf` for the Reporting design; the Direct Temperature Input note describes a charger-connected sensor input, which is the measurement design's scope. Alternative if the user rejects reuse semantics: `includes` / `includedIn` (any → any). Both source notes currently have an empty `dependsOn:` field.

## Local verification (before push)
- Identity check: PASS.
- Relationship findings: **26 → 4** (2 endpoint + 2 missing inverse, all from the two pairs above).
- Vault audit blocking findings: **13 → 2**.
- CI results to be added below after push.

## Handoff
1. Decide the two Design → Design pairs above.
2. Remaining gate failures outside this batch: 3 disposition registry errors, 2 end-to-end Function ↔ Design inverse pairs, 3 Designs without curated sources, 1 active weak-traceability item.
3. README and Runtime Handoff State still cite the older 256 missing-inverse / 75 incompatible-endpoint baseline; keep those numbers visible as the conflict record when updating.
