# Watering Systems

## Purpose

Battery watering systems.

Parent: [[README_Battery Accessories|Battery Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 13 / 13 |
| Typed model notes (incl. subfolders) | 13 (Object 13) |
| Status | Draft 13 of 13 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 7 / 5 of 13 |
| Tags | 13 distinct, 4 used once |
| Size | median 2,054 bytes; largest [[Philadelphia Scientific Stealth Watering System]] (3 KB) |

### Analysis

- 13 notes: 1 abstract category/family notes and 12 concrete offerings. 12 of 12 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 6 of 12 (50%) concrete offerings carry a `describedBy` link; 6 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 10 of 13 (77%) notes `performs` at least one Function; 7 of 13 (54%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 12 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 1 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 7 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 13 of 13 Objects; 3 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 13 distinct tags (4 used once); median note 2,054 bytes, largest Philadelphia Scientific Stealth Watering System (3 KB).

### Key links

- [[Flow-Rite Maverick Battery Watering System]] — 17 inbound links
- [[Philadelphia Scientific Stealth Watering System]] — 16 inbound links
- [[Battery Watering System]] (abstract) — 15 inbound links
- [[Crown V-Force Single Point Watering System]] — 15 inbound links
- [[Exide Automatic Watering System and Level Sensor]] — 15 inbound links
- [[PosiCharge Single-Point Automatic Battery Watering]] — 15 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 3 notes now using {'unknown': 3}: [[Amaron AFS System]], [[Banner Traction Bull Filling System]], [[Leoch PzS Automatic Water Filling System]].
2. **F-05** Backfill `productClass` on 13 Objects (the 1 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 6 concrete offerings with no source link: [[Crown V-Force Single Point Watering System]], [[Exide Automatic Watering System and Level Sensor]], [[Flow-Rite Maverick Battery Watering System]], [[Midac Aquamatic Watering System]], [[Philadelphia Scientific Stealth Watering System]], [[Philadelphia Scientific Water Injector System]].
4. **F-04** Consolidate the dated update blocks in 1 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 7 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
