# Class I Electric Rider Trucks

## Purpose

Class I electric rider truck models.

Parent: [[README_Forklifts|Forklifts]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 37 / 37 |
| Typed model notes (incl. subfolders) | 37 (Object 37) |
| Status | Draft 37 of 37 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 29 / 29 of 37 |
| Tags | 8 distinct, 2 used once |
| Size | median 2,118 bytes; largest [[Crown RC 5700 Series]] (7 KB) |

### Analysis

- 37 notes: 1 abstract category/family notes and 36 concrete offerings. 36 of 36 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 29 of 36 (81%) concrete offerings carry a `describedBy` link; 7 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 24 of 37 (65%) notes `performs` at least one Function; 31 of 37 (84%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 37 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 22 notes carry dated update blocks, 12 repeat a bold label inside the note and 2 contain an empty label block (F-04).
- Aliases: 32 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 37 of 37 Objects (F-05).
- Vocabulary and size: 8 distinct tags (2 used once); median note 2,118 bytes, largest Crown RC 5700 Series (7 KB).

### Key links

- [[Crown RC 5700 Series]] — 41 inbound links
- [[Class I Electric Rider Truck]] (abstract) — 39 inbound links
- [[Hangcha XC Series Electric Forklifts]] — 26 inbound links
- [[Yale ERC050-060VGL]] — 25 inbound links
- [[Hangcha A Series Electric Forklifts]] — 24 inbound links
- [[Raymond 4000 Series Counterbalanced Trucks]] — 23 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 37 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 7 concrete offerings with no source link: [[Doosan Bobcat 7-Series Plus Electric Forklifts]], [[Doosan Bobcat NXE Series Electric Forklifts]], [[Heli G Series Lithium Forklifts]], [[Komatsu FB Series Electric Forklifts]], [[Linde 6-8 t Electric Counterbalance Forklifts]], [[Mitsubishi FBC Cushion Tire Electric Forklifts]] and 1 more.
3. **F-04** Merge repeated or empty label blocks in [[Crown FC 5700 Series]], [[Crown RC 5700 Series]], [[Hangcha A Series Electric Forklifts]], [[Hangcha XC Series Electric Forklifts]], [[Heli G Series Lithium Forklifts]], [[Hyster J1.5-3.0UT(L)]] and 7 more.
4. **F-04** Consolidate the dated update blocks in 22 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 32 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
