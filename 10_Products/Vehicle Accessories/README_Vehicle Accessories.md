# Vehicle Accessories

## Purpose

Devices added to trucks and ground support equipment: access control, cameras, operator assistance and stability, convenience, displays, power-source interfaces, detection and warning devices.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 1 / 130 |
| Typed model notes (incl. subfolders) | 130 (Object 130) |
| Status | Draft 130 of 130 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 22 / 22 of 130 |
| Tags | 30 distinct, 11 used once |
| Size | median 2,294 bytes; largest [[Hyster Power Cellect]] (7 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| Access Control | 4 | 1 | source-linked 1/3; 2 body-alias |
| Cameras and Recorders | 8 | 1 | source-linked 0/7; 4 body-alias |
| Cold Storage Packages | 5 | 1 | source-linked 2/4; 2 body-alias |
| [[README_Operator Assist and Stability|Operator Assist and Stability]] | 43 | 1 | source-linked 6/42; 27 body-alias; 1 update-log |
| [[README_Operator Convenience|Operator Convenience]] | 12 | 1 | source-linked 6/11; 4 body-alias; 3 update-log |
| Operator Displays | 6 | 1 | source-linked 2/5; 3 body-alias; 1 update-log |
| Power Source Interfaces | 5 | 1 | source-linked 2/4; 3 body-alias; 2 update-log |
| [[README_Proximity and Object Detection|Proximity and Object Detection]] | 30 | 1 | source-linked 1/29; 26 body-alias |
| [[README_Warning Lights and Alerts|Warning Lights and Alerts]] | 16 | 1 | source-linked 2/15; 12 body-alias |

### Analysis

- 130 notes: 10 abstract category/family notes and 120 concrete offerings. 120 of 120 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 22 of 120 (18%) concrete offerings carry a `describedBy` link; 98 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 111 of 130 (85%) notes `performs` at least one Function; 56 of 130 (43%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 120 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 7 notes carry dated update blocks, 6 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 83 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 130 of 130 Objects (F-05).
- Vocabulary and size: 30 distinct tags (11 used once); median note 2,294 bytes, largest Hyster Power Cellect (7 KB).

### Key links

- [[Operator Assist and Stability System]] (abstract) — 43 inbound links
- [[Linde Safety Guard]] — 32 inbound links
- [[Toyota Assist]] — 32 inbound links
- [[Proximity and Object Detection System]] (abstract) — 30 inbound links
- [[EnerSys Truck iQ]] — 29 inbound links
- [[Hyster Power Cellect]] — 29 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 130 Objects (the 10 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 98 concrete offerings with no source link: [[Blaxtair Pedestrian Detection System]], [[Cat Presence Detection System]], [[Cat Safety Lighting Options]], [[Crown Capacity Data Monitor]], [[Crown Gena Operating System]], [[Crown InfoLink 7-inch Touch Display]] and 92 more.
3. **F-04** Merge repeated or empty label blocks in [[Hyster Power Cellect]], [[Hyster Reaction]], [[Linde Safety Guard]], [[Linde Safety Pilot]], [[STILL Safety Assist]], [[Toyota SEnS+ Pedestrian and Object Detection]].
4. **F-04** Consolidate the dated update blocks in 7 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 83 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
