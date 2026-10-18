# Proximity and Object Detection

## Purpose

Proximity and object-detection devices offered with trucks.

Parent: [[README_Vehicle Accessories|Vehicle Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 30 / 30 |
| Typed model notes (incl. subfolders) | 30 (Object 30) |
| Status | Draft 30 of 30 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 1 / 1 of 30 |
| Tags | 17 distinct, 5 used once |
| Size | median 2,866 bytes; largest [[Hyster Reaction]] (6 KB) |

### Analysis

- 30 notes: 1 abstract category/family notes and 29 concrete offerings. 29 of 29 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 1 of 29 (3%) concrete offerings carry a `describedBy` link; 28 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 29 of 30 (97%) notes `performs` at least one Function; 19 of 30 (63%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 29 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 0 notes carry dated update blocks, 3 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 26 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 30 of 30 Objects (F-05).
- Vocabulary and size: 17 distinct tags (5 used once); median note 2,866 bytes, largest Hyster Reaction (6 KB).

### Key links

- [[Linde Safety Guard]] — 32 inbound links
- [[Proximity and Object Detection System]] (abstract) — 30 inbound links
- [[TLD Aircraft Safety Docking]] — 27 inbound links
- [[Hyster Reaction]] — 25 inbound links
- [[Crown ProximityAssist System]] — 24 inbound links
- [[Toyota SEnS+ Pedestrian and Object Detection]] — 22 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 30 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 28 concrete offerings with no source link: [[Blaxtair Pedestrian Detection System]], [[Crown ProximityAssist System]], [[Doosan Bobcat Pedestrian Detection Camera]], [[Hyster Pedestrian Awareness Camera]], [[Hyster Reaction]], [[IRIS 860 Sensor Pack]] and 22 more.
3. **F-04** Merge repeated or empty label blocks in [[Hyster Reaction]], [[Linde Safety Guard]], [[Toyota SEnS+ Pedestrian and Object Detection]].
4. **F-03** Move 26 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
