# Forklifts

## Purpose

Powered industrial trucks by class (I to VII). Electric classes are in scope first; internal-combustion and tractor classes hold placeholders.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 8 / 58 |
| Typed model notes (incl. subfolders) | 58 (Object 58) |
| Status | Draft 58 of 58 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 44 / 43 of 58 |
| Tags | 10 distinct, 0 used once |
| Size | median 2,033 bytes; largest [[Crown RC 5700 Series]] (7 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Class I Electric Rider Trucks|Class I Electric Rider Trucks]] | 37 | 1 | source-linked 29/36; 32 body-alias; 22 update-log |
| Class II Electric Narrow Aisle Trucks | 6 | 1 | source-linked 5/5; 5 body-alias; 2 update-log |
| Class III Electric Hand and Hand-Rider Trucks | 3 | 1 | source-linked 2/2; 2 body-alias; 2 update-log |
| Class IV Internal Combustion Cushion Tire Trucks | 1 | 1 | source-linked 0/1; thin |
| Class V Internal Combustion Pneumatic Tire Trucks | 1 | 1 | source-linked 0/1; thin |
| Class VI Tractors | 1 | 1 | source-linked 0/1; thin |
| Class VII Rough Terrain Forklifts | 1 | 1 | source-linked 0/1; thin |

### Analysis

- 58 notes: 8 abstract category/family notes and 50 concrete offerings. 50 of 50 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 43 of 50 (86%) concrete offerings carry a `describedBy` link; 7 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 28 of 58 (48%) notes `performs` at least one Function; 38 of 58 (66%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 58 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 26 notes carry dated update blocks, 14 repeat a bold label inside the note and 2 contain an empty label block (F-04).
- Aliases: 46 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 58 of 58 Objects (F-05).
- Vocabulary and size: 10 distinct tags (0 used once); median note 2,033 bytes, largest Crown RC 5700 Series (7 KB).

### Key links

- [[Crown RC 5700 Series]] — 41 inbound links
- [[Class I Electric Rider Truck]] (abstract) — 39 inbound links
- [[Hangcha XC Series Electric Forklifts]] — 26 inbound links
- [[Yale ERC050-060VGL]] — 25 inbound links
- [[Hangcha A Series Electric Forklifts]] — 24 inbound links
- [[Raymond 4000 Series Counterbalanced Trucks]] — 23 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 58 Objects (the 8 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 7 concrete offerings with no source link: [[Doosan Bobcat 7-Series Plus Electric Forklifts]], [[Doosan Bobcat NXE Series Electric Forklifts]], [[Heli G Series Lithium Forklifts]], [[Komatsu FB Series Electric Forklifts]], [[Linde 6-8 t Electric Counterbalance Forklifts]], [[Mitsubishi FBC Cushion Tire Electric Forklifts]] and 1 more.
3. **F-04** Merge repeated or empty label blocks in [[Crown FC 5700 Series]], [[Crown RC 5700 Series]], [[Hangcha A Series Electric Forklifts]], [[Hangcha XC Series Electric Forklifts]], [[Heli G Series Lithium Forklifts]], [[Hyster J1.5-3.0UT(L)]] and 9 more.
4. **F-04** Consolidate the dated update blocks in 26 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 46 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
