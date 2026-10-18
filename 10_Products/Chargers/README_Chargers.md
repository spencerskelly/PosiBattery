# Chargers

## Purpose

Industrial battery chargers: industrial modular, light-duty, on-board and wireless.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 7 / 69 |
| Typed model notes (incl. subfolders) | 69 (Object 69) |
| Status | Draft 69 of 69 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 45 / 40 of 69 |
| Tags | 27 distinct, 11 used once |
| Size | median 1,964 bytes; largest [[EnerSys NexSys+ Charger]] (9 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Industrial Modular Chargers|Industrial Modular Chargers]] | 41 | 1 | source-linked 23/40; 38 body-alias; 9 update-log |
| Light-Duty Chargers | 4 | 1 | source-linked 1/3; 3 body-alias |
| On-board Chargers | 6 | 1 | source-linked 3/5; 4 body-alias; 2 update-log |
| [[README_Wireless Chargers|Wireless Chargers]] | 11 | 1 | source-linked 10/10; 9 body-alias; 2 update-log |

### Analysis

- 69 notes: 5 abstract category/family notes and 64 concrete offerings. 64 of 64 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 43 of 64 (67%) concrete offerings carry a `describedBy` link; 21 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 64 of 69 (93%) notes `performs` at least one Function; 48 of 69 (70%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 59 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 13 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 61 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 69 of 69 Objects (F-05).
- Vocabulary and size: 27 distinct tags (11 used once); median note 1,964 bytes, largest EnerSys NexSys+ Charger (9 KB).

### Key links

- [[Crown V-HFM3 Charger]] — 60 inbound links
- [[Industrial Battery Charger]] (abstract) — 54 inbound links
- [[EnerSys NexSys+ Charger]] — 45 inbound links
- [[Industrial Modular Charger]] (abstract) — 44 inbound links
- [[Power Designers REVOLUTION X]] — 42 inbound links
- [[PosiCharge ProCore Edge]] — 41 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 69 Objects (the 5 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 21 concrete offerings with no source link: [[ACT Quantum Outdoor]], [[AMETEK Prestolite Power Eclipse II]], [[AMETEK Prestolite Power ULTRA]], [[Crown Battery EVOLUTION Series]], [[Delta-Q IC650]], [[EnerSys NexSys COMpact Charger]] and 15 more.
3. **F-04** Consolidate the dated update blocks in 13 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 61 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
