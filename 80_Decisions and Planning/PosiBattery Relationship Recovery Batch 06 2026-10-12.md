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

## Decision applied: two Design → Design `designOf` pairs retyped to `dependsOn` (user confirmed 2026-10-12)

| Source Design | Entry | Target Design |
| --- | --- | --- |
| [[Direct Temperature Input Charge Compensation]] | `designOf` | [[Battery Temperature Measurement Design]] |
| [[Communicated Battery Temperature Charge Compensation]] | `designOf` | [[Battery Temperature Reporting to Charger]] |

`designOf` must target an Object or Document, so both are invalid. Applied: each `designOf` entry removed and the same target added under `dependsOn`; `dependencyOf` added on each target Design ([[Battery Temperature Measurement Design]] → [[Direct Temperature Input Charge Compensation]]; [[Battery Temperature Reporting to Charger]] → [[Communicated Battery Temperature Charge Compensation]]). Four files changed (4 additions, 2 deletions). Evidence: the Communicated note's body states it "reuses [[Battery Temperature Reporting to Charger]]"; the Measurement design already carries `dependencyOf` for the Reporting design; the Direct Temperature Input note describes a charger-connected sensor input, which is the measurement design's scope. Considered and not used: `includes` / `includedIn`.

## Local verification (before push)
- Identity check: PASS.
- Relationship findings: **26 → 0** (4 remained after the removals; the two pairs above cleared them).
- Vault audit blocking findings: **13 → 2**.
- CI results to be added below after push.

## Follow-on gate work (2026-10-12, same session)

| Item | Change | Evidence |
| --- | --- | --- |
| 3 disposition registry errors | Entries for three retired SOC algorithm Designs commented out in `Semantic Linking Review Dispositions 0.1.yaml`, text preserved | Notes no longer exist (retired in `aa369a95`, `7c00bd27`, `df4b9a55`); registry errors 3 → 0 |
| 3 realizing Designs without curated source | `supportedBy` added on the Designs; `supports` added on [[Document - PosiCharge BMID FAQ]] and [[Document - PosiCharge PosiConnect Product Page]], with scope limits written on those notes | Quotes from the live pages, re-read 2026-10-12; high-value evidence findings 3 → 0 |
| 2 end-to-end Function ↔ Design inverse findings | User decision: supporting designs need not link directly to the next element type. Chain spec in `review-end-to-end-product-chains.py` and Step 27 YAML now name the Designs that realize the Functions ([[Battery Temperature Reporting to Charger]], [[Device Configuration and Service Design]]); the earlier names ([[Electrolyte-Immersed Temperature Sensor]], [[Mobile App Interface]]) are kept as revision notes. Both new Designs classified `active_engineering` in the dispositions registry | Functions are already `realizedBy` those Designs with inverses; findings 2 → 0 |

Conflict record: the Step 27 YAML (2026-10-05) named the sensor and the app interface as direct realizing Designs. That text is superseded, not erased. The same YAML file already fails to parse (a `note:` key under a list, near the `supplemental_active_architecture_gaps` block); this was true before the edit and is not yet repaired.

Still failing locally: weak-traceability priority review (51 weak-queue registry findings, plus the legacy weak findings).

## Handoff
1. Remaining gate failures outside this batch: 3 disposition registry errors, 2 end-to-end Function ↔ Design inverse pairs, 3 Designs without curated sources, 1 active weak-traceability item.
2. README and Runtime Handoff State still cite the older 256 missing-inverse / 75 incompatible-endpoint baseline; keep those numbers visible as the conflict record when updating.
